# -*- coding: utf-8 -*-
"""

@author: Steinn Ymir Agustsson
"""


def main():
    pass

def camelCaseIt(snake_str):
    first, *others = snake_str.split('_')
    return ''.join([first.lower(), *map(str.title, others)])


if __name__ == '__main__':
    main()