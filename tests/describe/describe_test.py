import pytest
import pandas as pd
import numpy as np
from dslr.describe.describe import count, mean, std, minimum, maximum, describe, quantile


def test_count():
    df = pd.DataFrame({
        "Person": ["John", "Myla", "Lewis", "John", "Myla"],
        "Age": [24., np.nan, 21., 33, 26],
        "Single": [False, True, True, True, False]
    })
    result = count(df)
    assert result[0] == 5
    assert result[1] == 4
    assert result[2] == 5


def test_mean():
    df = pd.DataFrame({
        "A": [12, 4, 5, 44, 1],
        "B": [5, 2, 54, 3, 2],
        "C": [20, 16, 7, 3, 8],
        "D": [14, 3, 17, 2, 6]
    })
    result = mean(df)
    assert result[0] == 13.2
    assert result[1] == 13.2
    assert result[2] == 10.8
    assert result[3] == 8.4

def test_std():
    df = pd.read_csv("./resources/nba.csv")
    result = std(df)
    assert result[0] == 0
    assert result[1] == 0
    assert round(result[2], 1) == 15.9
    assert result[3] == 0
    assert round(result[4], 1) == 4.4
    assert result[5] == 0
    assert round(result[6], 1) == 26.3
    # assert result[7] == 0
    # assert round(result[8], 1) == 5.2

def test_minimum():
    df = pd.DataFrame({
        "A": [12, 4, 5, 44, 1],
        "B": [5, 2, 54, 3, 2],
        "C": [20, 16, 7, 3, 8],
        "D": [14, 3, 17, 2, 6]
    })
    result = minimum(df)
    assert result[0] == 1
    assert result[1] == 2
    assert result[2] == 3
    assert result[3] == 2

def test_maximum():
    df = pd.DataFrame({
        "A": [12, 4, 5, 44, 1],
        "B": [5, 2, 54, 3, 2],
        "C": [20, 16, 7, 3, 8],
        "D": [14, 3, 17, 2, 6]
    })
    result = maximum(df)
    assert result[0] == 44
    assert result[1] == 54
    assert result[2] == 20
    assert result[3] == 17

def test_quantile():
    df = pd.DataFrame({"A":[1, 5, 3, 4, 2],
                   "B":[3, 2, 4, 3, 4],
                   "C":[2, 2, 7, 3, 4],
                   "D":[4, 3, 6, 12, 7]})
    result = quantile(df, 0.2)
    assert result[0] == 1.8
    assert result[1] == 2.8
    assert result[2] == 2.0
    assert result[3] == 3.8
