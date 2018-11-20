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

def gaussian_normalized(x, mu, sig):
    return gaussian(x, mu, sig) / np.sqrt(2*np.pi * sig**2)

def lorentzian_normalized(x,x0,Gamma):
    """ Normalized lorentz model.

    :param x: 1D data array
    :param Gamma: float
        FWHM
    :param x0: float
        Center
    :return:
        lorentzian model
    """
    num = .5 * Gamma
    den = np.pi**2 * (x-x0)**2 + (.5*Gamma)**2
    return num/den

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

def lorentz_real(x,s,w0,t):
    num = s**2 * (w0**2 - x**2)
    den = (w0**2 - x**2)**2 + x**2/t**-2
    return num/den

def lorentz_imag(x,s,w0,t):
    num = (s)**2 * x / t
    den = (w0**2 - x**2)**2 + x**2/t**-2
    return num/den


if __name__ == '__main__':
    main()
