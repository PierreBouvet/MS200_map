# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(676, 474)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.b_ScanPorts = QPushButton(self.frame)
        self.b_ScanPorts.setObjectName(u"b_ScanPorts")

        self.gridLayout_2.addWidget(self.b_ScanPorts, 0, 0, 1, 1)

        self.b_ConnectDisconnect = QPushButton(self.frame)
        self.b_ConnectDisconnect.setObjectName(u"b_ConnectDisconnect")

        self.gridLayout_2.addWidget(self.b_ConnectDisconnect, 0, 3, 1, 1)

        self.cb_Ports = QComboBox(self.frame)
        self.cb_Ports.setObjectName(u"cb_Ports")

        self.gridLayout_2.addWidget(self.cb_Ports, 0, 1, 1, 1)

        self.cb_Baudrate = QComboBox(self.frame)
        self.cb_Baudrate.setObjectName(u"cb_Baudrate")

        self.gridLayout_2.addWidget(self.cb_Baudrate, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 3)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tB_Log = QTextBrowser(self.frame_3)
        self.tB_Log.setObjectName(u"tB_Log")

        self.gridLayout_5.addWidget(self.tB_Log, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_3, 2, 0, 1, 3)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.l_Nx = QLabel(self.frame_2)
        self.l_Nx.setObjectName(u"l_Nx")

        self.gridLayout_3.addWidget(self.l_Nx, 0, 0, 1, 2)

        self.sB_Nx = QSpinBox(self.frame_2)
        self.sB_Nx.setObjectName(u"sB_Nx")

        self.gridLayout_3.addWidget(self.sB_Nx, 0, 2, 1, 1)

        self.l_Ny = QLabel(self.frame_2)
        self.l_Ny.setObjectName(u"l_Ny")

        self.gridLayout_3.addWidget(self.l_Ny, 1, 0, 1, 2)

        self.sB_Ny = QSpinBox(self.frame_2)
        self.sB_Ny.setObjectName(u"sB_Ny")

        self.gridLayout_3.addWidget(self.sB_Ny, 1, 2, 1, 1)

        self.l_Rx = QLabel(self.frame_2)
        self.l_Rx.setObjectName(u"l_Rx")

        self.gridLayout_3.addWidget(self.l_Rx, 2, 0, 1, 1)

        self.le_Rx = QLineEdit(self.frame_2)
        self.le_Rx.setObjectName(u"le_Rx")

        self.gridLayout_3.addWidget(self.le_Rx, 2, 1, 1, 2)

        self.l_Ry = QLabel(self.frame_2)
        self.l_Ry.setObjectName(u"l_Ry")

        self.gridLayout_3.addWidget(self.l_Ry, 3, 0, 1, 1)

        self.le_Ry = QLineEdit(self.frame_2)
        self.le_Ry.setObjectName(u"le_Ry")

        self.gridLayout_3.addWidget(self.le_Ry, 3, 1, 1, 2)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.cb_Objective = QComboBox(self.frame_4)
        self.cb_Objective.setObjectName(u"cb_Objective")

        self.gridLayout_4.addWidget(self.cb_Objective, 0, 1, 1, 1)

        self.l_Objective = QLabel(self.frame_4)
        self.l_Objective.setObjectName(u"l_Objective")

        self.gridLayout_4.addWidget(self.l_Objective, 0, 0, 1, 1)

        self.b_Launch = QPushButton(self.frame_4)
        self.b_Launch.setObjectName(u"b_Launch")

        self.gridLayout_4.addWidget(self.b_Launch, 2, 0, 1, 2)

        self.l_Exposure = QLabel(self.frame_4)
        self.l_Exposure.setObjectName(u"l_Exposure")

        self.gridLayout_4.addWidget(self.l_Exposure, 1, 0, 1, 1)

        self.le_Exposure = QLineEdit(self.frame_4)
        self.le_Exposure.setObjectName(u"le_Exposure")

        self.gridLayout_4.addWidget(self.le_Exposure, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 676, 37))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.b_ScanPorts.setText(QCoreApplication.translate("MainWindow", u"Scan Ports", None))
        self.b_ConnectDisconnect.setText(QCoreApplication.translate("MainWindow", u"Connect/Disconnect", None))
        self.l_Nx.setText(QCoreApplication.translate("MainWindow", u"Number of points in x:", None))
        self.l_Ny.setText(QCoreApplication.translate("MainWindow", u"Number of points in y:", None))
        self.l_Rx.setText(QCoreApplication.translate("MainWindow", u"x resolution (mm):", None))
        self.l_Ry.setText(QCoreApplication.translate("MainWindow", u"y resolution(mm): ", None))
        self.l_Objective.setText(QCoreApplication.translate("MainWindow", u"Objective", None))
        self.b_Launch.setText(QCoreApplication.translate("MainWindow", u"Launch Mapping", None))
        self.l_Exposure.setText(QCoreApplication.translate("MainWindow", u"Exposure(ms)", None))
    # retranslateUi

