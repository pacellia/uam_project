import numpy as np
import matplotlib.pyplot as plt
from observational_loader import load_planck_binned_power
from uam_holography import bifurcation_projection

def validate_projection(planck_path, delta_theta=np.pi / 6, plot=True):
    """
    Runs UAM bifurcation projection against Planck D_ell spectrum.

    Args:
        planck_path (str): Path to Planck binned power spectrum file
        delta_theta (float): Angular bifurcation offset
        plot (bool): Whether to display comparison plot

    Returns:
        dict: Contains projected data, original data, multipoles, and log-likelihood
    """
    ℓ, D_l = load_planck_binned_power(planck_path)
    result = bifurcation_projection(D_l, delta_theta=delta_theta)

    if plot:
        plt.figure(figsize=(8,5))
        plt.plot(ℓ, D_l, label='Planck $D_\\ell$', lw=1.5)
        plt.plot(ℓ, result.data, label='UAM Projected $D_\\ell$', lw=1.5)
        plt.xlabel('Multipole moment $\\ell$')
        plt.ylabel('$D_\\ell$ amplitude')
        plt.title('Planck vs UAM Bifurcation Projection')
        plt.legend()
        plt.tight_layout()
        plt.show()

    return {
        'multipole': ℓ,
        'original_Dl': D_l,
        'projected_Dl': result.data,
        'log_likelihood': result.model.log_likelihood(D_l)
    }

if __name__ == "__main__":
    planck_path = "data/planck/COM_PowerSpect_CMB-TT-binned_R3.01.txt"
    output = validate_projection(planck_path)
    print("Log-likelihood:", output['log_likelihood'])
