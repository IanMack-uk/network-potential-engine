from network_potential_engine.symbolic.symbols import make_symbols


def test_make_symbols_shapes() -> None:
    w, theta = make_symbols(3, 2)

    assert w.shape == (3, 1)
    assert theta.shape == (2, 1)


def test_make_symbols_names() -> None:
    w, theta = make_symbols(3, 2)

    assert str(w[0, 0]) == "w0"
    assert str(w[1, 0]) == "w1"
    assert str(w[2, 0]) == "w2"

    assert str(theta[0, 0]) == "theta0"
    assert str(theta[1, 0]) == "theta1"