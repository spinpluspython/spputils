# -*- coding: utf-8 -*-
"""

@author: Steinn Ymir Agustsson
"""
import numpy as np


def main():
    pass


def monotonically_increasing(l):
    """ make a list of values monotonically increasing.

    Parameters:
        l (list,array): disordered list.
    Returns
        ml (list,array): monotonically increasing reordered list.

    """
    return all(x < y for x, y in zip(l, l[1:]))

def monotonically_decreasing(l):
    """ make a list of values monotonically decreasing.

    Parameters:
        l (list,array): disordered list.
    Returns
        ml (list,array): monotonically decreasing reordered list.

    """
    return all(x > y for x, y in zip(l, l[1:]))


def cart2pol_array(cartesian, center=None):
    """ Transform an array in cartesian coordinates to polar coordinates.

    Parameters:
         cartesian (array of int,float): 2D array in cartesian coordinates.
         xc (int,float):
    """
    lenX = len(cartesian[:, 0])
    lenY = len(cartesian[0, :])

    if center == None:
        xc = int(lenX / 2)
        yc = int(lenY / 2)
    else:
        xc = center[0]
        yc = center[1]
    polar = np.zeros((lenX, lenY))
    for xi in range(lenX):
        for yi in range(lenY):
            x = xi - xc
            y = yi - yc

            rho = int(np.sqrt(x ** 2 + y ** 2))
            phi = int((np.arctan2(y, x) + np.pi) * np.pi)
            polar[rho, phi] += cartesian[xi, yi]
    return polar


if __name__ == '__main__':
    main()
