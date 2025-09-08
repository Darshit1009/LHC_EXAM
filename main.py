import numpy as np
import matplotlib.pyplot as plt
from Signal_ICT_Darshit_kacha_92400133089 import (
    unit_step,
    unit_impulse,
    ramp_signal,
    sine_wave,
    cosine_wave,
    time_shift,
    time_scale,
    signal_addition,
    signal_multiplication
)
# 1. Generate and plot a unit step and unit impulse signal of length 20
n = 20
print("Generating unit step and unit impulse signals...")
step = unit_step(n)
impulse = unit_impulse(n)

# 2. Generate a sine wave of amplitude 2, frequency 5 Hz, phase 0, over t = 0 to 1 sec
t = np.linspace(0, 1, 500)
print("Generating sine wave...")
sine = sine_wave(A=2, f=5, phi=0, t=t)

# 3. Perform time shifting on the sine wave (discretized) by +5 units
print("Performing time shift on sine wave...")
sine_discrete = sine[:n]  # truncate to match discrete length
shifted_sine = time_shift(sine_discrete, 5)

# Plot original vs shifted discrete sine
plt.figure()
plt.stem(range(n), sine_discrete, label="Original Sine")
plt.stem(range(n), shifted_sine, label="Shifted Sine (+5)")
plt.title("Original vs Shifted Sine Wave (Discrete)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

# 4. Perform addition of unit step and ramp signal
print("Adding unit step and ramp signals...")
ramp = ramp_signal(n)
added = signal_addition(step, ramp)

# 5. Multiply sine and cosine waves (discretized)
print("Multiplying sine and cosine waves...")
cosine = cosine_wave(A=2, f=5, phi=0, t=t)
cosine_discrete = cosine[:n]
product = signal_multiplication(sine_discrete, cosine_discrete)

# Plot product of sine and cosine
plt.figure()
plt.stem(range(n), product)
plt.title("Sine × Cosine Wave (Discrete)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# 6. Optional: Time scaling
print("Performing time scaling on ramp signal...")
scaled_ramp = time_scale(ramp, 2)