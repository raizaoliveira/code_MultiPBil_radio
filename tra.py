#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import getrandbits, random
from math import pi, pow, ceil
from math import sqrt
import interface as UI
from PyQt4 import QtCore, QtGui
import sys
import os



class mid(QtGui.QMainWindow, UI.Ui_main_win):
	def __init__(self, parent=None):
		super(mid,self).__init__(parent)
		self.setupUi(self)
		lista = []
		self.connect(self.btn_exe, QtCore.SIGNAL("clicked()"),self.execut)   
	def execut(self):
		mut_prob = self.lbl_valmultprob.text()
		mut_sh = self.lbl_valmultsh.text() 
		alpha = self.lbl_valalpha.text()
		area = self.lbl_valarea.text()
		size_pop = self.spinBox.text()

		arquivo = open('input.txt', 'w')
		arquivo.write(mut_prob)
		arquivo.write('\n'+mut_sh)
		arquivo.write('\n'+alpha)
		arquivo.write('\n'+area)
		arquivo.write('\n'+size_pop)
		arquivo.close() 

		try:
			os.system('sh aux.sh')
		except IOError:
			print('dont work')
		#app.quit()

def main():
	app = QtGui.QApplication(sys.argv)
	main_window = mid()
	main_window.show()
	app.exec_()




	#init_exec(1000, 0.3, 0.04, 0.05, 10)



if __name__ == '__main__':
	main()
