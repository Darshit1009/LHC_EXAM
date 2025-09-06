# Signal_ICT_Darshit_kacha_92400133089

A modular signal processing toolkit built for ICT coursework. This package includes functions to generate unitary signals, trigonometric signals, and perform basic signal operations.

---

## 📦 Package Modules

- `unitary_signals.py`  
  - `unit_step(n)` – Generates a unit step signal  
  - `unit_impulse(n)` – Generates a unit impulse signal  
  - `ramp_signal(n)` – Generates a ramp signal  

- `trignometric_signals.py`  
  - `sine_wave(A, f, phi, t)` – Generates a sine wave  
  - `cosine_wave(A, f, phi, t)` – Generates a cosine wave  
  - `exponential_signal(A, a, t)` – Generates an exponential signal  

- `operations.py`  
  - `time_shift(signal, k)` – Shifts the signal by k units  
  - `time_scale(signal, k)` – Scales the time axis  
  - `signal_addition(signal1, signal2)` – Adds two signals  
  - `signal_multiplication(signal1, signal2)` – Multiplies two signals  

---

## ⚙️ Installation

### 🔹 From Wheel (Local)
```bash
pip install dist/Signal_ICT_Darshit_kacha_92400133089-0.1.0-py3-none-any.whl

## 📝 License

This project is licensed under the MIT License. See the (LICENSE) file for details.

### 🔹 From PyPI
```bash
pip install Signal-ICT-Darshit-Kacha
## 📚 Requirements

- Python 3.7+
- NumPy
- Matplotlib