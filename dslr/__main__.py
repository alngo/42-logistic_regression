import os
import argparse
from .dslr import Dslr


def arguments():
    parser = argparse.ArgumentParser(
        description="Logistic regression program")
    parser.add_argument('datapath', type=str)
    args = parser.parse_args()
    return args


def program():
    args = arguments()
    datapath = os.path.abspath(args.datapath)
    prog = Dslr(datapath)

    while True:
        action = input("What ?\n") #nosec
        if action == "exit":
            print("Bye~ !")
            break
        else:
            prog.run(action)


if __name__ == '__main__':
    program()
