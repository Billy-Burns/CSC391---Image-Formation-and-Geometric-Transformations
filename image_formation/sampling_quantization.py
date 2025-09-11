import numpy as np
import matplotlib.pyplot as plt

signal_freq = 5.0
duration = 2
sampling_freq = 8
num_bits = 3
min_signal = -1
max_signal = 1

def original_signal(t):
    return np.sin(2 * np.pi * signal_freq * t)

t_points = np.linspace(0, duration, 1000, endpoint=False)
cont_signal = original_signal(t_points)

plt.figure(figsize=(10, 6))
plt.plot(t_points, cont_signal, label='Continuous Signal', color='blue')

n_samples = int(sampling_freq * duration)
t_sampled = np.linspace(0, duration, n_samples, endpoint=False)
sampled_signal = original_signal(t_sampled)
plt.scatter(t_sampled, sampled_signal, color='k', label='Sampled Signal', zorder=5)

num_levels = 2 ** num_bits
qs = np.round((sampled_signal - min_signal) / (max_signal - min_signal) * (num_levels - 1))
qv = min_signal + qs * (max_signal - min_signal) / (num_levels - 1) 

plt.step(t_sampled, qv, where='post', color='red', label=f'Quantized Signal ({num_bits} bits)', linestyle = '--')

plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sampling and Quantization of a Sinusoidal Signal')
plt.ylim([min_signal-0.2, max_signal+0.2])
plt.legend()
plt.grid(True)
plt.show()
