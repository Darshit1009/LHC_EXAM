import numpy as np
import matplotlib.pyplot as plt

def time_shift(signal, k):
    """
    Shifts the signal by k units.
    Positive k shifts right, negative k shifts left.
    """
    shifted = np.roll(signal, k)
    plt.stem(range(len(shifted)), shifted)
    plt.title(f"Time-Shifted Signal (k = {k})")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return shifted


def time_scale(signal, k):
    """
    Scales the time axis by factor k.
    Only works for integer scaling factors.
    """
    if k <= 0 or not isinstance(k, int):
        raise ValueError("Scaling factor k must be a positive integer.")
    
    scaled = np.zeros(len(signal) * k)
    scaled[::k] = signal
    plt.stem(range(len(scaled)), scaled)
    plt.title(f"Time-Scaled Signal (k = {k})")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return scaled

def signal_addition(signal1, signal2):
    """
    Adds two signals element-wise.
    Pads shorter signal with zeros if lengths differ.
    """
    max_len = max(len(signal1), len(signal2))
    s1 = np.pad(signal1, (0, max_len - len(signal1)))
    s2 = np.pad(signal2, (0, max_len - len(signal2)))
    added = s1 + s2
    plt.stem(range(max_len), added)
    plt.title("Signal Addition")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return added

def signal_multiplication(signal1, signal2):
    """
    Multiplies two signals element-wise.
    Pads shorter signal with zeros if lengths differ.
    """
    max_len = max(len(signal1), len(signal2))
    s1 = np.pad(signal1, (0, max_len - len(signal1)))
    s2 = np.pad(signal2, (0, max_len - len(signal2)))
    multiplied = s1 * s2
    plt.stem(range(max_len), multiplied)
    plt.title("Signal Multiplication")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return multiplied