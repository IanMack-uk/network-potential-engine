from __future__ import annotations

from network_potential_engine.scripts.check_comparative_statics_chain import (
    main as run_comparative_statics_chain,
)


def main() -> None:
    print("P14 comparative statics layer wrapper")
    print("This step runs the certified comparative statics chain: C1 -> S3 -> D1 -> D2 -> D3")
    print()
    run_comparative_statics_chain()


if __name__ == "__main__":
    main()
