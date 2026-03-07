from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import bootstrap_potential


def main() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)

    print(phi)
    print(type(phi))


if __name__ == "__main__":
    main()
