# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    std.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/04 10:49:53 by alngo             #+#    #+#              #
#    Updated: 2020/03/04 14:38:26 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from mean import compute_mean

def compute_std(serie):
    """
    Compute std of a serie
    """
    clean_serie = serie.dropna()
    length = len(clean_serie)
    mean = compute_mean(clean_serie)
    acc = 0.0
    try:
        for _, value in clean_serie.iteritems():
            acc += ((value - mean) ** 2)
    except TypeError:
        return (float('NaN'))
    finally:
        variance = (1 / length) * acc
        return (np.sqrt(variance))



def std(dataframe):
    """
    Compute std of columns's element in a dataframe.
    """
    std = []
    for _, serie in dataframe.iteritems():
        std.append(compute_std(serie))
    return std
