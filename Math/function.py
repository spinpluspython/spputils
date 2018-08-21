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

def expfunc_const(x, A, t0, c):
    labels = ['A', 't0', 'c']
    return A * (1 - np.exp(- x / t0)) + c

def double_exponential_pos_neg(x, A1, t1, A2, t2, d):
    labels = ['A1', 't1', 'A2', 't2', 'c', 'd']
    return A1 * (1 - np.exp(- x / t1)) + A2 * (1 - np.exp(- x / t2)) + d

def expFunc_lin_const(x, A, t0, c, d):
    labels = ['A', 't0', 'c', 'd']
    return A * (1 - np.exp(- x / t0)) + c * x + d




if __name__ == '__main__':
    main()
