import numpy as np
import matplotlib.pyplot as plt
from observational_loader import load_planck_binned_power
from uam_core import baseline_projection

def run_baseline(planck_path, plot=True):
    """
    Computes baseline projection of Planck $D_\\ell$ without bifurcation.

    Args:
        planck_path (str): Path to Planck data file
        plot (bool): Whether to show comparison figure

    Returns:
        dict: Contains original data, baseline projection, multipoles
    """
    ℓ, D_l = load_planck_binned_power(planck_path)
    model = baseline_projection(D_l)

    if plot:
        plt.figure(figsize=(8,5))
        plt.plot(ℓ, D_l, label='Planck $D_\\ell$', lw=1.5)
        plt.plot(ℓ, model.data, label='UAM Baseline Projection', lw=1.5)
        plt.xlabel('Multipole moment $\\ell$')
        plt.ylabel('$D_\\ell$ amplitude')
        plt.title('UAM Baseline vs Planck Data')
        plt.legend()
        plt.tight_layout()
        plt.show()

    return {
        'multipole': ℓ,
        'original_Dl': D_l,
        'projected_Dl': model.data
    }

if __name__ == "__main__":
    planck_path = "data/planck/COM_PowerSpect_CMB-TT-binned_R3.01.txt"
    output = run_baseline(planck_path)
