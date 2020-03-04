# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mean.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/04 10:49:17 by alngo             #+#    #+#              #
#    Updated: 2020/03/04 14:29:27 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def compute_mean(serie):
    """
    Compute mean of a serie
    """
    clean_serie = serie.dropna()
    length = len(clean_serie)
    acc = 0.0
    try:
        for _, value in clean_serie.iteritems():
            acc += value
    except TypeError:
        return (float('NaN'))
    finally:
        return (acc / length)


def mean(dataframe):
    """
    Compute mean of column's element in a dataframe.
    """
    mean = []
    for _, serie in dataframe.iteritems():
        mean.append(compute_mean(serie))
    return mean
