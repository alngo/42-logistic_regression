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

import argparse
import pandas as pd
from .utils import read_csv


def arguments():
    parser = argparse.ArgumentParser(
        description="Describe dataset")

    parser.add_argument("datapath", metavar="<datapath>",
                        type=str, help="path to a valid dataset.")

    args = parser.parse_args()
    return args


def count():
    pass


def mean():
    pass


def std():
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

    for desc, feature in description.iterrows():
        if desc is "Min":
            print("min")
        if desc is "Max":
            print("max")

    # for exemple purpose only
    print(description.head())
    print(df.head())
    print(df.describe())


if __name__ == "__main__":
    describe()
