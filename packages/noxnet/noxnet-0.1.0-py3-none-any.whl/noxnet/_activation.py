import jax.nn as jnn
import noxjax as nox
from jaxtyping import Array, Float

from ._typecheck import typecheck_jax

__all__ = [
    "ELU",
    "GLU",
    "HardSigmoid",
    "HardSiLU",
    "HardTanh",
    "LeakyReLU",
    "LogSigmoid",
    "LogSoftmax",
    "LogSumExp",
    "OneHot",
    "ReLU",
    "ReLU6",
    "SeLU",
    "Sigmoid",
    "SiLU",
    "Softmax",
    "SoftPlus",
    "SoftSign",
    "SparsePlus",
    "SquarePlus",
    "Standardize",
]


class ELU(nox.Module):
    __noxname = "noxjax.ELU"

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.elu(x)


class GELU(nox.Module):
    __noxname = "noxjax.GELU"

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.gelu(x)


class GLU(nox.Module):
    __noxname = "noxjax.GLU"

    axis: int = -1

    @typecheck_jax
    def __call__(self, x: Float[Array, "..."]) -> Float[Array, "..."]:
        return jnn.glu(x, self.axis)


class HardSigmoid(nox.Module):
    __noxname = "noxjax.HardSigmoid"

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.hard_sigmoid(x)


class HardSiLU(nox.Module):
    __noxname = "noxjax.HardSiLU"

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.hard_silu(x)


class HardTanh(nox.Module):
    __noxname = "noxjax.HardTanh"

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.hard_tanh(x)


class LeakyReLU(nox.Module):
    __noxname = "noxjax.LeakyReLU"

    negative_slope: float = 1e-2

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.leaky_relu(x, self.negative_slope)


class LogSigmoid(nox.Module):
    __noxname = "noxjax.LogSigmoid"

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.log_sigmoid(x)


class LogSoftmax(nox.Module):
    __noxname = "noxjax.LogSoftmax"

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.log_softmax(x, axis=-1)


class LogSumExp(nox.Module):
    __noxname = "noxjax.LogSumExp"

    @typecheck_jax
    def __call__(self, x: Float[Array, "..."]) -> Float[Array, "..."]:
        return jnn.logsumexp(x, axis=-1)


class Standardize(nox.Module):
    __noxname = "noxjax.Standardize"

    axis: int = -1

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.standardize(x, axis=self.axis)


class OneHot(nox.Module):
    __noxname = "noxjax.OneHot"

    num_classes: int
    axis: int = -1

    @typecheck_jax
    def __call__(
        self,
        x: Float[Array, "*b"],
    ) -> Float[Array, "*b {self.dim}"]:
        return jnn.one_hot(x, self.num_classes, axis=self.axis)


class ReLU(nox.Module):
    __noxname = "noxjax.ReLU"

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.relu(x)


class ReLU6(nox.Module):
    __noxname = "noxjax.ReLU6"

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.relu6(x)


class SeLU(nox.Module):
    __noxname = "noxjax.SeLU"

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.selu(x)


class Sigmoid(nox.Module):
    __noxname = "noxjax.Sigmoid"

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.sigmoid(x)


class SoftSign(nox.Module):
    __noxname = "noxjax.SoftSign"

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.soft_sign(x)


class Softmax(nox.Module):
    __noxname = "noxjax.Softmax"

    axis: int = -1

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.softmax(x, axis=self.axis)


class SoftPlus(nox.Module):
    __noxname = "noxjax.SoftPlus"

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.softplus(x)


class SparsePlus(nox.Module):
    __noxname = "noxjax.SparsePlus"

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.sparse_plus(x)


class SiLU(nox.Module):
    __noxname = "noxjax.SiLU"

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.silu(x)


class SquarePlus(nox.Module):
    __noxname = "noxjax.SquarePlus"

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.squareplus(x)


class SquareReLU(nox.Module):
    __noxname = "noxjax.SquareReLU"

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        x = jnn.relu(x)
        return x * x


class Softcap(nox.Module):
    __noxname = "noxjax.Softcap"

    cap: float = -1

    @typecheck_jax
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        x = x / self.cap
        x = jnn.tanh(x)
        x = x * self.cap
        return x
