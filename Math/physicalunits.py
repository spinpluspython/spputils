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
    """
    area = ((spot_size / 2) ** 2 * spconst.pi) / 10 ** 8
    return (power / (rep_rate * area))


def get_nyquist_frequency(timedata):
    """returns the Nyquist frequency from time data"""
    return (abs(0.5 * len(timedata) / timedata[-1] - timedata[0]))



if __name__ == '__main__':
    main()