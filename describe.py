# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/02 14:51:23 by alngo             #+#    #+#              #
#    Updated: 2020/03/02 15:16:39 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
from utils.csv import read_csv

def arguments():
    parser = argparse.ArgumentParser(
            description="Describe dataset")

    parser.add_argument("datapath", metavar="<datapath>", type=str, help="path to a valid dataset.")

    args = parser.parse_args()
    return args

def describe():
    args = arguments()
    df = read_csv(args.datapath)
    # for exemple purpose only
    print(df.describe())


if __name__ == "__main__":
    describe()
