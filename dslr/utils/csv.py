# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csv.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 09:44:54 by alngo             #+#    #+#              #
#    Updated: 2020/03/02 15:10:16 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import sys


def read_csv(path):
    parameters = None
    try:
        parameters = pd.read_csv(path)
    except FileNotFoundError:
        print(f'File at path: "{path}" not found')
        sys.exit(1)
    except Exception:
        print(f'An unexpected error occured on read_csv')
        sys.exit(1)
    return parameters


def write_csv(data, output):
    df = pd.DataFrame(data=data, index=[0])
    df.to_csv(output, index=None)


def clean_dataframe(dataframe):
    cols_to_remove = []

    dataframe.drop(["Index"], axis=1, inplace=True)
    for col in dataframe.columns:
        try:
            _ = dataframe[col].astype(float)
        except ValueError:
            cols_to_remove.append(col)
            pass

    new_dataframe = dataframe[[
        col for col in dataframe.columns if col not in cols_to_remove
    ]]
    return new_dataframe


def check_csv(*fields):
    def wrapper(func):
        def new_f(self, *args, **kwargs):
            try:
                columns = self.data.columns.tolist()
                if (len(columns) != len(fields)):
                    raise IndexError
                for (a, b) in zip(columns, fields):
                    if (a != b):
                        raise IndexError
            except IndexError:
                print(f"Can't process {func.__name__}: invalid csv")
                sys.exit(1)
            except Exception:
                print(f'An unexpected error occured on read_csv')
                sys.exit(1)
            return func(self, *args, **kwargs)
        new_f.__name__ = func.__name__
        return new_f
    return wrapper
