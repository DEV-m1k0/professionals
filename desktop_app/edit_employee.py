# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_employee.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(700, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(700, 600))
        Dialog.setMaximumSize(QSize(700, 600))
        Dialog.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setStyleSheet(u"background-color: white;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 310, 818))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: black;")

        self.verticalLayout_2.addWidget(self.label_2)

        self.input_full_name_2 = QLineEdit(self.scrollAreaWidgetContents)
        self.input_full_name_2.setObjectName(u"input_full_name_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input_full_name_2.sizePolicy().hasHeightForWidth())
        self.input_full_name_2.setSizePolicy(sizePolicy1)
        self.input_full_name_2.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setKerning(True)
        self.input_full_name_2.setFont(font)
        self.input_full_name_2.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	color: black;\n"
"	border: 1px solid black;\n"
"}")

        self.verticalLayout_2.addWidget(self.input_full_name_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: black;")

        self.verticalLayout_6.addWidget(self.label_6)

        self.input_date_of_birth_2 = QDateEdit(self.scrollAreaWidgetContents)
        self.input_date_of_birth_2.setObjectName(u"input_date_of_birth_2")
        sizePolicy1.setHeightForWidth(self.input_date_of_birth_2.sizePolicy().hasHeightForWidth())
        self.input_date_of_birth_2.setSizePolicy(sizePolicy1)
        self.input_date_of_birth_2.setMinimumSize(QSize(0, 30))
        self.input_date_of_birth_2.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	color: black;\n"
"	border: 1px solid black;\n"
"}")

        self.verticalLayout_6.addWidget(self.input_date_of_birth_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: black;")

        self.verticalLayout_7.addWidget(self.label_7)

        self.input_home_number_2 = QLineEdit(self.scrollAreaWidgetContents)
        self.input_home_number_2.setObjectName(u"input_home_number_2")
        sizePolicy1.setHeightForWidth(self.input_home_number_2.sizePolicy().hasHeightForWidth())
        self.input_home_number_2.setSizePolicy(sizePolicy1)
        self.input_home_number_2.setMinimumSize(QSize(0, 30))
        self.input_home_number_2.setFont(font)
        self.input_home_number_2.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	color: black;\n"
"	border: 1px solid black;\n"
"}")

        self.verticalLayout_7.addWidget(self.input_home_number_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: black;")

        self.verticalLayout_3.addWidget(self.label_3)

        self.input_work_phone = QLineEdit(self.scrollAreaWidgetContents)
        self.input_work_phone.setObjectName(u"input_work_phone")
        sizePolicy1.setHeightForWidth(self.input_work_phone.sizePolicy().hasHeightForWidth())
        self.input_work_phone.setSizePolicy(sizePolicy1)
        self.input_work_phone.setMinimumSize(QSize(0, 30))
        self.input_work_phone.setFont(font)
        self.input_work_phone.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	color: black;\n"
"	border: 1px solid black;\n"
"}")

        self.verticalLayout_3.addWidget(self.input_work_phone)


        self.verticalLayout_9.addLayout(self.verticalLayout_3)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: black;")

        self.verticalLayout_8.addWidget(self.label_8)

        self.input_work_email = QLineEdit(self.scrollAreaWidgetContents)
        self.input_work_email.setObjectName(u"input_work_email")
        sizePolicy1.setHeightForWidth(self.input_work_email.sizePolicy().hasHeightForWidth())
        self.input_work_email.setSizePolicy(sizePolicy1)
        self.input_work_email.setMinimumSize(QSize(0, 30))
        self.input_work_email.setFont(font)
        self.input_work_email.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	color: black;\n"
"	border: 1px solid black;\n"
"}")

        self.verticalLayout_8.addWidget(self.input_work_email)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: black;")

        self.verticalLayout_13.addWidget(self.label_13)

        self.optional_job_titles = QComboBox(self.scrollAreaWidgetContents)
        self.optional_job_titles.setObjectName(u"optional_job_titles")
        sizePolicy1.setHeightForWidth(self.optional_job_titles.sizePolicy().hasHeightForWidth())
        self.optional_job_titles.setSizePolicy(sizePolicy1)
        self.optional_job_titles.setMinimumSize(QSize(0, 30))
        self.optional_job_titles.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_13.addWidget(self.optional_job_titles)


        self.verticalLayout_9.addLayout(self.verticalLayout_13)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: black;")

        self.verticalLayout_11.addWidget(self.label_11)

        self.optional_cabinets = QComboBox(self.scrollAreaWidgetContents)
        self.optional_cabinets.setObjectName(u"optional_cabinets")
        sizePolicy1.setHeightForWidth(self.optional_cabinets.sizePolicy().hasHeightForWidth())
        self.optional_cabinets.setSizePolicy(sizePolicy1)
        self.optional_cabinets.setMinimumSize(QSize(0, 30))
        self.optional_cabinets.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_11.addWidget(self.optional_cabinets)


        self.verticalLayout_9.addLayout(self.verticalLayout_11)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: black;")

        self.verticalLayout_14.addWidget(self.label_9)

        self.optional_boss = QComboBox(self.scrollAreaWidgetContents)
        self.optional_boss.setObjectName(u"optional_boss")
        sizePolicy1.setHeightForWidth(self.optional_boss.sizePolicy().hasHeightForWidth())
        self.optional_boss.setSizePolicy(sizePolicy1)
        self.optional_boss.setMinimumSize(QSize(0, 30))
        self.optional_boss.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_14.addWidget(self.optional_boss)


        self.verticalLayout_9.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: black;")

        self.verticalLayout_15.addWidget(self.label_14)

        self.optional_helpers_2 = QComboBox(self.scrollAreaWidgetContents)
        self.optional_helpers_2.setObjectName(u"optional_helpers_2")
        sizePolicy1.setHeightForWidth(self.optional_helpers_2.sizePolicy().hasHeightForWidth())
        self.optional_helpers_2.setSizePolicy(sizePolicy1)
        self.optional_helpers_2.setMinimumSize(QSize(0, 30))
        self.optional_helpers_2.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_15.addWidget(self.optional_helpers_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 20))
        self.label_15.setStyleSheet(u"color: black;")

        self.verticalLayout_16.addWidget(self.label_15)

        self.optional_organizations = QComboBox(self.scrollAreaWidgetContents)
        self.optional_organizations.setObjectName(u"optional_organizations")
        sizePolicy1.setHeightForWidth(self.optional_organizations.sizePolicy().hasHeightForWidth())
        self.optional_organizations.setSizePolicy(sizePolicy1)
        self.optional_organizations.setMinimumSize(QSize(0, 30))
        self.optional_organizations.setMaximumSize(QSize(16777215, 30))
        self.optional_organizations.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_16.addWidget(self.optional_organizations)


        self.verticalLayout_9.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)
        self.label_16.setMaximumSize(QSize(16777215, 20))
        self.label_16.setStyleSheet(u"color: black;")

        self.verticalLayout_17.addWidget(self.label_16)

        self.optional_sub_divisions = QComboBox(self.scrollAreaWidgetContents)
        self.optional_sub_divisions.setObjectName(u"optional_sub_divisions")
        sizePolicy1.setHeightForWidth(self.optional_sub_divisions.sizePolicy().hasHeightForWidth())
        self.optional_sub_divisions.setSizePolicy(sizePolicy1)
        self.optional_sub_divisions.setMinimumSize(QSize(0, 30))
        self.optional_sub_divisions.setMaximumSize(QSize(16777215, 30))
        self.optional_sub_divisions.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_17.addWidget(self.optional_sub_divisions)


        self.verticalLayout_9.addLayout(self.verticalLayout_17)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 20))
        self.label_10.setStyleSheet(u"color: black;")

        self.verticalLayout_10.addWidget(self.label_10)

        self.optional_department = QComboBox(self.scrollAreaWidgetContents)
        self.optional_department.setObjectName(u"optional_department")
        sizePolicy1.setHeightForWidth(self.optional_department.sizePolicy().hasHeightForWidth())
        self.optional_department.setSizePolicy(sizePolicy1)
        self.optional_department.setMinimumSize(QSize(0, 30))
        self.optional_department.setMaximumSize(QSize(16777215, 30))
        self.optional_department.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_10.addWidget(self.optional_department)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)

        self.btn_save = QPushButton(self.scrollAreaWidgetContents)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(0, 35))
        self.btn_save.setStyleSheet(u"background-color: green;\n"
"")

        self.verticalLayout_9.addWidget(self.btn_save)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setStyleSheet(u"background-color: white;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 35))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(18)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: red;\n"
"")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_4.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0424\u0418\u041e:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0414\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u043c\u0430\u0448\u043d\u0438\u0439 \u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430:", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0431\u043e\u0447\u0430\u044f \u043f\u043e\u0447\u0442\u0430:", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u0431\u0438\u043d\u0435\u0442:", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0438\u043a:", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043c\u043e\u0449\u043d\u0438\u043a:", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f:", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435:", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0434\u0435\u043b:", None))
        self.btn_save.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0423\u0432\u043e\u043b\u0438\u0442\u044c", None))
    # retranslateUi

