import numpy as np
import pathlib
import pytest

import cyl1tf

FPATH_DATA = pathlib.Path(__file__).parent / "data"


def load_file(fname):
    return np.loadtxt(FPATH_DATA / "snp500.txt")


@pytest.fixture()
def y():
    return load_file("snp500.txt")


def test_max_scale(y):
    max_scale = cyl1tf.calc_max_scale(y)
    np.testing.assert_allclose(max_scale, 3.739484e04, rtol=1e-4)


@pytest.mark.parametrize(
    "method,value,ref",
    [
        ("scale", 50, load_file("results-s50.txt")),
        ("rel_scale", 0.01, load_file("results-r0_01.txt")),
    ],
)
def test_calc_fit(y, method, value, ref):
    kwds = {method: value}
    fit = cyl1tf.calc_fit(y, **kwds)
    # Note that this are large testing bounds becuase of the number of
    # iterations were increased.
    np.testing.assert_allclose(fit, ref, rtol=1e-2, atol=0.2)
