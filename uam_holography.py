import numpy as np

def energy_partition_map(psi, phi0):
    """
    Computes the energy partitioning map in UAM formalism.

    Parameters:
        psi (float or ndarray): Angular deviation parameter
        phi0 (float): Initial bifurcation field value

    Returns:
        float or ndarray: Energy density map
    """
    return phi0 * np.cos(psi) + np.sin(psi)


def bifurcation_projection(data, delta_theta=np.pi / 6):
    """
    Projects input data using angular bifurcation logic.

    Parameters:
        data (ndarray): Observational dataset
        delta_theta (float): Angular offset

    Returns:
        object: Projection with transformed data and likelihood model
    """
    angular_factor = np.cos(delta_theta) + np.sin(delta_theta)
    projected = data * angular_factor

    class DummyModel:
        def log_likelihood(self, input_data):
            return -np.sum((input_data - projected) ** 2)

        num_params = 3

    return type("Projection", (), {"data": projected, "model": DummyModel()})
