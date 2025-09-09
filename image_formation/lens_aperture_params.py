import numpy as np
import matplotlib.pyplot as plt

def thin_lens(f, z0):
        return 1 / (1/f - 1/z0) 

focal_lengths = [3, 9, 50, 200]
colors = ['b', 'g', 'r', 'm']
z_minmax = [(1.1 * f, 104 * f) for f in focal_lengths]

plt.figure(figsize = (8,6))
for f, col in zip(focal_lengths, colors):
    z0 = np.linspace(1.1 * f, 104 * f, int(104 * f -1.1 * f) * 4)
    zi = thin_lens(f, z0)
    plt.loglog(z0, zi, color = col, label = f'f = {f} mm')
    plt.axvline(f, color=col, linestyle='--', alpha=0.7)

plt.xlabel('Object Distance z0 (mm)')
plt.ylabel('Image Distance zi (mm)')
plt.ylim([0, 3000])
plt.legend()
plt.grid(True, which="both", ls=':', linewidth=0.7)
plt.title('Thin Lens Equation: 1/f = 1/z0 + 1/zi')
plt.tight_layout()
plt.show()