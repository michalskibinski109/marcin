import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def first_order_lowpass(s: np.ndarray) -> np.ndarray:
    """First order lowpass filter."""
    b, a = signal.butter(3, 0.05)
    zi = signal.lfilter_zi(b, a)
    z, _ = signal.lfilter(b, a, s, zi=zi * s[0])
    return z


def transform_angle(angle: np.ndarray) -> np.ndarray:

    """Transform angle to [-pi, pi]."""
    angle = angle * 4  # max angle is 90 degrees
    return (angle + np.pi) % (2 * np.pi) - np.pi
