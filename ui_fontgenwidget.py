# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt\ui\fontgenwidget.ui'
#
# Created: Wed Dec 26 20:28:57 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FontGenWidget(object):
    def setupUi(self, FontGenWidget):
        FontGenWidget.setObjectName(_fromUtf8("FontGenWidget"))
        FontGenWidget.resize(542, 464)
        FontGenWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        FontGenWidget.setWindowTitle(QtGui.QApplication.translate("FontGenWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(FontGenWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(FontGenWidget)
        self.groupBox.setTitle(QtGui.QApplication.translate("FontGenWidget", "Font Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setContentsMargins(-1, 4, -1, 8)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.cboFont = QtGui.QFontComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        self.cboFont.setCurrentFont(font)
        self.cboFont.setObjectName(_fromUtf8("cboFont"))
        self.horizontalLayout_4.addWidget(self.cboFont)
        self.label_5 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setText(QtGui.QApplication.translate("FontGenWidget", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.spnFontSize = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spnFontSize.sizePolicy().hasHeightForWidth())
        self.spnFontSize.setSizePolicy(sizePolicy)
        self.spnFontSize.setMinimum(1)
        self.spnFontSize.setMaximum(128)
        self.spnFontSize.setProperty("value", 11)
        self.spnFontSize.setObjectName(_fromUtf8("spnFontSize"))
        self.horizontalLayout_4.addWidget(self.spnFontSize)
        self.label = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText(QtGui.QApplication.translate("FontGenWidget", "Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.spnFontWeight = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spnFontWeight.sizePolicy().hasHeightForWidth())
        self.spnFontWeight.setSizePolicy(sizePolicy)
        self.spnFontWeight.setProperty("value", 50)
        self.spnFontWeight.setObjectName(_fromUtf8("spnFontWeight"))
        self.horizontalLayout_4.addWidget(self.spnFontWeight)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(FontGenWidget)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("FontGenWidget", "Advanced", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setContentsMargins(-1, 4, -1, 8)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setText(QtGui.QApplication.translate("FontGenWidget", "X Offset", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_5.addWidget(self.label_7)
        self.spnXOffset = QtGui.QSpinBox(self.groupBox_2)
        self.spnXOffset.setMinimum(-25)
        self.spnXOffset.setMaximum(25)
        self.spnXOffset.setObjectName(_fromUtf8("spnXOffset"))
        self.horizontalLayout_5.addWidget(self.spnXOffset)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setText(QtGui.QApplication.translate("FontGenWidget", "Y Offset", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_6.addWidget(self.label_8)
        self.spnYOffset = QtGui.QSpinBox(self.groupBox_2)
        self.spnYOffset.setMinimum(-25)
        self.spnYOffset.setMaximum(25)
        self.spnYOffset.setProperty("value", 2)
        self.spnYOffset.setObjectName(_fromUtf8("spnYOffset"))
        self.horizontalLayout_6.addWidget(self.spnYOffset)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setText(QtGui.QApplication.translate("FontGenWidget", "X Margin", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_7.addWidget(self.label_2)
        self.spnXMargin = QtGui.QSpinBox(self.groupBox_2)
        self.spnXMargin.setProperty("value", 2)
        self.spnXMargin.setObjectName(_fromUtf8("spnXMargin"))
        self.horizontalLayout_7.addWidget(self.spnXMargin)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setText(QtGui.QApplication.translate("FontGenWidget", "Y Margin", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_8.addWidget(self.label_10)
        self.spnYMargin = QtGui.QSpinBox(self.groupBox_2)
        self.spnYMargin.setProperty("value", 2)
        self.spnYMargin.setObjectName(_fromUtf8("spnYMargin"))
        self.horizontalLayout_8.addWidget(self.spnYMargin)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setText(QtGui.QApplication.translate("FontGenWidget", "Y Shift", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout.addWidget(self.label_12)
        self.spnYShift = QtGui.QSpinBox(self.groupBox_2)
        self.spnYShift.setMinimum(-25)
        self.spnYShift.setMaximum(25)
        self.spnYShift.setProperty("value", -6)
        self.spnYShift.setObjectName(_fromUtf8("spnYShift"))
        self.horizontalLayout.addWidget(self.spnYShift)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(FontGenWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setText(QtGui.QApplication.translate("FontGenWidget", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.lblPreview = QtGui.QLabel(FontGenWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPreview.sizePolicy().hasHeightForWidth())
        self.lblPreview.setSizePolicy(sizePolicy)
        self.lblPreview.setMinimumSize(QtCore.QSize(256, 256))
        self.lblPreview.setStyleSheet(_fromUtf8("background-color: black;"))
        self.lblPreview.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lblPreview.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblPreview.setText(_fromUtf8(""))
        self.lblPreview.setObjectName(_fromUtf8("lblPreview"))
        self.verticalLayout_2.addWidget(self.lblPreview)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.chkBoundingBoxes = QtGui.QCheckBox(FontGenWidget)
        self.chkBoundingBoxes.setText(QtGui.QApplication.translate("FontGenWidget", "Bounding Boxes", None, QtGui.QApplication.UnicodeUTF8))
        self.chkBoundingBoxes.setChecked(True)
        self.chkBoundingBoxes.setObjectName(_fromUtf8("chkBoundingBoxes"))
        self.horizontalLayout_2.addWidget(self.chkBoundingBoxes)
        self.chkAutoRefresh = QtGui.QCheckBox(FontGenWidget)
        self.chkAutoRefresh.setText(QtGui.QApplication.translate("FontGenWidget", "Auto", None, QtGui.QApplication.UnicodeUTF8))
        self.chkAutoRefresh.setChecked(True)
        self.chkAutoRefresh.setObjectName(_fromUtf8("chkAutoRefresh"))
        self.horizontalLayout_2.addWidget(self.chkAutoRefresh)
        self.btnRefreshPreview = QtGui.QPushButton(FontGenWidget)
        self.btnRefreshPreview.setText(QtGui.QApplication.translate("FontGenWidget", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRefreshPreview.setObjectName(_fromUtf8("btnRefreshPreview"))
        self.horizontalLayout_2.addWidget(self.btnRefreshPreview)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_4 = QtGui.QLabel(FontGenWidget)
        self.label_4.setText(QtGui.QApplication.translate("FontGenWidget", "Characters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.txtChars = QtGui.QTextEdit(FontGenWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtChars.sizePolicy().hasHeightForWidth())
        self.txtChars.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        font.setPointSize(11)
        self.txtChars.setFont(font)
        self.txtChars.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.txtChars.setObjectName(_fromUtf8("txtChars"))
        self.verticalLayout_3.addWidget(self.txtChars)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(FontGenWidget)
        QtCore.QObject.connect(self.cboFont, QtCore.SIGNAL(_fromUtf8("currentFontChanged(QFont)")), FontGenWidget.font_changed)
        QtCore.QObject.connect(self.spnFontSize, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), FontGenWidget.font_changed)
        QtCore.QObject.connect(self.spnFontWeight, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), FontGenWidget.font_changed)
        QtCore.QObject.connect(self.spnXOffset, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), FontGenWidget.adv_changed)
        QtCore.QObject.connect(self.spnYOffset, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), FontGenWidget.adv_changed)
        QtCore.QObject.connect(self.btnRefreshPreview, QtCore.SIGNAL(_fromUtf8("clicked()")), FontGenWidget.update_preview)
        QtCore.QObject.connect(self.txtChars, QtCore.SIGNAL(_fromUtf8("textChanged()")), FontGenWidget.chars_changed)
        QtCore.QObject.connect(self.spnXMargin, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), FontGenWidget.adv_changed)
        QtCore.QObject.connect(self.spnYMargin, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), FontGenWidget.adv_changed)
        QtCore.QObject.connect(self.spnYShift, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), FontGenWidget.adv_changed)
        QtCore.QObject.connect(self.chkBoundingBoxes, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), FontGenWidget.adv_changed)
        QtCore.QMetaObject.connectSlotsByName(FontGenWidget)

    def retranslateUi(self, FontGenWidget):
        pass

