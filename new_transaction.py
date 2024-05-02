# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transaction.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)
import res

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(300, 285)
        Dialog.setStyleSheet(u"font-family: Noto Sans SC;\n"
"background-color: #000")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.new_transaction = QFrame(Dialog)
        self.new_transaction.setObjectName(u"new_transaction")
        self.new_transaction.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.new_transaction.setFrameShape(QFrame.NoFrame)
        self.new_transaction.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.new_transaction)
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(12, 12, 12, 12)
        self.lbl_new_transaction = QLabel(self.new_transaction)
        self.lbl_new_transaction.setObjectName(u"lbl_new_transaction")
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        font.setPointSize(20)
        font.setBold(True)
        self.lbl_new_transaction.setFont(font)
        self.lbl_new_transaction.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.lbl_new_transaction.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.lbl_new_transaction)

        self.cb_choose_category = QComboBox(self.new_transaction)
        self.cb_choose_category.addItem("")
        self.cb_choose_category.addItem("")
        self.cb_choose_category.addItem("")
        self.cb_choose_category.addItem("")
        self.cb_choose_category.addItem("")
        self.cb_choose_category.setObjectName(u"cb_choose_category")
        self.cb_choose_category.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"    color: black;\n"
"}")

        self.verticalLayout_21.addWidget(self.cb_choose_category)

        self.dateEdit = QDateEdit(self.new_transaction)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")
        self.dateEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.dateEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateEdit.setDateTime(QDateTime(QDate(2022, 12, 31), QTime(22, 0, 0)))
        self.dateEdit.setCurrentSectionIndex(0)

        self.verticalLayout_21.addWidget(self.dateEdit)

        self.le_description = QLineEdit(self.new_transaction)
        self.le_description.setObjectName(u"le_description")
        self.le_description.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")
        self.le_description.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_21.addWidget(self.le_description)

        self.le_balance = QSpinBox(self.new_transaction)
        self.le_balance.setObjectName(u"le_balance")
        self.le_balance.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")
        self.le_balance.setMaximum(999999)

        self.verticalLayout_21.addWidget(self.le_balance)

        self.btn_new_transaction = QPushButton(self.new_transaction)
        self.btn_new_transaction.setObjectName(u"btn_new_transaction")
        self.btn_new_transaction.setMinimumSize(QSize(230, 50))
        font1 = QFont()
        font1.setFamilies([u"Noto Sans SC"])
        font1.setBold(True)
        self.btn_new_transaction.setFont(font1)
        self.btn_new_transaction.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/post_add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new_transaction.setIcon(icon)
        self.btn_new_transaction.setIconSize(QSize(24, 24))

        self.verticalLayout_21.addWidget(self.btn_new_transaction)


        self.verticalLayout.addWidget(self.new_transaction)


        self.retranslateUi(Dialog)

        self.cb_choose_category.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_new_transaction.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u0430\u044f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044f", None))
        self.cb_choose_category.setItemText(0, QCoreApplication.translate("Dialog", u"\u0420\u0430\u0431\u043e\u0442\u0430", None))
        self.cb_choose_category.setItemText(1, QCoreApplication.translate("Dialog", u"\u0410\u0432\u0442\u043e", None))
        self.cb_choose_category.setItemText(2, QCoreApplication.translate("Dialog", u"\u041e\u0441\u0442\u0430\u043b\u044c\u043d\u043e\u0435", None))
        self.cb_choose_category.setItemText(3, QCoreApplication.translate("Dialog", u"\u0422\u0435\u0445\u043d\u0438\u043a\u0430", None))
        self.cb_choose_category.setItemText(4, QCoreApplication.translate("Dialog", u"\u0423\u0447\u0435\u0431\u0430", None))

        self.cb_choose_category.setProperty("placeholderText", QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.le_description.setText("")
        self.le_description.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.btn_new_transaction.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

