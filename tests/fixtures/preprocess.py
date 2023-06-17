import pandas as pd
import pytest


@pytest.fixture
def sample_df():
    df = pd.read_csv('tests/fixtures/data/sample.csv')
    return df
