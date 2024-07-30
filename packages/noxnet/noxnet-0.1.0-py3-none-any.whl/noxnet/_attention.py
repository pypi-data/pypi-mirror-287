import jax.nn as jnn
import jax.numpy as jnp
import jax.random as jrn
import noxjax as nox
from jaxtyping import Array, Float, PRNGKeyArray

from ._linear import Linear
from ._typecheck import typecheck_jax
from ._utils import sow_with_modes

__all__ = [
    "causal_mask",
    "MultiHeadSelfAttention",
    "MultiHeadCrossAttention",
]


@typecheck_jax
def causal_mask(seq: int) -> Float[Array, "{seq} {seq}"]:
    mask = jnp.triu(jnp.ones((seq, seq)), 1)
    return jnp.where(mask == 1, -jnp.inf, 0.0)


@typecheck_jax
def scaled_tanh(x: Float[Array, "*s"], softcap: float) -> Float[Array, "*s"]:
    return softcap * jnp.tanh(x / softcap)


class MultiHeadSelfAttention(nox.Module, replace=True):
    __noxname = "noxnet.MultiHeadSelfAttention"

    proj_qkv: Linear
    proj_out: Linear

    num_heads: int
    att_stanh: float | None

    @classmethod
    def init(
        cls,
        key: PRNGKeyArray,
        dim: int,
        num_heads: int,
        att_stanh: float | None = None,
    ):
        assert dim % num_heads == 0
        key_qkv, key_out = jrn.split(key)

        dim_heads = dim // num_heads
        return cls(
            proj_qkv=Linear.init(
                key_qkv,
                dim,
                3 * num_heads * dim_heads,
                use_bias=False,
            ),
            proj_out=Linear.init(
                key_out,
                dim,
                dim,
                use_bias=False,
            ),
            num_heads=num_heads,
            att_stanh=att_stanh,
        )

    @typecheck_jax
    def __call__(
        self,
        x: Float[Array, "seq {self.dim}"],
        *,
        mask: Float[Array, "seq seq"] | None = None,
    ) -> Float[Array, "seq {self.dim}"]:
        qkv = self.proj_qkv(x)
        qkv = qkv.reshape(self.num_heads, -1, self.dim_heads * 3)
        q, k, v = jnp.split(qkv, 3, axis=-1)

        q = sow_with_modes(q, name="q")
        k = sow_with_modes(k, name="k")
        v = sow_with_modes(v, name="v")

        q = q / self.dim_heads**0.5
        a = jnp.einsum("hqd,hkd->hqk", q, k)
        a = sow_with_modes(a, name="attention logits")

        if self.att_stanh is not None:
            a = scaled_tanh(a, self.att_stanh)
            a = sow_with_modes(a, name="attention stanh")

        if mask is not None:
            a = a + mask

        a = jnn.softmax(a, axis=-1)
        a = sow_with_modes(a, name="attention")

        r = jnp.einsum("hqk,hkd->hqd", a, v)
        r = sow_with_modes(r, name="attention output")

        r = r.reshape(-1, self.dim)
        return self.proj_out(r)

    @property
    def dim(self) -> int:
        return self.proj_out.dim

    @property
    def dim_heads(self) -> int:
        return self.dim // self.num_heads


class MultiHeadCrossAttention(nox.Module, replace=True):
    __noxname = "noxnet.MultiHeadCrossAttention"

    proj_q: Linear
    proj_kv: Linear

    proj_out: Linear

    num_heads: int
    att_stanh: float | None

    @classmethod
    def init(
        cls,
        key: PRNGKeyArray,
        dim: int,
        num_heads: int,
        att_stanh: float | None = None,
    ):
        key_q, key_kv, key_out = jrn.split(key, 3)

        dim_heads = dim // num_heads
        return cls(
            proj_q=Linear.init(
                key_q,
                dim,
                num_heads * dim_heads,
                use_bias=False,
            ),
            proj_kv=Linear.init(
                key_kv,
                dim,
                2 * num_heads * dim_heads,
                use_bias=False,
            ),
            proj_out=Linear.init(
                key_out,
                dim,
                dim,
                use_bias=False,
            ),
            num_heads=num_heads,
            att_stanh=att_stanh,
        )

    @typecheck_jax
    def __call__(
        self,
        x: Float[Array, "seq {self.dim}"],
        y: Float[Array, "aux {self.dim}"],
        *,
        mask: Float[Array, "seq aux"] | None = None,
    ) -> Float[Array, "seq {self.dim}"]:
        q = self.proj_q(x)
        kv = self.proj_kv(y)

        q = q.reshape(self.num_heads, -1, self.dim_heads)

        k, v = jnp.split(kv, 2, axis=-1)
        k = k.reshape(self.num_heads, -1, self.dim_heads)
        v = v.reshape(self.num_heads, -1, self.dim_heads)

        q = sow_with_modes(q, name="q")
        k = sow_with_modes(k, name="k")
        v = sow_with_modes(v, name="v")

        q = q / self.dim_heads**0.5
        a = jnp.einsum("hqd,hkd->hqk", q, k)
        a = sow_with_modes(a, name="attention logits")

        if self.att_stanh is not None:
            a = scaled_tanh(a, self.att_stanh)
            a = sow_with_modes(a, name="attention stanh")

        if mask is not None:
            a = a + mask

        a = jnn.softmax(a, axis=-1)
        a = sow_with_modes(a, name="attention")

        r = jnp.einsum("hqk,hkd->hqd", a, v)
        r = sow_with_modes(r, name="attention output")

        r = r.reshape(-1, self.dim)
        return self.proj_out(r)

    @property
    def dim(self) -> int:
        return self.proj_out.dim

    @property
    def dim_heads(self) -> int:
        return self.dim // self.num_heads
