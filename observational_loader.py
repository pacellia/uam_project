# observational_loader.py
import numpy as np

def load_cmb_spectrum():
    """
    Simulated CMB power spectrum data.
    Replace with actual file loading if available.
    """
    ℓ = np.arange(2, 2000)
    spectrum = np.exp(-ℓ/500) + np.random.normal(0, 0.01, len(ℓ))
    return spectrum

def load_bao_data():
    """
    Simulated BAO clustering scale data.
    Replace with actual file loading if available.
    """
    z = np.linspace(0.1, 2.0, 50)
    scale = 150 * (1 + z)**(-1) + np.random.normal(0, 2, len(z))
    return scale

def load_planck_binned_power(filepath):
    """
    Loads binned Planck CMB power spectrum data from text file.

    Parameters:
        filepath (str): Path to Planck binned CMB file

    Returns:
        tuple of ndarray: (ℓ, D_l)
    """
    data = np.loadtxt(filepath, skiprows=1)
    ℓ = data[:, 0]      # Multipole moment
    D_l = data[:, 1]    # Power spectrum amplitude
    return ℓ, D_l
