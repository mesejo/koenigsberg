from __future__ import annotations

import contextlib
import os
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from pytest import param

if TYPE_CHECKING:
    pass

import koenigsberg as kg


@contextlib.contextmanager
def pushd(new_dir):
    previous_dir = os.getcwd()
    os.chdir(new_dir)
    try:
        yield
    finally:
        os.chdir(previous_dir)


@pytest.fixture(scope="session")
def data_dir() -> Path:
    """Return the test data directory.

    Returns
    -------
    Path
        Test data directory
    """
    root = Path(__file__).absolute().parents[0]
    print(root)

    return root / "parquet"


@pytest.mark.parametrize(
    ("fname", "in_table_name", "out_table_name"),
    [
        param("functional_alltypes.parquet", "funk_all", "funk_all", id="basename"),
    ],
)
def test_register_parquet(
    tmp_path, data_dir, fname, in_table_name, out_table_name
):
    pq = pytest.importorskip("pyarrow.parquet")
    fname = Path(fname)

    con = kg.con()
    with pushd(tmp_path):
        table = con.register(data_dir / fname.name, table_name=in_table_name)

    assert any(out_table_name in t for t in con.list_tables())
    assert table.count() > 0
