# -*- coding: utf-8 -*-
"""

@author: Steinn Ymir Agustsson
"""
import numpy as np


def main():
    pass


def get_multiple_maxima(array, radius, number, returnPeaks=False):
    """ Get a list of 'number' maxima in an array.

    Parameters:
        array (array): 2d data array
        radius (float): minimum distance between two distinct peaks.
        number (int): number of maxima to search for.
        returnPeaks (bool): if True, it returns peaks, a list of images of each
            detected peak.
    Returns:
        maxima (list): x-y coordinates of each maxima found.
        peaks (np.ndarray): returned if returnPeaks=True. Image zoom of each peak.

    """
    maxima = []
    temp_array = array.copy()
    peaks = np.ndarray((number, radius * 2, radius * 2))
    # plt.imshow(dark_avg)
    for i in range(number):
        x_max, y_max = maxima(temp_array)
        maxima.append((x_max, y_max))
        peaks[i, ...] = temp_array[x_max - radius:x_max + radius, y_max - radius:y_max + radius]

        temp_array[x_max - radius:x_max + radius, y_max - radius:y_max + radius] = 0
    if returnPeaks:
        return maxima, peaks
    else:
        return maxima

def maxima(array):
    """ get the index of the maximum value in a 2D array"""
    return np.unravel_index(array.argmax(), array.shape)


if __name__ == '__main__':
    main()