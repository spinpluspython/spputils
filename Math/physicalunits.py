# -*- coding: utf-8 -*-
"""

@author: Steinn Ymir Agustsson
"""


def main():
    pass


def get_energy_density(spot_size=100, power=1, rep_rate=283000):
    """ Return energy density in microJoule /cm2
         spotsize as FWHM diameter of gaussian profile in micrometers
        power in mW
        reprate in Hz
    Parameters
        spot_size (float): FWHM of gaussian profile of laser spot in µm
        power (float): laser power in mW
        rep_rate (float): laser repetition rate in Hz
    Returns
        energy_density (float): laser energy density in µJ /cm2
    """
    area = ((spot_size / 2) ** 2 * spconst.pi) / 10 ** 8
    return (power / (rep_rate * area))


def get_nyquist_frequency(timedata):
    """returns the Nyquist frequency from time data
    Parameters:
        timedata (list,array): equally spaced time axis
    returns:
        nyq_freq (float): corresponding Nyquist frequency
    """
    return (abs(0.5 * len(timedata) / timedata[-1] - timedata[0]))


if __name__ == '__main__':
    main()
