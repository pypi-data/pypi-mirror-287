from typing import TypeVar

import noxjax as nox
import oryx.core.interpreters.harvest as harvest

T = TypeVar("T")


@nox.typecheck
def sow_with_modes(x: T, /, *, name: str) -> T:
    x = harvest.sow(x, name=name, tag="strict", mode="strict")
    x = harvest.sow(x, name=name, tag="clobber", mode="clobber")
    x = harvest.sow(x, name=name, tag="append", mode="append")
    return x
