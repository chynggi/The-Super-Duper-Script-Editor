# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt\ui\search.ui'
#
# Created: Mon Dec 31 22:31:10 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SearchMenu(object):
    def setupUi(self, SearchMenu):
        SearchMenu.setObjectName(_fromUtf8("SearchMenu"))
        SearchMenu.resize(847, 339)
        SearchMenu.setWindowTitle(QtGui.QApplication.translate("SearchMenu", "Search", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/monokuma-green.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SearchMenu.setWindowIcon(icon)
        SearchMenu.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout_3 = QtGui.QVBoxLayout(SearchMenu)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.txtQuery = QtGui.QLineEdit(SearchMenu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtQuery.sizePolicy().hasHeightForWidth())
        self.txtQuery.setSizePolicy(sizePolicy)
        self.txtQuery.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txtQuery.setText(_fromUtf8(""))
        self.txtQuery.setObjectName(_fromUtf8("txtQuery"))
        self.horizontalLayout.addWidget(self.txtQuery)
        self.btnSearch = QtGui.QPushButton(SearchMenu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSearch.sizePolicy().hasHeightForWidth())
        self.btnSearch.setSizePolicy(sizePolicy)
        self.btnSearch.setText(QtGui.QApplication.translate("SearchMenu", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSearch.setDefault(True)
        self.btnSearch.setObjectName(_fromUtf8("btnSearch"))
        self.horizontalLayout.addWidget(self.btnSearch)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeResults = QtGui.QTreeWidget(SearchMenu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeResults.sizePolicy().hasHeightForWidth())
        self.treeResults.setSizePolicy(sizePolicy)
        self.treeResults.setMinimumSize(QtCore.QSize(0, 0))
        self.treeResults.setMaximumSize(QtCore.QSize(283, 16777215))
        self.treeResults.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.treeResults.setIndentation(15)
        self.treeResults.setObjectName(_fromUtf8("treeResults"))
        self.treeResults.headerItem().setText(0, QtGui.QApplication.translate("SearchMenu", "Results (0)", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout.addWidget(self.treeResults)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_14 = QtGui.QLabel(SearchMenu)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setText(QtGui.QApplication.translate("SearchMenu", "Translated", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_2.addWidget(self.label_14)
        self.txtTranslated = QtGui.QPlainTextEdit(SearchMenu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtTranslated.sizePolicy().hasHeightForWidth())
        self.txtTranslated.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        font.setPointSize(10)
        self.txtTranslated.setFont(font)
        self.txtTranslated.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.txtTranslated.setTabChangesFocus(True)
        self.txtTranslated.setLineWrapMode(QtGui.QPlainTextEdit.WidgetWidth)
        self.txtTranslated.setReadOnly(True)
        self.txtTranslated.setPlainText(_fromUtf8(""))
        self.txtTranslated.setTabStopWidth(20)
        self.txtTranslated.setObjectName(_fromUtf8("txtTranslated"))
        self.verticalLayout_2.addWidget(self.txtTranslated)
        self.label_15 = QtGui.QLabel(SearchMenu)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setText(QtGui.QApplication.translate("SearchMenu", "Original", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_2.addWidget(self.label_15)
        self.txtOriginal = QtGui.QPlainTextEdit(SearchMenu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtOriginal.sizePolicy().hasHeightForWidth())
        self.txtOriginal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        font.setPointSize(10)
        self.txtOriginal.setFont(font)
        self.txtOriginal.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.txtOriginal.setTabChangesFocus(True)
        self.txtOriginal.setLineWrapMode(QtGui.QPlainTextEdit.WidgetWidth)
        self.txtOriginal.setReadOnly(True)
        self.txtOriginal.setPlainText(_fromUtf8(""))
        self.txtOriginal.setTabStopWidth(20)
        self.txtOriginal.setObjectName(_fromUtf8("txtOriginal"))
        self.verticalLayout_2.addWidget(self.txtOriginal)
        self.label_16 = QtGui.QLabel(SearchMenu)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setText(QtGui.QApplication.translate("SearchMenu", "Comments", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_2.addWidget(self.label_16)
        self.txtComments = QtGui.QPlainTextEdit(SearchMenu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtComments.sizePolicy().hasHeightForWidth())
        self.txtComments.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        font.setPointSize(10)
        self.txtComments.setFont(font)
        self.txtComments.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.txtComments.setTabChangesFocus(True)
        self.txtComments.setLineWrapMode(QtGui.QPlainTextEdit.WidgetWidth)
        self.txtComments.setReadOnly(True)
        self.txtComments.setPlainText(_fromUtf8(""))
        self.txtComments.setTabStopWidth(20)
        self.txtComments.setObjectName(_fromUtf8("txtComments"))
        self.verticalLayout_2.addWidget(self.txtComments)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.grpAdvanced = QtGui.QGroupBox(SearchMenu)
        self.grpAdvanced.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        font.setPointSize(9)
        self.grpAdvanced.setFont(font)
        self.grpAdvanced.setTitle(QtGui.QApplication.translate("SearchMenu", "Advanced", None, QtGui.QApplication.UnicodeUTF8))
        self.grpAdvanced.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.grpAdvanced.setCheckable(False)
        self.grpAdvanced.setChecked(False)
        self.grpAdvanced.setObjectName(_fromUtf8("grpAdvanced"))
        self.chkAdvCase = QtGui.QCheckBox(self.grpAdvanced)
        self.chkAdvCase.setGeometry(QtCore.QRect(10, 40, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.chkAdvCase.setFont(font)
        self.chkAdvCase.setText(QtGui.QApplication.translate("SearchMenu", "Case Sensitive", None, QtGui.QApplication.UnicodeUTF8))
        self.chkAdvCase.setObjectName(_fromUtf8("chkAdvCase"))
        self.groupBox_2 = QtGui.QGroupBox(self.grpAdvanced)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 60, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("SearchMenu", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.chkAdvTrans = QtGui.QCheckBox(self.groupBox_2)
        self.chkAdvTrans.setGeometry(QtCore.QRect(10, 18, 91, 17))
        self.chkAdvTrans.setText(QtGui.QApplication.translate("SearchMenu", "Translated", None, QtGui.QApplication.UnicodeUTF8))
        self.chkAdvTrans.setChecked(True)
        self.chkAdvTrans.setObjectName(_fromUtf8("chkAdvTrans"))
        self.chkAdvOrig = QtGui.QCheckBox(self.groupBox_2)
        self.chkAdvOrig.setGeometry(QtCore.QRect(10, 38, 70, 17))
        self.chkAdvOrig.setText(QtGui.QApplication.translate("SearchMenu", "Original", None, QtGui.QApplication.UnicodeUTF8))
        self.chkAdvOrig.setChecked(True)
        self.chkAdvOrig.setObjectName(_fromUtf8("chkAdvOrig"))
        self.chkAdvComments = QtGui.QCheckBox(self.groupBox_2)
        self.chkAdvComments.setGeometry(QtCore.QRect(10, 58, 91, 17))
        self.chkAdvComments.setText(QtGui.QApplication.translate("SearchMenu", "Comments", None, QtGui.QApplication.UnicodeUTF8))
        self.chkAdvComments.setChecked(True)
        self.chkAdvComments.setObjectName(_fromUtf8("chkAdvComments"))
        self.chkAdvRegex = QtGui.QCheckBox(self.grpAdvanced)
        self.chkAdvRegex.setGeometry(QtCore.QRect(10, 20, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.chkAdvRegex.setFont(font)
        self.chkAdvRegex.setText(QtGui.QApplication.translate("SearchMenu", "Regex Search", None, QtGui.QApplication.UnicodeUTF8))
        self.chkAdvRegex.setChecked(True)
        self.chkAdvRegex.setObjectName(_fromUtf8("chkAdvRegex"))
        self.groupBox_3 = QtGui.QGroupBox(self.grpAdvanced)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 140, 181, 141))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setTitle(QtGui.QApplication.translate("SearchMenu", "Search Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(10, 94, 81, 16))
        self.label.setText(QtGui.QApplication.translate("SearchMenu", "Filter Regex", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.txtFilterRe = QtGui.QLineEdit(self.groupBox_3)
        self.txtFilterRe.setGeometry(QtCore.QRect(10, 114, 161, 20))
        self.txtFilterRe.setObjectName(_fromUtf8("txtFilterRe"))
        self.gridLayoutWidget = QtGui.QWidget(self.groupBox_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 161, 71))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.layoutSearchFilter = QtGui.QGridLayout(self.gridLayoutWidget)
        self.layoutSearchFilter.setMargin(0)
        self.layoutSearchFilter.setObjectName(_fromUtf8("layoutSearchFilter"))
        self.chkSearchCh3 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.chkSearchCh3.setText(QtGui.QApplication.translate("SearchMenu", "CH3", None, QtGui.QApplication.UnicodeUTF8))
        self.chkSearchCh3.setChecked(False)
        self.chkSearchCh3.setObjectName(_fromUtf8("chkSearchCh3"))
        self.layoutSearchFilter.addWidget(self.chkSearchCh3, 1, 0, 1, 1)
        self.chkSearchPlg = QtGui.QCheckBox(self.gridLayoutWidget)
        self.chkSearchPlg.setText(QtGui.QApplication.translate("SearchMenu", "PLG", None, QtGui.QApplication.UnicodeUTF8))
        self.chkSearchPlg.setChecked(False)
        self.chkSearchPlg.setObjectName(_fromUtf8("chkSearchPlg"))
        self.layoutSearchFilter.addWidget(self.chkSearchPlg, 0, 0, 1, 1)
        self.chkSearchCh1 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.chkSearchCh1.setText(QtGui.QApplication.translate("SearchMenu", "CH1", None, QtGui.QApplication.UnicodeUTF8))
        self.chkSearchCh1.setChecked(False)
        self.chkSearchCh1.setObjectName(_fromUtf8("chkSearchCh1"))
        self.layoutSearchFilter.addWidget(self.chkSearchCh1, 0, 1, 1, 1)
        self.chkSearchCh2 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.chkSearchCh2.setText(QtGui.QApplication.translate("SearchMenu", "CH2", None, QtGui.QApplication.UnicodeUTF8))
        self.chkSearchCh2.setChecked(False)
        self.chkSearchCh2.setObjectName(_fromUtf8("chkSearchCh2"))
        self.layoutSearchFilter.addWidget(self.chkSearchCh2, 0, 2, 1, 1)
        self.chkSearchCh4 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.chkSearchCh4.setText(QtGui.QApplication.translate("SearchMenu", "CH4", None, QtGui.QApplication.UnicodeUTF8))
        self.chkSearchCh4.setChecked(False)
        self.chkSearchCh4.setObjectName(_fromUtf8("chkSearchCh4"))
        self.layoutSearchFilter.addWidget(self.chkSearchCh4, 1, 1, 1, 1)
        self.chkSearchCh5 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.chkSearchCh5.setText(QtGui.QApplication.translate("SearchMenu", "CH5", None, QtGui.QApplication.UnicodeUTF8))
        self.chkSearchCh5.setChecked(False)
        self.chkSearchCh5.setObjectName(_fromUtf8("chkSearchCh5"))
        self.layoutSearchFilter.addWidget(self.chkSearchCh5, 1, 2, 1, 1)
        self.chkSearchCh6 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.chkSearchCh6.setText(QtGui.QApplication.translate("SearchMenu", "CH6", None, QtGui.QApplication.UnicodeUTF8))
        self.chkSearchCh6.setChecked(False)
        self.chkSearchCh6.setObjectName(_fromUtf8("chkSearchCh6"))
        self.layoutSearchFilter.addWidget(self.chkSearchCh6, 2, 0, 1, 1)
        self.chkSearchEpg = QtGui.QCheckBox(self.gridLayoutWidget)
        self.chkSearchEpg.setText(QtGui.QApplication.translate("SearchMenu", "EPG", None, QtGui.QApplication.UnicodeUTF8))
        self.chkSearchEpg.setChecked(False)
        self.chkSearchEpg.setObjectName(_fromUtf8("chkSearchEpg"))
        self.layoutSearchFilter.addWidget(self.chkSearchEpg, 2, 1, 1, 1)
        self.chkSearchFt = QtGui.QCheckBox(self.gridLayoutWidget)
        self.chkSearchFt.setText(QtGui.QApplication.translate("SearchMenu", "FT", None, QtGui.QApplication.UnicodeUTF8))
        self.chkSearchFt.setChecked(False)
        self.chkSearchFt.setObjectName(_fromUtf8("chkSearchFt"))
        self.layoutSearchFilter.addWidget(self.chkSearchFt, 2, 2, 1, 1)
        self.chkSearchEtc = QtGui.QCheckBox(self.gridLayoutWidget)
        self.chkSearchEtc.setText(QtGui.QApplication.translate("SearchMenu", "ETC", None, QtGui.QApplication.UnicodeUTF8))
        self.chkSearchEtc.setChecked(False)
        self.chkSearchEtc.setObjectName(_fromUtf8("chkSearchEtc"))
        self.layoutSearchFilter.addWidget(self.chkSearchEtc, 3, 1, 1, 1)
        self.chkSearchSys = QtGui.QCheckBox(self.gridLayoutWidget)
        self.chkSearchSys.setText(QtGui.QApplication.translate("SearchMenu", "SYS", None, QtGui.QApplication.UnicodeUTF8))
        self.chkSearchSys.setChecked(False)
        self.chkSearchSys.setObjectName(_fromUtf8("chkSearchSys"))
        self.layoutSearchFilter.addWidget(self.chkSearchSys, 3, 0, 1, 1)
        self.btnFilterSelAll = QtGui.QPushButton(self.grpAdvanced)
        self.btnFilterSelAll.setGeometry(QtCore.QRect(107, 140, 48, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btnFilterSelAll.setFont(font)
        self.btnFilterSelAll.setText(QtGui.QApplication.translate("SearchMenu", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFilterSelAll.setObjectName(_fromUtf8("btnFilterSelAll"))
        self.btnFilterSelNone = QtGui.QPushButton(self.grpAdvanced)
        self.btnFilterSelNone.setGeometry(QtCore.QRect(155, 140, 32, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btnFilterSelNone.setFont(font)
        self.btnFilterSelNone.setText(QtGui.QApplication.translate("SearchMenu", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFilterSelNone.setObjectName(_fromUtf8("btnFilterSelNone"))
        self.chkAdvNewline = QtGui.QCheckBox(self.grpAdvanced)
        self.chkAdvNewline.setGeometry(QtCore.QRect(110, 20, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.chkAdvNewline.setFont(font)
        self.chkAdvNewline.setText(QtGui.QApplication.translate("SearchMenu", "w/Newlines", None, QtGui.QApplication.UnicodeUTF8))
        self.chkAdvNewline.setChecked(False)
        self.chkAdvNewline.setObjectName(_fromUtf8("chkAdvNewline"))
        self.chkAdvNoTags = QtGui.QCheckBox(self.grpAdvanced)
        self.chkAdvNoTags.setGeometry(QtCore.QRect(110, 40, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.chkAdvNoTags.setFont(font)
        self.chkAdvNoTags.setText(QtGui.QApplication.translate("SearchMenu", "Ignore CLT", None, QtGui.QApplication.UnicodeUTF8))
        self.chkAdvNoTags.setChecked(False)
        self.chkAdvNoTags.setObjectName(_fromUtf8("chkAdvNoTags"))
        self.horizontalLayout_2.addWidget(self.grpAdvanced)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(SearchMenu)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Open)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(SearchMenu)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SearchMenu.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SearchMenu.accept)
        QtCore.QObject.connect(self.btnSearch, QtCore.SIGNAL(_fromUtf8("clicked()")), SearchMenu.search)
        QtCore.QObject.connect(self.treeResults, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QTreeWidgetItem*,QTreeWidgetItem*)")), SearchMenu.changedSelection)
        QtCore.QObject.connect(self.treeResults, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QTreeWidgetItem*,int)")), SearchMenu.doubleClicked)
        QtCore.QObject.connect(self.chkSearchPlg, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), SearchMenu.changedSearchFilter)
        QtCore.QObject.connect(self.chkSearchCh1, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), SearchMenu.changedSearchFilter)
        QtCore.QObject.connect(self.chkSearchCh2, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), SearchMenu.changedSearchFilter)
        QtCore.QObject.connect(self.chkSearchCh3, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), SearchMenu.changedSearchFilter)
        QtCore.QObject.connect(self.chkSearchCh4, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), SearchMenu.changedSearchFilter)
        QtCore.QObject.connect(self.chkSearchCh5, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), SearchMenu.changedSearchFilter)
        QtCore.QObject.connect(self.chkSearchCh6, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), SearchMenu.changedSearchFilter)
        QtCore.QObject.connect(self.chkSearchEpg, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), SearchMenu.changedSearchFilter)
        QtCore.QObject.connect(self.chkSearchFt, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), SearchMenu.changedSearchFilter)
        QtCore.QObject.connect(self.chkSearchEtc, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), SearchMenu.changedSearchFilter)
        QtCore.QObject.connect(self.chkSearchSys, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), SearchMenu.changedSearchFilter)
        QtCore.QMetaObject.connectSlotsByName(SearchMenu)
        SearchMenu.setTabOrder(self.txtQuery, self.btnSearch)
        SearchMenu.setTabOrder(self.btnSearch, self.treeResults)
        SearchMenu.setTabOrder(self.treeResults, self.chkAdvRegex)
        SearchMenu.setTabOrder(self.chkAdvRegex, self.chkAdvCase)
        SearchMenu.setTabOrder(self.chkAdvCase, self.chkAdvTrans)
        SearchMenu.setTabOrder(self.chkAdvTrans, self.chkAdvOrig)
        SearchMenu.setTabOrder(self.chkAdvOrig, self.chkAdvComments)
        SearchMenu.setTabOrder(self.chkAdvComments, self.btnFilterSelAll)
        SearchMenu.setTabOrder(self.btnFilterSelAll, self.btnFilterSelNone)
        SearchMenu.setTabOrder(self.btnFilterSelNone, self.chkSearchPlg)
        SearchMenu.setTabOrder(self.chkSearchPlg, self.chkSearchCh1)
        SearchMenu.setTabOrder(self.chkSearchCh1, self.chkSearchCh2)
        SearchMenu.setTabOrder(self.chkSearchCh2, self.chkSearchCh3)
        SearchMenu.setTabOrder(self.chkSearchCh3, self.chkSearchCh4)
        SearchMenu.setTabOrder(self.chkSearchCh4, self.chkSearchCh5)
        SearchMenu.setTabOrder(self.chkSearchCh5, self.chkSearchCh6)
        SearchMenu.setTabOrder(self.chkSearchCh6, self.chkSearchEpg)
        SearchMenu.setTabOrder(self.chkSearchEpg, self.chkSearchFt)
        SearchMenu.setTabOrder(self.chkSearchFt, self.chkSearchSys)
        SearchMenu.setTabOrder(self.chkSearchSys, self.chkSearchEtc)
        SearchMenu.setTabOrder(self.chkSearchEtc, self.txtFilterRe)
        SearchMenu.setTabOrder(self.txtFilterRe, self.txtTranslated)
        SearchMenu.setTabOrder(self.txtTranslated, self.txtOriginal)
        SearchMenu.setTabOrder(self.txtOriginal, self.txtComments)
        SearchMenu.setTabOrder(self.txtComments, self.buttonBox)

    def retranslateUi(self, SearchMenu):
        pass

import icons_rc
