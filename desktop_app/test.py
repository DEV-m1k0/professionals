import os
import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QFormLayout, QFrame, QGridLayout,
                               QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
                               QWidget, QLabel, QVBoxLayout, QDialog, QDialogButtonBox)




class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(417, 120)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setAlignment(Qt.AlignCenter)
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0412\u044b \u0443\u0432\u0435\u0440\u0435\u043d\u044b?", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u0430", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u041d\u0435\u0442", None))


class Widget(QWidget, Ui_Form): 
    def __init__(self):
        super(Widget, self).__init__()
        self.setupUi(self)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(808, 510)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.image_label = QLabel(alignment=Qt.AlignCenter)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setPixmap(QPixmap("head3.png"))
        lay = QVBoxLayout(self.frame)
        lay.addWidget(self.image_label)

        self.widget = QWidget(self.image_label)
        self.widget.setObjectName(u"widget")

        self.formLayout = QFormLayout(self.widget)  # - (self.frame)
        self.formLayout.setObjectName(u"formLayout")

        self.pushButton = QPushButton()  # - (self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(50, 30))
        self.pushButton.setMaximumSize(QSize(16777214, 16777215))
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.formLayout.setItem(0, QFormLayout.LabelRole, self.verticalSpacer)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Test", None))


# +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
class Dialog(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        
        lbl = QLabel("please click something ...")
        lbl.setObjectName(u"lbl")
        buttonCancel = QPushButton('Cancel')
        buttonApply = QPushButton('Apply')
            
        layout = QGridLayout(self)            
        layout.addWidget(lbl, 0, 0, 1, 2, alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(buttonCancel, 1, 0)
        layout.addWidget(buttonApply, 1, 1)

        buttonApply.clicked.connect(self.apply)
        buttonCancel.clicked.connect(self._reject)
        
    def apply(self):
        print("Dialog: in apply") 

    def _reject(self): 
        self.parent.hide()    

    def closeEvent(self, event): 
        self.parent.hide()


class Window(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)        
        self.setObjectName(u"window")

        self.dialog = Dialog(self)
        self.dialog.setObjectName(u"dialog")
        
        gridLayout = QGridLayout(self) 
        gridLayout.addWidget(self.dialog, 1, 1, 1, 1)
        
        gridLayout.setColumnStretch(0, 1)
        gridLayout.setColumnStretch(1, 2)
        gridLayout.setColumnStretch(2, 1)
        gridLayout.setRowStretch(0, 1)
        gridLayout.setRowStretch(1, 2)
        gridLayout.setRowStretch(2, 1)
# +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
        

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setMouseTracking(True)
        self.setupUi(self)

# +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        self.pushButton.clicked.connect(self.create_dialog) 
        
        self.window = Window(self)
        self.window.hide()
        
    def create_dialog(self):
        self.window.resize(self.size()) 
        self.window.show()
        
    def resizeEvent(self, event):                                    
        self.window.resize(self.size()) 
# +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 


Stylesheet = """
#centralwidget {
    background-color:  rgb(37, 237, 37);
}
#frame {
    background-color:  rgb(37, 37, 237);
}

#pushButton {
    background-color: rgba(233, 33, 33, 0.7);
    color: #bfbfbf;
}
#image_label {
    background-color:  rgb(137, 137, 237);
}
#window {
    background-color: rgba(233, 33, 33, 0.5);
    color: #bfbfbf;
}
#dialog {
    background-color: rgba(133, 133, 233, 0.7);
    color: #406343;
}
#lbl {
    color: #FFF;
    font-size: 22px;
}
"""

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyleSheet(Stylesheet)  
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())