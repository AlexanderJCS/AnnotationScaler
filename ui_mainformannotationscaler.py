# Form implementation generated from reading ui file '.\mainformannotationscaler.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainFormAnnotationscaler(object):
    def setupUi(self, MainFormAnnotationscaler):
        MainFormAnnotationscaler.setObjectName("MainFormAnnotationscaler")
        MainFormAnnotationscaler.resize(339, 573)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainFormAnnotationscaler.sizePolicy().hasHeightForWidth())
        MainFormAnnotationscaler.setSizePolicy(sizePolicy)
        MainFormAnnotationscaler.setMinimumSize(QtCore.QSize(339, 573))
        self.verticalLayout = QtWidgets.QVBoxLayout(MainFormAnnotationscaler)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(MainFormAnnotationscaler)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.groupBox = QtWidgets.QGroupBox(MainFormAnnotationscaler)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 301, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.edit_scale_initial_x = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.edit_scale_initial_x.setObjectName("edit_scale_initial_x")
        self.horizontalLayout_5.addWidget(self.edit_scale_initial_x)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.edit_scale_initial_y = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.edit_scale_initial_y.setObjectName("edit_scale_initial_y")
        self.horizontalLayout_3.addWidget(self.edit_scale_initial_y)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.edit_scale_initial_z = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.edit_scale_initial_z.setObjectName("edit_scale_initial_z")
        self.horizontalLayout_7.addWidget(self.edit_scale_initial_z)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(MainFormAnnotationscaler)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 301, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.edit_scale_final_x = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_scale_final_x.setObjectName("edit_scale_final_x")
        self.horizontalLayout.addWidget(self.edit_scale_final_x)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.edit_scale_final_y = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_scale_final_y.setObjectName("edit_scale_final_y")
        self.horizontalLayout_2.addWidget(self.edit_scale_final_y)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.edit_scale_final_z = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_scale_final_z.setObjectName("edit_scale_final_z")
        self.horizontalLayout_6.addWidget(self.edit_scale_final_z)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.btn_process = QtWidgets.QPushButton(MainFormAnnotationscaler)
        self.btn_process.setMinimumSize(QtCore.QSize(0, 26))
        self.btn_process.setObjectName("btn_process")
        self.verticalLayout.addWidget(self.btn_process)
        self.btn_reverse = QtWidgets.QPushButton(MainFormAnnotationscaler)
        self.btn_reverse.setMinimumSize(QtCore.QSize(0, 26))
        self.btn_reverse.setObjectName("btn_reverse")
        self.verticalLayout.addWidget(self.btn_reverse)
        self.label_output = QtWidgets.QLabel(MainFormAnnotationscaler)
        self.label_output.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_output.setText("")
        self.label_output.setObjectName("label_output")
        self.verticalLayout.addWidget(self.label_output)

        self.retranslateUi(MainFormAnnotationscaler)
        QtCore.QMetaObject.connectSlotsByName(MainFormAnnotationscaler)

    def retranslateUi(self, MainFormAnnotationscaler):
        _translate = QtCore.QCoreApplication.translate
        MainFormAnnotationscaler.setWindowTitle(_translate("MainFormAnnotationscaler", "Form"))
        self.label.setText(_translate("MainFormAnnotationscaler", "<html><head/><body><p><span style=\" font-weight:700;\">Instructions:</span></p><p>1. Input the initial (current) scale of the annotations.</p><p>2. Input the final (desired) scale of the annotations.</p><p>3. Select the annotations to change the scale of on the right.</p><p>4. Click <span style=\" font-style:italic;\">Process</span> once.<span style=\" font-weight:700;\"/>If pressed too many times, click <span style=\" font-style:italic;\">Reverse</span>.</p></body></html>"))
        self.groupBox.setTitle(_translate("MainFormAnnotationscaler", "Initial Scale"))
        self.label_4.setText(_translate("MainFormAnnotationscaler", "X (nm):"))
        self.label_5.setText(_translate("MainFormAnnotationscaler", "Y (nm):"))
        self.label_7.setText(_translate("MainFormAnnotationscaler", "Z (nm):"))
        self.groupBox_2.setTitle(_translate("MainFormAnnotationscaler", "Final Scale"))
        self.label_2.setText(_translate("MainFormAnnotationscaler", "X (nm):"))
        self.label_3.setText(_translate("MainFormAnnotationscaler", "Y (nm):"))
        self.label_6.setText(_translate("MainFormAnnotationscaler", "Z (nm):"))
        self.btn_process.setText(_translate("MainFormAnnotationscaler", "Process"))
        self.btn_reverse.setText(_translate("MainFormAnnotationscaler", "Reverse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainFormAnnotationscaler = QtWidgets.QWidget()
    ui = Ui_MainFormAnnotationscaler()
    ui.setupUi(MainFormAnnotationscaler)
    MainFormAnnotationscaler.show()
    sys.exit(app.exec())
