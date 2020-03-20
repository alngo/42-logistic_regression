import argparse
import chart_studio.plotly as plt
import cufflinks as cf
import sys
import os
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
    G_mask, S_mask, H_mask, R_mask = generate_hogwarts_house_mask(df=df)
    df = drop_columns(df, ["Index", "Hogwarts House", "First Name",
                           "Last Name", "Birthday", "Best Hand"])

    test = df.iplot(kind='histogram', filename='cufflinks/basic-histogram')
    plt.offline.plot(test)
    # index = 1
    # for column in df:
    #     G_marks = normalize(df[column][G_mask])
    #     S_marks = normalize(df[column][S_mask])
    #     H_marks = normalize(df[column][H_mask])
    #     R_marks = normalize(df[column][R_mask])

    #     try:
    #         plt.hist(G_marks)
    #         plt.hist(S_marks)
    #         plt.hist(H_marks)
    #         plt.hist(R_marks)
    #     except Exception:
    #         pass

    #     plt.title(column)
    #     index = index + 1

    # plt.show()


if __name__ == "__main__":
    histogram()
