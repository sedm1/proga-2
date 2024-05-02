# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(803, 673)
        MainWindow.setMinimumSize(QSize(800, 600))
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"font-family: Noto Sans SC;\n"
"background-color: #000")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.balances_frame = QFrame(self.centralwidget)
        self.balances_frame.setObjectName(u"balances_frame")
        self.balances_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.balances_frame.setFrameShape(QFrame.NoFrame)
        self.balances_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.balances_frame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(12, 12, 12, 12)
        self.lbl_current_balance = QLabel(self.balances_frame)
        self.lbl_current_balance.setObjectName(u"lbl_current_balance")
        font1 = QFont()
        font1.setFamilies([u"Noto Sans SC"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.lbl_current_balance.setFont(font1)
        self.lbl_current_balance.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_21.addWidget(self.lbl_current_balance)

        self.current_balance = QLabel(self.balances_frame)
        self.current_balance.setObjectName(u"current_balance")
        font2 = QFont()
        font2.setFamilies([u"Noto Sans SC"])
        font2.setPointSize(30)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setKerning(True)
        self.current_balance.setFont(font2)
        self.current_balance.setStyleSheet(u"color: white;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")
        self.current_balance.setLineWidth(0)

        self.verticalLayout_21.addWidget(self.current_balance)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        self.verticalLayout_21.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")

        self.verticalLayout_21.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_2.addWidget(self.balances_frame)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.btn_frame = QFrame(self.centralwidget)
        self.btn_frame.setObjectName(u"btn_frame")
        self.btn_frame.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout = QHBoxLayout(self.btn_frame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_new_transaction = QPushButton(self.btn_frame)
        self.btn_new_transaction.setObjectName(u"btn_new_transaction")
        self.btn_new_transaction.setMinimumSize(QSize(230, 50))
        font3 = QFont()
        font3.setFamilies([u"Noto Sans SC"])
        font3.setBold(True)
        self.btn_new_transaction.setFont(font3)
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

        self.horizontalLayout.addWidget(self.btn_new_transaction)

        self.btn_delete_transaction = QPushButton(self.btn_frame)
        self.btn_delete_transaction.setObjectName(u"btn_delete_transaction")
        self.btn_delete_transaction.setMinimumSize(QSize(230, 50))
        self.btn_delete_transaction.setFont(font3)
        self.btn_delete_transaction.setStyleSheet(u"QPushButton{\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/delete_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_transaction.setIcon(icon1)
        self.btn_delete_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_delete_transaction)


        self.verticalLayout_2.addWidget(self.btn_frame)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px; \n"
"border-bottom-left-radius: 7px; \n"
"color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgb(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 16pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgba(255,255,255,50);\n"
"    padding-left: auto;\n"
"    padding-right: auto;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setTextElideMode(Qt.ElideRight)
        self.tableView.setShowGrid(False)
        self.tableView.setSortingEnabled(True)
        self.tableView.horizontalHeader().setDefaultSectionSize(155)
        self.tableView.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_current_balance.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043b\u0430\u043d\u0441", None))
        self.current_balance.setText(QCoreApplication.translate("MainWindow", u"\u20bd3235,50", None))
        self.btn_new_transaction.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044f", None))
        self.btn_delete_transaction.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044e", None))
    # retranslateUi

