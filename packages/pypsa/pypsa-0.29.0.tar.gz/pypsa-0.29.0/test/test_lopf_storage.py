import os

import pandas as pd
import pytest
from numpy.testing import assert_array_almost_equal as equal

import pypsa


@pytest.fixture
def target_gen_p():
    target_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "examples",
        "opf-storage-hvdc",
        "opf-storage-data",
        "results",
        "generators-p.csv",
    )
    return pd.read_csv(target_path, index_col=0, parse_dates=True)


@pytest.fixture
def network():
    csv_folder = os.path.join(
        os.path.dirname(__file__),
        "..",
        "examples",
        "opf-storage-hvdc",
        "opf-storage-data",
    )
    return pypsa.Network(csv_folder)


def test_optimize(network, target_gen_p):
    network.optimize()
    equal(network.generators_t.p.reindex_like(target_gen_p), target_gen_p, decimal=2)
