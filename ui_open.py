# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt\ui\openmenu.ui'
#
# Created: Wed Dec 05 21:19:58 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_OpenMenu(object):
    def setupUi(self, OpenMenu):
        OpenMenu.setObjectName(_fromUtf8("OpenMenu"))
        OpenMenu.resize(480, 324)
        OpenMenu.setMinimumSize(QtCore.QSize(480, 324))
        OpenMenu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        OpenMenu.setWindowTitle(QtGui.QApplication.translate("OpenMenu", "Open", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/monokuma-green.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        OpenMenu.setWindowIcon(icon)
        self.horizontalLayout = QtGui.QHBoxLayout(OpenMenu)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.treeFileList = QtGui.QTreeWidget(OpenMenu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeFileList.sizePolicy().hasHeightForWidth())
        self.treeFileList.setSizePolicy(sizePolicy)
        self.treeFileList.setAlternatingRowColors(True)
        self.treeFileList.setIndentation(15)
        self.treeFileList.setAnimated(True)
        self.treeFileList.setObjectName(_fromUtf8("treeFileList"))
        self.treeFileList.headerItem().setText(0, QtGui.QApplication.translate("OpenMenu", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.treeFileList.header().setVisible(False)
        self.horizontalLayout.addWidget(self.treeFileList)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(OpenMenu)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("OpenMenu", "Chapter", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.lblChapter = QtGui.QLabel(OpenMenu)
        self.lblChapter.setText(QtGui.QApplication.translate("OpenMenu", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.lblChapter.setIndent(10)
        self.lblChapter.setObjectName(_fromUtf8("lblChapter"))
        self.verticalLayout.addWidget(self.lblChapter)
        self.label_3 = QtGui.QLabel(OpenMenu)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setText(QtGui.QApplication.translate("OpenMenu", "Scene", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.lblScene = QtGui.QLabel(OpenMenu)
        self.lblScene.setText(QtGui.QApplication.translate("OpenMenu", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.lblScene.setIndent(10)
        self.lblScene.setObjectName(_fromUtf8("lblScene"))
        self.verticalLayout.addWidget(self.lblScene)
        self.label_4 = QtGui.QLabel(OpenMenu)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setText(QtGui.QApplication.translate("OpenMenu", "Room", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.lblRoom = QtGui.QLabel(OpenMenu)
        self.lblRoom.setText(QtGui.QApplication.translate("OpenMenu", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.lblRoom.setIndent(10)
        self.lblRoom.setObjectName(_fromUtf8("lblRoom"))
        self.verticalLayout.addWidget(self.lblRoom)
        self.label_6 = QtGui.QLabel(OpenMenu)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setText(QtGui.QApplication.translate("OpenMenu", "Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.lblMode = QtGui.QLabel(OpenMenu)
        self.lblMode.setText(QtGui.QApplication.translate("OpenMenu", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMode.setIndent(10)
        self.lblMode.setObjectName(_fromUtf8("lblMode"))
        self.verticalLayout.addWidget(self.lblMode)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(OpenMenu)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setText(QtGui.QApplication.translate("OpenMenu", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.txtSearch = QtGui.QLineEdit(OpenMenu)
        self.txtSearch.setObjectName(_fromUtf8("txtSearch"))
        self.verticalLayout.addWidget(self.txtSearch)
        self.buttonBox = QtGui.QDialogButtonBox(OpenMenu)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(OpenMenu)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), OpenMenu.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), OpenMenu.reject)
        QtCore.QObject.connect(self.treeFileList, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QTreeWidgetItem*,QTreeWidgetItem*)")), OpenMenu.changeSelection)
        QtCore.QObject.connect(self.treeFileList, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QTreeWidgetItem*,int)")), OpenMenu.doubleClicked)
        QtCore.QObject.connect(self.txtSearch, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), OpenMenu.findDirectory)
        QtCore.QMetaObject.connectSlotsByName(OpenMenu)

    def retranslateUi(self, OpenMenu):
        pass

import icons_rc
