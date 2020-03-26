import os
path = os.path.dirname(__file__)
describe_path = os.path.join(path, "describe/describe.py")
histogram_path = os.path.join(path, "histogram/")
scatter_plot_path = os.path.join(path, "scatter_plot/")


class Dslr:
    def __init__(self, datapath):
        self.datapath = datapath

    def run(self, action):
        if action == "describe":
            os.system(f"python {describe_path} {self.datapath}")  # nosec
        elif action == "histogram":
            os.system(f"jupyter notebook {histogram_path}")  # nosec
        elif action == "pair_plot":
            os.system(f"jupyter notebook {scatter_plot_path}")  # nosec
        elif action == "scatter_plot":
            raise NotImplementedError("Method is required!")
        elif action == "loreg_train":
            raise NotImplementedError("Method is required!")
        elif action == "loreg_predict":
            raise NotImplementedError("Method is required!")
        else:
            print("Unsupported option.")
