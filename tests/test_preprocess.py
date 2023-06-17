from datetime import date

import pandas as pd
from pandas.testing import assert_frame_equal

from src.preprocess import parse_date_columns


def test_parse_date_columns():
    # Arrange
    data = pd.DataFrame([{"date_col": "2021-01-01"}])
    expected = pd.DataFrame([{"date_col": date(2021, 1, 1)}])
    # Act
    actual = parse_date_columns(data, ["date_col"])
    # Assert
    assert_frame_equal(expected, actual)


def test_scale_columns():
    # Arrange

    # Act

    # Assert
    assert False


def test_label_encode_columns():
    # Arrange

    # Act

    # Assert
    assert False


def test_cast_columns_astype():
    # Arrange

    # Act

    # Assert
    assert False


def test_fill_na_columns():
    # Arrange

    # Act

    # Assert
    assert False


def test_rename_columns():
    # Arrange

    # Act

    # Assert
    assert False


def test_preprocess(sample_df):
    # Arrange

    # Act

    # Assert
    assert False
