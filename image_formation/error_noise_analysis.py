import numpy as np
import matplotlib.pyplot as plt

mean = 0
std_dev = 0.1 
num_samples = 500
quant_levels = 32

def generate_signal(num_samples):
    x = np.linspace(0, 2*np.pi, num_samples)
    signal = np.sin(x)
    return x, signal

def add_Gaussian_noise(signal, mean, std):
    mag = np.max(signal) - np.min(signal)
    noise = np.random.normal(mean, std * mag, len(signal))
    return signal + noise

def sample_signal(signal, step):
    return signal[::step]


def quantize_signal(signal, num_levels):
    min_val, max_val = np.min(signal), np.max(signal)
    step = (max_val - min_val) / num_levels
    quantized = np.floor((signal - min_val) / step) * step + min_val
    return quantized


def mean_square_error(original, noisy):
    return np.mean((original - noisy) ** 2)

def root_mean_square_error(original, noisy):
    return np.sqrt(mean_square_error(original, noisy))

def peak_signal_to_noise_ratio(original, noisy):
    mse = mean_square_error(original, noisy)
    peak = np.max(np.abs(original))
    if mse == 0:
        return np.inf
    return 10 * np.log10(peak ** 2 / mse)


def plot_signals(x, original, noisy, quantized):
    plt.figure(figsize=(10, 6))
    plt.plot(x, original, label="Original Signal")
    plt.plot(x, noisy, label="Noisy Signal", alpha=0.7)
    plt.plot(x, quantized, label="Quantized Noisy Signal", linestyle='--', alpha=0.5)
    plt.title("Signal with Gaussian Noise and Quantization")
    plt.xlabel("x")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.show()


x, signal = generate_signal(num_samples)
noisy_signal = add_Gaussian_noise(signal, mean, std_dev)
quantized_signal = quantize_signal(noisy_signal, quant_levels)

mse = mean_square_error(signal, noisy_signal)
rmse = root_mean_square_error(signal, noisy_signal)
psnr = peak_signal_to_noise_ratio(signal, noisy_signal)

print(f"MSE: {mse:.6f}")
print(f"RMSE: {rmse:.6f}")
print(f"PSNR: {psnr:.2f} dB")

plot_signals(x, signal, noisy_signal, quantized_signal)
