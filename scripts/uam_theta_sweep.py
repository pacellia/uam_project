import numpy as np
import matplotlib.pyplot as plt
from observational_loader import load_planck_binned_power
from uam_holography import bifurcation_projection

def theta_sweep(planck_path, theta_range=None, plot=True):
    """
    Evaluates projection fit across a range of angular bifurcations.

    Args:
        planck_path (str): Path to Planck binned power spectrum
        theta_range (np.ndarray): Angular bifurcation values in radians
        plot (bool): Whether to plot likelihood curve

    Returns:
        dict: Map of Δθ to log-likelihood
    """
    if theta_range is None:
        theta_range = np.linspace(np.pi/10, np.pi/2, 20)

    ℓ, D_l = load_planck_binned_power(planck_path)
    likelihoods = []

    for Δθ in theta_range:
        result = bifurcation_projection(D_l, delta_theta=Δθ)
        ℒ = result.model.log_likelihood(D_l)
        likelihoods.append(ℒ)

    if plot:
        plt.figure(figsize=(7,4))
        plt.plot(theta_range, likelihoods, marker='o', lw=1.5)
        plt.xlabel('Angular bifurcation Δθ (radians)')
        plt.ylabel('Log-likelihood')
        plt.title('Δθ Sensitivity Sweep')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    return dict(zip(theta_range, likelihoods))

if __name__ == "__main__":
    planck_path = "data/planck/COM_PowerSpect_CMB-TT-binned_R3.01.txt"
    results = theta_sweep(planck_path)
    optimal_theta = max(results, key=results.get)
    print(f"Optimal Δθ: {optimal_theta:.3f} rad")
