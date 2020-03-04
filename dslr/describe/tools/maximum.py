# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    maximum.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/04 11:05:59 by alngo             #+#    #+#              #
#    Updated: 2020/03/04 11:17:42 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def maximum(dataframe):
    """
    Return maximum for each column
    """
    maximum = []
    for _, serie in dataframe.iteritems():
        clean_serie = serie.dropna()
        maximum.append(max(clean_serie))
    return maximum
