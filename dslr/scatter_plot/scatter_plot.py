import os
import sys
import argparse
import plotly.express as px
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'tools')))

from utils import read_csv, drop_columns, normalize  # noqa # pylint: disable=wrong-import-position


def arguments():
    parser = argparse.ArgumentParser(
        description="Describe dataset")

    parser.add_argument("datapath", metavar="<datapath>",
                        type=str, help="path to a valid dataset.")

    parser.add_argument("--interactive", metavar="<datapath>",
                        type=bool, default=False,
                        help="histogram with plotly")

    args = parser.parse_args()
    return args


def plotly_scatter_plot(df, X, y):
    X_marks = normalize(df[X])
    y_marks = normalize(df[y])

    fig = px.scatter(x=X_marks, y=y_marks)
    fig.show()


def manual_scatter_plot():
    pass


def scatter_plot():
    args = arguments()
    df = read_csv(args.datapath)
    df = drop_columns(df, ["Index", "Hogwarts House", "First Name",
                           "Last Name", "Birthday", "Best Hand"])

    if args.interactive is True:
        plotly_scatter_plot(df, "Muggle Studies", "Ancient Runes")
    else:
        manual_scatter_plot()


if __name__ == "__main__":
    scatter_plot()
