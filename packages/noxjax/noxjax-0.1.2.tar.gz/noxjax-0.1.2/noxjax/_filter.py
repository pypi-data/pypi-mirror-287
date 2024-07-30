import functools
from typing import Any, Callable, ParamSpec, Self, TypeVar

import jax
import jax.tree_util as jtu
from jaxtyping import PyTree

from ._module import Module


__all__ = [
    "ModulePart",
    "merge",
    "split",
    "filter_jit",
    "FilterJit",
]


T = TypeVar("T")
P = ParamSpec("P")


class ModulePart(Module):
    __noxname = "noxjax.ModulePart"

    leaves: tuple
    struct: jtu.PyTreeDef

    def tree_flatten_with_keys(
        self: Self,
    ) -> tuple[tuple[tuple[jtu.GetAttrKey, Any], ...], jtu.PyTreeDef]:
        return ((jtu.GetAttrKey("leaves"), self.leaves),), self.struct

    @classmethod
    def tree_unflatten(cls, aux_data: jtu.PyTreeDef, leaves):
        return cls(leaves[0], aux_data)


def merge(tree1: ModulePart, tree2: ModulePart) -> PyTree:
    if tree1.struct != tree2.struct:
        raise ValueError("Structures must match")

    leaves = []

    for l1, l2 in zip(tree1.leaves, tree2.leaves):
        leaves.append(l1 if l1 is not None else l2)

    return jtu.tree_unflatten(tree1.struct, leaves)


def split(
    tree: PyTree,
    func: Callable[[Any], bool],
) -> tuple[ModulePart, ModulePart]:
    leaves, struct = jtu.tree_flatten(tree)

    leaves_1 = []
    leaves_2 = []

    for leaf in leaves:
        if func(leaf):
            leaves_1.append(leaf)
            leaves_2.append(None)
        else:
            leaves_1.append(None)
            leaves_2.append(leaf)

    part1 = ModulePart(leaves=tuple(leaves_1), struct=struct)
    part2 = ModulePart(leaves=tuple(leaves_2), struct=struct)
    return part1, part2


@functools.partial(
    jax.jit,
    static_argnames=(
        "func",
        "args_static",
        "kwargs_static",
    ),
)
def _filter_jit_apply(
    func,
    args_active,
    args_static,
    kwargs_active,
    kwargs_static,
):
    args = merge(args_active, args_static)
    kwargs = merge(kwargs_active, kwargs_static)
    return func(*args, **kwargs)


def filter_jit(func: Callable[P, T]) -> Callable[P, T]:
    def is_jitable_type(obj: Any) -> bool:
        return isinstance(obj, jax.Array)

    @functools.wraps(func)
    def wrapped(*args: P.args, **kwargs: P.kwargs) -> T:
        args_active, args_static = split(args, is_jitable_type)
        kwargs_active, kwargs_static = split(kwargs, is_jitable_type)
        return _filter_jit_apply(
            func,
            args_active,
            args_static,
            kwargs_active,
            kwargs_static,
        )

    return wrapped


@filter_jit
def _filter_jit_apply_layer(
    module: Callable[P, T],
    *args: P.args,
    **kwargs: P.kwargs,
) -> T:
    return module(*args, **kwargs)


class FilterJit(Module):
    __noxname = "noxjax.FilterJit"

    module: Callable

    def __post_init__(self: Self) -> None:
        if not callable(self.module):
            error = f"Module {self.module} is not callable."
            raise ValueError(error)

    def __call__(self: Self, *args, **kwargs):
        return _filter_jit_apply_layer(self.module, *args, **kwargs)
