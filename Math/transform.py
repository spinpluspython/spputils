# -*- coding: utf-8 -*-
"""

@author: Steinn Ymir Agustsson
"""
import numpy as np

def main():
    pass

def monotonically_increasing(l):
    return all(x < y for x, y in zip(l, l[1:]))

def cart2pol_array(cartesian, xc=None, yc=None):

    lenX = len(cartesian[:, 0])
    lenY = len(cartesian[0, :])

    if xc == None:
        xc = int(lenX / 2)
    if yc is None:
        yc = int(lenY / 2)

    polar = np.zeros((lenX, lenY))
    for xi in range(lenX):
        for yi in range(lenY):
            x = xi - xc
            y = yi - yc

            rho = int(np.sqrt(x ** 2 + y ** 2))
            phi = int((np.arctan2(y, x) + np.pi) * np.pi)
            #            print('rho:{} phi:{}'.format(rho,phi))
            polar[rho, phi] += cartesian[xi, yi]
    return polar


if __name__ == '__main__':
    main()