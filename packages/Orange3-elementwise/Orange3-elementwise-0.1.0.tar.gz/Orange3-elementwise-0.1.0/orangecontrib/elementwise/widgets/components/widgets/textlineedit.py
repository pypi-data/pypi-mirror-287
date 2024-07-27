from AnyQt import QtGui, QtWidgets

from orangewidget.utils import getdeepattr
from orangewidget.gui import CallFrontLineEdit, connectControl



class TextLineEdit(QtWidgets.QLineEdit):
    def __init__(self, master, value=None, label=None, labelWidth=None, callback=None,
             valueType=None, controlWidth=None,
             callbackOnType=False, focusInCallback=None, **misc):

        
        super().__init__(master)
        
        if callbackOnType:
            self.textChanged.connect(callback)
        else:
            self.editingFinished.connect(callback)

        if controlWidth:
            self.setFixedWidth(controlWidth)

        current_value = getdeepattr(master, value) if value else ""
        self.setText(current_value)

        if value:
            self.cback = connectControl(
                master, value,
                callbackOnType and callback, self.textChanged[str],
                CallFrontLineEdit(self), fvcb=valueType or type(current_value))[1]
