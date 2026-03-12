from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class AssumptionRecord:
    assumption_id: str
    description: str | None = None
    evidence_ref: str | None = None
    status: str = "unknown"
    evidence: dict[str, Any] | None = None


@dataclass
class AssumptionRegistry:
    records: dict[str, AssumptionRecord] = field(default_factory=dict)

    def add(self, record: AssumptionRecord) -> None:
        if record.assumption_id in self.records:
            raise ValueError(f"Assumption '{record.assumption_id}' is already registered.")
        self.records[record.assumption_id] = record

    def get(self, assumption_id: str) -> AssumptionRecord:
        try:
            return self.records[assumption_id]
        except KeyError as exc:
            raise KeyError(f"Unknown assumption_id '{assumption_id}'.") from exc

    def ids(self) -> list[str]:
        return sorted(self.records.keys())
