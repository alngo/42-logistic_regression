# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/04 10:48:59 by alngo             #+#    #+#              #
#    Updated: 2020/03/04 10:49:09 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd


def count(dataframe):
    """
    Compute number of non-NA elements in a dataframe.
    """
    count = []
    for _, serie in dataframe.iteritems():
        counter = 0
        for _, value in serie.iteritems():
            if not pd.isna(value):
                counter += 1
        count.append(counter)
    return count
