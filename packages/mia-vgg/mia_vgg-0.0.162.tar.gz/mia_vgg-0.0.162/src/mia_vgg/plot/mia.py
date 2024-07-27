import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
from pathlib import Path
import sys


def boxplot(task):
    labels = ["Real images",
              "Synthetic images",
              ]
    path = Path("result",str(task), "mia", "real", "balanced_accuracy.pickle")
    with open(path, 'rb') as f:
        x_real = pickle.load(f)

    path = Path("result", str(task),"mia", "synth", "balanced_accuracy.pickle")
    with open(path, 'rb') as f:
        x_synth = pickle.load(f)

    x = [x_real, x_synth]

    save_path = Path("plot", "mia")
    os.makedirs(save_path, exist_ok=True)
    save_path = Path(save_path, "balanced_accuracy.pdf")

    font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 18}

    matplotlib.rc('font', **font)

    plt.boxplot(x, tick_labels=labels)
    plt.ylabel("Balanced accuracy of the MIA")
    #plt.xlabel("Data type")
    plt.savefig(save_path, bbox_inches="tight")

if __name__=="__main__":
    task = int(sys.argv[1])
    boxplot(task)
