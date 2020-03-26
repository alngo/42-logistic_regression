import os
path = os.path.dirname(__file__)
describe_path = os.path.join(path, "describe/describe.py")
histogram_path = os.path.join(path, "histogram/histogram.py")


class Dslr:
    def __init__(self, datapath):
        self.datapath = datapath

    def run(self, action):
        if action == "describe":
            os.system(f"python {describe_path} {self.datapath}")  # nosec
        elif action == "histogram":
            os.system(f"python {histogram_path} {self.datapath}")  # nosec
        elif action == "pair_plot":
            raise NotImplementedError("Method is required!")
        elif action == "scatter_plot":
            raise NotImplementedError("Method is required!")
        elif action == "loreg_train":
            raise NotImplementedError("Method is required!")
        elif action == "loreg_predict":
            raise NotImplementedError("Method is required!")
        else:
            print("Unsupported option.")
