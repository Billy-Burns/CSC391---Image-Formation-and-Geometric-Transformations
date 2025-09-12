import numpy as np
import matplotlib.pyplot as plt

def thin_lens_zi(f, z0):
    return 1 / (1 / f - 1 / z0)

# Thin lens plot data
focal_lengths = [3, 9, 50, 200]
colors = ['b', 'g', 'r', 'm']

# Aperture diameter data
lens_specs = [
    (24, 1.4),
    (50, 1.8),
    (70, 2.8),
    (200, 2.8),
    (400, 2.8),
    (600, 4.0)
]
lens_names = [
    "24mm f/1.4",
    "50mm f/1.8",
    "70mm f/2.8",
    "200mm f/2.8",
    "400mm f/2.8",
    "600mm f/4.0"
]
def aperture_diameter(f, n):
    return f / n

apertures = [aperture_diameter(f, n) for f, n in lens_specs]

print("Lens Type           Focal Length (mm)   f-number   Aperture Diameter (mm)")
for name, (f, n), D in zip(lens_names, lens_specs, apertures):
    print(f"{name:<20} {f:<18} {n:<9} {D:<.2f}")

# Create side-by-side plots
fig, axs = plt.subplots(1, 2, figsize=(15, 6))

# Thin lens plot (left)
for f, col in zip(focal_lengths, colors):
    z0 = np.linspace(1.1 * f, 104 * f, int((104 * f - 1.1 * f) * 4))
    zi = thin_lens_zi(f, z0)
    axs[0].loglog(z0, zi, color=col, label=f'f = {f} mm')
    axs[0].axvline(f, color=col, linestyle='--', alpha=0.7)
axs[0].set_xlabel('Object Distance z0 (mm)')
axs[0].set_ylabel('Image Distance zi (mm)')
axs[0].set_ylim([0, 3000])
axs[0].legend()
axs[0].grid(True, which="both", ls=':', linewidth=0.7)
axs[0].set_title('Thin Lens Equation\n$1/f = 1/z_0 + 1/z_i$')

# Aperture diameter plot (right)
axs[1].bar(lens_names, apertures, color='c')
axs[1].set_ylabel('Aperture Diameter D (mm)')
axs[1].set_title('Aperture Diameter vs. Lens Spec')
axs[1].set_xticklabels(lens_names, rotation=30)
axs[1].grid(True, axis='y', ls=':', linewidth=0.7)

plt.tight_layout()
plt.show()
