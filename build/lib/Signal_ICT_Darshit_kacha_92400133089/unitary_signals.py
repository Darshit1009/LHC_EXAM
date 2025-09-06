import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    """Generates a unit step signal of length n."""
    signal = np.ones(n)
    plt.stem(range(n), signal)
    plt.title("Unit Step Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal

def unit_impulse(n):
    """Generates a unit impulse signal of length n."""
    signal = np.zeros(n)
    signal[0] = 1
    plt.stem(range(n), signal)
    plt.title("Unit Impulse Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal

def ramp_signal(n):
    """Generates a ramp signal of length n."""
    signal = np.arange(n)
    plt.stem(range(n), signal)
    plt.title("Ramp Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal