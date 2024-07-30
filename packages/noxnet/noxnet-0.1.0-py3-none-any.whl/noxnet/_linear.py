import math

import jax.nn as jnn
import jax.numpy as jnp
import jax.random as jrn
import noxjax as nox
from jaxtyping import Array, Float, PRNGKeyArray

from ._typecheck import typecheck_jax
from ._utils import sow_with_modes

__all__ = [
    "Linear",
    "Bias",
    "Scale",
    "Constant",
]


class Linear(nox.Module):
    """
    Apply a learanable affine transformation to the input data. That takes the
    form of a matrix multiplication and an optional bias addition.

    The last input axis has dimensionality 'dim_in', the output shares all axes,
    except the last one with the input, which has dimensionality 'dim'.

    Attributes:
    ---
    w: jax.Array
        The learnable weights of the layer. This has shape (dim_in, dim).

    b: jax.Array | None
        The learnable bias of the layer. This has shape (dim,) or is None, if
        the layer does not have a bias.
    """

    __noxname = "noxnet.Linear"

    w: Float[Array, "dim_in dim"]
    b: Float[Array, "dim"] | None

    @typecheck_jax
    @classmethod
    def init(
        cls,
        key: PRNGKeyArray,
        dim_in: int,
        dim: int,
        use_bias: bool = False,
    ):
        """
        Initialize the layer with random weights and biases. The default
        initialization is based on the Glorot uniform initialization, which
        is the same as the PyTorch default.

        Parameters:
        ---
        key: PRNGKey
            The random key to use for initialization.

        dim_in: int
            The number of input features.

        dim: int
            The number of output features.

        use_bias: bool
            Whether to use a bias term in the layer.

        Returns:
        ---
        Linear
            The initialized layer.
        """
        scale = 1 / math.sqrt(dim_in)
        w_key, b_key = jrn.split(key)

        w = jrn.uniform(w_key, (dim_in, dim), minval=-1, maxval=1) * scale

        if use_bias:
            b = jrn.uniform(b_key, (dim,), minval=-1, maxval=1) * scale
        else:
            b = None

        return cls(w=w, b=b)

    @typecheck_jax
    def __call__(
        self,
        x: Float[Array, "*b {self.dim_in}"],
    ) -> Float[Array, "*b {self.dim}"]:
        y = jnp.dot(x, self.w)

        y = sow_with_modes(y, name="x @ w")

        if self.use_bias:
            y += self.b
            y = sow_with_modes(y, name="x @ w + b")

        return y

    @property
    def dim_in(self) -> int:
        return self.w.shape[0]

    @property
    def dim(self) -> int:
        return self.w.shape[1]

    @property
    def use_bias(self) -> bool:
        return self.b is not None


class LinearGeGLU(nox.Module):
    __noxname = "noxnet.LinearGeGLU"

    w: Linear

    @classmethod
    def init(cls, key, dim_in: int, dim: int, use_bias: bool = False):
        return cls(w=Linear.init(key, dim_in, 2 * dim, use_bias=use_bias))

    @typecheck_jax
    def __call__(self, x: Array) -> Array:
        x = self.w(x)
        x, g = jnp.split(x, 2, axis=-1)
        return x * jnn.gelu(g, approximate=True)

    @property
    def dim_in(self):
        return self.w.dim_in

    @property
    def dim(self):
        return self.w.dim // 2


class Bias(nox.Module):
    __noxname = "noxnet.Bias"

    b: Float[Array, "..."]

    @classmethod
    def init(cls, dim: int):
        return cls(b=jnp.zeros((dim,)))

    @typecheck_jax
    def __call__(
        self,
        x: Float[Array, "*b {self.dim}"],
    ) -> Float[Array, "*b {self.dim}"]:
        y = x + self.b
        y = sow_with_modes(y, name="x + b")
        return y

    @property
    def dim(self) -> int:
        return self.b.shape[0]


class Scale(nox.Module):
    __noxname = "noxnet.Scale"

    s: Float[Array, "..."]
    offset: bool = True

    @classmethod
    def init(cls, dim: int, offset: bool = False):
        return cls(s=jnp.zeros((dim,)), offset=offset)

    @typecheck_jax
    def __call__(
        self, x: Float[Array, "*b {self.dim}"]
    ) -> Float[Array, "*b {self.dim}"]:
        s = 1 + self.s if self.offset else self.s
        y = x * s
        y = sow_with_modes(y, name="x * s")
        return y

    @property
    def dim(self) -> int:
        return self.s.shape[0]


class Constant(nox.Module):
    __noxname = "noxnet.Constant"

    x: Float[Array, "..."]

    @typecheck_jax
    @classmethod
    def random_normal(
        cls,
        key: PRNGKeyArray,
        shape: tuple[int, ...],
        std: float = 1.0,
    ):
        return cls(x=jrn.normal(key, shape) * std)

    @typecheck_jax
    @classmethod
    def random_uniform(
        cls,
        key: PRNGKeyArray,
        shape: tuple[int, ...],
        low: float = -1.0,
        high: float = 1.0,
    ):
        return cls(x=jrn.uniform(key, shape, minval=low, maxval=high))

    @classmethod
    def full(cls, x: float = 0.0, shape: tuple[int, ...] = ()):
        return cls(x=jnp.full(shape, x))

    @property
    def shape(self) -> tuple[int, ...]:
        return self.x.shape

    @property
    def dtype(self) -> jnp.dtype:
        return self.x.dtype

    @typecheck_jax
    def __call__(self, *args, **kwargs) -> Array:
        return self.x
