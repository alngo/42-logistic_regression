import pytest
from dslr.utils.csv import read_csv


def test_get_parameters_with_none(capsys):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        read_csv(None)
    captured = capsys.readouterr()
    assert captured.out == 'An unexpected error occured on read_csv\n'
    assert pytest_wrapped_e.value.code == 1


def test_get_parameters_with_empty_file(capsys):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        path = "./resources/empty.csv"
        read_csv(path)
    captured = capsys.readouterr()
    assert captured.out == 'An unexpected error occured on read_csv\n'
    assert pytest_wrapped_e.value.code == 1


def test_get_parameters_with_invalid_path(capsys):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        path = "./resources/qwe.csv"
        read_csv(path)
    captured = capsys.readouterr()
    assert captured.out == 'File at path: "./resources/qwe.csv" not found\n'
    assert pytest_wrapped_e.value.code == 1
