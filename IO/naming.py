# -*- coding: utf-8 -*-
"""

@author: Steinn Ymir Agustsson
"""


def main():
    pass


def camelCaseIt(snake_str):
    """ transform a snake string into camelCase

    Parameters:
        snake_str (str): snake_case style string
    Returns
        camelCaseStr (str): camelCase style of the input string.
    """
    first, *others = snake_str.split('_')
    return ''.join([first.lower(), *map(str.title, others)])


if __name__ == '__main__':
    main()
