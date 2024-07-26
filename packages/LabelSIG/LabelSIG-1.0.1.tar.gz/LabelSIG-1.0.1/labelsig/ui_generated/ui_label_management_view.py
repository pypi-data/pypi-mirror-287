# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_label_management_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_input_dialog(object):
    def setupUi(self, input_dialog):
        input_dialog.setObjectName("input_dialog")
        input_dialog.resize(349, 250)
        input_dialog.setStyleSheet("background-color: rgb(220, 233, 243);")
        self.listWidget = QtWidgets.QListWidget(input_dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 90, 221, 151))
        self.listWidget.setStyleSheet("font: 15pt \"Bahnschrift Condensed\";\n"
"background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(input_dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 221, 21))
        self.lineEdit.setStyleSheet("font: 15pt \"Bahnschrift Condensed\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.widget_6 = QtWidgets.QWidget(input_dialog)
        self.widget_6.setGeometry(QtCore.QRect(0, 0, 351, 40))
        self.widget_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"黑体\";\n"
"background-color: rgb(48, 105, 176);")
        self.widget_6.setObjectName("widget_6")
        self.label_name_cfg_8 = QtWidgets.QLabel(self.widget_6)
        self.label_name_cfg_8.setGeometry(QtCore.QRect(45, 5, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label_name_cfg_8.sizePolicy().hasHeightForWidth())
        self.label_name_cfg_8.setSizePolicy(sizePolicy)
        self.label_name_cfg_8.setStyleSheet("\n"
"font: 20pt \'Bahnschrift Condensed\';")
        self.label_name_cfg_8.setObjectName("label_name_cfg_8")
        self.label_logo = QtWidgets.QLabel(self.widget_6)
        self.label_logo.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.button_max = QtWidgets.QPushButton(self.widget_6)
        self.button_max.setGeometry(QtCore.QRect(278, 10, 20, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_max.sizePolicy().hasHeightForWidth())
        self.button_max.setSizePolicy(sizePolicy)
        self.button_max.setStyleSheet("border: none;")
        self.button_max.setText("")
        self.button_max.setObjectName("button_max")
        self.button_close = QtWidgets.QPushButton(self.widget_6)
        self.button_close.setGeometry(QtCore.QRect(320, 10, 20, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_close.sizePolicy().hasHeightForWidth())
        self.button_close.setSizePolicy(sizePolicy)
        self.button_close.setStyleSheet("border: none;")
        self.button_close.setText("")
        self.button_close.setAutoDefault(True)
        self.button_close.setDefault(False)
        self.button_close.setObjectName("button_close")
        self.button_min = QtWidgets.QPushButton(self.widget_6)
        self.button_min.setGeometry(QtCore.QRect(236, 10, 20, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_min.sizePolicy().hasHeightForWidth())
        self.button_min.setSizePolicy(sizePolicy)
        self.button_min.setStyleSheet("border: none;")
        self.button_min.setText("")
        self.button_min.setObjectName("button_min")
        self.label_name_cfg_8.raise_()
        self.label_logo.raise_()
        self.button_max.raise_()
        self.button_min.raise_()
        self.button_close.raise_()
        self.layoutWidget = QtWidgets.QWidget(input_dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(250, 50, 91, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.button_cancel = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_cancel.sizePolicy().hasHeightForWidth())
        self.button_cancel.setSizePolicy(sizePolicy)
        self.button_cancel.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Bahnschrift Condensed\";\n"
"background-color: rgb(48, 105, 176);border-radius: 13px;")
        self.button_cancel.setObjectName("button_cancel")
        self.gridLayout.addWidget(self.button_cancel, 1, 0, 1, 1)
        self.button_delete = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_delete.sizePolicy().hasHeightForWidth())
        self.button_delete.setSizePolicy(sizePolicy)
        self.button_delete.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Bahnschrift Condensed\";\n"
"background-color: rgb(48, 105, 176);border-radius: 13px;")
        self.button_delete.setAutoDefault(False)
        self.button_delete.setObjectName("button_delete")
        self.gridLayout.addWidget(self.button_delete, 2, 0, 1, 1)
        self.button_confirm = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_confirm.sizePolicy().hasHeightForWidth())
        self.button_confirm.setSizePolicy(sizePolicy)
        self.button_confirm.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Bahnschrift Condensed\";\n"
"background-color: rgb(48, 105, 176);border-radius: 13px;")
        self.button_confirm.setObjectName("button_confirm")
        self.gridLayout.addWidget(self.button_confirm, 0, 0, 1, 1)
        self.button_edit = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_edit.sizePolicy().hasHeightForWidth())
        self.button_edit.setSizePolicy(sizePolicy)
        self.button_edit.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Bahnschrift Condensed\";\n"
"background-color: rgb(48, 105, 176);border-radius: 13px;")
        self.button_edit.setObjectName("button_edit")
        self.gridLayout.addWidget(self.button_edit, 3, 0, 1, 1)
        self.gridLayout.setRowMinimumHeight(0, 1)
        self.gridLayout.setRowMinimumHeight(1, 1)
        self.gridLayout.setRowMinimumHeight(2, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)

        self.retranslateUi(input_dialog)
        QtCore.QMetaObject.connectSlotsByName(input_dialog)

    def retranslateUi(self, input_dialog):
        _translate = QtCore.QCoreApplication.translate
        input_dialog.setWindowTitle(_translate("input_dialog", "Dialog"))
        self.label_name_cfg_8.setText(_translate("input_dialog", "LabelSIG"))
        self.button_cancel.setText(_translate("input_dialog", "Cancel"))
        self.button_delete.setText(_translate("input_dialog", "Delete"))
        self.button_confirm.setText(_translate("input_dialog", "Confirm"))
        self.button_edit.setText(_translate("input_dialog", "Edit"))
