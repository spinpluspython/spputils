# -*- coding: utf-8 -*-
"""

@author: Steinn Ymir Agustsson
"""
import numpy as np


def main():
    pass


def get_multiple_maxima(array, radius, number):
    maxima = []
    temp_array = array.copy()
    peaks = np.ndarray((number, radius * 2, radius * 2))
    # plt.imshow(dark_avg)
    for i in range(number):
        x_max, y_max = maxima(temp_array)
        maxima.append((x_max, y_max))
        peaks[i, ...] = temp_array[x_max - radius:x_max + radius, y_max - radius:y_max + radius]

        temp_array[x_max - radius:x_max + radius, y_max - radius:y_max + radius] = 0

    return maxima, peaks

def maxima(array):
    return np.unravel_index(array.argmax(), array.shape)


if __name__ == '__main__':
    main()