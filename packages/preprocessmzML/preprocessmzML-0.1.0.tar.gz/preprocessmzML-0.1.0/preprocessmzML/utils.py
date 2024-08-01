import itertools
import matplotlib.pyplot as plt
import pyopenms as oms

def plot_spectrum(spectrum, title, save_path):
    plt.figure()
    mz, intensity = spectrum.get_peaks()
    plt.plot(mz, intensity)
    plt.xlabel("m/z")
    plt.ylabel("Intensity")
    plt.title(title)
    plt.savefig(save_path)
    plt.close()

def get_param_combinations(param_grid):
    keys, values = zip(*param_grid.items())
    all_combinations = [dict(zip(keys, combination)) for combination in itertools.product(*values)]
    return all_combinations
