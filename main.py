import numpy as np
from Signal_ICT_Darshit_kacha_92400133089 import (
    unit_step,
    unit_impulse,
    ramp_signal,
    sine_wave,
    cosine_wave,
    time_shift,
    signal_addition,
    signal_multiplication
)
import matplotlib.pyplot as plt

# 1. Generate and plot a unit step signal and a unit impulse signal of length 20
n = 20
print("Generating unit step and unit impulse signals...")
step = unit_step(n)
impulse = unit_impulse(n)

# 2. Generate a sine wave of amplitude 2, frequency 5 Hz, phase 0, over t = 0 to 1 sec
t = np.linspace(0, 1, 500)
print("Generating sine wave...")
sine = sine_wave(A=2, f=5, phi=0, t=t)

# 3. Perform time shifting on the sine wave by +5 units and plot both original and shifted signals
print("Performing time shift on sine wave...")
shifted_sine = time_shift(sine, 5)

plt.figure()
plt.plot(t, sine, label="Original Sine")
plt.plot(t, shifted_sine, label="Shifted Sine (+5)")
plt.title("Original vs Shifted Sine Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

# 4. Perform addition of the unit step and ramp signal and plot the result
print("Adding unit step and ramp signals...")
ramp = ramp_signal(n)
added = signal_addition(step, ramp)

# 5. Multiply a sine and cosine wave of same frequency and plot the result
print("Multiplying sine and cosine waves...")
cosine = cosine_wave(A=2, f=5, phi=0, t=t)
product = signal_multiplication(sine, cosine)

plt.figure()
plt.plot(t, product)
plt.title("Sine × Cosine Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()