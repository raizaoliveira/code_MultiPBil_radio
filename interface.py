# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_main_win(object):
    def setupUi(self, main_win):
        main_win.setObjectName(_fromUtf8("main_win"))
        main_win.resize(519, 387)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Imagens/antena.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_win.setWindowIcon(icon)
        main_win.setAutoFillBackground(True)
        self.centralwidget = QtGui.QWidget(main_win)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(230, 250, 61, 27))
        self.spinBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(1000)
        self.spinBox.setProperty("value", 100)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 240, 201, 41))
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 170, 181, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lbl_multprob = QtGui.QLabel(self.centralwidget)
        self.lbl_multprob.setGeometry(QtCore.QRect(20, 90, 71, 17))
        self.lbl_multprob.setMouseTracking(False)
        self.lbl_multprob.setToolTip(_fromUtf8(""))
        self.lbl_multprob.setOpenExternalLinks(False)
        self.lbl_multprob.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.lbl_multprob.setObjectName(_fromUtf8("lbl_multprob"))
        self.lbl_multsh = QtGui.QLabel(self.centralwidget)
        self.lbl_multsh.setGeometry(QtCore.QRect(200, 90, 66, 16))
        self.lbl_multsh.setObjectName(_fromUtf8("lbl_multsh"))
        self.dial_multprob = QtGui.QDial(self.centralwidget)
        self.dial_multprob.setGeometry(QtCore.QRect(110, 70, 50, 64))
        self.dial_multprob.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.dial_multprob.setMinimum(0)
        self.dial_multprob.setObjectName(_fromUtf8("dial_multprob"))
        self.lbl_valmultprob = QtGui.QLabel(self.centralwidget)
        self.lbl_valmultprob.setGeometry(QtCore.QRect(110, 130, 66, 17))
        self.lbl_valmultprob.setObjectName(_fromUtf8("lbl_valmultprob"))
        self.dial_multsh = QtGui.QDial(self.centralwidget)
        self.dial_multsh.setGeometry(QtCore.QRect(270, 70, 50, 64))
        self.dial_multsh.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.dial_multsh.setMinimum(1)
        self.dial_multsh.setMaximum(100)
        self.dial_multsh.setObjectName(_fromUtf8("dial_multsh"))
        self.lbl_valmultsh = QtGui.QLabel(self.centralwidget)
        self.lbl_valmultsh.setGeometry(QtCore.QRect(260, 130, 66, 17))
        self.lbl_valmultsh.setObjectName(_fromUtf8("lbl_valmultsh"))
        self.lbl_alpha = QtGui.QLabel(self.centralwidget)
        self.lbl_alpha.setGeometry(QtCore.QRect(350, 90, 66, 17))
        self.lbl_alpha.setObjectName(_fromUtf8("lbl_alpha"))
        self.dial_alpha = QtGui.QDial(self.centralwidget)
        self.dial_alpha.setGeometry(QtCore.QRect(430, 70, 50, 64))
        self.dial_alpha.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.dial_alpha.setObjectName(_fromUtf8("dial_alpha"))
        self.lbl_valalpha = QtGui.QLabel(self.centralwidget)
        self.lbl_valalpha.setGeometry(QtCore.QRect(420, 130, 66, 17))
        self.lbl_valalpha.setObjectName(_fromUtf8("lbl_valalpha"))
        self.slider_area = QtGui.QSlider(self.centralwidget)
        self.slider_area.setGeometry(QtCore.QRect(170, 170, 301, 29))
        self.slider_area.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.slider_area.setMinimum(1000)
        self.slider_area.setMaximum(4000)
        self.slider_area.setSingleStep(50)
        self.slider_area.setOrientation(QtCore.Qt.Horizontal)
        self.slider_area.setObjectName(_fromUtf8("slider_area"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 200, 31, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lbl_valarea = QtGui.QLabel(self.centralwidget)
        self.lbl_valarea.setGeometry(QtCore.QRect(400, 200, 51, 21))
        self.lbl_valarea.setObjectName(_fromUtf8("lbl_valarea"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btn_exe = QtGui.QPushButton(self.centralwidget)
        self.btn_exe.setGeometry(QtCore.QRect(350, 300, 141, 31))
        self.btn_exe.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_exe.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btn_exe.setObjectName(_fromUtf8("btn_exe"))
        main_win.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(main_win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 519, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        main_win.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(main_win)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        main_win.setStatusBar(self.statusbar)

        self.retranslateUi(main_win)
        QtCore.QObject.connect(self.dial_multprob, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lbl_valmultprob.setNum)
        QtCore.QObject.connect(self.dial_multsh, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lbl_valmultsh.setNum)
        QtCore.QObject.connect(self.dial_alpha, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lbl_valalpha.setNum)
        QtCore.QObject.connect(self.slider_area, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lbl_valarea.setNum)
        QtCore.QMetaObject.connectSlotsByName(main_win)

    def retranslateUi(self, main_win):
        main_win.setWindowTitle(_translate("main_win", "ERB", None))
        self.label.setText(_translate("main_win", "Tamanho da população inicial:", None))
        self.label_2.setText(_translate("main_win", "Área de cobertura:", None))
        self.lbl_multprob.setText(_translate("main_win", "Mult Prob: ", None))
        self.lbl_multsh.setText(_translate("main_win", "Mult Sh:", None))
        self.lbl_valmultprob.setText(_translate("main_win", "0.3", None))
        self.lbl_valmultsh.setText(_translate("main_win", "0.04", None))
        self.lbl_alpha.setText(_translate("main_win", "Alpha:", None))
        self.lbl_valalpha.setText(_translate("main_win", "0.05", None))
        self.label_3.setText(_translate("main_win", "m²", None))
        self.lbl_valarea.setText(_translate("main_win", "1000", None))
        self.label_4.setText(_translate("main_win", " Parâmetros de Configuração:", None))
        self.btn_exe.setText(_translate("main_win", "Rodar Algoritmo", None))

