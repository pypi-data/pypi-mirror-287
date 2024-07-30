from AnyQt.QtWidgets import QLineEdit, QApplication
from AnyQt.QtGui import QIntValidator

from AnyQt.QtCore import Qt

from orangewidget.utils import getdeepattr
from orangewidget.gui import CallFrontLineEdit, connectControl




class IntLineEdit(QLineEdit):
    FAST_KEY = Qt.Key_Shift

    def __init__(self, master, value=None, label=None, labelWidth=None, callback=None,
             valueType=None, bounds=None, controlWidth=None,
             callbackOnType=False, focusInCallback=None, **misc):
        
        super().__init__(master)
        self.faster = False
        self.slower = False
        self.bounds = bounds

        self.editingFinished.connect(self._ensureInt)
        
        if callbackOnType:
            self.textChanged.connect(callback)
        else:
            self.editingFinished.connect(callback)
        
        if bounds:
            self.validator = QIntValidator(*self.bounds)
        
        else:
            self.validator = QIntValidator()

        self.setValidator(self.validator)

        if controlWidth:
            self.setFixedWidth(controlWidth)

        current_value = getdeepattr(master, value) if value else 0
        self.setText(str(current_value))

        if value:
            self.cback = connectControl(
                master, value,
                callbackOnType and callback, self.textChanged[str],
                CallFrontLineEdit(self), fvcb=valueType or type(current_value))[1]
            
        
    def validate(self):
        return self.validator.validate(self.text(), self.cursorPosition())[0]
        

    def keyPressEvent(self, event):
        if event.key() == IntLineEdit.FAST_KEY:
            self.faster = True

        QLineEdit.keyPressEvent(self, event)


    def keyReleaseEvent(self, event):
        if event.key() == IntLineEdit.FAST_KEY:
            self.faster = False

        if event.key() == Qt.Key_Return:
            self.clearFocus()

        QLineEdit.keyReleaseEvent(self, event)


    def focusInEvent(self, event):
        self.setReadOnly(False)
        super().focusInEvent(event)

    
    def focusOutEvent(self, event):
        self.setReadOnly(True)
        self._ensureInt()
        super().focusOutEvent(event)

    
    def _ensureInt(self):
        if self.text().strip() == "":
            self.setText("0")

        self.validate()
        

        # elif '.' not in self.text():
        #     self.setText(self.text() + ".0")
    
    def wrap_increment(self, increment):
        value = int(self.text()) + increment

        if self.bounds is None:
            return value
        
        lower, upper = self.bounds

        span = upper - lower + 1

        return ((value - lower) % span) + lower
            
        
    def wheelEvent(self, event):
        delta = 1 if event.angleDelta().y() > 0 else -1

        modifiers = QApplication.keyboardModifiers()

        if modifiers == Qt.ShiftModifier:
        # if self.faster:
            delta *= 10

        new_value = self.wrap_increment(int(delta))

        self.setText(str(new_value))
        event.accept()