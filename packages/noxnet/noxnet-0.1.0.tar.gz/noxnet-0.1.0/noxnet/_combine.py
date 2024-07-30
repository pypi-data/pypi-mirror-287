from typing import Any, TypeVar

import jax
import jax.numpy as jnp
import noxjax as nox
import oryx.core.interpreters.harvest as harvest

T = TypeVar("T")


__all__ = [
    "Add",
    "Sequential",
    "Multiply",
    "Concat",
    "Identity",
    "Residual",
    "Index",
]


class Sequential(nox.ModuleSequence):
    __noxname = "noxnet.Sequential"

    def __call__(self, x, *args, **kwargs) -> Any:
        for i, layer in enumerate(self):
            assert callable(layer), f"Layer {layer} is not callable."

            layer = harvest.nest(layer, scope=str(i))
            x = layer(x, *args, **kwargs)

        return x


class Add(Sequential):
    __noxname = "noxnet.Add"

    def __call__(self, x, *args, **kwargs) -> Any:
        y = 0

        for i, layer in enumerate(self):
            assert callable(layer), f"Layer {layer} is not callable."

            layer = harvest.nest(layer, scope=str(i))
            y = y + layer(x, *args, **kwargs)

        return y


class Multiply(Sequential):
    __noxname = "noxnet.Multiply"

    def __call__(self, x, *args, **kwargs) -> Any:
        y = 1

        for i, layer in enumerate(self):
            assert callable(layer), f"Layer {layer} is not callable."

            layer = harvest.nest(layer, scope=str(i))
            y = y * layer(x, *args, **kwargs)

        return y


class Concat(Sequential):
    __noxname = "noxnet.Concat"

    def __call__(self, x, *args, **kwargs) -> jax.Array:
        ys = []

        for i, layer in enumerate(self):
            assert callable(layer), f"Layer {layer} is not callable."

            layer = harvest.nest(layer, scope=str(i))
            ys.append(layer(x, *args, **kwargs))

        return jnp.concatenate(ys, axis=-1)


class Identity(nox.Module):
    __noxname = "noxnet.Identity"

    def __call__(self, x: T, *args, **kwargs) -> T:
        return x


class Residual(nox.Module):
    __noxname = "noxnet.Residual"

    layer: nox.Module

    def __call__(self, x, *args, **kwargs) -> Any:
        assert callable(self.layer), f"Layer {self.layer} is not callable."
        return x + self.layer(x, *args, **kwargs)


class Index(nox.Module):
    __noxname = "noxnet.Index"

    index: int | slice | tuple[int | slice, ...]

    def __call__(self, x) -> Any:
        return x[self.index]
