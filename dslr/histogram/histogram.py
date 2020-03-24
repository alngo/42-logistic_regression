import os
import sys
import pandas as pd
import argparse
import plotly
import cufflinks as cf
cf.go_offline()
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

    args = parser.parse_args()
    return args


def generate_hogwarts_house_mask(df=None):
    isGryffindor = df["Hogwarts House"] == "Gryffindor"
    isSlytherin = df["Hogwarts House"] == "Slytherin"
    isRavenclaw = df["Hogwarts House"] == "Ravenclaw"
    isHufflepuff = df["Hogwarts House"] == "Hufflepuff"

    return [isGryffindor, isSlytherin, isHufflepuff, isRavenclaw]


def histogram():
    args = arguments()
    df = read_csv(args.datapath)
    G_mask, S_mask, H_mask, R_mask = generate_hogwarts_house_mask(df)
    df = drop_columns(df, ["Index", "Hogwarts House", "First Name",
                           "Last Name", "Birthday", "Best Hand"])

    for column in df:
        G_marks = df[column][G_mask]
        S_marks = df[column][S_mask]
        H_marks = df[column][H_mask]
        R_marks = df[column][R_mask]

        subfig = plotly.graph_objs.Figure(
        )

        subfig.add_trace(plotly.graph_objs.Histogram(
            x=G_marks, name="Gryffindor", marker=dict(color="#ff0000")))
        subfig.add_trace(plotly.graph_objs.Histogram(
            x=S_marks, name="Slytherin", marker=dict(color="#008000")))
        subfig.add_trace(plotly.graph_objs.Histogram(
            x=H_marks, name="Hufflepuff", marker=dict(color="#ffff00")))
        subfig.add_trace(plotly.graph_objs.Histogram(
            x=R_marks, name="Ravenclaw", marker=dict(color="#0000ff")))

        title = f"Histogram {column}"
        subfig.update_layout(title_text=title, barmode="overlay")
        subfig.update_traces(opacity=0.50)
        subfig.show()


if __name__ == "__main__":
    histogram()
