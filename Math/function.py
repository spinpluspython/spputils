# -*- coding: utf-8 -*-
"""

@author: Steinn Ymir Agustsson
"""
import numpy as np


def main():
    pass


def gaussian(x, mu, sig):
    """ one dimensional gaussian function.
    Parameters:
        x (1d array): coordinate axis
        mu (float):  mean or expectation of the distribution
        sig (float): standard deviation
    """
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

def lorentz(p,x):
    return p[2] / (1.0 + (x / p[0] - 1.0)**4 * p[1]**2)

def errorfunc(p, x, z):
    return lorentz(p, x) - z

if __name__ == '__main__':
    main()
