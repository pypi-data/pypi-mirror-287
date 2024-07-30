import jax.lax as lax
import jax.numpy as jnp
import noxjax as nox
from jaxtyping import Array, Float

from ._linear import Bias, Scale
from ._typecheck import typecheck_jax


class LayerNorm(nox.Module):
    __noxname = "noxnet.LayerNorm"

    b: Bias
    s: Scale

    epsilon: float
    axis: int
    offset: bool

    @classmethod
    def init(
        cls,
        dim: int,
        epsilon: float = 1e-4,
        axis: int = -1,
        offset: bool = False,
    ):
        return cls(
            b=Bias.init(dim),
            s=Scale.init(dim, offset=offset),
            epsilon=epsilon,
            axis=axis,
            offset=offset,
        )

    @typecheck_jax
    def __call__(
        self,
        x: Float[Array, "*b {self.dim}"],
    ) -> Float[Array, "*b {self.dim}"]:
        m = jnp.mean(x, axis=self.axis, keepdims=True)
        x = x - m

        v = jnp.mean(x**2, axis=self.axis, keepdims=True)
        x = x * lax.rsqrt(v + self.epsilon)
        return self.s(self.b(x))

    @property
    def dim(self) -> int:
        return self.b.dim


class RMSNorm(LayerNorm):
    __noxname = "noxnet.RMSNorm"

    @typecheck_jax
    def __call__(
        self,
        x: Float[Array, "*b {self.dim}"],
    ) -> Float[Array, "*b {self.dim}"]:
        v = jnp.mean(x**2, axis=self.axis, keepdims=True)
        x = x * lax.rsqrt(v + self.epsilon)
        return self.s(self.b(x))
