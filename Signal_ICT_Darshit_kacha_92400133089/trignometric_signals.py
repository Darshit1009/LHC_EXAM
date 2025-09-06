import numpy as np
import matplotlib.pyplot as plt

def sine_wave(A, f, phi, t):
    """
    Generates a sine wave: y(t) = A * sin(2πft + φ)
    
    Parameters:
        A (float): Amplitude
        f (float): Frequency in Hz
        phi (float): Phase in radians
        t (ndarray): Time vector
    
    Returns:
        ndarray: Sine wave signal
    """
    y = A * np.sin(2 * np.pi * f * t + phi)
    plt.plot(t, y)
    plt.title("Sine Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return y

def cosine_wave(A, f, phi, t):
    """
    Generates a cosine wave: y(t) = A * cos(2πft + φ)
    
    Parameters:
        A (float): Amplitude
        f (float): Frequency in Hz
        phi (float): Phase in radians
        t (ndarray): Time vector
    
    Returns:
        ndarray: Cosine wave signal
    """
    y = A * np.cos(2 * np.pi * f * t + phi)
    plt.plot(t, y)
    plt.title("Cosine Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return y

def exponential_signal(A, a, t):
    """
    Generates an exponential signal: y(t) = A * exp(a * t)
    
    Parameters:
        A (float): Initial amplitude
        a (float): Growth/decay rate
        t (ndarray): Time vector
    
    Returns:
        ndarray: Exponential signal
    """
    y = A * np.exp(a * t)
    plt.plot(t, y)
    plt.title("Exponential Signal")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return y