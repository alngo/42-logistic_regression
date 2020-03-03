# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/02 14:51:23 by alngo             #+#    #+#              #
#    Updated: 2020/03/02 16:05:37 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import argparse
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from utils import *  # noqa # pylint: disable=wrong-import-position


def arguments():
    parser = argparse.ArgumentParser(
        description="Describe dataset")

    parser.add_argument("datapath", metavar="<datapath>",
                        type=str, help="path to a valid dataset.")

    args = parser.parse_args()
    return args


def count(dataframe):
    """
    Number of non-NA elements in a Series.
    """
    count = []
    for column, values in dataframe.iteritems():
        counter = 0
        for key, value in values.iteritems():
            if not pd.isna(value):
                counter += 1
        count.append(counter)
    return count


def mean(dataframe):
    pass


def std(dataframe):
    pass


def quantile(amount):
    pass


def minimum():
    pass


def maximum():
    pass


def describe():
    args = arguments()
    df = read_csv(args.datapath)
    df.drop(["Index"], axis=1, inplace=True)
    description = pd.DataFrame(
        columns=df.columns,
        index=[
            "Count",
            "Mean",
            "Std",
            "Min",
            "25%",
            "50%",
            "75%",
            "Max"
        ]
    )

    description.iloc[0] = count(df)
    description.iloc[1] = mean(df)

    # for exemple purpose only
    print(description.head())
    print(df.head())
    print(df.describe())


if __name__ == "__main__":
    describe()
