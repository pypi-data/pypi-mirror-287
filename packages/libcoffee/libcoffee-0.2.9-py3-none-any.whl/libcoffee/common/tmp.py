import numpy as np
import numpy.typing as npt

from .molbase import MolBase


class Conformer:
    coordinates: npt.NDArray[np.float_]


class State:
    smiles: str
    conformers: list[Conformer]
    molobj: MolBase


class Compound:
    states: list[State]
    name: str
