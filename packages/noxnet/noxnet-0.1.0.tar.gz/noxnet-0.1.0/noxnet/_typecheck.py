import noxjax as nox
from jaxtyping import jaxtyped

__all__ = ["typecheck_jax"]


# typecheck functions with jaxtyping annotations
typecheck_jax = jaxtyped(typechecker=nox.typecheck)
