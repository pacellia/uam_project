import numpy as np

class BaselineModel:
    def __init__(self, data):
        self.data = self.project(data)

    def project(self, spectrum):
        # Simple smoothing + scale adjustment (example logic)
        smoothed = np.convolve(spectrum, np.ones(5)/5, mode='same')
        scaled = smoothed * 0.97  # empirical tuning
        return scaled

def baseline_projection(spectrum):
    """
    Constructs baseline UAM projection without bifurcation.

    Args:
        spectrum (np.ndarray): Planck binned D_ell array

    Returns:
        BaselineModel: Contains projected data
    """
    return BaselineModel(spectrum)
