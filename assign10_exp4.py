"""Take N (N >= 10) random 2-dimensional points represented in cartesian coordinate space.
Store them in a numpy array. Convert them to polar coordinates."""

import numpy as np

def cartesian_to_polar(points):
    x = points[:, 0]
    y = points[:, 1]
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    polar = np.column_stack((r, theta))
    return polar

N = 10 
cartesian_points = np.random.uniform(low=-10.0, high=10.0, size=(N, 2))

polar_points = cartesian_to_polar(cartesian_points)

print("Cartesian Coordinates:\n", cartesian_points)
print("\nPolar Coordinates (r, θ):\n", polar_points)
