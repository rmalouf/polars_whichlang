import polars as pl
import pytest
from polars.exceptions import ComputeError
from polars.testing import assert_series_equal

from polars_whichlang import detect_lang


@pytest.fixture
def sample_df():
    yield pl.DataFrame(
        {
            "index": [1, 2, 3, 4, 5],
            "text": ["This is a test.", "이건 테스트야", "Dies ist ein Test", "", " "],
            "lang_code": ["eng", "kor", "deu", "eng", "ita"],
        }
    )


def test_whichlang_dataframe(sample_df):
    df = sample_df.with_columns(predicted=detect_lang("text"))
    assert len(df) == 5
    assert_series_equal(df["lang_code"], df["predicted"], check_names=False)


def test_whichlang_lazyframe(sample_df):
    df = sample_df.lazy().with_columns(predicted=detect_lang("text"))
    assert isinstance(df, pl.LazyFrame)
    df = df.collect()
    assert len(df) == 5
    assert_series_equal(df["lang_code"], df["predicted"], check_names=False)


def test_whichlang_dataframe_error(sample_df):
    with pytest.raises(ComputeError):
        _ = sample_df.with_columns(predicted=detect_lang("index"))


def test_whichlang_lazyframe_error(sample_df):
    df = sample_df.lazy().with_columns(predicted=detect_lang("index"))
    assert isinstance(df, pl.LazyFrame)
    with pytest.raises(ComputeError):
        _ = df.collect()
