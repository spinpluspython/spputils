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


if __name__ == '__main__':
    main()
