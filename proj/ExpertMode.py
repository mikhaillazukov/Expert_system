# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExpertMode.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExpertMode(object):
    def setupUi(self, ExpertMode):
        ExpertMode.setObjectName("ExpertMode")
        ExpertMode.resize(1127, 599)
        ExpertMode.setMinimumSize(QtCore.QSize(1127, 599))
        self.gridLayout = QtWidgets.QGridLayout(ExpertMode)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(ExpertMode)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonAddEvidence = QtWidgets.QPushButton(self.groupBox)
        self.buttonAddEvidence.setObjectName("buttonAddEvidence")
        self.gridLayout_2.addWidget(self.buttonAddEvidence, 0, 0, 1, 1)
        self.tableEvidence = QtWidgets.QTableWidget(self.groupBox)
        self.tableEvidence.setShowGrid(True)
        self.tableEvidence.setObjectName("tableEvidence")
        self.tableEvidence.setColumnCount(2)
        self.tableEvidence.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableEvidence.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setKerning(True)
        item.setFont(font)
        self.tableEvidence.setHorizontalHeaderItem(1, item)
        self.gridLayout_2.addWidget(self.tableEvidence, 1, 0, 1, 2)
        self.buttonDeleteEvidence = QtWidgets.QPushButton(self.groupBox)
        self.buttonDeleteEvidence.setObjectName("buttonDeleteEvidence")
        self.gridLayout_2.addWidget(self.buttonDeleteEvidence, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(ExpertMode)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.buttonAddHypothesis = QtWidgets.QPushButton(self.groupBox_2)
        self.buttonAddHypothesis.setObjectName("buttonAddHypothesis")
        self.gridLayout_3.addWidget(self.buttonAddHypothesis, 0, 0, 1, 1)
        self.buttonDeleteHypothesis = QtWidgets.QPushButton(self.groupBox_2)
        self.buttonDeleteHypothesis.setObjectName("buttonDeleteHypothesis")
        self.gridLayout_3.addWidget(self.buttonDeleteHypothesis, 0, 1, 1, 1)
        self.tableHypothesis = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableHypothesis.setObjectName("tableHypotesis")
        self.tableHypothesis.setColumnCount(2)
        self.tableHypothesis.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableHypothesis.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setKerning(True)
        item.setFont(font)
        self.tableHypothesis.setHorizontalHeaderItem(1, item)
        self.gridLayout_3.addWidget(self.tableHypothesis, 3, 0, 1, 2)
        self.horizontalLayout_3.addLayout(self.gridLayout_3)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.retranslateUi(ExpertMode)
        QtCore.QMetaObject.connectSlotsByName(ExpertMode)

    def retranslateUi(self, ExpertMode):
        _translate = QtCore.QCoreApplication.translate
        ExpertMode.setWindowTitle(_translate("ExpertMode", "Form"))
        self.groupBox.setTitle(_translate("ExpertMode", "Свидетельства"))
        self.buttonAddEvidence.setText(_translate("ExpertMode", "Добавить"))
        item = self.tableEvidence.horizontalHeaderItem(0)
        item.setText(_translate("ExpertMode", "Название"))
        item = self.tableEvidence.horizontalHeaderItem(1)
        item.setText(_translate("ExpertMode", "Вопрос"))
        self.buttonDeleteEvidence.setText(_translate("ExpertMode", "Удалить"))
        self.groupBox_2.setTitle(_translate("ExpertMode", "Гипотезы"))
        self.buttonAddHypothesis.setText(_translate("ExpertMode", "Добавить"))
        self.buttonDeleteHypothesis.setText(_translate("ExpertMode", "Удалить"))
        item = self.tableHypothesis.horizontalHeaderItem(0)
        item.setText(_translate("ExpertMode", "Название"))
        item = self.tableHypothesis.horizontalHeaderItem(1)
        item.setText(_translate("ExpertMode", "Априорная P"))
        headers = self.tableEvidence.horizontalHeader()
        headers.setSectionResizeMode(0,QtWidgets.QHeaderView.ResizeToContents)
        headers.setSectionResizeMode(1,QtWidgets.QHeaderView.ResizeToContents)
        headers = self.tableHypothesis.horizontalHeader()
        headers.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        headers.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)