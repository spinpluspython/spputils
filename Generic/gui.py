# -*- coding: utf-8 -*-
"""

@author: Steinn Ymir Agustsson
"""
import sys

from PyQt5 import QtWidgets


def main():
    pass


def my_exception_hook(exctype, value, traceback):
    """ Exception handler for PyCharm

    Prints explicitly the exception occured, toghether with traceback and kills
    the process. This is usefull when launching GUI from PyCharm.

    parameters:
        exctype (): exception type.
        value (): information about the exception.
        traceback (): traceback of where the exception was generated.
    """
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


def raise_Qerror(self, doingWhat, errorHandle, type='Warning', popup=True):
    """ opens a dialog window showing the error

    Parameters:
        doingWhat (str): Brief description of what the code was doing when
            this exception was risen.
        errorHandle (error): handle to the exception generated.
        type (str): Gravity of the error: possible choices are "Warning" "Critical".
        popup (bool): if True, generates a popup window (pyqt) with description
            of the error.
    """
    errorMessage = 'Thread Error while {0}:\n{1}'.format(doingWhat, errorHandle)
    print(errorMessage)
    if popup:
        errorDialog = QtWidgets.QMessageBox()
        errorDialog.setText(errorMessage)
        if type == 'Warning':
            errorDialog.setIcon(QtWidgets.QMessageBox.Warning)
        elif type == 'Critical':
            errorDialog.setIcon(QtWidgets.QMessageBox.Critical)
        errorDialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        errorDialog.exec_()


if __name__ == '__main__':
    main()
