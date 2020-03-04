# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    minimum.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/04 11:05:40 by alngo             #+#    #+#              #
#    Updated: 2020/03/04 11:17:07 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def minimum(dataframe):
    """
    Return minimum for each column
    """
    minimum = []
    for _, serie in dataframe.iteritems():
        clean_serie = serie.dropna()
        minimum.append(min(clean_serie))
    return minimum
