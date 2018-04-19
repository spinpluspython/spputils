# -*- coding: utf-8 -*-
"""

@author: Steinn Ymir Agustsson
"""
import sys
from PyQt5 import QtWidgets

def main():
    pass

def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

def raise_Qerror(self, doingWhat, errorHandle, type='Warning', popup=True):
    """ opens a dialog window showing the error"""
    errorMessage = 'Thread Error while {0}:\n{1}'.format(doingWhat,errorHandle)
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