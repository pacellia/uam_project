import numpy as np

def chord_length(radius, angle_rad):
    """
    Computes chord length in a circle given radius and subtended angle.

    Args:
        radius (float): Radius of the sphere
        angle_rad (float): Angle in radians

    Returns:
        float: Chord length
    """
    return 2 * radius * np.sin(angle_rad / 2)

def sphere_wedge_area(radius, angle_rad):
    """
    Computes surface area of spherical wedge (angular sector on a sphere).

    Args:
        radius (float): Radius of sphere
        angle_rad (float): Central angle in radians

    Returns:
        float: Area of spherical wedge
    """
    return 2 * np.pi * radius**2 * (angle_rad / (2 * np.pi))

def angular_displacement_chord(x1, x2, radius):
    """
    Converts planar displacement to angular offset on sphere.

    Args:
        x1, x2 (np.ndarray): 3D coordinates
        radius (float): Sphere radius

    Returns:
        float: Angular displacement in radians
    """
    dot = np.dot(x1, x2)
    angle = np.arccos(np.clip(dot / radius**2, -1.0, 1.0))
    return angle
