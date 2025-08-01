"""
UAM Cosmological Simulation Script
Generates angular power spectra and BAO scale predictions based on Unified Angular Mathematics.
"""

import numpy as np
import pandas as pd
from scipy.integrate import quad
import matplotlib.pyplot as plt

def compute_power_spectrum(l_values):
    # Placeholder function — replace with UAM-based calculation
    Dl_values = [220 + 5*np.sin(l / 25.0) for l in l_values]
    return Dl_values

def main():
    l_values = np.arange(2, 2501)
    Dl_values = compute_power_spectrum(l_values)

    spectrum_df = pd.DataFrame({'l': l_values, 'Dl': Dl_values})
    spectrum_df.to_csv('data/cmb_spectrum.csv', index=False)
    print("Simulation complete. Output saved to data/cmb_spectrum.csv.")

if __name__ == "__main__":
    main()
