from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping

import numpy as np


@dataclass(frozen=True, slots=True)
class NodeAttributes:
    r: float
    extras: Mapping[str, float] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not isinstance(self.r, (int, float, np.floating)):
            raise TypeError("r must be a real scalar")

        for k, v in self.extras.items():
            if not isinstance(k, str):
                raise TypeError("extras keys must be strings")
            if not isinstance(v, (int, float, np.floating)):
                raise TypeError("extras values must be real scalars")


@dataclass(frozen=True, slots=True)
class NodeAttributeField:
    by_node: Mapping[int, NodeAttributes]
    n_nodes: int

    def __post_init__(self) -> None:
        if not isinstance(self.n_nodes, int) or self.n_nodes <= 0:
            raise ValueError("n_nodes must be a positive integer")

        for i, attrs in self.by_node.items():
            if not isinstance(i, int):
                raise TypeError("node indices must be integers")
            if i < 0 or i >= self.n_nodes:
                raise ValueError("node index out of range")
            if not isinstance(attrs, NodeAttributes):
                raise TypeError("by_node values must be NodeAttributes")


def capacity_vector(x: NodeAttributeField) -> np.ndarray:
    r = np.zeros(x.n_nodes, dtype=float)
    for i in range(x.n_nodes):
        try:
            r[i] = float(x.by_node[i].r)
        except KeyError as e:
            raise ValueError(f"missing NodeAttributes for node {i}") from e
    return r
