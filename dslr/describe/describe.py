# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/02 14:51:23 by alngo             #+#    #+#              #
#    Updated: 2020/03/04 14:46:49 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import numpy as np
import argparse
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'tools')))

from utils import read_csv  # noqa # pylint: disable=wrong-import-position

from count import count
from mean import mean
from std import std
from quantile import quantile
from minimum import minimum
from maximum import maximum

def arguments():
    parser = argparse.ArgumentParser(
        description="Describe dataset")

    parser.add_argument("datapath", metavar="<datapath>",
                        type=str, help="path to a valid dataset.")

    args = parser.parse_args()
    return args

def remove_undescribable_column(dataframe):
    cols_to_remove = []

    dataframe.drop(["Index"], axis=1, inplace=True)
    for col in dataframe.columns:
        try:
            _ = dataframe[col].astype(float)
        except ValueError:
            cols_to_remove.append(col)
            pass

    clean_dataframe = dataframe[[
        col for col in dataframe.columns if col not in cols_to_remove
        ]]
    return clean_dataframe


def describe():
    args = arguments()
    df = read_csv(args.datapath)
    df = remove_undescribable_column(df)
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
    description.iloc[2] = std(df)
    description.iloc[3] = minimum(df)
    description.iloc[4] = quantile(df, 0.25)
    description.iloc[5] = quantile(df, 0.50)
    description.iloc[6] = quantile(df, 0.75)
    description.iloc[7] = maximum(df)

    print(description)

if __name__ == "__main__":
    describe()
