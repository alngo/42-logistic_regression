# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/02 14:51:23 by alngo             #+#    #+#              #
#    Updated: 2020/03/04 11:09:39 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import numpy as np
import argparse
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from utils import read_csv  # noqa # pylint: disable=wrong-import-position

from .tools import count, mean, std, quantile, minimum, maximum

def arguments():
    parser = argparse.ArgumentParser(
        description="Describe dataset")

    parser.add_argument("datapath", metavar="<datapath>",
                        type=str, help="path to a valid dataset.")

    args = parser.parse_args()
    return args


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
    description.iloc[2] = std(df)
    description.iloc[3] = minimum(df)
    description.iloc[4] = quantile(df)
    description.iloc[5] = quantile(df)
    description.iloc[6] = quantile(df)
    description.iloc[7] = maximum(df)

    # for exemple purpose only
    print(description.head())
    print(df.describe())


if __name__ == "__main__":
    describe()
