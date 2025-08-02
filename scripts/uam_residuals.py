import numpy as np
import matplotlib.pyplot as plt
from observational_loader import load_planck_binned_power
from uam_holography import bifurcation_projection

def compute_residuals(planck_path, delta_theta=np.pi/6, normalize=True, plot=True):
    """
    Calculates residuals between Planck data and UAM projection.

    Args:
        planck_path (str): Path to Planck data file
        delta_theta (float): Angular bifurcation offset
        normalize (bool): Scale residuals to Planck power
        plot (bool): Display residual plot

    Returns:
        dict: ℓ, residuals, RMSE
    """
    ℓ, D_l = load_planck_binned_power(planck_path)
    result = bifurcation_projection(D_l, delta_theta=delta_theta)
    projection = result.data
    residual = D_l - projection

    if normalize:
        residual /= D_l

    rmse = np.sqrt(np.mean(residual**2))

    if plot:
        plt.figure(figsize=(7,4))
        plt.plot(ℓ, residual, label='Residuals', lw=1.5)
        plt.axhline(0, color='gray', ls='--', lw=0.8)
        plt.xlabel('Multipole moment $\\ell$')
        plt.ylabel('Residuals (normalized)' if normalize else 'Residuals')
        plt.title(f'Residuals vs Planck: Δθ = {delta_theta:.2f} rad')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    return {
        'multipole': ℓ,
        'residuals': residual,
        'rmse': rmse
    }

if __name__ == "__main__":
    planck_path = "data/planck/COM_PowerSpect_CMB-TT-binned_R3.01.txt"
    output = compute_residuals(planck_path)
    print(f"RMSE: {output['rmse']:.5f}")
