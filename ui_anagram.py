# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt\ui\anagram.ui'
#
# Created: Mon Dec 31 22:31:09 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Anagram(object):
    def setupUi(self, Anagram):
        Anagram.setObjectName(_fromUtf8("Anagram"))
        Anagram.resize(498, 607)
        Anagram.setMinimumSize(QtCore.QSize(498, 607))
        Anagram.setMaximumSize(QtCore.QSize(498, 607))
        Anagram.setWindowTitle(QtGui.QApplication.translate("Anagram", "Anagram Editor", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/monokuma.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Anagram.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(Anagram)
        self.buttonBox.setGeometry(QtCore.QRect(395, 545, 90, 50))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lblPreview = QtGui.QLabel(Anagram)
        self.lblPreview.setGeometry(QtCore.QRect(9, 9, 480, 272))
        self.lblPreview.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lblPreview.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblPreview.setText(_fromUtf8(""))
        self.lblPreview.setObjectName(_fromUtf8("lblPreview"))
        self.groupBox = QtGui.QGroupBox(Anagram)
        self.groupBox.setGeometry(QtCore.QRect(10, 290, 481, 221))
        self.groupBox.setTitle(QtGui.QApplication.translate("Anagram", "Solution", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.txtSolutionTrans = QtGui.QLineEdit(self.groupBox)
        self.txtSolutionTrans.setGeometry(QtCore.QRect(10, 20, 461, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        self.txtSolutionTrans.setFont(font)
        self.txtSolutionTrans.setText(QtGui.QApplication.translate("Anagram", "ＨＡＧＡＫＵＲＥ", None, QtGui.QApplication.UnicodeUTF8))
        self.txtSolutionTrans.setMaxLength(15)
        self.txtSolutionTrans.setCursorPosition(0)
        self.txtSolutionTrans.setAlignment(QtCore.Qt.AlignCenter)
        self.txtSolutionTrans.setObjectName(_fromUtf8("txtSolutionTrans"))
        self.txtSolutionOrig = QtGui.QLineEdit(self.groupBox)
        self.txtSolutionOrig.setGeometry(QtCore.QRect(10, 120, 461, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        self.txtSolutionOrig.setFont(font)
        self.txtSolutionOrig.setText(QtGui.QApplication.translate("Anagram", "はがくれ", None, QtGui.QApplication.UnicodeUTF8))
        self.txtSolutionOrig.setMaxLength(15)
        self.txtSolutionOrig.setAlignment(QtCore.Qt.AlignCenter)
        self.txtSolutionOrig.setReadOnly(True)
        self.txtSolutionOrig.setObjectName(_fromUtf8("txtSolutionOrig"))
        self.chkTransEasy1 = QtGui.QCheckBox(self.groupBox)
        self.chkTransEasy1.setGeometry(QtCore.QRect(170, 50, 16, 17))
        self.chkTransEasy1.setText(_fromUtf8(""))
        self.chkTransEasy1.setCheckable(True)
        self.chkTransEasy1.setObjectName(_fromUtf8("chkTransEasy1"))
        self.chkTransEasy2 = QtGui.QCheckBox(self.groupBox)
        self.chkTransEasy2.setGeometry(QtCore.QRect(190, 50, 16, 17))
        self.chkTransEasy2.setText(_fromUtf8(""))
        self.chkTransEasy2.setObjectName(_fromUtf8("chkTransEasy2"))
        self.chkTransEasy3 = QtGui.QCheckBox(self.groupBox)
        self.chkTransEasy3.setGeometry(QtCore.QRect(210, 50, 16, 17))
        self.chkTransEasy3.setText(_fromUtf8(""))
        self.chkTransEasy3.setObjectName(_fromUtf8("chkTransEasy3"))
        self.chkTransEasy4 = QtGui.QCheckBox(self.groupBox)
        self.chkTransEasy4.setGeometry(QtCore.QRect(230, 50, 16, 17))
        self.chkTransEasy4.setText(_fromUtf8(""))
        self.chkTransEasy4.setObjectName(_fromUtf8("chkTransEasy4"))
        self.chkTransEasy5 = QtGui.QCheckBox(self.groupBox)
        self.chkTransEasy5.setGeometry(QtCore.QRect(250, 50, 16, 17))
        self.chkTransEasy5.setText(_fromUtf8(""))
        self.chkTransEasy5.setObjectName(_fromUtf8("chkTransEasy5"))
        self.chkTransEasy6 = QtGui.QCheckBox(self.groupBox)
        self.chkTransEasy6.setGeometry(QtCore.QRect(270, 50, 16, 17))
        self.chkTransEasy6.setText(_fromUtf8(""))
        self.chkTransEasy6.setObjectName(_fromUtf8("chkTransEasy6"))
        self.chkTransEasy7 = QtGui.QCheckBox(self.groupBox)
        self.chkTransEasy7.setGeometry(QtCore.QRect(290, 50, 16, 17))
        self.chkTransEasy7.setText(_fromUtf8(""))
        self.chkTransEasy7.setObjectName(_fromUtf8("chkTransEasy7"))
        self.chkTransEasy8 = QtGui.QCheckBox(self.groupBox)
        self.chkTransEasy8.setGeometry(QtCore.QRect(310, 50, 16, 17))
        self.chkTransEasy8.setText(_fromUtf8(""))
        self.chkTransEasy8.setObjectName(_fromUtf8("chkTransEasy8"))
        self.chkTransEasy9 = QtGui.QCheckBox(self.groupBox)
        self.chkTransEasy9.setGeometry(QtCore.QRect(330, 50, 16, 17))
        self.chkTransEasy9.setText(_fromUtf8(""))
        self.chkTransEasy9.setObjectName(_fromUtf8("chkTransEasy9"))
        self.chkTransEasy10 = QtGui.QCheckBox(self.groupBox)
        self.chkTransEasy10.setGeometry(QtCore.QRect(350, 50, 16, 17))
        self.chkTransEasy10.setText(_fromUtf8(""))
        self.chkTransEasy10.setObjectName(_fromUtf8("chkTransEasy10"))
        self.chkTransEasy11 = QtGui.QCheckBox(self.groupBox)
        self.chkTransEasy11.setGeometry(QtCore.QRect(370, 50, 16, 17))
        self.chkTransEasy11.setText(_fromUtf8(""))
        self.chkTransEasy11.setObjectName(_fromUtf8("chkTransEasy11"))
        self.chkTransEasy12 = QtGui.QCheckBox(self.groupBox)
        self.chkTransEasy12.setGeometry(QtCore.QRect(390, 50, 16, 17))
        self.chkTransEasy12.setText(_fromUtf8(""))
        self.chkTransEasy12.setObjectName(_fromUtf8("chkTransEasy12"))
        self.chkTransEasy13 = QtGui.QCheckBox(self.groupBox)
        self.chkTransEasy13.setGeometry(QtCore.QRect(410, 50, 16, 17))
        self.chkTransEasy13.setText(_fromUtf8(""))
        self.chkTransEasy13.setObjectName(_fromUtf8("chkTransEasy13"))
        self.chkTransEasy14 = QtGui.QCheckBox(self.groupBox)
        self.chkTransEasy14.setGeometry(QtCore.QRect(430, 50, 16, 17))
        self.chkTransEasy14.setText(_fromUtf8(""))
        self.chkTransEasy14.setObjectName(_fromUtf8("chkTransEasy14"))
        self.chkTransEasy15 = QtGui.QCheckBox(self.groupBox)
        self.chkTransEasy15.setGeometry(QtCore.QRect(450, 50, 16, 17))
        self.chkTransEasy15.setText(_fromUtf8(""))
        self.chkTransEasy15.setObjectName(_fromUtf8("chkTransEasy15"))
        self.chkTransNorm10 = QtGui.QCheckBox(self.groupBox)
        self.chkTransNorm10.setGeometry(QtCore.QRect(350, 70, 16, 17))
        self.chkTransNorm10.setText(_fromUtf8(""))
        self.chkTransNorm10.setObjectName(_fromUtf8("chkTransNorm10"))
        self.chkTransNorm8 = QtGui.QCheckBox(self.groupBox)
        self.chkTransNorm8.setGeometry(QtCore.QRect(310, 70, 16, 17))
        self.chkTransNorm8.setText(_fromUtf8(""))
        self.chkTransNorm8.setObjectName(_fromUtf8("chkTransNorm8"))
        self.chkTransNorm6 = QtGui.QCheckBox(self.groupBox)
        self.chkTransNorm6.setGeometry(QtCore.QRect(270, 70, 16, 17))
        self.chkTransNorm6.setText(_fromUtf8(""))
        self.chkTransNorm6.setObjectName(_fromUtf8("chkTransNorm6"))
        self.chkTransNorm15 = QtGui.QCheckBox(self.groupBox)
        self.chkTransNorm15.setGeometry(QtCore.QRect(450, 70, 16, 17))
        self.chkTransNorm15.setText(_fromUtf8(""))
        self.chkTransNorm15.setObjectName(_fromUtf8("chkTransNorm15"))
        self.chkTransNorm4 = QtGui.QCheckBox(self.groupBox)
        self.chkTransNorm4.setGeometry(QtCore.QRect(230, 70, 16, 17))
        self.chkTransNorm4.setText(_fromUtf8(""))
        self.chkTransNorm4.setObjectName(_fromUtf8("chkTransNorm4"))
        self.chkTransNorm13 = QtGui.QCheckBox(self.groupBox)
        self.chkTransNorm13.setGeometry(QtCore.QRect(410, 70, 16, 17))
        self.chkTransNorm13.setText(_fromUtf8(""))
        self.chkTransNorm13.setObjectName(_fromUtf8("chkTransNorm13"))
        self.chkTransNorm2 = QtGui.QCheckBox(self.groupBox)
        self.chkTransNorm2.setGeometry(QtCore.QRect(190, 70, 16, 17))
        self.chkTransNorm2.setText(_fromUtf8(""))
        self.chkTransNorm2.setObjectName(_fromUtf8("chkTransNorm2"))
        self.chkTransNorm11 = QtGui.QCheckBox(self.groupBox)
        self.chkTransNorm11.setGeometry(QtCore.QRect(370, 70, 16, 17))
        self.chkTransNorm11.setText(_fromUtf8(""))
        self.chkTransNorm11.setObjectName(_fromUtf8("chkTransNorm11"))
        self.chkTransNorm1 = QtGui.QCheckBox(self.groupBox)
        self.chkTransNorm1.setGeometry(QtCore.QRect(170, 70, 16, 17))
        self.chkTransNorm1.setText(_fromUtf8(""))
        self.chkTransNorm1.setObjectName(_fromUtf8("chkTransNorm1"))
        self.chkTransNorm9 = QtGui.QCheckBox(self.groupBox)
        self.chkTransNorm9.setGeometry(QtCore.QRect(330, 70, 16, 17))
        self.chkTransNorm9.setText(_fromUtf8(""))
        self.chkTransNorm9.setObjectName(_fromUtf8("chkTransNorm9"))
        self.chkTransNorm7 = QtGui.QCheckBox(self.groupBox)
        self.chkTransNorm7.setGeometry(QtCore.QRect(290, 70, 16, 17))
        self.chkTransNorm7.setText(_fromUtf8(""))
        self.chkTransNorm7.setObjectName(_fromUtf8("chkTransNorm7"))
        self.chkTransNorm5 = QtGui.QCheckBox(self.groupBox)
        self.chkTransNorm5.setGeometry(QtCore.QRect(250, 70, 16, 17))
        self.chkTransNorm5.setText(_fromUtf8(""))
        self.chkTransNorm5.setObjectName(_fromUtf8("chkTransNorm5"))
        self.chkTransNorm14 = QtGui.QCheckBox(self.groupBox)
        self.chkTransNorm14.setGeometry(QtCore.QRect(430, 70, 16, 17))
        self.chkTransNorm14.setText(_fromUtf8(""))
        self.chkTransNorm14.setObjectName(_fromUtf8("chkTransNorm14"))
        self.chkTransNorm12 = QtGui.QCheckBox(self.groupBox)
        self.chkTransNorm12.setGeometry(QtCore.QRect(390, 70, 16, 17))
        self.chkTransNorm12.setText(_fromUtf8(""))
        self.chkTransNorm12.setObjectName(_fromUtf8("chkTransNorm12"))
        self.chkTransNorm3 = QtGui.QCheckBox(self.groupBox)
        self.chkTransNorm3.setGeometry(QtCore.QRect(210, 70, 16, 17))
        self.chkTransNorm3.setText(_fromUtf8(""))
        self.chkTransNorm3.setObjectName(_fromUtf8("chkTransNorm3"))
        self.chkTransHard10 = QtGui.QCheckBox(self.groupBox)
        self.chkTransHard10.setGeometry(QtCore.QRect(350, 90, 16, 17))
        self.chkTransHard10.setText(_fromUtf8(""))
        self.chkTransHard10.setObjectName(_fromUtf8("chkTransHard10"))
        self.chkTransHard8 = QtGui.QCheckBox(self.groupBox)
        self.chkTransHard8.setGeometry(QtCore.QRect(310, 90, 16, 17))
        self.chkTransHard8.setText(_fromUtf8(""))
        self.chkTransHard8.setObjectName(_fromUtf8("chkTransHard8"))
        self.chkTransHard6 = QtGui.QCheckBox(self.groupBox)
        self.chkTransHard6.setGeometry(QtCore.QRect(270, 90, 16, 17))
        self.chkTransHard6.setText(_fromUtf8(""))
        self.chkTransHard6.setObjectName(_fromUtf8("chkTransHard6"))
        self.chkTransHard15 = QtGui.QCheckBox(self.groupBox)
        self.chkTransHard15.setGeometry(QtCore.QRect(450, 90, 16, 17))
        self.chkTransHard15.setText(_fromUtf8(""))
        self.chkTransHard15.setObjectName(_fromUtf8("chkTransHard15"))
        self.chkTransHard4 = QtGui.QCheckBox(self.groupBox)
        self.chkTransHard4.setGeometry(QtCore.QRect(230, 90, 16, 17))
        self.chkTransHard4.setText(_fromUtf8(""))
        self.chkTransHard4.setObjectName(_fromUtf8("chkTransHard4"))
        self.chkTransHard13 = QtGui.QCheckBox(self.groupBox)
        self.chkTransHard13.setGeometry(QtCore.QRect(410, 90, 16, 17))
        self.chkTransHard13.setText(_fromUtf8(""))
        self.chkTransHard13.setObjectName(_fromUtf8("chkTransHard13"))
        self.chkTransHard2 = QtGui.QCheckBox(self.groupBox)
        self.chkTransHard2.setGeometry(QtCore.QRect(190, 90, 16, 17))
        self.chkTransHard2.setText(_fromUtf8(""))
        self.chkTransHard2.setObjectName(_fromUtf8("chkTransHard2"))
        self.chkTransHard11 = QtGui.QCheckBox(self.groupBox)
        self.chkTransHard11.setGeometry(QtCore.QRect(370, 90, 16, 17))
        self.chkTransHard11.setText(_fromUtf8(""))
        self.chkTransHard11.setObjectName(_fromUtf8("chkTransHard11"))
        self.chkTransHard1 = QtGui.QCheckBox(self.groupBox)
        self.chkTransHard1.setGeometry(QtCore.QRect(170, 90, 16, 17))
        self.chkTransHard1.setText(_fromUtf8(""))
        self.chkTransHard1.setObjectName(_fromUtf8("chkTransHard1"))
        self.chkTransHard9 = QtGui.QCheckBox(self.groupBox)
        self.chkTransHard9.setGeometry(QtCore.QRect(330, 90, 16, 17))
        self.chkTransHard9.setText(_fromUtf8(""))
        self.chkTransHard9.setObjectName(_fromUtf8("chkTransHard9"))
        self.chkTransHard7 = QtGui.QCheckBox(self.groupBox)
        self.chkTransHard7.setGeometry(QtCore.QRect(290, 90, 16, 17))
        self.chkTransHard7.setText(_fromUtf8(""))
        self.chkTransHard7.setObjectName(_fromUtf8("chkTransHard7"))
        self.chkTransHard5 = QtGui.QCheckBox(self.groupBox)
        self.chkTransHard5.setGeometry(QtCore.QRect(250, 90, 16, 17))
        self.chkTransHard5.setText(_fromUtf8(""))
        self.chkTransHard5.setObjectName(_fromUtf8("chkTransHard5"))
        self.chkTransHard14 = QtGui.QCheckBox(self.groupBox)
        self.chkTransHard14.setGeometry(QtCore.QRect(430, 90, 16, 17))
        self.chkTransHard14.setText(_fromUtf8(""))
        self.chkTransHard14.setObjectName(_fromUtf8("chkTransHard14"))
        self.chkTransHard12 = QtGui.QCheckBox(self.groupBox)
        self.chkTransHard12.setGeometry(QtCore.QRect(390, 90, 16, 17))
        self.chkTransHard12.setText(_fromUtf8(""))
        self.chkTransHard12.setObjectName(_fromUtf8("chkTransHard12"))
        self.chkTransHard3 = QtGui.QCheckBox(self.groupBox)
        self.chkTransHard3.setGeometry(QtCore.QRect(210, 90, 16, 17))
        self.chkTransHard3.setText(_fromUtf8(""))
        self.chkTransHard3.setObjectName(_fromUtf8("chkTransHard3"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(90, 49, 71, 17))
        self.label.setText(QtGui.QApplication.translate("Anagram", "Easy", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(90, 69, 71, 17))
        self.label_2.setText(QtGui.QApplication.translate("Anagram", "Normal", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(90, 89, 71, 17))
        self.label_3.setText(QtGui.QApplication.translate("Anagram", "Hard", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(90, 149, 71, 17))
        self.label_4.setText(QtGui.QApplication.translate("Anagram", "Easy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(90, 169, 71, 17))
        self.label_5.setText(QtGui.QApplication.translate("Anagram", "Normal", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(90, 189, 71, 17))
        self.label_6.setText(QtGui.QApplication.translate("Anagram", "Hard", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 49, 131, 57))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setText(QtGui.QApplication.translate("Anagram", "Translated", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 149, 131, 57))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setText(QtGui.QApplication.translate("Anagram", "Original", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.chkOrigEasy10 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigEasy10.setGeometry(QtCore.QRect(350, 150, 16, 17))
        self.chkOrigEasy10.setText(_fromUtf8(""))
        self.chkOrigEasy10.setObjectName(_fromUtf8("chkOrigEasy10"))
        self.chkOrigEasy6 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigEasy6.setGeometry(QtCore.QRect(270, 150, 16, 17))
        self.chkOrigEasy6.setText(_fromUtf8(""))
        self.chkOrigEasy6.setObjectName(_fromUtf8("chkOrigEasy6"))
        self.chkOrigNorm9 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigNorm9.setGeometry(QtCore.QRect(330, 170, 16, 17))
        self.chkOrigNorm9.setText(_fromUtf8(""))
        self.chkOrigNorm9.setObjectName(_fromUtf8("chkOrigNorm9"))
        self.chkOrigHard13 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigHard13.setGeometry(QtCore.QRect(410, 190, 16, 17))
        self.chkOrigHard13.setText(_fromUtf8(""))
        self.chkOrigHard13.setObjectName(_fromUtf8("chkOrigHard13"))
        self.chkOrigNorm2 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigNorm2.setGeometry(QtCore.QRect(190, 170, 16, 17))
        self.chkOrigNorm2.setText(_fromUtf8(""))
        self.chkOrigNorm2.setObjectName(_fromUtf8("chkOrigNorm2"))
        self.chkOrigHard7 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigHard7.setGeometry(QtCore.QRect(290, 190, 16, 17))
        self.chkOrigHard7.setText(_fromUtf8(""))
        self.chkOrigHard7.setObjectName(_fromUtf8("chkOrigHard7"))
        self.chkOrigHard11 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigHard11.setGeometry(QtCore.QRect(370, 190, 16, 17))
        self.chkOrigHard11.setText(_fromUtf8(""))
        self.chkOrigHard11.setObjectName(_fromUtf8("chkOrigHard11"))
        self.chkOrigEasy1 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigEasy1.setGeometry(QtCore.QRect(170, 150, 16, 17))
        self.chkOrigEasy1.setText(_fromUtf8(""))
        self.chkOrigEasy1.setCheckable(True)
        self.chkOrigEasy1.setChecked(False)
        self.chkOrigEasy1.setObjectName(_fromUtf8("chkOrigEasy1"))
        self.chkOrigHard4 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigHard4.setGeometry(QtCore.QRect(230, 190, 16, 17))
        self.chkOrigHard4.setText(_fromUtf8(""))
        self.chkOrigHard4.setObjectName(_fromUtf8("chkOrigHard4"))
        self.chkOrigNorm13 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigNorm13.setGeometry(QtCore.QRect(410, 170, 16, 17))
        self.chkOrigNorm13.setText(_fromUtf8(""))
        self.chkOrigNorm13.setObjectName(_fromUtf8("chkOrigNorm13"))
        self.chkOrigHard8 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigHard8.setGeometry(QtCore.QRect(310, 190, 16, 17))
        self.chkOrigHard8.setText(_fromUtf8(""))
        self.chkOrigHard8.setObjectName(_fromUtf8("chkOrigHard8"))
        self.chkOrigEasy4 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigEasy4.setGeometry(QtCore.QRect(230, 150, 16, 17))
        self.chkOrigEasy4.setText(_fromUtf8(""))
        self.chkOrigEasy4.setObjectName(_fromUtf8("chkOrigEasy4"))
        self.chkOrigNorm10 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigNorm10.setGeometry(QtCore.QRect(350, 170, 16, 17))
        self.chkOrigNorm10.setText(_fromUtf8(""))
        self.chkOrigNorm10.setObjectName(_fromUtf8("chkOrigNorm10"))
        self.chkOrigEasy12 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigEasy12.setGeometry(QtCore.QRect(390, 150, 16, 17))
        self.chkOrigEasy12.setText(_fromUtf8(""))
        self.chkOrigEasy12.setObjectName(_fromUtf8("chkOrigEasy12"))
        self.chkOrigEasy2 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigEasy2.setGeometry(QtCore.QRect(190, 150, 16, 17))
        self.chkOrigEasy2.setText(_fromUtf8(""))
        self.chkOrigEasy2.setObjectName(_fromUtf8("chkOrigEasy2"))
        self.chkOrigNorm15 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigNorm15.setGeometry(QtCore.QRect(450, 170, 16, 17))
        self.chkOrigNorm15.setText(_fromUtf8(""))
        self.chkOrigNorm15.setObjectName(_fromUtf8("chkOrigNorm15"))
        self.chkOrigEasy9 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigEasy9.setGeometry(QtCore.QRect(330, 150, 16, 17))
        self.chkOrigEasy9.setText(_fromUtf8(""))
        self.chkOrigEasy9.setObjectName(_fromUtf8("chkOrigEasy9"))
        self.chkOrigNorm7 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigNorm7.setGeometry(QtCore.QRect(290, 170, 16, 17))
        self.chkOrigNorm7.setText(_fromUtf8(""))
        self.chkOrigNorm7.setObjectName(_fromUtf8("chkOrigNorm7"))
        self.chkOrigEasy14 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigEasy14.setGeometry(QtCore.QRect(430, 150, 16, 17))
        self.chkOrigEasy14.setText(_fromUtf8(""))
        self.chkOrigEasy14.setObjectName(_fromUtf8("chkOrigEasy14"))
        self.chkOrigNorm11 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigNorm11.setGeometry(QtCore.QRect(370, 170, 16, 17))
        self.chkOrigNorm11.setText(_fromUtf8(""))
        self.chkOrigNorm11.setObjectName(_fromUtf8("chkOrigNorm11"))
        self.chkOrigHard2 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigHard2.setGeometry(QtCore.QRect(190, 190, 16, 17))
        self.chkOrigHard2.setText(_fromUtf8(""))
        self.chkOrigHard2.setObjectName(_fromUtf8("chkOrigHard2"))
        self.chkOrigNorm4 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigNorm4.setGeometry(QtCore.QRect(230, 170, 16, 17))
        self.chkOrigNorm4.setText(_fromUtf8(""))
        self.chkOrigNorm4.setObjectName(_fromUtf8("chkOrigNorm4"))
        self.chkOrigHard10 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigHard10.setGeometry(QtCore.QRect(350, 190, 16, 17))
        self.chkOrigHard10.setText(_fromUtf8(""))
        self.chkOrigHard10.setObjectName(_fromUtf8("chkOrigHard10"))
        self.chkOrigHard5 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigHard5.setGeometry(QtCore.QRect(250, 190, 16, 17))
        self.chkOrigHard5.setText(_fromUtf8(""))
        self.chkOrigHard5.setObjectName(_fromUtf8("chkOrigHard5"))
        self.chkOrigNorm14 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigNorm14.setGeometry(QtCore.QRect(430, 170, 16, 17))
        self.chkOrigNorm14.setText(_fromUtf8(""))
        self.chkOrigNorm14.setObjectName(_fromUtf8("chkOrigNorm14"))
        self.chkOrigHard1 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigHard1.setGeometry(QtCore.QRect(170, 190, 16, 17))
        self.chkOrigHard1.setText(_fromUtf8(""))
        self.chkOrigHard1.setObjectName(_fromUtf8("chkOrigHard1"))
        self.chkOrigNorm8 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigNorm8.setGeometry(QtCore.QRect(310, 170, 16, 17))
        self.chkOrigNorm8.setText(_fromUtf8(""))
        self.chkOrigNorm8.setObjectName(_fromUtf8("chkOrigNorm8"))
        self.chkOrigEasy15 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigEasy15.setGeometry(QtCore.QRect(450, 150, 16, 17))
        self.chkOrigEasy15.setText(_fromUtf8(""))
        self.chkOrigEasy15.setObjectName(_fromUtf8("chkOrigEasy15"))
        self.chkOrigEasy3 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigEasy3.setGeometry(QtCore.QRect(210, 150, 16, 17))
        self.chkOrigEasy3.setText(_fromUtf8(""))
        self.chkOrigEasy3.setObjectName(_fromUtf8("chkOrigEasy3"))
        self.chkOrigHard6 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigHard6.setGeometry(QtCore.QRect(270, 190, 16, 17))
        self.chkOrigHard6.setText(_fromUtf8(""))
        self.chkOrigHard6.setObjectName(_fromUtf8("chkOrigHard6"))
        self.chkOrigHard12 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigHard12.setGeometry(QtCore.QRect(390, 190, 16, 17))
        self.chkOrigHard12.setText(_fromUtf8(""))
        self.chkOrigHard12.setObjectName(_fromUtf8("chkOrigHard12"))
        self.chkOrigNorm3 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigNorm3.setGeometry(QtCore.QRect(210, 170, 16, 17))
        self.chkOrigNorm3.setText(_fromUtf8(""))
        self.chkOrigNorm3.setObjectName(_fromUtf8("chkOrigNorm3"))
        self.chkOrigNorm5 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigNorm5.setGeometry(QtCore.QRect(250, 170, 16, 17))
        self.chkOrigNorm5.setText(_fromUtf8(""))
        self.chkOrigNorm5.setObjectName(_fromUtf8("chkOrigNorm5"))
        self.chkOrigNorm1 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigNorm1.setGeometry(QtCore.QRect(170, 170, 16, 17))
        self.chkOrigNorm1.setText(_fromUtf8(""))
        self.chkOrigNorm1.setObjectName(_fromUtf8("chkOrigNorm1"))
        self.chkOrigEasy7 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigEasy7.setGeometry(QtCore.QRect(290, 150, 16, 17))
        self.chkOrigEasy7.setText(_fromUtf8(""))
        self.chkOrigEasy7.setObjectName(_fromUtf8("chkOrigEasy7"))
        self.chkOrigEasy11 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigEasy11.setGeometry(QtCore.QRect(370, 150, 16, 17))
        self.chkOrigEasy11.setText(_fromUtf8(""))
        self.chkOrigEasy11.setObjectName(_fromUtf8("chkOrigEasy11"))
        self.chkOrigEasy13 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigEasy13.setGeometry(QtCore.QRect(410, 150, 16, 17))
        self.chkOrigEasy13.setText(_fromUtf8(""))
        self.chkOrigEasy13.setObjectName(_fromUtf8("chkOrigEasy13"))
        self.chkOrigEasy5 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigEasy5.setGeometry(QtCore.QRect(250, 150, 16, 17))
        self.chkOrigEasy5.setText(_fromUtf8(""))
        self.chkOrigEasy5.setObjectName(_fromUtf8("chkOrigEasy5"))
        self.chkOrigHard14 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigHard14.setGeometry(QtCore.QRect(430, 190, 16, 17))
        self.chkOrigHard14.setText(_fromUtf8(""))
        self.chkOrigHard14.setObjectName(_fromUtf8("chkOrigHard14"))
        self.chkOrigNorm12 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigNorm12.setGeometry(QtCore.QRect(390, 170, 16, 17))
        self.chkOrigNorm12.setText(_fromUtf8(""))
        self.chkOrigNorm12.setObjectName(_fromUtf8("chkOrigNorm12"))
        self.chkOrigHard9 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigHard9.setGeometry(QtCore.QRect(330, 190, 16, 17))
        self.chkOrigHard9.setText(_fromUtf8(""))
        self.chkOrigHard9.setObjectName(_fromUtf8("chkOrigHard9"))
        self.chkOrigEasy8 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigEasy8.setGeometry(QtCore.QRect(310, 150, 16, 17))
        self.chkOrigEasy8.setText(_fromUtf8(""))
        self.chkOrigEasy8.setObjectName(_fromUtf8("chkOrigEasy8"))
        self.chkOrigHard15 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigHard15.setGeometry(QtCore.QRect(450, 190, 16, 17))
        self.chkOrigHard15.setText(_fromUtf8(""))
        self.chkOrigHard15.setObjectName(_fromUtf8("chkOrigHard15"))
        self.chkOrigHard3 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigHard3.setGeometry(QtCore.QRect(210, 190, 16, 17))
        self.chkOrigHard3.setText(_fromUtf8(""))
        self.chkOrigHard3.setObjectName(_fromUtf8("chkOrigHard3"))
        self.chkOrigNorm6 = QtGui.QCheckBox(self.groupBox)
        self.chkOrigNorm6.setGeometry(QtCore.QRect(270, 170, 16, 17))
        self.chkOrigNorm6.setText(_fromUtf8(""))
        self.chkOrigNorm6.setObjectName(_fromUtf8("chkOrigNorm6"))
        self.groupBox_2 = QtGui.QGroupBox(Anagram)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 520, 311, 80))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Anagram", "Extra Letters", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.txtExtraTrans = QtGui.QLineEdit(self.groupBox_2)
        self.txtExtraTrans.setGeometry(QtCore.QRect(70, 20, 231, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        self.txtExtraTrans.setFont(font)
        self.txtExtraTrans.setText(QtGui.QApplication.translate("Anagram", "ＸＸＸＸＸＸＸＸＸＸＸＸＸＸＸ", None, QtGui.QApplication.UnicodeUTF8))
        self.txtExtraTrans.setMaxLength(15)
        self.txtExtraTrans.setObjectName(_fromUtf8("txtExtraTrans"))
        self.txtExtraOrig = QtGui.QLineEdit(self.groupBox_2)
        self.txtExtraOrig.setGeometry(QtCore.QRect(70, 50, 231, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        self.txtExtraOrig.setFont(font)
        self.txtExtraOrig.setText(QtGui.QApplication.translate("Anagram", "まいぞのなえぎ", None, QtGui.QApplication.UnicodeUTF8))
        self.txtExtraOrig.setMaxLength(15)
        self.txtExtraOrig.setReadOnly(True)
        self.txtExtraOrig.setObjectName(_fromUtf8("txtExtraOrig"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(-10, 20, 71, 20))
        self.label_9.setText(QtGui.QApplication.translate("Anagram", "Translated", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(-10, 50, 71, 20))
        self.label_10.setText(QtGui.QApplication.translate("Anagram", "Original", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))

        self.retranslateUi(Anagram)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Anagram.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Anagram.reject)
        QtCore.QObject.connect(self.txtSolutionTrans, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Anagram.changed_solution)
        QtCore.QObject.connect(self.txtExtraTrans, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), Anagram.edited_extra)
        QtCore.QObject.connect(self.txtSolutionTrans, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), Anagram.edited_solution)
        QtCore.QMetaObject.connectSlotsByName(Anagram)
        Anagram.setTabOrder(self.txtSolutionTrans, self.chkTransEasy1)
        Anagram.setTabOrder(self.chkTransEasy1, self.chkTransEasy2)
        Anagram.setTabOrder(self.chkTransEasy2, self.chkTransEasy3)
        Anagram.setTabOrder(self.chkTransEasy3, self.chkTransEasy4)
        Anagram.setTabOrder(self.chkTransEasy4, self.chkTransEasy5)
        Anagram.setTabOrder(self.chkTransEasy5, self.chkTransEasy6)
        Anagram.setTabOrder(self.chkTransEasy6, self.chkTransEasy7)
        Anagram.setTabOrder(self.chkTransEasy7, self.chkTransEasy8)
        Anagram.setTabOrder(self.chkTransEasy8, self.chkTransEasy9)
        Anagram.setTabOrder(self.chkTransEasy9, self.chkTransEasy10)
        Anagram.setTabOrder(self.chkTransEasy10, self.chkTransEasy11)
        Anagram.setTabOrder(self.chkTransEasy11, self.chkTransEasy12)
        Anagram.setTabOrder(self.chkTransEasy12, self.chkTransEasy13)
        Anagram.setTabOrder(self.chkTransEasy13, self.chkTransEasy14)
        Anagram.setTabOrder(self.chkTransEasy14, self.chkTransEasy15)
        Anagram.setTabOrder(self.chkTransEasy15, self.chkTransNorm1)
        Anagram.setTabOrder(self.chkTransNorm1, self.chkTransNorm2)
        Anagram.setTabOrder(self.chkTransNorm2, self.chkTransNorm3)
        Anagram.setTabOrder(self.chkTransNorm3, self.chkTransNorm4)
        Anagram.setTabOrder(self.chkTransNorm4, self.chkTransNorm5)
        Anagram.setTabOrder(self.chkTransNorm5, self.chkTransNorm6)
        Anagram.setTabOrder(self.chkTransNorm6, self.chkTransNorm7)
        Anagram.setTabOrder(self.chkTransNorm7, self.chkTransNorm8)
        Anagram.setTabOrder(self.chkTransNorm8, self.chkTransNorm9)
        Anagram.setTabOrder(self.chkTransNorm9, self.chkTransNorm10)
        Anagram.setTabOrder(self.chkTransNorm10, self.chkTransNorm11)
        Anagram.setTabOrder(self.chkTransNorm11, self.chkTransNorm12)
        Anagram.setTabOrder(self.chkTransNorm12, self.chkTransNorm13)
        Anagram.setTabOrder(self.chkTransNorm13, self.chkTransNorm14)
        Anagram.setTabOrder(self.chkTransNorm14, self.chkTransNorm15)
        Anagram.setTabOrder(self.chkTransNorm15, self.chkTransHard1)
        Anagram.setTabOrder(self.chkTransHard1, self.chkTransHard2)
        Anagram.setTabOrder(self.chkTransHard2, self.chkTransHard3)
        Anagram.setTabOrder(self.chkTransHard3, self.chkTransHard4)
        Anagram.setTabOrder(self.chkTransHard4, self.chkTransHard5)
        Anagram.setTabOrder(self.chkTransHard5, self.chkTransHard6)
        Anagram.setTabOrder(self.chkTransHard6, self.chkTransHard7)
        Anagram.setTabOrder(self.chkTransHard7, self.chkTransHard8)
        Anagram.setTabOrder(self.chkTransHard8, self.chkTransHard9)
        Anagram.setTabOrder(self.chkTransHard9, self.chkTransHard10)
        Anagram.setTabOrder(self.chkTransHard10, self.chkTransHard11)
        Anagram.setTabOrder(self.chkTransHard11, self.chkTransHard12)
        Anagram.setTabOrder(self.chkTransHard12, self.chkTransHard13)
        Anagram.setTabOrder(self.chkTransHard13, self.chkTransHard14)
        Anagram.setTabOrder(self.chkTransHard14, self.chkTransHard15)
        Anagram.setTabOrder(self.chkTransHard15, self.txtSolutionOrig)
        Anagram.setTabOrder(self.txtSolutionOrig, self.chkOrigEasy1)
        Anagram.setTabOrder(self.chkOrigEasy1, self.chkOrigEasy2)
        Anagram.setTabOrder(self.chkOrigEasy2, self.chkOrigEasy3)
        Anagram.setTabOrder(self.chkOrigEasy3, self.chkOrigEasy4)
        Anagram.setTabOrder(self.chkOrigEasy4, self.chkOrigEasy5)
        Anagram.setTabOrder(self.chkOrigEasy5, self.chkOrigEasy6)
        Anagram.setTabOrder(self.chkOrigEasy6, self.chkOrigEasy7)
        Anagram.setTabOrder(self.chkOrigEasy7, self.chkOrigEasy8)
        Anagram.setTabOrder(self.chkOrigEasy8, self.chkOrigEasy9)
        Anagram.setTabOrder(self.chkOrigEasy9, self.chkOrigEasy10)
        Anagram.setTabOrder(self.chkOrigEasy10, self.chkOrigEasy11)
        Anagram.setTabOrder(self.chkOrigEasy11, self.chkOrigEasy12)
        Anagram.setTabOrder(self.chkOrigEasy12, self.chkOrigEasy13)
        Anagram.setTabOrder(self.chkOrigEasy13, self.chkOrigEasy14)
        Anagram.setTabOrder(self.chkOrigEasy14, self.chkOrigEasy15)
        Anagram.setTabOrder(self.chkOrigEasy15, self.chkOrigNorm1)
        Anagram.setTabOrder(self.chkOrigNorm1, self.chkOrigNorm2)
        Anagram.setTabOrder(self.chkOrigNorm2, self.chkOrigNorm3)
        Anagram.setTabOrder(self.chkOrigNorm3, self.chkOrigNorm4)
        Anagram.setTabOrder(self.chkOrigNorm4, self.chkOrigNorm5)
        Anagram.setTabOrder(self.chkOrigNorm5, self.chkOrigNorm6)
        Anagram.setTabOrder(self.chkOrigNorm6, self.chkOrigNorm7)
        Anagram.setTabOrder(self.chkOrigNorm7, self.chkOrigNorm8)
        Anagram.setTabOrder(self.chkOrigNorm8, self.chkOrigNorm9)
        Anagram.setTabOrder(self.chkOrigNorm9, self.chkOrigNorm10)
        Anagram.setTabOrder(self.chkOrigNorm10, self.chkOrigNorm11)
        Anagram.setTabOrder(self.chkOrigNorm11, self.chkOrigNorm12)
        Anagram.setTabOrder(self.chkOrigNorm12, self.chkOrigNorm13)
        Anagram.setTabOrder(self.chkOrigNorm13, self.chkOrigNorm14)
        Anagram.setTabOrder(self.chkOrigNorm14, self.chkOrigNorm15)
        Anagram.setTabOrder(self.chkOrigNorm15, self.chkOrigHard1)
        Anagram.setTabOrder(self.chkOrigHard1, self.chkOrigHard2)
        Anagram.setTabOrder(self.chkOrigHard2, self.chkOrigHard3)
        Anagram.setTabOrder(self.chkOrigHard3, self.chkOrigHard4)
        Anagram.setTabOrder(self.chkOrigHard4, self.chkOrigHard5)
        Anagram.setTabOrder(self.chkOrigHard5, self.chkOrigHard6)
        Anagram.setTabOrder(self.chkOrigHard6, self.chkOrigHard7)
        Anagram.setTabOrder(self.chkOrigHard7, self.chkOrigHard8)
        Anagram.setTabOrder(self.chkOrigHard8, self.chkOrigHard9)
        Anagram.setTabOrder(self.chkOrigHard9, self.chkOrigHard10)
        Anagram.setTabOrder(self.chkOrigHard10, self.chkOrigHard11)
        Anagram.setTabOrder(self.chkOrigHard11, self.chkOrigHard12)
        Anagram.setTabOrder(self.chkOrigHard12, self.chkOrigHard13)
        Anagram.setTabOrder(self.chkOrigHard13, self.chkOrigHard14)
        Anagram.setTabOrder(self.chkOrigHard14, self.chkOrigHard15)
        Anagram.setTabOrder(self.chkOrigHard15, self.txtExtraTrans)
        Anagram.setTabOrder(self.txtExtraTrans, self.txtExtraOrig)
        Anagram.setTabOrder(self.txtExtraOrig, self.buttonBox)

    def retranslateUi(self, Anagram):
        pass

import icons_rc
