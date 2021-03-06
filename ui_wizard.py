# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt\ui\wizard.ui'
#
# Created: Mon Jun 03 01:17:18 2013
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SetupWizard(object):
    def setupUi(self, SetupWizard):
        SetupWizard.setObjectName(_fromUtf8("SetupWizard"))
        SetupWizard.resize(585, 666)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        SetupWizard.setFont(font)
        SetupWizard.setWindowTitle(QtGui.QApplication.translate("SetupWizard", "The Super Duper Script Editor - Setup Wizard", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/monokuma.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SetupWizard.setWindowIcon(icon)
        SetupWizard.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout = QtGui.QVBoxLayout(SetupWizard)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.grpStep1 = QtGui.QGroupBox(SetupWizard)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        font.setPointSize(8)
        self.grpStep1.setFont(font)
        self.grpStep1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.grpStep1.setTitle(QtGui.QApplication.translate("SetupWizard", "Step 1", None, QtGui.QApplication.UnicodeUTF8))
        self.grpStep1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.grpStep1.setObjectName(_fromUtf8("grpStep1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.grpStep1)
        self.verticalLayout_2.setContentsMargins(-1, 2, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.grpStep1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("SetupWizard", "Extract the Danganronpa (PSP The Best) ISO somewhere and point to that folder.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.txtIso = QtGui.QLineEdit(self.grpStep1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtIso.setFont(font)
        self.txtIso.setText(_fromUtf8(""))
        self.txtIso.setObjectName(_fromUtf8("txtIso"))
        self.horizontalLayout.addWidget(self.txtIso)
        self.btnIsoBrowse = QtGui.QPushButton(self.grpStep1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btnIsoBrowse.setFont(font)
        self.btnIsoBrowse.setText(QtGui.QApplication.translate("SetupWizard", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnIsoBrowse.setObjectName(_fromUtf8("btnIsoBrowse"))
        self.horizontalLayout.addWidget(self.btnIsoBrowse)
        self.btnIsoOK = QtGui.QPushButton(self.grpStep1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnIsoOK.sizePolicy().hasHeightForWidth())
        self.btnIsoOK.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btnIsoOK.setFont(font)
        self.btnIsoOK.setText(QtGui.QApplication.translate("SetupWizard", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.btnIsoOK.setObjectName(_fromUtf8("btnIsoOK"))
        self.horizontalLayout.addWidget(self.btnIsoOK)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.grpStep1)
        self.grpStep2 = QtGui.QGroupBox(SetupWizard)
        self.grpStep2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        font.setPointSize(8)
        self.grpStep2.setFont(font)
        self.grpStep2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.grpStep2.setTitle(QtGui.QApplication.translate("SetupWizard", "Step 2", None, QtGui.QApplication.UnicodeUTF8))
        self.grpStep2.setObjectName(_fromUtf8("grpStep2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.grpStep2)
        self.verticalLayout_4.setContentsMargins(-1, 2, -1, -1)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_2 = QtGui.QLabel(self.grpStep2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setText(QtGui.QApplication.translate("SetupWizard", "Select a folder for your workspace. (At least 3 GB free space necessary.)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.txtWorkspace = QtGui.QLineEdit(self.grpStep2)
        self.txtWorkspace.setText(_fromUtf8(""))
        self.txtWorkspace.setObjectName(_fromUtf8("txtWorkspace"))
        self.horizontalLayout_3.addWidget(self.txtWorkspace)
        self.btnWorkspaceBrowse = QtGui.QPushButton(self.grpStep2)
        self.btnWorkspaceBrowse.setText(QtGui.QApplication.translate("SetupWizard", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnWorkspaceBrowse.setObjectName(_fromUtf8("btnWorkspaceBrowse"))
        self.horizontalLayout_3.addWidget(self.btnWorkspaceBrowse)
        self.btnWorkspaceOK = QtGui.QPushButton(self.grpStep2)
        self.btnWorkspaceOK.setText(QtGui.QApplication.translate("SetupWizard", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.btnWorkspaceOK.setObjectName(_fromUtf8("btnWorkspaceOK"))
        self.horizontalLayout_3.addWidget(self.btnWorkspaceOK)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.grpStep2)
        self.grpStep3 = QtGui.QGroupBox(SetupWizard)
        self.grpStep3.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        font.setPointSize(8)
        self.grpStep3.setFont(font)
        self.grpStep3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.grpStep3.setTitle(QtGui.QApplication.translate("SetupWizard", "Step 3", None, QtGui.QApplication.UnicodeUTF8))
        self.grpStep3.setObjectName(_fromUtf8("grpStep3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.grpStep3)
        self.verticalLayout_3.setContentsMargins(0, 2, 0, -1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_4 = QtGui.QLabel(self.grpStep3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setText(QtGui.QApplication.translate("SetupWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Meiryo UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Download <a href=\"http://wololo.net/downloads/index.php/download/1254\"><span style=\" text-decoration: underline; color:#0000ff;\">PRX Decrypter</span></a> and install it on your PSP.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Create a directory named &quot;enc&quot; on the root of your PSP.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copy EBOOT.BIN from ISO/PSP_GAME/SYSDIR to &quot;enc&quot; on your PSP.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Run PRX Decrypter.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Decrypt the EBOOT.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copy the decrypted EBOOT into your workspace.</li></ol></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.btnEbootOK = QtGui.QPushButton(self.grpStep3)
        self.btnEbootOK.setText(QtGui.QApplication.translate("SetupWizard", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEbootOK.setObjectName(_fromUtf8("btnEbootOK"))
        self.horizontalLayout_5.addWidget(self.btnEbootOK)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.grpStep3)
        self.grpStep4 = QtGui.QGroupBox(SetupWizard)
        self.grpStep4.setEnabled(False)
        self.grpStep4.setTitle(QtGui.QApplication.translate("SetupWizard", "Step 4", None, QtGui.QApplication.UnicodeUTF8))
        self.grpStep4.setObjectName(_fromUtf8("grpStep4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.grpStep4)
        self.horizontalLayout_2.setContentsMargins(9, 2, 9, 9)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(172, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btnSetupWorkspace = QtGui.QPushButton(self.grpStep4)
        self.btnSetupWorkspace.setText(QtGui.QApplication.translate("SetupWizard", "Set up workspace", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSetupWorkspace.setObjectName(_fromUtf8("btnSetupWorkspace"))
        self.horizontalLayout_2.addWidget(self.btnSetupWorkspace)
        self.btnWorkspaceSkip = QtGui.QPushButton(self.grpStep4)
        self.btnWorkspaceSkip.setText(QtGui.QApplication.translate("SetupWizard", "Skip", None, QtGui.QApplication.UnicodeUTF8))
        self.btnWorkspaceSkip.setObjectName(_fromUtf8("btnWorkspaceSkip"))
        self.horizontalLayout_2.addWidget(self.btnWorkspaceSkip)
        spacerItem3 = QtGui.QSpacerItem(172, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.grpStep4)
        self.grpStep5 = QtGui.QGroupBox(SetupWizard)
        self.grpStep5.setEnabled(False)
        self.grpStep5.setTitle(QtGui.QApplication.translate("SetupWizard", "Step 5", None, QtGui.QApplication.UnicodeUTF8))
        self.grpStep5.setObjectName(_fromUtf8("grpStep5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.grpStep5)
        self.verticalLayout_5.setContentsMargins(-1, 2, -1, -1)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.btnCopyGfx = QtGui.QPushButton(self.grpStep5)
        self.btnCopyGfx.setText(QtGui.QApplication.translate("SetupWizard", "Copy graphical data for editor", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCopyGfx.setObjectName(_fromUtf8("btnCopyGfx"))
        self.horizontalLayout_7.addWidget(self.btnCopyGfx)
        self.chkGimToPng = QtGui.QCheckBox(self.grpStep5)
        self.chkGimToPng.setText(QtGui.QApplication.translate("SetupWizard", "Convert to PNG", None, QtGui.QApplication.UnicodeUTF8))
        self.chkGimToPng.setChecked(True)
        self.chkGimToPng.setObjectName(_fromUtf8("chkGimToPng"))
        self.horizontalLayout_7.addWidget(self.chkGimToPng)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.label_3 = QtGui.QLabel(self.grpStep5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setText(QtGui.QApplication.translate("SetupWizard", "NOTE: You can only convert to PNG on Windows. If you\'re on another OS, you will need to find something else to convert the GIM files in [Workspace]/!editor/gfx to PNG.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_5.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.grpStep5)
        self.grpStep6 = QtGui.QGroupBox(SetupWizard)
        self.grpStep6.setEnabled(False)
        self.grpStep6.setTitle(QtGui.QApplication.translate("SetupWizard", "Step 6", None, QtGui.QApplication.UnicodeUTF8))
        self.grpStep6.setObjectName(_fromUtf8("grpStep6"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.grpStep6)
        self.verticalLayout_6.setContentsMargins(-1, 2, -1, -1)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_5 = QtGui.QLabel(self.grpStep6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setText(QtGui.QApplication.translate("SetupWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Meiryo UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Point to (or create) a CSV file for terminology.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you\'re working in a group, this should be someplace everyone can access changes immediately, like a shared Dropbox folder.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setScaledContents(False)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_6.addWidget(self.label_5)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.txtTerminology = QtGui.QLineEdit(self.grpStep6)
        self.txtTerminology.setObjectName(_fromUtf8("txtTerminology"))
        self.horizontalLayout_8.addWidget(self.txtTerminology)
        self.btnTerminologyNew = QtGui.QPushButton(self.grpStep6)
        self.btnTerminologyNew.setText(QtGui.QApplication.translate("SetupWizard", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTerminologyNew.setObjectName(_fromUtf8("btnTerminologyNew"))
        self.horizontalLayout_8.addWidget(self.btnTerminologyNew)
        self.btnTerminologyBrowse = QtGui.QPushButton(self.grpStep6)
        self.btnTerminologyBrowse.setText(QtGui.QApplication.translate("SetupWizard", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTerminologyBrowse.setObjectName(_fromUtf8("btnTerminologyBrowse"))
        self.horizontalLayout_8.addWidget(self.btnTerminologyBrowse)
        self.btnTerminologyOK = QtGui.QPushButton(self.grpStep6)
        self.btnTerminologyOK.setText(QtGui.QApplication.translate("SetupWizard", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTerminologyOK.setObjectName(_fromUtf8("btnTerminologyOK"))
        self.horizontalLayout_8.addWidget(self.btnTerminologyOK)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addWidget(self.grpStep6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.btnFinish = QtGui.QPushButton(SetupWizard)
        self.btnFinish.setEnabled(False)
        self.btnFinish.setText(QtGui.QApplication.translate("SetupWizard", "Finish", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFinish.setObjectName(_fromUtf8("btnFinish"))
        self.horizontalLayout_4.addWidget(self.btnFinish)
        self.btnCancel = QtGui.QPushButton(SetupWizard)
        self.btnCancel.setText(QtGui.QApplication.translate("SetupWizard", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout_4.addWidget(self.btnCancel)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(SetupWizard)
        QtCore.QObject.connect(self.btnCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), SetupWizard.reject)
        QtCore.QObject.connect(self.btnFinish, QtCore.SIGNAL(_fromUtf8("clicked()")), SetupWizard.accept)
        QtCore.QMetaObject.connectSlotsByName(SetupWizard)

    def retranslateUi(self, SetupWizard):
        pass

import icons_rc
