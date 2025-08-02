import numpy as np
from scipy.stats import pearsonr

def compute_metrics(truth, prediction):
    """
    Evaluates projection fidelity with multiple metrics.

    Args:
        truth (np.ndarray): Reference Planck $D_\\ell$ values
        prediction (np.ndarray): Projected $D_\\ell$ from UAM

    Returns:
        dict: RMSE, MSE, Pearson r
    """
    residuals = truth - prediction
    mse = np.mean(residuals**2)
    rmse = np.sqrt(mse)
    r, _ = pearsonr(truth, prediction)

    return {
        'MSE': mse,
        'RMSE': rmse,
        'Pearson_r': r
    }

if __name__ == "__main__":
    # Demo: Plug in paths or arrays directly here
    from observational_loader import load_planck_binned_power
    from uam_core import baseline_projection

    planck_path = "data/planck/COM_PowerSpect_CMB-TT-binned_R3.01.txt"
    ℓ, D_l = load_planck_binned_power(planck_path)
    model = baseline_projection(D_l)

    metrics = compute_metrics(D_l, model.data)
    print("Fit metrics:")
    for k, v in metrics.items():
        print(f"{k}: {v:.5f}")
