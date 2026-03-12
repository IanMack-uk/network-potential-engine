from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

import numpy as np

from network_potential_engine.attributes.node_attributes import NodeAttributeField, NodeAttributes
from network_potential_engine.source.node_source_value import psi_reference, source_vector


@dataclass(frozen=True, slots=True)
class ValueModel:
    psi: Callable[[NodeAttributes], float] = psi_reference

    def source(self, x: NodeAttributeField) -> np.ndarray:
        return source_vector(x, psi=self.psi)
