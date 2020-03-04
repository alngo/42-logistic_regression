# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    quantile.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/04 11:03:19 by alngo             #+#    #+#              #
#    Updated: 2020/03/04 14:22:33 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math

def compute_quantile(serie, q):
    clean_serie = serie.dropna()
    sorted_serie = clean_serie.sort_values(ascending=True)
    length = len(sorted_serie)
    observation = q * (length - 1)
    fraction = observation % 1
    if fraction:
        i = sorted_serie.iloc[math.floor(observation)]
        j = sorted_serie.iloc[math.ceil(observation)]
        return i + (j - i) * fraction
    return observation


def quantile(dataframe, q):
    """
    """
    quantile = []
    for _, serie in dataframe.iteritems():
        quantile.append(compute_quantile(serie, q))
    return quantile
