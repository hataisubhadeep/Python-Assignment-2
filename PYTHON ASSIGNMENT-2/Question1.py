#Question 1: Perform a Fast Fourier Transform (FFT) on a sine wave signal and visualize both the original signal and its frequency spectrum.

import numpy as np
import matplotlib.pyplot as plt

# Parameters for the sine wave
Fs = 1000  # Sampling frequency (samples per second)
T = 1.0 / Fs  # Sampling interval (seconds)
t = np.arange(0, 1, T)  # Time vector (1 second)

f = 5  # Frequency of the sine wave (Hz)
A = 1  # Amplitude of the sine wave

# Generate the sine wave signal
signal = A * np.sin(2 * np.pi * f * t)

# Perform FFT
N = len(signal)
fft_signal = np.fft.fft(signal)
fft_signal = fft_signal[0:N//2]  # Keep only the positive frequencies
frequencies = np.fft.fftfreq(N, T)[:N//2]

# Calculate the magnitude of the FFT
magnitude = np.abs(fft_signal)

# Plot the original signal
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title("Original Sine Wave Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# Plot the frequency spectrum
plt.subplot(2, 1, 2)
plt.plot(frequencies, magnitude)
plt.title("Frequency Spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")

# Show the plots
plt.tight_layout()
plt.show()
