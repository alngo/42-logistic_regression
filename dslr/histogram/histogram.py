import argparse
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'tools')))

from utils import read_csv, drop_columns  # noqa # pylint: disable=wrong-import-position


def arguments():
    parser = argparse.ArgumentParser(
        description="Describe dataset")

    parser.add_argument("datapath", metavar="<datapath>",
                        type=str, help="path to a valid dataset.")

    args = parser.parse_args()
    return args


def histogram():
    args = arguments()
    df = read_csv(args.datapath)
    df = drop_columns(df, ["Index", "First Name", "Last Name",
                           "Birthday", "Best Hand"])
    print(df.head())


if __name__ == "__main__":
    histogram()
