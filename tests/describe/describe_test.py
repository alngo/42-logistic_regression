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
    assert result[2] == 1.596609e+01
    assert result[3] == 0
    assert result[4] == 4.404016e+00
    assert result[5] == 0
    assert result[6] == 2.636834e+01
    assert result[7] == 0
    assert result[8] == 5.229238e+6

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
    assert result[0] == 1
    assert result[1] == 2
    assert result[2] == 3
    assert result[3] == 2

def test_quantile():
    df = pd.DataFrame({
        "A": [12, 4, 5, 44, 1],
        "B": [5, 2, 54, 3, 2],
        "C": [20, 16, 7, 3, 8],
        "D": [14, 3, 17, 2, 6]
    })
    result = quantile(df, 0.2)
    assert result[0] == 1.8
    assert result[1] == 2.8
    assert result[2] == 2.0
    assert result[3] == 3.8
