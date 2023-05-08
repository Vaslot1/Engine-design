# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSlider, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1548, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMaximumSize(QSize(1600, 900))
        mainWindow.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_6 = QGridLayout(mainWindow)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.scrollArea = QScrollArea(mainWindow)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1528, 880))
        self.gridLayout_19 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.tabWidget = QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.Input = QLabel(self.tab_4)
        self.Input.setObjectName(u"Input")
        self.Input.setGeometry(QRect(9, 9, 74, 26))
        self.submitValues = QPushButton(self.tab_4)
        self.submitValues.setObjectName(u"submitValues")
        self.submitValues.setGeometry(QRect(0, 240, 154, 34))
        self.layoutWidget = QWidget(self.tab_4)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 50, 431, 188))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Power = QLabel(self.layoutWidget)
        self.Power.setObjectName(u"Power")

        self.verticalLayout_2.addWidget(self.Power)

        self.Voltage = QLabel(self.layoutWidget)
        self.Voltage.setObjectName(u"Voltage")

        self.verticalLayout_2.addWidget(self.Voltage)

        self.polarity = QLabel(self.layoutWidget)
        self.polarity.setObjectName(u"polarity")

        self.verticalLayout_2.addWidget(self.polarity)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.Snom = QLabel(self.layoutWidget)
        self.Snom.setObjectName(u"Snom")

        self.verticalLayout_2.addWidget(self.Snom)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.linePower = QComboBox(self.layoutWidget)
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.addItem("")
        self.linePower.setObjectName(u"linePower")
        self.linePower.setEditable(False)

        self.verticalLayout.addWidget(self.linePower)

        self.lineVoltage = QComboBox(self.layoutWidget)
        self.lineVoltage.addItem("")
        self.lineVoltage.addItem("")
        self.lineVoltage.addItem("")
        self.lineVoltage.setObjectName(u"lineVoltage")
        self.lineVoltage.setEditable(False)

        self.verticalLayout.addWidget(self.lineVoltage)

        self.linePolarity = QComboBox(self.layoutWidget)
        self.linePolarity.addItem("")
        self.linePolarity.addItem("")
        self.linePolarity.addItem("")
        self.linePolarity.addItem("")
        self.linePolarity.addItem("")
        self.linePolarity.addItem("")
        self.linePolarity.setObjectName(u"linePolarity")
        self.linePolarity.setEditable(False)

        self.verticalLayout.addWidget(self.linePolarity)

        self.cmb_heatClass = QComboBox(self.layoutWidget)
        self.cmb_heatClass.addItem("")
        self.cmb_heatClass.addItem("")
        self.cmb_heatClass.addItem("")
        self.cmb_heatClass.setObjectName(u"cmb_heatClass")

        self.verticalLayout.addWidget(self.cmb_heatClass)

        self.lineSnom = QLineEdit(self.layoutWidget)
        self.lineSnom.setObjectName(u"lineSnom")

        self.verticalLayout.addWidget(self.lineSnom)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setEnabled(True)
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        if (self.tableWidget.rowCount() < 20):
            self.tableWidget.setRowCount(20)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget.setItem(0, 1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget.setItem(0, 2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget.setItem(0, 3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget.setItem(0, 4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget.setItem(0, 5, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget.setItem(0, 6, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget.setItem(0, 7, __qtablewidgetitem36)
        font1 = QFont()
        font1.setBold(True)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFont(font1);
        __qtablewidgetitem37.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(0, 8, __qtablewidgetitem37)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font2);
        __qtablewidgetitem38.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(1, 1, __qtablewidgetitem39)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        brush1 = QBrush(QColor(255, 0, 0, 120))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setBackground(brush1);
        __qtablewidgetitem40.setForeground(brush);
        self.tableWidget.setItem(1, 8, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setFont(font1);
        __qtablewidgetitem41.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(2, 1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget.setItem(2, 8, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setFont(font1);
        __qtablewidgetitem45.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(3, 0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(3, 1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget.setItem(3, 8, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setFont(font1);
        __qtablewidgetitem48.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(4, 0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(4, 1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget.setItem(4, 8, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setFont(font1);
        __qtablewidgetitem51.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(5, 0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(5, 1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget.setItem(5, 8, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setFont(font1);
        __qtablewidgetitem54.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(6, 0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(6, 1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget.setItem(6, 8, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setFont(font1);
        __qtablewidgetitem57.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(7, 0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(7, 1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget.setItem(7, 8, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setFont(font1);
        __qtablewidgetitem60.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(8, 0, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(8, 1, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget.setItem(8, 8, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setFont(font1);
        __qtablewidgetitem63.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(9, 0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(9, 1, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget.setItem(9, 8, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setFont(font1);
        __qtablewidgetitem66.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(10, 0, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(10, 1, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableWidget.setItem(10, 8, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setFont(font1);
        __qtablewidgetitem69.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(11, 0, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(11, 1, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableWidget.setItem(11, 8, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setFont(font1);
        __qtablewidgetitem72.setFlags(Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsEnabled);
        self.tableWidget.setItem(12, 0, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(12, 1, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tableWidget.setItem(12, 8, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setFont(font1);
        __qtablewidgetitem75.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(13, 0, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(13, 1, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableWidget.setItem(13, 8, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setFont(font1);
        __qtablewidgetitem78.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(14, 0, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(14, 1, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget.setItem(14, 8, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        __qtablewidgetitem81.setFont(font1);
        __qtablewidgetitem81.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(15, 0, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        __qtablewidgetitem82.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(15, 1, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tableWidget.setItem(15, 8, __qtablewidgetitem83)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Symbol"])
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setKerning(False)
        __qtablewidgetitem84 = QTableWidgetItem()
        __qtablewidgetitem84.setFont(font3);
        __qtablewidgetitem84.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(16, 0, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(16, 1, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tableWidget.setItem(16, 8, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        __qtablewidgetitem87.setFont(font1);
        __qtablewidgetitem87.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(17, 0, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        __qtablewidgetitem88.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(17, 1, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tableWidget.setItem(17, 8, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        __qtablewidgetitem90.setFont(font1);
        __qtablewidgetitem90.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(18, 0, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        __qtablewidgetitem91.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(18, 1, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tableWidget.setItem(18, 8, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        __qtablewidgetitem93.setFont(font1);
        __qtablewidgetitem93.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(19, 0, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        __qtablewidgetitem94.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(19, 1, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget.setItem(19, 8, __qtablewidgetitem95)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(False)
        self.tableWidget.setMinimumSize(QSize(820, 0))
        self.tableWidget.setMaximumSize(QSize(850, 720))
        self.tableWidget.setFont(font)
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setInputMethodHints(Qt.ImhNone)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(34)

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.vl_variables = QVBoxLayout()
        self.vl_variables.setSpacing(0)
        self.vl_variables.setObjectName(u"vl_variables")
        self.hl_I0a = QHBoxLayout()
        self.hl_I0a.setSpacing(1)
        self.hl_I0a.setObjectName(u"hl_I0a")
        self.hl_I0a.setContentsMargins(2, -1, -1, -1)
        self.lb_I0a = QLabel(self.tab)
        self.lb_I0a.setObjectName(u"lb_I0a")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lb_I0a.sizePolicy().hasHeightForWidth())
        self.lb_I0a.setSizePolicy(sizePolicy2)

        self.hl_I0a.addWidget(self.lb_I0a)

        self.le_I0a = QLineEdit(self.tab)
        self.le_I0a.setObjectName(u"le_I0a")
        self.le_I0a.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.le_I0a.sizePolicy().hasHeightForWidth())
        self.le_I0a.setSizePolicy(sizePolicy3)
        self.le_I0a.setMinimumSize(QSize(100, 32))

        self.hl_I0a.addWidget(self.le_I0a)

        self.hl_I0a.setStretch(0, 10)
        self.hl_I0a.setStretch(1, 10)

        self.vl_variables.addLayout(self.hl_I0a)

        self.hl_I0p = QHBoxLayout()
        self.hl_I0p.setObjectName(u"hl_I0p")
        self.hl_I0p.setContentsMargins(0, -1, -1, -1)
        self.lb_I0p = QLabel(self.tab)
        self.lb_I0p.setObjectName(u"lb_I0p")
        sizePolicy2.setHeightForWidth(self.lb_I0p.sizePolicy().hasHeightForWidth())
        self.lb_I0p.setSizePolicy(sizePolicy2)

        self.hl_I0p.addWidget(self.lb_I0p)

        self.le_I0p = QLineEdit(self.tab)
        self.le_I0p.setObjectName(u"le_I0p")
        self.le_I0p.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_I0p.sizePolicy().hasHeightForWidth())
        self.le_I0p.setSizePolicy(sizePolicy3)

        self.hl_I0p.addWidget(self.le_I0p)


        self.vl_variables.addLayout(self.hl_I0p)

        self.hl_Pst = QHBoxLayout()
        self.hl_Pst.setObjectName(u"hl_Pst")
        self.hl_Pst.setContentsMargins(-1, -1, 6, -1)
        self.lb_Pst = QLabel(self.tab)
        self.lb_Pst.setObjectName(u"lb_Pst")
        sizePolicy2.setHeightForWidth(self.lb_Pst.sizePolicy().hasHeightForWidth())
        self.lb_Pst.setSizePolicy(sizePolicy2)

        self.hl_Pst.addWidget(self.lb_Pst)

        self.le_Pst = QLineEdit(self.tab)
        self.le_Pst.setObjectName(u"le_Pst")
        self.le_Pst.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_Pst.sizePolicy().hasHeightForWidth())
        self.le_Pst.setSizePolicy(sizePolicy3)

        self.hl_Pst.addWidget(self.le_Pst)


        self.vl_variables.addLayout(self.hl_Pst)

        self.hl_Pmeh = QHBoxLayout()
        self.hl_Pmeh.setSpacing(0)
        self.hl_Pmeh.setObjectName(u"hl_Pmeh")
        self.hl_Pmeh.setContentsMargins(-1, -1, 6, -1)
        self.lb_Pmeh = QLabel(self.tab)
        self.lb_Pmeh.setObjectName(u"lb_Pmeh")
        sizePolicy2.setHeightForWidth(self.lb_Pmeh.sizePolicy().hasHeightForWidth())
        self.lb_Pmeh.setSizePolicy(sizePolicy2)

        self.hl_Pmeh.addWidget(self.lb_Pmeh)

        self.le_Pmeh = QLineEdit(self.tab)
        self.le_Pmeh.setObjectName(u"le_Pmeh")
        self.le_Pmeh.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(100)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.le_Pmeh.sizePolicy().hasHeightForWidth())
        self.le_Pmeh.setSizePolicy(sizePolicy4)
        self.le_Pmeh.setMinimumSize(QSize(20, 20))
        self.le_Pmeh.setSizeIncrement(QSize(100, 0))

        self.hl_Pmeh.addWidget(self.le_Pmeh)


        self.vl_variables.addLayout(self.hl_Pmeh)

        self.hl_r1 = QHBoxLayout()
        self.hl_r1.setObjectName(u"hl_r1")
        self.lb_r1 = QLabel(self.tab)
        self.lb_r1.setObjectName(u"lb_r1")
        sizePolicy2.setHeightForWidth(self.lb_r1.sizePolicy().hasHeightForWidth())
        self.lb_r1.setSizePolicy(sizePolicy2)

        self.hl_r1.addWidget(self.lb_r1)

        self.le_r1 = QLineEdit(self.tab)
        self.le_r1.setObjectName(u"le_r1")
        self.le_r1.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_r1.sizePolicy().hasHeightForWidth())
        self.le_r1.setSizePolicy(sizePolicy3)
        self.le_r1.setLayoutDirection(Qt.LeftToRight)

        self.hl_r1.addWidget(self.le_r1)


        self.vl_variables.addLayout(self.hl_r1)

        self.hl_r2_shtrih = QHBoxLayout()
        self.hl_r2_shtrih.setObjectName(u"hl_r2_shtrih")
        self.hl_r2_shtrih.setContentsMargins(0, -1, -1, -1)
        self.lb_r2_shtrih = QLabel(self.tab)
        self.lb_r2_shtrih.setObjectName(u"lb_r2_shtrih")
        sizePolicy2.setHeightForWidth(self.lb_r2_shtrih.sizePolicy().hasHeightForWidth())
        self.lb_r2_shtrih.setSizePolicy(sizePolicy2)
        self.lb_r2_shtrih.setFrameShape(QFrame.NoFrame)

        self.hl_r2_shtrih.addWidget(self.lb_r2_shtrih)

        self.le_r2_shtrih = QLineEdit(self.tab)
        self.le_r2_shtrih.setObjectName(u"le_r2_shtrih")
        self.le_r2_shtrih.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_r2_shtrih.sizePolicy().hasHeightForWidth())
        self.le_r2_shtrih.setSizePolicy(sizePolicy3)

        self.hl_r2_shtrih.addWidget(self.le_r2_shtrih)


        self.vl_variables.addLayout(self.hl_r2_shtrih)

        self.hl_c1 = QHBoxLayout()
        self.hl_c1.setObjectName(u"hl_c1")
        self.lb_c1 = QLabel(self.tab)
        self.lb_c1.setObjectName(u"lb_c1")
        sizePolicy2.setHeightForWidth(self.lb_c1.sizePolicy().hasHeightForWidth())
        self.lb_c1.setSizePolicy(sizePolicy2)

        self.hl_c1.addWidget(self.lb_c1)

        self.le_c1 = QLineEdit(self.tab)
        self.le_c1.setObjectName(u"le_c1")
        self.le_c1.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_c1.sizePolicy().hasHeightForWidth())
        self.le_c1.setSizePolicy(sizePolicy3)

        self.hl_c1.addWidget(self.le_c1)


        self.vl_variables.addLayout(self.hl_c1)

        self.hl_a_shtrih = QHBoxLayout()
        self.hl_a_shtrih.setObjectName(u"hl_a_shtrih")
        self.lb_a_shtrih = QLabel(self.tab)
        self.lb_a_shtrih.setObjectName(u"lb_a_shtrih")
        sizePolicy2.setHeightForWidth(self.lb_a_shtrih.sizePolicy().hasHeightForWidth())
        self.lb_a_shtrih.setSizePolicy(sizePolicy2)

        self.hl_a_shtrih.addWidget(self.lb_a_shtrih)

        self.le_a_shtrih = QLineEdit(self.tab)
        self.le_a_shtrih.setObjectName(u"le_a_shtrih")
        self.le_a_shtrih.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_a_shtrih.sizePolicy().hasHeightForWidth())
        self.le_a_shtrih.setSizePolicy(sizePolicy3)

        self.hl_a_shtrih.addWidget(self.le_a_shtrih)


        self.vl_variables.addLayout(self.hl_a_shtrih)

        self.hl_a = QHBoxLayout()
        self.hl_a.setObjectName(u"hl_a")
        self.lb_a = QLabel(self.tab)
        self.lb_a.setObjectName(u"lb_a")
        sizePolicy2.setHeightForWidth(self.lb_a.sizePolicy().hasHeightForWidth())
        self.lb_a.setSizePolicy(sizePolicy2)

        self.hl_a.addWidget(self.lb_a)

        self.le_a = QLineEdit(self.tab)
        self.le_a.setObjectName(u"le_a")
        self.le_a.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_a.sizePolicy().hasHeightForWidth())
        self.le_a.setSizePolicy(sizePolicy3)

        self.hl_a.addWidget(self.le_a)


        self.vl_variables.addLayout(self.hl_a)

        self.hl_b_shtrih = QHBoxLayout()
        self.hl_b_shtrih.setObjectName(u"hl_b_shtrih")
        self.lb_b_shtrih = QLabel(self.tab)
        self.lb_b_shtrih.setObjectName(u"lb_b_shtrih")
        sizePolicy2.setHeightForWidth(self.lb_b_shtrih.sizePolicy().hasHeightForWidth())
        self.lb_b_shtrih.setSizePolicy(sizePolicy2)

        self.hl_b_shtrih.addWidget(self.lb_b_shtrih)

        self.le_b_shtrih = QLineEdit(self.tab)
        self.le_b_shtrih.setObjectName(u"le_b_shtrih")
        self.le_b_shtrih.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_b_shtrih.sizePolicy().hasHeightForWidth())
        self.le_b_shtrih.setSizePolicy(sizePolicy3)

        self.hl_b_shtrih.addWidget(self.le_b_shtrih)


        self.vl_variables.addLayout(self.hl_b_shtrih)

        self.hl_b = QHBoxLayout()
        self.hl_b.setObjectName(u"hl_b")
        self.lb_b = QLabel(self.tab)
        self.lb_b.setObjectName(u"lb_b")
        sizePolicy2.setHeightForWidth(self.lb_b.sizePolicy().hasHeightForWidth())
        self.lb_b.setSizePolicy(sizePolicy2)

        self.hl_b.addWidget(self.lb_b)

        self.le_b = QLineEdit(self.tab)
        self.le_b.setObjectName(u"le_b")
        self.le_b.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_b.sizePolicy().hasHeightForWidth())
        self.le_b.setSizePolicy(sizePolicy3)

        self.hl_b.addWidget(self.le_b)


        self.vl_variables.addLayout(self.hl_b)


        self.gridLayout.addLayout(self.vl_variables, 0, 1, 1, 1)

        self.hl_buttons = QHBoxLayout()
        self.hl_buttons.setObjectName(u"hl_buttons")
        self.bt_check_table_1 = QPushButton(self.tab)
        self.bt_check_table_1.setObjectName(u"bt_check_table_1")
        self.bt_check_table_1.setEnabled(False)

        self.hl_buttons.addWidget(self.bt_check_table_1)

        self.bt_calculate_table1 = QPushButton(self.tab)
        self.bt_calculate_table1.setObjectName(u"bt_calculate_table1")
        self.bt_calculate_table1.setEnabled(False)

        self.hl_buttons.addWidget(self.bt_calculate_table1)

        self.bt_show_chart_1 = QPushButton(self.tab)
        self.bt_show_chart_1.setObjectName(u"bt_show_chart_1")
        self.bt_show_chart_1.setEnabled(False)

        self.hl_buttons.addWidget(self.bt_show_chart_1)

        self.bt_export_xl_1 = QPushButton(self.tab)
        self.bt_export_xl_1.setObjectName(u"bt_export_xl_1")
        self.bt_export_xl_1.setEnabled(False)
        self.bt_export_xl_1.setAutoDefault(False)

        self.hl_buttons.addWidget(self.bt_export_xl_1)


        self.gridLayout.addLayout(self.hl_buttons, 1, 0, 1, 1)

        self.lb_error = QLabel(self.tab)
        self.lb_error.setObjectName(u"lb_error")

        self.gridLayout.addWidget(self.lb_error, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setEnabled(False)
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget_2 = QTableWidget(self.tab_2)
        if (self.tableWidget_2.columnCount() < 8):
            self.tableWidget_2.setColumnCount(8)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem103)
        if (self.tableWidget_2.rowCount() < 15):
            self.tableWidget_2.setRowCount(15)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        __qtablewidgetitem119.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        __qtablewidgetitem120.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        __qtablewidgetitem121.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        __qtablewidgetitem122.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 3, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        __qtablewidgetitem123.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 4, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        __qtablewidgetitem124.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 5, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        __qtablewidgetitem125.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 6, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        __qtablewidgetitem126.setFont(font1);
        self.tableWidget_2.setItem(0, 7, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        __qtablewidgetitem127.setFont(font1);
        __qtablewidgetitem127.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        __qtablewidgetitem128.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 2, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        __qtablewidgetitem130.setFont(font1);
        __qtablewidgetitem130.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(2, 0, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        __qtablewidgetitem131.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(2, 1, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 2, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        __qtablewidgetitem133.setFont(font1);
        __qtablewidgetitem133.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(3, 0, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        __qtablewidgetitem134.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(3, 1, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 2, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        __qtablewidgetitem136.setFont(font1);
        __qtablewidgetitem136.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(4, 0, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        __qtablewidgetitem137.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(4, 1, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 2, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        __qtablewidgetitem139.setFont(font1);
        __qtablewidgetitem139.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(5, 0, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        __qtablewidgetitem140.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(5, 1, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 2, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        __qtablewidgetitem142.setFont(font1);
        __qtablewidgetitem142.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(6, 0, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        __qtablewidgetitem143.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(6, 1, __qtablewidgetitem143)
        __qtablewidgetitem144 = QTableWidgetItem()
        self.tableWidget_2.setItem(6, 2, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        __qtablewidgetitem145.setFont(font1);
        __qtablewidgetitem145.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(7, 0, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        __qtablewidgetitem146.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(7, 1, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        self.tableWidget_2.setItem(7, 2, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        __qtablewidgetitem148.setFont(font1);
        __qtablewidgetitem148.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(8, 0, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        __qtablewidgetitem149.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(8, 1, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        self.tableWidget_2.setItem(8, 2, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        __qtablewidgetitem151.setFont(font1);
        __qtablewidgetitem151.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(9, 0, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        __qtablewidgetitem152.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(9, 1, __qtablewidgetitem152)
        __qtablewidgetitem153 = QTableWidgetItem()
        self.tableWidget_2.setItem(9, 2, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        __qtablewidgetitem154.setFont(font1);
        __qtablewidgetitem154.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(10, 0, __qtablewidgetitem154)
        __qtablewidgetitem155 = QTableWidgetItem()
        __qtablewidgetitem155.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(10, 1, __qtablewidgetitem155)
        __qtablewidgetitem156 = QTableWidgetItem()
        self.tableWidget_2.setItem(10, 2, __qtablewidgetitem156)
        __qtablewidgetitem157 = QTableWidgetItem()
        __qtablewidgetitem157.setFont(font1);
        __qtablewidgetitem157.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(11, 0, __qtablewidgetitem157)
        __qtablewidgetitem158 = QTableWidgetItem()
        __qtablewidgetitem158.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(11, 1, __qtablewidgetitem158)
        __qtablewidgetitem159 = QTableWidgetItem()
        self.tableWidget_2.setItem(11, 2, __qtablewidgetitem159)
        __qtablewidgetitem160 = QTableWidgetItem()
        __qtablewidgetitem160.setFont(font1);
        __qtablewidgetitem160.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(12, 0, __qtablewidgetitem160)
        __qtablewidgetitem161 = QTableWidgetItem()
        __qtablewidgetitem161.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(12, 1, __qtablewidgetitem161)
        __qtablewidgetitem162 = QTableWidgetItem()
        self.tableWidget_2.setItem(12, 2, __qtablewidgetitem162)
        __qtablewidgetitem163 = QTableWidgetItem()
        __qtablewidgetitem163.setFont(font1);
        __qtablewidgetitem163.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(13, 0, __qtablewidgetitem163)
        __qtablewidgetitem164 = QTableWidgetItem()
        __qtablewidgetitem164.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(13, 1, __qtablewidgetitem164)
        __qtablewidgetitem165 = QTableWidgetItem()
        self.tableWidget_2.setItem(13, 2, __qtablewidgetitem165)
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        __qtablewidgetitem166 = QTableWidgetItem()
        __qtablewidgetitem166.setFont(font4);
        __qtablewidgetitem166.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(14, 0, __qtablewidgetitem166)
        __qtablewidgetitem167 = QTableWidgetItem()
        __qtablewidgetitem167.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(14, 1, __qtablewidgetitem167)
        __qtablewidgetitem168 = QTableWidgetItem()
        self.tableWidget_2.setItem(14, 2, __qtablewidgetitem168)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setEnabled(False)
        self.tableWidget_2.setMinimumSize(QSize(1050, 0))
        self.tableWidget_2.setMaximumSize(QSize(1050, 480))
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(170)

        self.gridLayout_2.addWidget(self.tableWidget_2, 0, 0, 1, 1, Qt.AlignLeft)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, -1, -1, -1)
        self.hl_h_c = QHBoxLayout()
        self.hl_h_c.setSpacing(6)
        self.hl_h_c.setObjectName(u"hl_h_c")
        self.hl_h_c.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.hl_h_c.setContentsMargins(0, -1, -1, -1)
        self.lb_h_c = QLabel(self.tab_2)
        self.lb_h_c.setObjectName(u"lb_h_c")
        sizePolicy2.setHeightForWidth(self.lb_h_c.sizePolicy().hasHeightForWidth())
        self.lb_h_c.setSizePolicy(sizePolicy2)
        self.lb_h_c.setMaximumSize(QSize(50, 16777215))

        self.hl_h_c.addWidget(self.lb_h_c)

        self.le_h_c = QLineEdit(self.tab_2)
        self.le_h_c.setObjectName(u"le_h_c")
        self.le_h_c.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_h_c.sizePolicy().hasHeightForWidth())
        self.le_h_c.setSizePolicy(sizePolicy3)
        self.le_h_c.setMinimumSize(QSize(50, 32))
        self.le_h_c.setMaximumSize(QSize(100, 16777215))
        self.le_h_c.setSizeIncrement(QSize(0, 0))
        self.le_h_c.setBaseSize(QSize(0, 0))
        self.le_h_c.setLayoutDirection(Qt.LeftToRight)
        self.le_h_c.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.hl_h_c.addWidget(self.le_h_c)

        self.hl_h_p_2 = QHBoxLayout()
        self.hl_h_p_2.setSpacing(6)
        self.hl_h_p_2.setObjectName(u"hl_h_p_2")
        self.hl_h_p_2.setContentsMargins(0, -1, -1, -1)
        self.lb_h_p_2 = QLabel(self.tab_2)
        self.lb_h_p_2.setObjectName(u"lb_h_p_2")
        sizePolicy2.setHeightForWidth(self.lb_h_p_2.sizePolicy().hasHeightForWidth())
        self.lb_h_p_2.setSizePolicy(sizePolicy2)
        self.lb_h_p_2.setMaximumSize(QSize(50, 16777215))

        self.hl_h_p_2.addWidget(self.lb_h_p_2)

        self.le_h_p_2 = QLineEdit(self.tab_2)
        self.le_h_p_2.setObjectName(u"le_h_p_2")
        self.le_h_p_2.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_h_p_2.sizePolicy().hasHeightForWidth())
        self.le_h_p_2.setSizePolicy(sizePolicy3)
        self.le_h_p_2.setMinimumSize(QSize(100, 0))
        self.le_h_p_2.setMaximumSize(QSize(100, 16777215))

        self.hl_h_p_2.addWidget(self.le_h_p_2)


        self.hl_h_c.addLayout(self.hl_h_p_2)


        self.gridLayout_4.addLayout(self.hl_h_c, 0, 0, 1, 1)

        self.hl_h_sh = QHBoxLayout()
        self.hl_h_sh.setSpacing(6)
        self.hl_h_sh.setObjectName(u"hl_h_sh")
        self.hl_h_sh.setContentsMargins(-1, -1, 0, -1)
        self.lb_h_sh = QLabel(self.tab_2)
        self.lb_h_sh.setObjectName(u"lb_h_sh")
        sizePolicy2.setHeightForWidth(self.lb_h_sh.sizePolicy().hasHeightForWidth())
        self.lb_h_sh.setSizePolicy(sizePolicy2)
        self.lb_h_sh.setMaximumSize(QSize(50, 16777215))

        self.hl_h_sh.addWidget(self.lb_h_sh)

        self.le_h_sh = QLineEdit(self.tab_2)
        self.le_h_sh.setObjectName(u"le_h_sh")
        self.le_h_sh.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_h_sh.sizePolicy().hasHeightForWidth())
        self.le_h_sh.setSizePolicy(sizePolicy3)
        self.le_h_sh.setMaximumSize(QSize(100, 16777215))

        self.hl_h_sh.addWidget(self.le_h_sh)

        self.hl_h_sh_shtrih = QHBoxLayout()
        self.hl_h_sh_shtrih.setSpacing(6)
        self.hl_h_sh_shtrih.setObjectName(u"hl_h_sh_shtrih")
        self.hl_h_sh_shtrih.setContentsMargins(0, -1, 0, -1)
        self.lb_h_sh_shtrih = QLabel(self.tab_2)
        self.lb_h_sh_shtrih.setObjectName(u"lb_h_sh_shtrih")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lb_h_sh_shtrih.sizePolicy().hasHeightForWidth())
        self.lb_h_sh_shtrih.setSizePolicy(sizePolicy5)
        self.lb_h_sh_shtrih.setMaximumSize(QSize(50, 16777215))

        self.hl_h_sh_shtrih.addWidget(self.lb_h_sh_shtrih)

        self.le_h_sh_shtrih = QLineEdit(self.tab_2)
        self.le_h_sh_shtrih.setObjectName(u"le_h_sh_shtrih")
        self.le_h_sh_shtrih.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.le_h_sh_shtrih.sizePolicy().hasHeightForWidth())
        self.le_h_sh_shtrih.setSizePolicy(sizePolicy4)
        self.le_h_sh_shtrih.setMinimumSize(QSize(20, 20))
        self.le_h_sh_shtrih.setMaximumSize(QSize(100, 16777215))
        self.le_h_sh_shtrih.setSizeIncrement(QSize(100, 0))

        self.hl_h_sh_shtrih.addWidget(self.le_h_sh_shtrih)


        self.hl_h_sh.addLayout(self.hl_h_sh_shtrih)


        self.gridLayout_4.addLayout(self.hl_h_sh, 2, 0, 1, 1)

        self.hl_b_1_r = QHBoxLayout()
        self.hl_b_1_r.setSpacing(6)
        self.hl_b_1_r.setObjectName(u"hl_b_1_r")
        self.hl_b_1_r.setSizeConstraint(QLayout.SetMinimumSize)
        self.hl_b_1_r.setContentsMargins(0, -1, -1, -1)
        self.lb_b_1_r = QLabel(self.tab_2)
        self.lb_b_1_r.setObjectName(u"lb_b_1_r")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lb_b_1_r.sizePolicy().hasHeightForWidth())
        self.lb_b_1_r.setSizePolicy(sizePolicy6)
        self.lb_b_1_r.setMaximumSize(QSize(50, 16777215))
        self.lb_b_1_r.setLineWidth(1)
        self.lb_b_1_r.setMargin(0)

        self.hl_b_1_r.addWidget(self.lb_b_1_r)

        self.le_b_1_r = QLineEdit(self.tab_2)
        self.le_b_1_r.setObjectName(u"le_b_1_r")
        self.le_b_1_r.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_b_1_r.sizePolicy().hasHeightForWidth())
        self.le_b_1_r.setSizePolicy(sizePolicy3)
        self.le_b_1_r.setMinimumSize(QSize(100, 0))
        self.le_b_1_r.setMaximumSize(QSize(100, 16777215))
        self.le_b_1_r.setLayoutDirection(Qt.LeftToRight)

        self.hl_b_1_r.addWidget(self.le_b_1_r)

        self.hl_b_2_r = QHBoxLayout()
        self.hl_b_2_r.setObjectName(u"hl_b_2_r")
        self.hl_b_2_r.setContentsMargins(0, -1, -1, -1)
        self.lb_b_2_r = QLabel(self.tab_2)
        self.lb_b_2_r.setObjectName(u"lb_b_2_r")
        sizePolicy2.setHeightForWidth(self.lb_b_2_r.sizePolicy().hasHeightForWidth())
        self.lb_b_2_r.setSizePolicy(sizePolicy2)
        self.lb_b_2_r.setMaximumSize(QSize(100, 16777215))
        self.lb_b_2_r.setFrameShape(QFrame.NoFrame)

        self.hl_b_2_r.addWidget(self.lb_b_2_r)

        self.le_b_2_r = QLineEdit(self.tab_2)
        self.le_b_2_r.setObjectName(u"le_b_2_r")
        self.le_b_2_r.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_b_2_r.sizePolicy().hasHeightForWidth())
        self.le_b_2_r.setSizePolicy(sizePolicy3)
        self.le_b_2_r.setMaximumSize(QSize(100, 16777215))

        self.hl_b_2_r.addWidget(self.le_b_2_r)


        self.hl_b_1_r.addLayout(self.hl_b_2_r)


        self.gridLayout_4.addLayout(self.hl_b_1_r, 4, 0, 1, 1)

        self.hl_h_0 = QHBoxLayout()
        self.hl_h_0.setObjectName(u"hl_h_0")
        self.lb_h_0 = QLabel(self.tab_2)
        self.lb_h_0.setObjectName(u"lb_h_0")
        sizePolicy2.setHeightForWidth(self.lb_h_0.sizePolicy().hasHeightForWidth())
        self.lb_h_0.setSizePolicy(sizePolicy2)
        self.lb_h_0.setMaximumSize(QSize(50, 16777215))

        self.hl_h_0.addWidget(self.lb_h_0)

        self.le_h_0 = QLineEdit(self.tab_2)
        self.le_h_0.setObjectName(u"le_h_0")
        self.le_h_0.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_h_0.sizePolicy().hasHeightForWidth())
        self.le_h_0.setSizePolicy(sizePolicy3)
        self.le_h_0.setMaximumSize(QSize(100, 16777215))

        self.hl_h_0.addWidget(self.le_h_0)

        self.hl_b_sh_2 = QHBoxLayout()
        self.hl_b_sh_2.setObjectName(u"hl_b_sh_2")
        self.lb_b_sh_2 = QLabel(self.tab_2)
        self.lb_b_sh_2.setObjectName(u"lb_b_sh_2")
        sizePolicy2.setHeightForWidth(self.lb_b_sh_2.sizePolicy().hasHeightForWidth())
        self.lb_b_sh_2.setSizePolicy(sizePolicy2)
        self.lb_b_sh_2.setMaximumSize(QSize(50, 16777215))

        self.hl_b_sh_2.addWidget(self.lb_b_sh_2)

        self.le_b_sh_2 = QLineEdit(self.tab_2)
        self.le_b_sh_2.setObjectName(u"le_b_sh_2")
        self.le_b_sh_2.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_b_sh_2.sizePolicy().hasHeightForWidth())
        self.le_b_sh_2.setSizePolicy(sizePolicy3)
        self.le_b_sh_2.setMaximumSize(QSize(100, 16777215))

        self.hl_b_sh_2.addWidget(self.le_b_sh_2)


        self.hl_h_0.addLayout(self.hl_b_sh_2)


        self.gridLayout_4.addLayout(self.hl_h_0, 10, 0, 1, 1)

        self.hl_Lamda_d_2 = QHBoxLayout()
        self.hl_Lamda_d_2.setObjectName(u"hl_Lamda_d_2")
        self.lb_Lamda_d_2 = QLabel(self.tab_2)
        self.lb_Lamda_d_2.setObjectName(u"lb_Lamda_d_2")
        sizePolicy2.setHeightForWidth(self.lb_Lamda_d_2.sizePolicy().hasHeightForWidth())
        self.lb_Lamda_d_2.setSizePolicy(sizePolicy2)
        self.lb_Lamda_d_2.setMaximumSize(QSize(50, 16777215))

        self.hl_Lamda_d_2.addWidget(self.lb_Lamda_d_2)

        self.le_Lamda_d_2 = QLineEdit(self.tab_2)
        self.le_Lamda_d_2.setObjectName(u"le_Lamda_d_2")
        self.le_Lamda_d_2.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_Lamda_d_2.sizePolicy().hasHeightForWidth())
        self.le_Lamda_d_2.setSizePolicy(sizePolicy3)
        self.le_Lamda_d_2.setMaximumSize(QSize(100, 16777215))

        self.hl_Lamda_d_2.addWidget(self.le_Lamda_d_2)

        self.hl_X_2_shtrih = QHBoxLayout()
        self.hl_X_2_shtrih.setObjectName(u"hl_X_2_shtrih")
        self.lb_X_2_shtrih = QLabel(self.tab_2)
        self.lb_X_2_shtrih.setObjectName(u"lb_X_2_shtrih")
        sizePolicy2.setHeightForWidth(self.lb_X_2_shtrih.sizePolicy().hasHeightForWidth())
        self.lb_X_2_shtrih.setSizePolicy(sizePolicy2)
        self.lb_X_2_shtrih.setMaximumSize(QSize(50, 16777215))

        self.hl_X_2_shtrih.addWidget(self.lb_X_2_shtrih)

        self.le_X_2_shtrih = QLineEdit(self.tab_2)
        self.le_X_2_shtrih.setObjectName(u"le_X_2_shtrih")
        self.le_X_2_shtrih.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_X_2_shtrih.sizePolicy().hasHeightForWidth())
        self.le_X_2_shtrih.setSizePolicy(sizePolicy3)
        self.le_X_2_shtrih.setMaximumSize(QSize(100, 16777215))

        self.hl_X_2_shtrih.addWidget(self.le_X_2_shtrih)


        self.hl_Lamda_d_2.addLayout(self.hl_X_2_shtrih)


        self.gridLayout_4.addLayout(self.hl_Lamda_d_2, 14, 0, 1, 1)

        self.hl_x_1_2_p = QHBoxLayout()
        self.hl_x_1_2_p.setObjectName(u"hl_x_1_2_p")
        self.lb_x_1_2_p = QLabel(self.tab_2)
        self.lb_x_1_2_p.setObjectName(u"lb_x_1_2_p")
        sizePolicy2.setHeightForWidth(self.lb_x_1_2_p.sizePolicy().hasHeightForWidth())
        self.lb_x_1_2_p.setSizePolicy(sizePolicy2)
        self.lb_x_1_2_p.setMaximumSize(QSize(50, 16777215))

        self.hl_x_1_2_p.addWidget(self.lb_x_1_2_p)

        self.le_x_1_2_p = QLineEdit(self.tab_2)
        self.le_x_1_2_p.setObjectName(u"le_x_1_2_p")
        self.le_x_1_2_p.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_x_1_2_p.sizePolicy().hasHeightForWidth())
        self.le_x_1_2_p.setSizePolicy(sizePolicy3)
        self.le_x_1_2_p.setMaximumSize(QSize(100, 16777215))

        self.hl_x_1_2_p.addWidget(self.le_x_1_2_p)

        self.hl_c_1_p = QHBoxLayout()
        self.hl_c_1_p.setObjectName(u"hl_c_1_p")
        self.lb_c_1_p = QLabel(self.tab_2)
        self.lb_c_1_p.setObjectName(u"lb_c_1_p")
        sizePolicy2.setHeightForWidth(self.lb_c_1_p.sizePolicy().hasHeightForWidth())
        self.lb_c_1_p.setSizePolicy(sizePolicy2)
        self.lb_c_1_p.setMaximumSize(QSize(50, 16777215))

        self.hl_c_1_p.addWidget(self.lb_c_1_p)

        self.le_c_1_p = QLineEdit(self.tab_2)
        self.le_c_1_p.setObjectName(u"le_c_1_p")
        self.le_c_1_p.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_c_1_p.sizePolicy().hasHeightForWidth())
        self.le_c_1_p.setSizePolicy(sizePolicy3)
        self.le_c_1_p.setMaximumSize(QSize(100, 16777215))

        self.hl_c_1_p.addWidget(self.le_c_1_p)


        self.hl_x_1_2_p.addLayout(self.hl_c_1_p)


        self.gridLayout_4.addLayout(self.hl_x_1_2_p, 16, 0, 1, 1)

        self.hl_X_1 = QHBoxLayout()
        self.hl_X_1.setObjectName(u"hl_X_1")
        self.lb_X_1 = QLabel(self.tab_2)
        self.lb_X_1.setObjectName(u"lb_X_1")
        sizePolicy2.setHeightForWidth(self.lb_X_1.sizePolicy().hasHeightForWidth())
        self.lb_X_1.setSizePolicy(sizePolicy2)
        self.lb_X_1.setMaximumSize(QSize(50, 16777215))

        self.hl_X_1.addWidget(self.lb_X_1)

        self.le_X_1 = QLineEdit(self.tab_2)
        self.le_X_1.setObjectName(u"le_X_1")
        self.le_X_1.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_X_1.sizePolicy().hasHeightForWidth())
        self.le_X_1.setSizePolicy(sizePolicy3)
        self.le_X_1.setMaximumSize(QSize(100, 16777215))

        self.hl_X_1.addWidget(self.le_X_1)


        self.gridLayout_4.addLayout(self.hl_X_1, 18, 0, 1, 1)

        self.hl_h_1 = QHBoxLayout()
        self.hl_h_1.setObjectName(u"hl_h_1")
        self.lb_h_1 = QLabel(self.tab_2)
        self.lb_h_1.setObjectName(u"lb_h_1")
        sizePolicy2.setHeightForWidth(self.lb_h_1.sizePolicy().hasHeightForWidth())
        self.lb_h_1.setSizePolicy(sizePolicy2)
        self.lb_h_1.setMaximumSize(QSize(50, 16777215))

        self.hl_h_1.addWidget(self.lb_h_1)

        self.le_h_1 = QLineEdit(self.tab_2)
        self.le_h_1.setObjectName(u"le_h_1")
        self.le_h_1.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_h_1.sizePolicy().hasHeightForWidth())
        self.le_h_1.setSizePolicy(sizePolicy3)
        self.le_h_1.setMaximumSize(QSize(100, 16777215))

        self.hl_h_1.addWidget(self.le_h_1)

        self.hl_q_c = QHBoxLayout()
        self.hl_q_c.setObjectName(u"hl_q_c")
        self.lb_q_c = QLabel(self.tab_2)
        self.lb_q_c.setObjectName(u"lb_q_c")
        sizePolicy2.setHeightForWidth(self.lb_q_c.sizePolicy().hasHeightForWidth())
        self.lb_q_c.setSizePolicy(sizePolicy2)
        self.lb_q_c.setMaximumSize(QSize(50, 16777215))

        self.hl_q_c.addWidget(self.lb_q_c)

        self.le_q_c = QLineEdit(self.tab_2)
        self.le_q_c.setObjectName(u"le_q_c")
        self.le_q_c.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_q_c.sizePolicy().hasHeightForWidth())
        self.le_q_c.setSizePolicy(sizePolicy3)
        self.le_q_c.setMaximumSize(QSize(100, 16777215))

        self.hl_q_c.addWidget(self.le_q_c)


        self.hl_h_1.addLayout(self.hl_q_c)


        self.gridLayout_4.addLayout(self.hl_h_1, 6, 0, 1, 1)

        self.hl_r_c = QHBoxLayout()
        self.hl_r_c.setObjectName(u"hl_r_c")
        self.lb_r_c = QLabel(self.tab_2)
        self.lb_r_c.setObjectName(u"lb_r_c")
        sizePolicy2.setHeightForWidth(self.lb_r_c.sizePolicy().hasHeightForWidth())
        self.lb_r_c.setSizePolicy(sizePolicy2)
        self.lb_r_c.setMaximumSize(QSize(50, 16777215))

        self.hl_r_c.addWidget(self.lb_r_c)

        self.le_r_c = QLineEdit(self.tab_2)
        self.le_r_c.setObjectName(u"le_r_c")
        self.le_r_c.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_r_c.sizePolicy().hasHeightForWidth())
        self.le_r_c.setSizePolicy(sizePolicy3)
        self.le_r_c.setMaximumSize(QSize(100, 16777215))

        self.hl_r_c.addWidget(self.le_r_c)

        self.hl_r_2 = QHBoxLayout()
        self.hl_r_2.setObjectName(u"hl_r_2")
        self.lb_r_2 = QLabel(self.tab_2)
        self.lb_r_2.setObjectName(u"lb_r_2")
        sizePolicy2.setHeightForWidth(self.lb_r_2.sizePolicy().hasHeightForWidth())
        self.lb_r_2.setSizePolicy(sizePolicy2)
        self.lb_r_2.setMaximumSize(QSize(50, 16777215))

        self.hl_r_2.addWidget(self.lb_r_2)

        self.le_r_2 = QLineEdit(self.tab_2)
        self.le_r_2.setObjectName(u"le_r_2")
        self.le_r_2.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_r_2.sizePolicy().hasHeightForWidth())
        self.le_r_2.setSizePolicy(sizePolicy3)
        self.le_r_2.setMaximumSize(QSize(100, 16777215))

        self.hl_r_2.addWidget(self.le_r_2)


        self.hl_r_c.addLayout(self.hl_r_2)


        self.gridLayout_4.addLayout(self.hl_r_c, 8, 0, 1, 1)

        self.hl_Lamda_p_2 = QHBoxLayout()
        self.hl_Lamda_p_2.setObjectName(u"hl_Lamda_p_2")
        self.lb_Lamda_p_2 = QLabel(self.tab_2)
        self.lb_Lamda_p_2.setObjectName(u"lb_Lamda_p_2")
        sizePolicy2.setHeightForWidth(self.lb_Lamda_p_2.sizePolicy().hasHeightForWidth())
        self.lb_Lamda_p_2.setSizePolicy(sizePolicy2)
        self.lb_Lamda_p_2.setMaximumSize(QSize(50, 16777215))

        self.hl_Lamda_p_2.addWidget(self.lb_Lamda_p_2)

        self.le_Lamda_p_2 = QLineEdit(self.tab_2)
        self.le_Lamda_p_2.setObjectName(u"le_Lamda_p_2")
        self.le_Lamda_p_2.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_Lamda_p_2.sizePolicy().hasHeightForWidth())
        self.le_Lamda_p_2.setSizePolicy(sizePolicy3)
        self.le_Lamda_p_2.setMaximumSize(QSize(100, 16777215))

        self.hl_Lamda_p_2.addWidget(self.le_Lamda_p_2)

        self.hl_Lamda_l_2 = QHBoxLayout()
        self.hl_Lamda_l_2.setObjectName(u"hl_Lamda_l_2")
        self.lb_Lamda_l_2 = QLabel(self.tab_2)
        self.lb_Lamda_l_2.setObjectName(u"lb_Lamda_l_2")
        sizePolicy2.setHeightForWidth(self.lb_Lamda_l_2.sizePolicy().hasHeightForWidth())
        self.lb_Lamda_l_2.setSizePolicy(sizePolicy2)
        self.lb_Lamda_l_2.setMaximumSize(QSize(50, 16777215))

        self.hl_Lamda_l_2.addWidget(self.lb_Lamda_l_2)

        self.le_Lamda_l_2 = QLineEdit(self.tab_2)
        self.le_Lamda_l_2.setObjectName(u"le_Lamda_l_2")
        self.le_Lamda_l_2.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_Lamda_l_2.sizePolicy().hasHeightForWidth())
        self.le_Lamda_l_2.setSizePolicy(sizePolicy3)
        self.le_Lamda_l_2.setMaximumSize(QSize(100, 16777215))

        self.hl_Lamda_l_2.addWidget(self.le_Lamda_l_2)


        self.hl_Lamda_p_2.addLayout(self.hl_Lamda_l_2)


        self.gridLayout_4.addLayout(self.hl_Lamda_p_2, 12, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 1, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.bt_calculate_table2 = QPushButton(self.tab_2)
        self.bt_calculate_table2.setObjectName(u"bt_calculate_table2")

        self.gridLayout_5.addWidget(self.bt_calculate_table2, 0, 1, 1, 1)

        self.bt_check_table_2 = QPushButton(self.tab_2)
        self.bt_check_table_2.setObjectName(u"bt_check_table_2")

        self.gridLayout_5.addWidget(self.bt_check_table_2, 0, 0, 1, 1)

        self.bt_export_xl_table_2 = QPushButton(self.tab_2)
        self.bt_export_xl_table_2.setObjectName(u"bt_export_xl_table_2")

        self.gridLayout_5.addWidget(self.bt_export_xl_table_2, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_5, 1, 0, 1, 1)

        self.lb_error_2 = QLabel(self.tab_2)
        self.lb_error_2.setObjectName(u"lb_error_2")

        self.gridLayout_2.addWidget(self.lb_error_2, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setEnabled(False)
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bt_check_table_3 = QPushButton(self.tab_3)
        self.bt_check_table_3.setObjectName(u"bt_check_table_3")

        self.horizontalLayout.addWidget(self.bt_check_table_3)

        self.bt_calculate_table3 = QPushButton(self.tab_3)
        self.bt_calculate_table3.setObjectName(u"bt_calculate_table3")

        self.horizontalLayout.addWidget(self.bt_calculate_table3)

        self.bt_show_chart_table3 = QPushButton(self.tab_3)
        self.bt_show_chart_table3.setObjectName(u"bt_show_chart_table3")
        self.bt_show_chart_table3.setEnabled(False)

        self.horizontalLayout.addWidget(self.bt_show_chart_table3)

        self.bt_export_xl_table_3 = QPushButton(self.tab_3)
        self.bt_export_xl_table_3.setObjectName(u"bt_export_xl_table_3")

        self.horizontalLayout.addWidget(self.bt_export_xl_table_3)


        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.tableWidget_3 = QTableWidget(self.tab_3)
        if (self.tableWidget_3.columnCount() < 8):
            self.tableWidget_3.setColumnCount(8)
        __qtablewidgetitem169 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem169)
        __qtablewidgetitem170 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem170)
        __qtablewidgetitem171 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem171)
        __qtablewidgetitem172 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem172)
        __qtablewidgetitem173 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem173)
        __qtablewidgetitem174 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem174)
        __qtablewidgetitem175 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem175)
        __qtablewidgetitem176 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem176)
        if (self.tableWidget_3.rowCount() < 21):
            self.tableWidget_3.setRowCount(21)
        __qtablewidgetitem177 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem177)
        __qtablewidgetitem178 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem178)
        __qtablewidgetitem179 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, __qtablewidgetitem179)
        __qtablewidgetitem180 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, __qtablewidgetitem180)
        __qtablewidgetitem181 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, __qtablewidgetitem181)
        __qtablewidgetitem182 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, __qtablewidgetitem182)
        __qtablewidgetitem183 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(6, __qtablewidgetitem183)
        __qtablewidgetitem184 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(7, __qtablewidgetitem184)
        __qtablewidgetitem185 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(8, __qtablewidgetitem185)
        __qtablewidgetitem186 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(9, __qtablewidgetitem186)
        __qtablewidgetitem187 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(10, __qtablewidgetitem187)
        __qtablewidgetitem188 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(11, __qtablewidgetitem188)
        __qtablewidgetitem189 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(12, __qtablewidgetitem189)
        __qtablewidgetitem190 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(13, __qtablewidgetitem190)
        __qtablewidgetitem191 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(14, __qtablewidgetitem191)
        __qtablewidgetitem192 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(15, __qtablewidgetitem192)
        __qtablewidgetitem193 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(16, __qtablewidgetitem193)
        __qtablewidgetitem194 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(17, __qtablewidgetitem194)
        __qtablewidgetitem195 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(18, __qtablewidgetitem195)
        __qtablewidgetitem196 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(19, __qtablewidgetitem196)
        __qtablewidgetitem197 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(20, __qtablewidgetitem197)
        __qtablewidgetitem198 = QTableWidgetItem()
        __qtablewidgetitem198.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_3.setItem(0, 2, __qtablewidgetitem198)
        __qtablewidgetitem199 = QTableWidgetItem()
        __qtablewidgetitem199.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_3.setItem(0, 3, __qtablewidgetitem199)
        __qtablewidgetitem200 = QTableWidgetItem()
        __qtablewidgetitem200.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_3.setItem(0, 4, __qtablewidgetitem200)
        __qtablewidgetitem201 = QTableWidgetItem()
        __qtablewidgetitem201.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_3.setItem(0, 5, __qtablewidgetitem201)
        __qtablewidgetitem202 = QTableWidgetItem()
        __qtablewidgetitem202.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_3.setItem(0, 6, __qtablewidgetitem202)
        __qtablewidgetitem203 = QTableWidgetItem()
        __qtablewidgetitem203.setFont(font1);
        self.tableWidget_3.setItem(0, 7, __qtablewidgetitem203)
        __qtablewidgetitem204 = QTableWidgetItem()
        __qtablewidgetitem204.setFont(font1);
        __qtablewidgetitem204.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(1, 0, __qtablewidgetitem204)
        __qtablewidgetitem205 = QTableWidgetItem()
        __qtablewidgetitem205.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(1, 1, __qtablewidgetitem205)
        __qtablewidgetitem206 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 2, __qtablewidgetitem206)
        __qtablewidgetitem207 = QTableWidgetItem()
        __qtablewidgetitem207.setFont(font4);
        __qtablewidgetitem207.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(2, 0, __qtablewidgetitem207)
        __qtablewidgetitem208 = QTableWidgetItem()
        __qtablewidgetitem208.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(2, 1, __qtablewidgetitem208)
        __qtablewidgetitem209 = QTableWidgetItem()
        self.tableWidget_3.setItem(2, 2, __qtablewidgetitem209)
        __qtablewidgetitem210 = QTableWidgetItem()
        __qtablewidgetitem210.setFont(font4);
        __qtablewidgetitem210.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(3, 0, __qtablewidgetitem210)
        __qtablewidgetitem211 = QTableWidgetItem()
        __qtablewidgetitem211.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(3, 1, __qtablewidgetitem211)
        __qtablewidgetitem212 = QTableWidgetItem()
        self.tableWidget_3.setItem(3, 2, __qtablewidgetitem212)
        __qtablewidgetitem213 = QTableWidgetItem()
        __qtablewidgetitem213.setFont(font1);
        __qtablewidgetitem213.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(4, 0, __qtablewidgetitem213)
        __qtablewidgetitem214 = QTableWidgetItem()
        __qtablewidgetitem214.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(4, 1, __qtablewidgetitem214)
        __qtablewidgetitem215 = QTableWidgetItem()
        self.tableWidget_3.setItem(4, 2, __qtablewidgetitem215)
        __qtablewidgetitem216 = QTableWidgetItem()
        __qtablewidgetitem216.setFont(font1);
        __qtablewidgetitem216.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(5, 0, __qtablewidgetitem216)
        __qtablewidgetitem217 = QTableWidgetItem()
        __qtablewidgetitem217.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(5, 1, __qtablewidgetitem217)
        __qtablewidgetitem218 = QTableWidgetItem()
        self.tableWidget_3.setItem(5, 2, __qtablewidgetitem218)
        __qtablewidgetitem219 = QTableWidgetItem()
        __qtablewidgetitem219.setFont(font1);
        __qtablewidgetitem219.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(6, 0, __qtablewidgetitem219)
        __qtablewidgetitem220 = QTableWidgetItem()
        __qtablewidgetitem220.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(6, 1, __qtablewidgetitem220)
        __qtablewidgetitem221 = QTableWidgetItem()
        self.tableWidget_3.setItem(6, 2, __qtablewidgetitem221)
        __qtablewidgetitem222 = QTableWidgetItem()
        __qtablewidgetitem222.setFont(font1);
        __qtablewidgetitem222.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(7, 0, __qtablewidgetitem222)
        __qtablewidgetitem223 = QTableWidgetItem()
        __qtablewidgetitem223.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(7, 1, __qtablewidgetitem223)
        __qtablewidgetitem224 = QTableWidgetItem()
        self.tableWidget_3.setItem(7, 2, __qtablewidgetitem224)
        __qtablewidgetitem225 = QTableWidgetItem()
        __qtablewidgetitem225.setFont(font1);
        __qtablewidgetitem225.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(8, 0, __qtablewidgetitem225)
        __qtablewidgetitem226 = QTableWidgetItem()
        __qtablewidgetitem226.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(8, 1, __qtablewidgetitem226)
        __qtablewidgetitem227 = QTableWidgetItem()
        self.tableWidget_3.setItem(8, 2, __qtablewidgetitem227)
        __qtablewidgetitem228 = QTableWidgetItem()
        __qtablewidgetitem228.setFont(font1);
        __qtablewidgetitem228.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(9, 0, __qtablewidgetitem228)
        __qtablewidgetitem229 = QTableWidgetItem()
        __qtablewidgetitem229.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(9, 1, __qtablewidgetitem229)
        __qtablewidgetitem230 = QTableWidgetItem()
        self.tableWidget_3.setItem(9, 2, __qtablewidgetitem230)
        __qtablewidgetitem231 = QTableWidgetItem()
        __qtablewidgetitem231.setFont(font1);
        __qtablewidgetitem231.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(10, 0, __qtablewidgetitem231)
        __qtablewidgetitem232 = QTableWidgetItem()
        __qtablewidgetitem232.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(10, 1, __qtablewidgetitem232)
        __qtablewidgetitem233 = QTableWidgetItem()
        self.tableWidget_3.setItem(10, 2, __qtablewidgetitem233)
        __qtablewidgetitem234 = QTableWidgetItem()
        __qtablewidgetitem234.setFont(font1);
        __qtablewidgetitem234.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(11, 0, __qtablewidgetitem234)
        __qtablewidgetitem235 = QTableWidgetItem()
        __qtablewidgetitem235.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(11, 1, __qtablewidgetitem235)
        __qtablewidgetitem236 = QTableWidgetItem()
        self.tableWidget_3.setItem(11, 2, __qtablewidgetitem236)
        __qtablewidgetitem237 = QTableWidgetItem()
        __qtablewidgetitem237.setFont(font1);
        __qtablewidgetitem237.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(12, 0, __qtablewidgetitem237)
        __qtablewidgetitem238 = QTableWidgetItem()
        __qtablewidgetitem238.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(12, 1, __qtablewidgetitem238)
        __qtablewidgetitem239 = QTableWidgetItem()
        self.tableWidget_3.setItem(12, 2, __qtablewidgetitem239)
        __qtablewidgetitem240 = QTableWidgetItem()
        __qtablewidgetitem240.setFont(font1);
        __qtablewidgetitem240.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(13, 0, __qtablewidgetitem240)
        __qtablewidgetitem241 = QTableWidgetItem()
        __qtablewidgetitem241.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(13, 1, __qtablewidgetitem241)
        __qtablewidgetitem242 = QTableWidgetItem()
        self.tableWidget_3.setItem(13, 2, __qtablewidgetitem242)
        __qtablewidgetitem243 = QTableWidgetItem()
        __qtablewidgetitem243.setFont(font4);
        __qtablewidgetitem243.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(14, 0, __qtablewidgetitem243)
        __qtablewidgetitem244 = QTableWidgetItem()
        __qtablewidgetitem244.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(14, 1, __qtablewidgetitem244)
        __qtablewidgetitem245 = QTableWidgetItem()
        self.tableWidget_3.setItem(14, 2, __qtablewidgetitem245)
        __qtablewidgetitem246 = QTableWidgetItem()
        __qtablewidgetitem246.setFont(font4);
        __qtablewidgetitem246.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(15, 0, __qtablewidgetitem246)
        __qtablewidgetitem247 = QTableWidgetItem()
        __qtablewidgetitem247.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(15, 1, __qtablewidgetitem247)
        __qtablewidgetitem248 = QTableWidgetItem()
        self.tableWidget_3.setItem(15, 2, __qtablewidgetitem248)
        __qtablewidgetitem249 = QTableWidgetItem()
        __qtablewidgetitem249.setFont(font4);
        __qtablewidgetitem249.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(16, 0, __qtablewidgetitem249)
        __qtablewidgetitem250 = QTableWidgetItem()
        __qtablewidgetitem250.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(16, 1, __qtablewidgetitem250)
        __qtablewidgetitem251 = QTableWidgetItem()
        self.tableWidget_3.setItem(16, 2, __qtablewidgetitem251)
        __qtablewidgetitem252 = QTableWidgetItem()
        __qtablewidgetitem252.setFont(font4);
        __qtablewidgetitem252.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(17, 0, __qtablewidgetitem252)
        __qtablewidgetitem253 = QTableWidgetItem()
        __qtablewidgetitem253.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(17, 1, __qtablewidgetitem253)
        __qtablewidgetitem254 = QTableWidgetItem()
        self.tableWidget_3.setItem(17, 2, __qtablewidgetitem254)
        __qtablewidgetitem255 = QTableWidgetItem()
        __qtablewidgetitem255.setFont(font4);
        __qtablewidgetitem255.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(18, 0, __qtablewidgetitem255)
        __qtablewidgetitem256 = QTableWidgetItem()
        __qtablewidgetitem256.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(18, 1, __qtablewidgetitem256)
        __qtablewidgetitem257 = QTableWidgetItem()
        self.tableWidget_3.setItem(18, 2, __qtablewidgetitem257)
        __qtablewidgetitem258 = QTableWidgetItem()
        __qtablewidgetitem258.setFont(font1);
        __qtablewidgetitem258.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(19, 0, __qtablewidgetitem258)
        __qtablewidgetitem259 = QTableWidgetItem()
        __qtablewidgetitem259.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(19, 1, __qtablewidgetitem259)
        __qtablewidgetitem260 = QTableWidgetItem()
        self.tableWidget_3.setItem(19, 2, __qtablewidgetitem260)
        __qtablewidgetitem261 = QTableWidgetItem()
        __qtablewidgetitem261.setFont(font1);
        __qtablewidgetitem261.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(20, 0, __qtablewidgetitem261)
        __qtablewidgetitem262 = QTableWidgetItem()
        __qtablewidgetitem262.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(20, 1, __qtablewidgetitem262)
        __qtablewidgetitem263 = QTableWidgetItem()
        self.tableWidget_3.setItem(20, 2, __qtablewidgetitem263)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setMinimumSize(QSize(1100, 0))
        self.tableWidget_3.setMaximumSize(QSize(1100, 680))
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(170)

        self.gridLayout_3.addWidget(self.tableWidget_3, 0, 0, 1, 1, Qt.AlignLeft)

        self.vl_variables_t3 = QVBoxLayout()
        self.vl_variables_t3.setSpacing(6)
        self.vl_variables_t3.setObjectName(u"vl_variables_t3")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, -1, -1, -1)
        self.le_C_N = QLineEdit(self.tab_3)
        self.le_C_N.setObjectName(u"le_C_N")
        self.le_C_N.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_C_N.sizePolicy().hasHeightForWidth())
        self.le_C_N.setSizePolicy(sizePolicy3)
        self.le_C_N.setMinimumSize(QSize(100, 32))
        self.le_C_N.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_12.addWidget(self.le_C_N, 0, 1, 1, 1)

        self.hl_k_y_1 = QHBoxLayout()
        self.hl_k_y_1.setObjectName(u"hl_k_y_1")
        self.hl_k_y_1.setContentsMargins(0, -1, -1, -1)
        self.lb_k_y_1 = QLabel(self.tab_3)
        self.lb_k_y_1.setObjectName(u"lb_k_y_1")
        sizePolicy2.setHeightForWidth(self.lb_k_y_1.sizePolicy().hasHeightForWidth())
        self.lb_k_y_1.setSizePolicy(sizePolicy2)
        self.lb_k_y_1.setMaximumSize(QSize(50, 16777215))

        self.hl_k_y_1.addWidget(self.lb_k_y_1)

        self.le_k_y_1 = QLineEdit(self.tab_3)
        self.le_k_y_1.setObjectName(u"le_k_y_1")
        self.le_k_y_1.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_k_y_1.sizePolicy().hasHeightForWidth())
        self.le_k_y_1.setSizePolicy(sizePolicy3)
        self.le_k_y_1.setMaximumSize(QSize(100, 16777215))

        self.hl_k_y_1.addWidget(self.le_k_y_1)


        self.gridLayout_12.addLayout(self.hl_k_y_1, 0, 2, 1, 1)

        self.lb_C_N = QLabel(self.tab_3)
        self.lb_C_N.setObjectName(u"lb_C_N")
        sizePolicy2.setHeightForWidth(self.lb_C_N.sizePolicy().hasHeightForWidth())
        self.lb_C_N.setSizePolicy(sizePolicy2)
        self.lb_C_N.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_12.addWidget(self.lb_C_N, 0, 0, 1, 1)


        self.vl_variables_t3.addLayout(self.gridLayout_12)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(-1, -1, 0, -1)
        self.lb_u_p = QLabel(self.tab_3)
        self.lb_u_p.setObjectName(u"lb_u_p")
        sizePolicy2.setHeightForWidth(self.lb_u_p.sizePolicy().hasHeightForWidth())
        self.lb_u_p.setSizePolicy(sizePolicy2)
        self.lb_u_p.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_11.addWidget(self.lb_u_p, 0, 0, 1, 1)

        self.le_u_p = QLineEdit(self.tab_3)
        self.le_u_p.setObjectName(u"le_u_p")
        self.le_u_p.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_u_p.sizePolicy().hasHeightForWidth())
        self.le_u_p.setSizePolicy(sizePolicy3)
        self.le_u_p.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_11.addWidget(self.le_u_p, 0, 1, 1, 1)

        self.hl_k_ob = QHBoxLayout()
        self.hl_k_ob.setSpacing(0)
        self.hl_k_ob.setObjectName(u"hl_k_ob")
        self.hl_k_ob.setContentsMargins(-1, -1, 0, -1)
        self.lb_k_ob = QLabel(self.tab_3)
        self.lb_k_ob.setObjectName(u"lb_k_ob")
        sizePolicy2.setHeightForWidth(self.lb_k_ob.sizePolicy().hasHeightForWidth())
        self.lb_k_ob.setSizePolicy(sizePolicy2)
        self.lb_k_ob.setMaximumSize(QSize(50, 16777215))

        self.hl_k_ob.addWidget(self.lb_k_ob)

        self.le_k_ob = QLineEdit(self.tab_3)
        self.le_k_ob.setObjectName(u"le_k_ob")
        self.le_k_ob.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.le_k_ob.sizePolicy().hasHeightForWidth())
        self.le_k_ob.setSizePolicy(sizePolicy4)
        self.le_k_ob.setMinimumSize(QSize(20, 20))
        self.le_k_ob.setMaximumSize(QSize(100, 16777215))
        self.le_k_ob.setSizeIncrement(QSize(100, 0))

        self.hl_k_ob.addWidget(self.le_k_ob)


        self.gridLayout_11.addLayout(self.hl_k_ob, 0, 2, 1, 1)


        self.vl_variables_t3.addLayout(self.gridLayout_11)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.lb_Z_1 = QLabel(self.tab_3)
        self.lb_Z_1.setObjectName(u"lb_Z_1")
        sizePolicy2.setHeightForWidth(self.lb_Z_1.sizePolicy().hasHeightForWidth())
        self.lb_Z_1.setSizePolicy(sizePolicy2)
        self.lb_Z_1.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_10.addWidget(self.lb_Z_1, 0, 0, 1, 1)

        self.le_Z_1 = QLineEdit(self.tab_3)
        self.le_Z_1.setObjectName(u"le_Z_1")
        self.le_Z_1.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_Z_1.sizePolicy().hasHeightForWidth())
        self.le_Z_1.setSizePolicy(sizePolicy3)
        self.le_Z_1.setMaximumSize(QSize(100, 16777215))
        self.le_Z_1.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_10.addWidget(self.le_Z_1, 0, 1, 1, 1)

        self.hl_Z_2 = QHBoxLayout()
        self.hl_Z_2.setObjectName(u"hl_Z_2")
        self.hl_Z_2.setContentsMargins(0, -1, -1, -1)
        self.lb_Z_2 = QLabel(self.tab_3)
        self.lb_Z_2.setObjectName(u"lb_Z_2")
        sizePolicy2.setHeightForWidth(self.lb_Z_2.sizePolicy().hasHeightForWidth())
        self.lb_Z_2.setSizePolicy(sizePolicy2)
        self.lb_Z_2.setMaximumSize(QSize(50, 16777215))
        self.lb_Z_2.setFrameShape(QFrame.NoFrame)

        self.hl_Z_2.addWidget(self.lb_Z_2)

        self.le_Z_2 = QLineEdit(self.tab_3)
        self.le_Z_2.setObjectName(u"le_Z_2")
        self.le_Z_2.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_Z_2.sizePolicy().hasHeightForWidth())
        self.le_Z_2.setSizePolicy(sizePolicy3)
        self.le_Z_2.setMaximumSize(QSize(100, 16777215))

        self.hl_Z_2.addWidget(self.le_Z_2)


        self.gridLayout_10.addLayout(self.hl_Z_2, 0, 2, 1, 1)


        self.vl_variables_t3.addLayout(self.gridLayout_10)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.lb_sigma = QLabel(self.tab_3)
        self.lb_sigma.setObjectName(u"lb_sigma")
        sizePolicy2.setHeightForWidth(self.lb_sigma.sizePolicy().hasHeightForWidth())
        self.lb_sigma.setSizePolicy(sizePolicy2)
        self.lb_sigma.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_9.addWidget(self.lb_sigma, 0, 0, 1, 1)

        self.le_sigma = QLineEdit(self.tab_3)
        self.le_sigma.setObjectName(u"le_sigma")
        self.le_sigma.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_sigma.sizePolicy().hasHeightForWidth())
        self.le_sigma.setSizePolicy(sizePolicy3)
        self.le_sigma.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_9.addWidget(self.le_sigma, 0, 1, 1, 1)

        self.hl_t_z_1 = QHBoxLayout()
        self.hl_t_z_1.setObjectName(u"hl_t_z_1")
        self.lb_t_z_1 = QLabel(self.tab_3)
        self.lb_t_z_1.setObjectName(u"lb_t_z_1")
        sizePolicy2.setHeightForWidth(self.lb_t_z_1.sizePolicy().hasHeightForWidth())
        self.lb_t_z_1.setSizePolicy(sizePolicy2)
        self.lb_t_z_1.setMaximumSize(QSize(50, 16777215))

        self.hl_t_z_1.addWidget(self.lb_t_z_1)

        self.le_t_z_1 = QLineEdit(self.tab_3)
        self.le_t_z_1.setObjectName(u"le_t_z_1")
        self.le_t_z_1.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_t_z_1.sizePolicy().hasHeightForWidth())
        self.le_t_z_1.setSizePolicy(sizePolicy3)
        self.le_t_z_1.setMaximumSize(QSize(100, 16777215))

        self.hl_t_z_1.addWidget(self.le_t_z_1)


        self.gridLayout_9.addLayout(self.hl_t_z_1, 0, 2, 1, 1)


        self.vl_variables_t3.addLayout(self.gridLayout_9)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.lb_b_sh = QLabel(self.tab_3)
        self.lb_b_sh.setObjectName(u"lb_b_sh")
        sizePolicy2.setHeightForWidth(self.lb_b_sh.sizePolicy().hasHeightForWidth())
        self.lb_b_sh.setSizePolicy(sizePolicy2)
        self.lb_b_sh.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_8.addWidget(self.lb_b_sh, 0, 0, 1, 1)

        self.le_b_sh = QLineEdit(self.tab_3)
        self.le_b_sh.setObjectName(u"le_b_sh")
        self.le_b_sh.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_b_sh.sizePolicy().hasHeightForWidth())
        self.le_b_sh.setSizePolicy(sizePolicy3)
        self.le_b_sh.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_8.addWidget(self.le_b_sh, 0, 1, 1, 1)

        self.hl_h_sh_r = QHBoxLayout()
        self.hl_h_sh_r.setObjectName(u"hl_h_sh_r")
        self.lb_h_sh_r = QLabel(self.tab_3)
        self.lb_h_sh_r.setObjectName(u"lb_h_sh_r")
        sizePolicy2.setHeightForWidth(self.lb_h_sh_r.sizePolicy().hasHeightForWidth())
        self.lb_h_sh_r.setSizePolicy(sizePolicy2)
        self.lb_h_sh_r.setMaximumSize(QSize(75, 16777215))

        self.hl_h_sh_r.addWidget(self.lb_h_sh_r)

        self.le_h_sh_r = QLineEdit(self.tab_3)
        self.le_h_sh_r.setObjectName(u"le_h_sh_r")
        self.le_h_sh_r.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_h_sh_r.sizePolicy().hasHeightForWidth())
        self.le_h_sh_r.setSizePolicy(sizePolicy3)
        self.le_h_sh_r.setMaximumSize(QSize(75, 16777215))

        self.hl_h_sh_r.addWidget(self.le_h_sh_r)


        self.gridLayout_8.addLayout(self.hl_h_sh_r, 0, 2, 1, 1)


        self.vl_variables_t3.addLayout(self.gridLayout_8)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.lb_Lamda_p_1 = QLabel(self.tab_3)
        self.lb_Lamda_p_1.setObjectName(u"lb_Lamda_p_1")
        sizePolicy2.setHeightForWidth(self.lb_Lamda_p_1.sizePolicy().hasHeightForWidth())
        self.lb_Lamda_p_1.setSizePolicy(sizePolicy2)
        self.lb_Lamda_p_1.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_13.addWidget(self.lb_Lamda_p_1, 0, 0, 1, 1)

        self.le_Lamda_p_1 = QLineEdit(self.tab_3)
        self.le_Lamda_p_1.setObjectName(u"le_Lamda_p_1")
        self.le_Lamda_p_1.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_Lamda_p_1.sizePolicy().hasHeightForWidth())
        self.le_Lamda_p_1.setSizePolicy(sizePolicy3)
        self.le_Lamda_p_1.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_13.addWidget(self.le_Lamda_p_1, 0, 1, 1, 1)

        self.hl_Lamda_d_1 = QHBoxLayout()
        self.hl_Lamda_d_1.setObjectName(u"hl_Lamda_d_1")
        self.lb_Lamda_d_1 = QLabel(self.tab_3)
        self.lb_Lamda_d_1.setObjectName(u"lb_Lamda_d_1")
        sizePolicy2.setHeightForWidth(self.lb_Lamda_d_1.sizePolicy().hasHeightForWidth())
        self.lb_Lamda_d_1.setSizePolicy(sizePolicy2)
        self.lb_Lamda_d_1.setMaximumSize(QSize(50, 16777215))

        self.hl_Lamda_d_1.addWidget(self.lb_Lamda_d_1)

        self.le_Lamda_d_1 = QLineEdit(self.tab_3)
        self.le_Lamda_d_1.setObjectName(u"le_Lamda_d_1")
        self.le_Lamda_d_1.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_Lamda_d_1.sizePolicy().hasHeightForWidth())
        self.le_Lamda_d_1.setSizePolicy(sizePolicy3)
        self.le_Lamda_d_1.setMaximumSize(QSize(100, 16777215))

        self.hl_Lamda_d_1.addWidget(self.le_Lamda_d_1)


        self.gridLayout_13.addLayout(self.hl_Lamda_d_1, 0, 2, 1, 1)


        self.vl_variables_t3.addLayout(self.gridLayout_13)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.lb_Lamda_l_1 = QLabel(self.tab_3)
        self.lb_Lamda_l_1.setObjectName(u"lb_Lamda_l_1")
        sizePolicy2.setHeightForWidth(self.lb_Lamda_l_1.sizePolicy().hasHeightForWidth())
        self.lb_Lamda_l_1.setSizePolicy(sizePolicy2)
        self.lb_Lamda_l_1.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_14.addWidget(self.lb_Lamda_l_1, 0, 0, 1, 1)

        self.le_Lamda_l_1 = QLineEdit(self.tab_3)
        self.le_Lamda_l_1.setObjectName(u"le_Lamda_l_1")
        self.le_Lamda_l_1.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_Lamda_l_1.sizePolicy().hasHeightForWidth())
        self.le_Lamda_l_1.setSizePolicy(sizePolicy3)
        self.le_Lamda_l_1.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_14.addWidget(self.le_Lamda_l_1, 0, 1, 1, 1)

        self.hl_t_z_2 = QHBoxLayout()
        self.hl_t_z_2.setObjectName(u"hl_t_z_2")
        self.lb_t_z_2 = QLabel(self.tab_3)
        self.lb_t_z_2.setObjectName(u"lb_t_z_2")
        sizePolicy2.setHeightForWidth(self.lb_t_z_2.sizePolicy().hasHeightForWidth())
        self.lb_t_z_2.setSizePolicy(sizePolicy2)
        self.lb_t_z_2.setMaximumSize(QSize(50, 16777215))

        self.hl_t_z_2.addWidget(self.lb_t_z_2)

        self.le_t_z_2 = QLineEdit(self.tab_3)
        self.le_t_z_2.setObjectName(u"le_t_z_2")
        self.le_t_z_2.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_t_z_2.sizePolicy().hasHeightForWidth())
        self.le_t_z_2.setSizePolicy(sizePolicy3)
        self.le_t_z_2.setMaximumSize(QSize(100, 16777215))

        self.hl_t_z_2.addWidget(self.le_t_z_2)


        self.gridLayout_14.addLayout(self.hl_t_z_2, 0, 2, 1, 1)


        self.vl_variables_t3.addLayout(self.gridLayout_14)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.lb_r_2_Ksi_shtrih = QLabel(self.tab_3)
        self.lb_r_2_Ksi_shtrih.setObjectName(u"lb_r_2_Ksi_shtrih")
        sizePolicy2.setHeightForWidth(self.lb_r_2_Ksi_shtrih.sizePolicy().hasHeightForWidth())
        self.lb_r_2_Ksi_shtrih.setSizePolicy(sizePolicy2)
        self.lb_r_2_Ksi_shtrih.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_15.addWidget(self.lb_r_2_Ksi_shtrih, 0, 0, 1, 1)

        self.le_r_2_Ksi_shtrih = QLineEdit(self.tab_3)
        self.le_r_2_Ksi_shtrih.setObjectName(u"le_r_2_Ksi_shtrih")
        self.le_r_2_Ksi_shtrih.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_r_2_Ksi_shtrih.sizePolicy().hasHeightForWidth())
        self.le_r_2_Ksi_shtrih.setSizePolicy(sizePolicy3)
        self.le_r_2_Ksi_shtrih.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_15.addWidget(self.le_r_2_Ksi_shtrih, 0, 1, 1, 1)

        self.hl_I_1_p = QHBoxLayout()
        self.hl_I_1_p.setObjectName(u"hl_I_1_p")
        self.lb_I_1_p = QLabel(self.tab_3)
        self.lb_I_1_p.setObjectName(u"lb_I_1_p")
        sizePolicy2.setHeightForWidth(self.lb_I_1_p.sizePolicy().hasHeightForWidth())
        self.lb_I_1_p.setSizePolicy(sizePolicy2)
        self.lb_I_1_p.setMaximumSize(QSize(50, 16777215))

        self.hl_I_1_p.addWidget(self.lb_I_1_p)

        self.le_I_1_p = QLineEdit(self.tab_3)
        self.le_I_1_p.setObjectName(u"le_I_1_p")
        self.le_I_1_p.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_I_1_p.sizePolicy().hasHeightForWidth())
        self.le_I_1_p.setSizePolicy(sizePolicy3)
        self.le_I_1_p.setMaximumSize(QSize(100, 16777215))

        self.hl_I_1_p.addWidget(self.le_I_1_p)


        self.gridLayout_15.addLayout(self.hl_I_1_p, 0, 2, 1, 1)


        self.vl_variables_t3.addLayout(self.gridLayout_15)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.lb_I_1_nom = QLabel(self.tab_3)
        self.lb_I_1_nom.setObjectName(u"lb_I_1_nom")
        sizePolicy2.setHeightForWidth(self.lb_I_1_nom.sizePolicy().hasHeightForWidth())
        self.lb_I_1_nom.setSizePolicy(sizePolicy2)
        self.lb_I_1_nom.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_16.addWidget(self.lb_I_1_nom, 0, 0, 1, 1)

        self.le_I_1_nom = QLineEdit(self.tab_3)
        self.le_I_1_nom.setObjectName(u"le_I_1_nom")
        self.le_I_1_nom.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_I_1_nom.sizePolicy().hasHeightForWidth())
        self.le_I_1_nom.setSizePolicy(sizePolicy3)
        self.le_I_1_nom.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_16.addWidget(self.le_I_1_nom, 0, 1, 1, 1)

        self.hl_h_k = QHBoxLayout()
        self.hl_h_k.setObjectName(u"hl_h_k")
        self.lb_h_k = QLabel(self.tab_3)
        self.lb_h_k.setObjectName(u"lb_h_k")
        sizePolicy2.setHeightForWidth(self.lb_h_k.sizePolicy().hasHeightForWidth())
        self.lb_h_k.setSizePolicy(sizePolicy2)
        self.lb_h_k.setMaximumSize(QSize(50, 16777215))

        self.hl_h_k.addWidget(self.lb_h_k)

        self.le_h_k = QLineEdit(self.tab_3)
        self.le_h_k.setObjectName(u"le_h_k")
        self.le_h_k.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_h_k.sizePolicy().hasHeightForWidth())
        self.le_h_k.setSizePolicy(sizePolicy3)
        self.le_h_k.setMaximumSize(QSize(100, 16777215))

        self.hl_h_k.addWidget(self.le_h_k)


        self.gridLayout_16.addLayout(self.hl_h_k, 0, 2, 1, 1)


        self.vl_variables_t3.addLayout(self.gridLayout_16)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.lb_Lamda_p_2_Ksi = QLabel(self.tab_3)
        self.lb_Lamda_p_2_Ksi.setObjectName(u"lb_Lamda_p_2_Ksi")
        sizePolicy2.setHeightForWidth(self.lb_Lamda_p_2_Ksi.sizePolicy().hasHeightForWidth())
        self.lb_Lamda_p_2_Ksi.setSizePolicy(sizePolicy2)
        self.lb_Lamda_p_2_Ksi.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_17.addWidget(self.lb_Lamda_p_2_Ksi, 0, 0, 1, 1)

        self.le_Lamda_p_2_Ksi = QLineEdit(self.tab_3)
        self.le_Lamda_p_2_Ksi.setObjectName(u"le_Lamda_p_2_Ksi")
        self.le_Lamda_p_2_Ksi.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_Lamda_p_2_Ksi.sizePolicy().hasHeightForWidth())
        self.le_Lamda_p_2_Ksi.setSizePolicy(sizePolicy3)
        self.le_Lamda_p_2_Ksi.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_17.addWidget(self.le_Lamda_p_2_Ksi, 0, 1, 1, 1)

        self.hl_K_R = QHBoxLayout()
        self.hl_K_R.setObjectName(u"hl_K_R")
        self.lb_K_R = QLabel(self.tab_3)
        self.lb_K_R.setObjectName(u"lb_K_R")
        sizePolicy2.setHeightForWidth(self.lb_K_R.sizePolicy().hasHeightForWidth())
        self.lb_K_R.setSizePolicy(sizePolicy2)
        self.lb_K_R.setMaximumSize(QSize(50, 16777215))

        self.hl_K_R.addWidget(self.lb_K_R)

        self.le_K_R = QLineEdit(self.tab_3)
        self.le_K_R.setObjectName(u"le_K_R")
        self.le_K_R.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.le_K_R.sizePolicy().hasHeightForWidth())
        self.le_K_R.setSizePolicy(sizePolicy3)
        self.le_K_R.setMaximumSize(QSize(100, 16777215))

        self.hl_K_R.addWidget(self.le_K_R)


        self.gridLayout_17.addLayout(self.hl_K_R, 0, 2, 1, 1)


        self.vl_variables_t3.addLayout(self.gridLayout_17)


        self.gridLayout_3.addLayout(self.vl_variables_t3, 0, 1, 1, 1)

        self.lb_error_3 = QLabel(self.tab_3)
        self.lb_error_3.setObjectName(u"lb_error_3")

        self.gridLayout_3.addWidget(self.lb_error_3, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tb_thermal_calc = QWidget()
        self.tb_thermal_calc.setObjectName(u"tb_thermal_calc")
        self.gridLayout_7 = QGridLayout(self.tb_thermal_calc)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_D = QLabel(self.tb_thermal_calc)
        self.lb_D.setObjectName(u"lb_D")
        self.lb_D.setMinimumSize(QSize(50, 0))
        self.lb_D.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_4.addWidget(self.lb_D)

        self.le_D = QLineEdit(self.tb_thermal_calc)
        self.le_D.setObjectName(u"le_D")
        self.le_D.setMinimumSize(QSize(100, 0))
        self.le_D.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_4.addWidget(self.le_D)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_P_st_main = QLabel(self.tb_thermal_calc)
        self.lb_P_st_main.setObjectName(u"lb_P_st_main")
        self.lb_P_st_main.setMinimumSize(QSize(50, 0))
        self.lb_P_st_main.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_2.addWidget(self.lb_P_st_main)

        self.le_P_st_main = QLineEdit(self.tb_thermal_calc)
        self.le_P_st_main.setObjectName(u"le_P_st_main")
        self.le_P_st_main.setMinimumSize(QSize(100, 0))
        self.le_P_st_main.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.le_P_st_main)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout_7.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_l_1 = QLabel(self.tb_thermal_calc)
        self.lb_l_1.setObjectName(u"lb_l_1")
        self.lb_l_1.setMinimumSize(QSize(50, 0))
        self.lb_l_1.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.lb_l_1)

        self.le_l_1 = QLineEdit(self.tb_thermal_calc)
        self.le_l_1.setObjectName(u"le_l_1")
        self.le_l_1.setMinimumSize(QSize(100, 0))
        self.le_l_1.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.le_l_1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_a_1 = QLabel(self.tb_thermal_calc)
        self.lb_a_1.setObjectName(u"lb_a_1")
        self.lb_a_1.setMinimumSize(QSize(50, 0))
        self.lb_a_1.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_6.addWidget(self.lb_a_1)

        self.le_a_1 = QLineEdit(self.tb_thermal_calc)
        self.le_a_1.setObjectName(u"le_a_1")
        self.le_a_1.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.le_a_1)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)


        self.gridLayout_7.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.l_delta_nu_pov_1 = QLabel(self.tb_thermal_calc)
        self.l_delta_nu_pov_1.setObjectName(u"l_delta_nu_pov_1")

        self.horizontalLayout_20.addWidget(self.l_delta_nu_pov_1)

        self.lb_delta_nu_pov_1 = QLabel(self.tb_thermal_calc)
        self.lb_delta_nu_pov_1.setObjectName(u"lb_delta_nu_pov_1")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.lb_delta_nu_pov_1.sizePolicy().hasHeightForWidth())
        self.lb_delta_nu_pov_1.setSizePolicy(sizePolicy7)

        self.horizontalLayout_20.addWidget(self.lb_delta_nu_pov_1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.l_delta_nu_iz_p_1 = QLabel(self.tb_thermal_calc)
        self.l_delta_nu_iz_p_1.setObjectName(u"l_delta_nu_iz_p_1")

        self.horizontalLayout_21.addWidget(self.l_delta_nu_iz_p_1)

        self.lb_delta_nu_iz_p_1 = QLabel(self.tb_thermal_calc)
        self.lb_delta_nu_iz_p_1.setObjectName(u"lb_delta_nu_iz_p_1")
        sizePolicy7.setHeightForWidth(self.lb_delta_nu_iz_p_1.sizePolicy().hasHeightForWidth())
        self.lb_delta_nu_iz_p_1.setSizePolicy(sizePolicy7)

        self.horizontalLayout_21.addWidget(self.lb_delta_nu_iz_p_1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.l_delta_nu_iz_l_1 = QLabel(self.tb_thermal_calc)
        self.l_delta_nu_iz_l_1.setObjectName(u"l_delta_nu_iz_l_1")

        self.horizontalLayout_22.addWidget(self.l_delta_nu_iz_l_1)

        self.lb_delta_nu_iz_l_1 = QLabel(self.tb_thermal_calc)
        self.lb_delta_nu_iz_l_1.setObjectName(u"lb_delta_nu_iz_l_1")
        sizePolicy7.setHeightForWidth(self.lb_delta_nu_iz_l_1.sizePolicy().hasHeightForWidth())
        self.lb_delta_nu_iz_l_1.setSizePolicy(sizePolicy7)

        self.horizontalLayout_22.addWidget(self.lb_delta_nu_iz_l_1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.l_delta_nu_pov_l_1 = QLabel(self.tb_thermal_calc)
        self.l_delta_nu_pov_l_1.setObjectName(u"l_delta_nu_pov_l_1")

        self.horizontalLayout_23.addWidget(self.l_delta_nu_pov_l_1)

        self.lb_delta_nu_pov_l_1 = QLabel(self.tb_thermal_calc)
        self.lb_delta_nu_pov_l_1.setObjectName(u"lb_delta_nu_pov_l_1")
        sizePolicy7.setHeightForWidth(self.lb_delta_nu_pov_l_1.sizePolicy().hasHeightForWidth())
        self.lb_delta_nu_pov_l_1.setSizePolicy(sizePolicy7)

        self.horizontalLayout_23.addWidget(self.lb_delta_nu_pov_l_1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.l_Q_v = QLabel(self.tb_thermal_calc)
        self.l_Q_v.setObjectName(u"l_Q_v")

        self.horizontalLayout_24.addWidget(self.l_Q_v)

        self.lb_delta_nu_1_shtrih = QLabel(self.tb_thermal_calc)
        self.lb_delta_nu_1_shtrih.setObjectName(u"lb_delta_nu_1_shtrih")
        sizePolicy7.setHeightForWidth(self.lb_delta_nu_1_shtrih.sizePolicy().hasHeightForWidth())
        self.lb_delta_nu_1_shtrih.setSizePolicy(sizePolicy7)

        self.horizontalLayout_24.addWidget(self.lb_delta_nu_1_shtrih)


        self.verticalLayout_3.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.l_delta_nu_1_shtrih = QLabel(self.tb_thermal_calc)
        self.l_delta_nu_1_shtrih.setObjectName(u"l_delta_nu_1_shtrih")

        self.horizontalLayout_25.addWidget(self.l_delta_nu_1_shtrih)

        self.lb_delta_gamma_v = QLabel(self.tb_thermal_calc)
        self.lb_delta_gamma_v.setObjectName(u"lb_delta_gamma_v")
        sizePolicy7.setHeightForWidth(self.lb_delta_gamma_v.sizePolicy().hasHeightForWidth())
        self.lb_delta_gamma_v.setSizePolicy(sizePolicy7)

        self.horizontalLayout_25.addWidget(self.lb_delta_gamma_v)


        self.verticalLayout_3.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.l_teta_v_shtrih = QLabel(self.tb_thermal_calc)
        self.l_teta_v_shtrih.setObjectName(u"l_teta_v_shtrih")

        self.horizontalLayout_26.addWidget(self.l_teta_v_shtrih)

        self.lb_delta_nu_1 = QLabel(self.tb_thermal_calc)
        self.lb_delta_nu_1.setObjectName(u"lb_delta_nu_1")
        sizePolicy7.setHeightForWidth(self.lb_delta_nu_1.sizePolicy().hasHeightForWidth())
        self.lb_delta_nu_1.setSizePolicy(sizePolicy7)

        self.horizontalLayout_26.addWidget(self.lb_delta_nu_1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.l_delta_nu_1 = QLabel(self.tb_thermal_calc)
        self.l_delta_nu_1.setObjectName(u"l_delta_nu_1")

        self.horizontalLayout_27.addWidget(self.l_delta_nu_1)

        self.lb_Q_v = QLabel(self.tb_thermal_calc)
        self.lb_Q_v.setObjectName(u"lb_Q_v")
        sizePolicy7.setHeightForWidth(self.lb_Q_v.sizePolicy().hasHeightForWidth())
        self.lb_Q_v.setSizePolicy(sizePolicy7)

        self.horizontalLayout_27.addWidget(self.lb_Q_v)


        self.verticalLayout_3.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.l_delta_gamma_v = QLabel(self.tb_thermal_calc)
        self.l_delta_gamma_v.setObjectName(u"l_delta_gamma_v")

        self.horizontalLayout_28.addWidget(self.l_delta_gamma_v)

        self.lb_teta_v_shtrih = QLabel(self.tb_thermal_calc)
        self.lb_teta_v_shtrih.setObjectName(u"lb_teta_v_shtrih")
        sizePolicy7.setHeightForWidth(self.lb_teta_v_shtrih.sizePolicy().hasHeightForWidth())
        self.lb_teta_v_shtrih.setSizePolicy(sizePolicy7)

        self.horizontalLayout_28.addWidget(self.lb_teta_v_shtrih)


        self.verticalLayout_3.addLayout(self.horizontalLayout_28)


        self.gridLayout_7.addLayout(self.verticalLayout_3, 1, 1, 5, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_h_pk = QLabel(self.tb_thermal_calc)
        self.lb_h_pk.setObjectName(u"lb_h_pk")
        self.lb_h_pk.setMinimumSize(QSize(50, 0))
        self.lb_h_pk.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_7.addWidget(self.lb_h_pk)

        self.le_h_pk = QLineEdit(self.tb_thermal_calc)
        self.le_h_pk.setObjectName(u"le_h_pk")
        self.le_h_pk.setMinimumSize(QSize(100, 0))
        self.le_h_pk.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_7.addWidget(self.le_h_pk)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lb_b_1 = QLabel(self.tb_thermal_calc)
        self.lb_b_1.setObjectName(u"lb_b_1")
        self.lb_b_1.setMinimumSize(QSize(50, 0))
        self.lb_b_1.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_8.addWidget(self.lb_b_1)

        self.le_b_1 = QLineEdit(self.tb_thermal_calc)
        self.le_b_1.setObjectName(u"le_b_1")
        self.le_b_1.setMinimumSize(QSize(100, 0))
        self.le_b_1.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_8.addWidget(self.le_b_1)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)


        self.gridLayout_7.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lb_b_2 = QLabel(self.tb_thermal_calc)
        self.lb_b_2.setObjectName(u"lb_b_2")
        self.lb_b_2.setMinimumSize(QSize(50, 0))
        self.lb_b_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_9.addWidget(self.lb_b_2)

        self.le_b_2 = QLineEdit(self.tb_thermal_calc)
        self.le_b_2.setObjectName(u"le_b_2")
        self.le_b_2.setMinimumSize(QSize(100, 0))
        self.le_b_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_9.addWidget(self.le_b_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lb_b_iz_p_1 = QLabel(self.tb_thermal_calc)
        self.lb_b_iz_p_1.setObjectName(u"lb_b_iz_p_1")
        self.lb_b_iz_p_1.setMinimumSize(QSize(50, 0))
        self.lb_b_iz_p_1.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_10.addWidget(self.lb_b_iz_p_1)

        self.le_b_iz_p_1 = QLineEdit(self.tb_thermal_calc)
        self.le_b_iz_p_1.setObjectName(u"le_b_iz_p_1")
        self.le_b_iz_p_1.setMinimumSize(QSize(100, 0))
        self.le_b_iz_p_1.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_10.addWidget(self.le_b_iz_p_1)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)


        self.gridLayout_7.addLayout(self.horizontalLayout_9, 3, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lb_lambda_ekv_shtrih = QLabel(self.tb_thermal_calc)
        self.lb_lambda_ekv_shtrih.setObjectName(u"lb_lambda_ekv_shtrih")
        self.lb_lambda_ekv_shtrih.setMinimumSize(QSize(50, 0))
        self.lb_lambda_ekv_shtrih.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_11.addWidget(self.lb_lambda_ekv_shtrih)

        self.le_lambda_ekv_shtrih = QLineEdit(self.tb_thermal_calc)
        self.le_lambda_ekv_shtrih.setObjectName(u"le_lambda_ekv_shtrih")
        self.le_lambda_ekv_shtrih.setMinimumSize(QSize(100, 0))
        self.le_lambda_ekv_shtrih.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_11.addWidget(self.le_lambda_ekv_shtrih)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, -1, -1, -1)
        self.lb_l_l_1 = QLabel(self.tb_thermal_calc)
        self.lb_l_l_1.setObjectName(u"lb_l_l_1")
        self.lb_l_l_1.setMinimumSize(QSize(50, 0))
        self.lb_l_l_1.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_12.addWidget(self.lb_l_l_1)

        self.le_l_l_1 = QLineEdit(self.tb_thermal_calc)
        self.le_l_l_1.setObjectName(u"le_l_l_1")
        self.le_l_l_1.setMinimumSize(QSize(100, 0))
        self.le_l_l_1.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_12.addWidget(self.le_l_l_1)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_12)


        self.gridLayout_7.addLayout(self.horizontalLayout_11, 4, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lb_b_iz_l_1 = QLabel(self.tb_thermal_calc)
        self.lb_b_iz_l_1.setObjectName(u"lb_b_iz_l_1")
        self.lb_b_iz_l_1.setMinimumSize(QSize(50, 0))
        self.lb_b_iz_l_1.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_13.addWidget(self.lb_b_iz_l_1)

        self.le_b_iz_l_1 = QLineEdit(self.tb_thermal_calc)
        self.le_b_iz_l_1.setObjectName(u"le_b_iz_l_1")
        self.le_b_iz_l_1.setMinimumSize(QSize(100, 0))
        self.le_b_iz_l_1.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_13.addWidget(self.le_b_iz_l_1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lb_h_p_1 = QLabel(self.tb_thermal_calc)
        self.lb_h_p_1.setObjectName(u"lb_h_p_1")
        self.lb_h_p_1.setMinimumSize(QSize(50, 0))
        self.lb_h_p_1.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_14.addWidget(self.lb_h_p_1)

        self.le_h_p_1 = QLineEdit(self.tb_thermal_calc)
        self.le_h_p_1.setObjectName(u"le_h_p_1")
        self.le_h_p_1.setMinimumSize(QSize(100, 0))
        self.le_h_p_1.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_14.addWidget(self.le_h_p_1)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)


        self.gridLayout_7.addLayout(self.horizontalLayout_13, 5, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lb_l_vbl = QLabel(self.tb_thermal_calc)
        self.lb_l_vbl.setObjectName(u"lb_l_vbl")
        self.lb_l_vbl.setMinimumSize(QSize(50, 0))
        self.lb_l_vbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_15.addWidget(self.lb_l_vbl)

        self.le_l_vbl = QLineEdit(self.tb_thermal_calc)
        self.le_l_vbl.setObjectName(u"le_l_vbl")
        self.le_l_vbl.setMinimumSize(QSize(100, 0))
        self.le_l_vbl.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_15.addWidget(self.le_l_vbl)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lb_l_avg_1 = QLabel(self.tb_thermal_calc)
        self.lb_l_avg_1.setObjectName(u"lb_l_avg_1")
        self.lb_l_avg_1.setMinimumSize(QSize(50, 0))
        self.lb_l_avg_1.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_16.addWidget(self.lb_l_avg_1)

        self.le_l_avg_1 = QLineEdit(self.tb_thermal_calc)
        self.le_l_avg_1.setObjectName(u"le_l_avg_1")
        self.le_l_avg_1.setMinimumSize(QSize(100, 0))
        self.le_l_avg_1.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_16.addWidget(self.le_l_avg_1)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_16)


        self.gridLayout_7.addLayout(self.horizontalLayout_15, 6, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lb_a_v = QLabel(self.tb_thermal_calc)
        self.lb_a_v.setObjectName(u"lb_a_v")
        self.lb_a_v.setMinimumSize(QSize(50, 0))
        self.lb_a_v.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_18.addWidget(self.lb_a_v)

        self.le_a_v = QLineEdit(self.tb_thermal_calc)
        self.le_a_v.setObjectName(u"le_a_v")
        self.le_a_v.setMinimumSize(QSize(100, 0))
        self.le_a_v.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_18.addWidget(self.le_a_v)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lb_D_a = QLabel(self.tb_thermal_calc)
        self.lb_D_a.setObjectName(u"lb_D_a")
        self.lb_D_a.setMinimumSize(QSize(50, 0))
        self.lb_D_a.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_19.addWidget(self.lb_D_a)

        self.le_D_a = QLineEdit(self.tb_thermal_calc)
        self.le_D_a.setObjectName(u"le_D_a")
        self.le_D_a.setMinimumSize(QSize(100, 0))
        self.le_D_a.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_19.addWidget(self.le_D_a)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_19)


        self.gridLayout_7.addLayout(self.horizontalLayout_18, 7, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lb_s_kor = QLabel(self.tb_thermal_calc)
        self.lb_s_kor.setObjectName(u"lb_s_kor")
        self.lb_s_kor.setMinimumSize(QSize(50, 0))
        self.lb_s_kor.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_17.addWidget(self.lb_s_kor)

        self.le_s_kor = QLineEdit(self.tb_thermal_calc)
        self.le_s_kor.setObjectName(u"le_s_kor")
        self.le_s_kor.setMinimumSize(QSize(100, 0))
        self.le_s_kor.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_17.addWidget(self.le_s_kor)


        self.gridLayout_7.addLayout(self.horizontalLayout_17, 8, 0, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.bt_thermal_calc = QPushButton(self.tb_thermal_calc)
        self.bt_thermal_calc.setObjectName(u"bt_thermal_calc")

        self.gridLayout_18.addWidget(self.bt_thermal_calc, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_18, 9, 0, 1, 1)

        self.tabWidget.addTab(self.tb_thermal_calc, "")
        self.tb_settings = QWidget()
        self.tb_settings.setObjectName(u"tb_settings")
        self.formLayout = QFormLayout(self.tb_settings)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.lb_valueOfError = QLabel(self.tb_settings)
        self.lb_valueOfError.setObjectName(u"lb_valueOfError")
        self.lb_valueOfError.setMargin(0)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lb_valueOfError)

        self.sl_ValueOfError = QSlider(self.tb_settings)
        self.sl_ValueOfError.setObjectName(u"sl_ValueOfError")
        self.sl_ValueOfError.setMaximumSize(QSize(150, 16777215))
        self.sl_ValueOfError.setMinimum(5)
        self.sl_ValueOfError.setMaximum(35)
        self.sl_ValueOfError.setSingleStep(5)
        self.sl_ValueOfError.setPageStep(5)
        self.sl_ValueOfError.setValue(10)
        self.sl_ValueOfError.setOrientation(Qt.Horizontal)
        self.sl_ValueOfError.setTickPosition(QSlider.TicksBelow)
        self.sl_ValueOfError.setTickInterval(5)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.sl_ValueOfError)

        self.tabWidget.addTab(self.tb_settings, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.label = QLabel(self.tab_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 1371, 471))
        self.label.setWordWrap(True)
        self.tabWidget.addTab(self.tab_5, "")

        self.gridLayout_19.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_6.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(mainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.linePower.setCurrentIndex(18)
        self.lineVoltage.setCurrentIndex(1)
        self.linePolarity.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0447\u0451\u0442\u043d\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.Input.setText(QCoreApplication.translate("mainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435:", None))
        self.submitValues.setText(QCoreApplication.translate("mainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        self.Power.setText(QCoreApplication.translate("mainWindow", u"\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f ", None))
        self.Voltage.setText(QCoreApplication.translate("mainWindow", u"\u041d\u043e\u043c\u0438\u043d\u0430\u043b\u044c\u043d\u043e\u0435 \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435", None))
        self.polarity.setText(QCoreApplication.translate("mainWindow", u"\u041f\u043e\u043b\u044f\u0440\u043d\u043e\u0441\u0442\u044c", None))
        self.label_7.setText(QCoreApplication.translate("mainWindow", u"\u041a\u043b\u0430\u0441\u0441 \u043d\u0430\u0433\u0440\u0435\u0432\u043e\u0441\u0442\u043e\u0439\u043a\u043e\u0441\u0442\u0438", None))
        self.Snom.setText(QCoreApplication.translate("mainWindow", u"S_\u043d\u043e\u043c\u0438\u043d\u0430\u043b\u044c\u043d\u043e\u0435", None))
        self.linePower.setItemText(0, QCoreApplication.translate("mainWindow", u"0.06", None))
        self.linePower.setItemText(1, QCoreApplication.translate("mainWindow", u"0.09", None))
        self.linePower.setItemText(2, QCoreApplication.translate("mainWindow", u"0.12", None))
        self.linePower.setItemText(3, QCoreApplication.translate("mainWindow", u"0.18", None))
        self.linePower.setItemText(4, QCoreApplication.translate("mainWindow", u"0.25", None))
        self.linePower.setItemText(5, QCoreApplication.translate("mainWindow", u"0.37", None))
        self.linePower.setItemText(6, QCoreApplication.translate("mainWindow", u"0.56", None))
        self.linePower.setItemText(7, QCoreApplication.translate("mainWindow", u"0.75", None))
        self.linePower.setItemText(8, QCoreApplication.translate("mainWindow", u"1.1", None))
        self.linePower.setItemText(9, QCoreApplication.translate("mainWindow", u"1.5", None))
        self.linePower.setItemText(10, QCoreApplication.translate("mainWindow", u"2.2", None))
        self.linePower.setItemText(11, QCoreApplication.translate("mainWindow", u"3.0", None))
        self.linePower.setItemText(12, QCoreApplication.translate("mainWindow", u"4.0", None))
        self.linePower.setItemText(13, QCoreApplication.translate("mainWindow", u"5.5", None))
        self.linePower.setItemText(14, QCoreApplication.translate("mainWindow", u"7.5", None))
        self.linePower.setItemText(15, QCoreApplication.translate("mainWindow", u"11", None))
        self.linePower.setItemText(16, QCoreApplication.translate("mainWindow", u"15", None))
        self.linePower.setItemText(17, QCoreApplication.translate("mainWindow", u"18.5", None))
        self.linePower.setItemText(18, QCoreApplication.translate("mainWindow", u"22", None))
        self.linePower.setItemText(19, QCoreApplication.translate("mainWindow", u"30", None))
        self.linePower.setItemText(20, QCoreApplication.translate("mainWindow", u"37", None))
        self.linePower.setItemText(21, QCoreApplication.translate("mainWindow", u"45", None))
        self.linePower.setItemText(22, QCoreApplication.translate("mainWindow", u"55", None))
        self.linePower.setItemText(23, QCoreApplication.translate("mainWindow", u"75", None))
        self.linePower.setItemText(24, QCoreApplication.translate("mainWindow", u"90", None))
        self.linePower.setItemText(25, QCoreApplication.translate("mainWindow", u"110", None))
        self.linePower.setItemText(26, QCoreApplication.translate("mainWindow", u"132", None))
        self.linePower.setItemText(27, QCoreApplication.translate("mainWindow", u"160", None))
        self.linePower.setItemText(28, QCoreApplication.translate("mainWindow", u"200", None))
        self.linePower.setItemText(29, QCoreApplication.translate("mainWindow", u"250", None))
        self.linePower.setItemText(30, QCoreApplication.translate("mainWindow", u"315", None))

        self.lineVoltage.setItemText(0, QCoreApplication.translate("mainWindow", u"220", None))
        self.lineVoltage.setItemText(1, QCoreApplication.translate("mainWindow", u"380", None))
        self.lineVoltage.setItemText(2, QCoreApplication.translate("mainWindow", u"660", None))

        self.linePolarity.setItemText(0, QCoreApplication.translate("mainWindow", u"2", None))
        self.linePolarity.setItemText(1, QCoreApplication.translate("mainWindow", u"4", None))
        self.linePolarity.setItemText(2, QCoreApplication.translate("mainWindow", u"6", None))
        self.linePolarity.setItemText(3, QCoreApplication.translate("mainWindow", u"8", None))
        self.linePolarity.setItemText(4, QCoreApplication.translate("mainWindow", u"10", None))
        self.linePolarity.setItemText(5, QCoreApplication.translate("mainWindow", u"12", None))

        self.cmb_heatClass.setItemText(0, QCoreApplication.translate("mainWindow", u"F", None))
        self.cmb_heatClass.setItemText(1, QCoreApplication.translate("mainWindow", u"B", None))
        self.cmb_heatClass.setItemText(2, QCoreApplication.translate("mainWindow", u"H", None))

        self.lineSnom.setText(QCoreApplication.translate("mainWindow", u"0.024", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("mainWindow", u"\u0412\u0432\u043e\u0434 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0447\u0451\u0442\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0443\u043b\u0430", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440\u043d\u043e\u0441\u0442\u044c", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043a\u043e\u043b\u044c\u0436\u0435\u043d\u0438\u0435 s", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("mainWindow", u"s nom", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("mainWindow", u"1", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("mainWindow", u"2", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("mainWindow", u"3", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("mainWindow", u"4", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("mainWindow", u"5", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("mainWindow", u"6", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("mainWindow", u"7", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("mainWindow", u"8", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("mainWindow", u"9", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("mainWindow", u"10", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("mainWindow", u"11", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("mainWindow", u"12", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("mainWindow", u"13", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("mainWindow", u"14", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("mainWindow", u"15", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(16)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("mainWindow", u"16", None));
        ___qtablewidgetitem20 = self.tableWidget.verticalHeaderItem(17)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("mainWindow", u"17", None));
        ___qtablewidgetitem21 = self.tableWidget.verticalHeaderItem(18)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("mainWindow", u"18", None));
        ___qtablewidgetitem22 = self.tableWidget.verticalHeaderItem(19)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("mainWindow", u"19", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem23 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("mainWindow", u"0.005", None));
        ___qtablewidgetitem24 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("mainWindow", u"0.01", None));
        ___qtablewidgetitem25 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("mainWindow", u"0.015", None));
        ___qtablewidgetitem26 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("mainWindow", u"0.02", None));
        ___qtablewidgetitem27 = self.tableWidget.item(0, 6)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("mainWindow", u"0.025", None));
        ___qtablewidgetitem28 = self.tableWidget.item(0, 7)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("mainWindow", u"0.03", None));
        ___qtablewidgetitem29 = self.tableWidget.item(0, 8)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("mainWindow", u"0.024", None));
        ___qtablewidgetitem30 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("mainWindow", u"a'r'_2/s'", None));
        ___qtablewidgetitem31 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem32 = self.tableWidget.item(1, 8)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("mainWindow", u"16.692", None));
        ___qtablewidgetitem33 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("mainWindow", u"R = a+a'r'_2/s", None));
        ___qtablewidgetitem34 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem35 = self.tableWidget.item(2, 8)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("mainWindow", u"17.344", None));
        ___qtablewidgetitem36 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("mainWindow", u"X = b+b'r'_2/s", None));
        ___qtablewidgetitem37 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem38 = self.tableWidget.item(3, 8)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("mainWindow", u"4.123", None));
        ___qtablewidgetitem39 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("mainWindow", u"Z = \u221a(R^2+X^2)", None));
        ___qtablewidgetitem40 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem41 = self.tableWidget.item(4, 8)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("mainWindow", u"17.828", None));
        ___qtablewidgetitem42 = self.tableWidget.item(5, 0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("mainWindow", u"I'_2 = U/Z", None));
        ___qtablewidgetitem43 = self.tableWidget.item(5, 1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem44 = self.tableWidget.item(5, 8)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("mainWindow", u"21.315", None));
        ___qtablewidgetitem45 = self.tableWidget.item(6, 0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("mainWindow", u"cos(\u03c6)'_2 = R/Z", None));
        ___qtablewidgetitem46 = self.tableWidget.item(6, 1)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem47 = self.tableWidget.item(6, 8)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("mainWindow", u"0.973", None));
        ___qtablewidgetitem48 = self.tableWidget.item(7, 0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("mainWindow", u"sin(\u03c6)'_2 = X/Z", None));
        ___qtablewidgetitem49 = self.tableWidget.item(7, 1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem50 = self.tableWidget.item(7, 8)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("mainWindow", u"0.231", None));
        ___qtablewidgetitem51 = self.tableWidget.item(8, 0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("mainWindow", u"I_1\u043f = I_0\u043f+I'_2cos(\u03c6)'_2", None));
        ___qtablewidgetitem52 = self.tableWidget.item(8, 1)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem53 = self.tableWidget.item(8, 8)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("mainWindow", u"21.128", None));
        ___qtablewidgetitem54 = self.tableWidget.item(9, 0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("mainWindow", u"I_1\u0440 = I_0\u043f+I'_2sin(\u03c6)'_2", None));
        ___qtablewidgetitem55 = self.tableWidget.item(9, 1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem56 = self.tableWidget.item(9, 8)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("mainWindow", u"10.459", None));
        ___qtablewidgetitem57 = self.tableWidget.item(10, 0)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("mainWindow", u"I_1 = \u221a(I_1\u043f^2+I_1\u0440^2)", None));
        ___qtablewidgetitem58 = self.tableWidget.item(10, 1)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem59 = self.tableWidget.item(10, 8)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("mainWindow", u"23.575", None));
        ___qtablewidgetitem60 = self.tableWidget.item(11, 0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("mainWindow", u"I'_2 = c_1 I'_2", None));
        ___qtablewidgetitem61 = self.tableWidget.item(11, 1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem62 = self.tableWidget.item(11, 8)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("mainWindow", u"21.856", None));
        ___qtablewidgetitem63 = self.tableWidget.item(12, 0)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("mainWindow", u"P_1 = 3U I_1a * 10^-3", None));
        ___qtablewidgetitem64 = self.tableWidget.item(12, 1)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("mainWindow", u"\u043a\u0412\u0442", None));
        ___qtablewidgetitem65 = self.tableWidget.item(12, 8)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("mainWindow", u"24.086", None));
        ___qtablewidgetitem66 = self.tableWidget.item(13, 0)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("mainWindow", u"P_\u044d1 = 3I_1^2*r_1*10^-3", None));
        ___qtablewidgetitem67 = self.tableWidget.item(13, 1)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("mainWindow", u"\u043a\u0412\u0442", None));
        ___qtablewidgetitem68 = self.tableWidget.item(13, 8)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("mainWindow", u"1.06", None));
        ___qtablewidgetitem69 = self.tableWidget.item(14, 0)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("mainWindow", u"P_\u044d2=3I'_2^2*r'_2*10^-3", None));
        ___qtablewidgetitem70 = self.tableWidget.item(14, 1)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("mainWindow", u"\u043a\u0412\u0442", None));
        ___qtablewidgetitem71 = self.tableWidget.item(14, 8)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("mainWindow", u"0.546", None));
        ___qtablewidgetitem72 = self.tableWidget.item(15, 0)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("mainWindow", u"P_\u0434\u043e\u0431 = 0,005P_1", None));
        ___qtablewidgetitem73 = self.tableWidget.item(15, 1)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("mainWindow", u"\u043a\u0412\u0442", None));
        ___qtablewidgetitem74 = self.tableWidget.item(15, 8)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("mainWindow", u"0.12", None));
        ___qtablewidgetitem75 = self.tableWidget.item(16, 0)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("mainWindow", u"\u03a3P=P\u0441\u0442+P\u043c\u0435\u0445+P\u044d2+P\u044d1+P\u044d.\u0449+P\u0434\u043e\u0431", None));
        ___qtablewidgetitem76 = self.tableWidget.item(16, 1)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("mainWindow", u"\u043a\u0412\u0442", None));
        ___qtablewidgetitem77 = self.tableWidget.item(16, 8)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("mainWindow", u"2.341", None));
        ___qtablewidgetitem78 = self.tableWidget.item(17, 0)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("mainWindow", u"P_2 = P_1 - \u03a3P", None));
        ___qtablewidgetitem79 = self.tableWidget.item(17, 1)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("mainWindow", u"\u043a\u0412\u0442", None));
        ___qtablewidgetitem80 = self.tableWidget.item(17, 8)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("mainWindow", u"21.745", None));
        ___qtablewidgetitem81 = self.tableWidget.item(18, 0)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("mainWindow", u"\u03b7 = 1 - \u03a3P/P_1", None));
        ___qtablewidgetitem82 = self.tableWidget.item(18, 1)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem83 = self.tableWidget.item(18, 8)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("mainWindow", u"0.903", None));
        ___qtablewidgetitem84 = self.tableWidget.item(19, 0)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("mainWindow", u"cos(\u03c6) = I_1a/I_1", None));
        ___qtablewidgetitem85 = self.tableWidget.item(19, 1)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem86 = self.tableWidget.item(19, 8)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("mainWindow", u"0.896", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.lb_I0a.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">I</span><span style=\" font-size:14pt; vertical-align:sub;\">0a </span><span style=\" font-size:14pt;\">=</span></p></body></html>", None))
        self.le_I0a.setText(QCoreApplication.translate("mainWindow", u"0.37", None))
        self.lb_I0p.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">I</span><span style=\" font-size:14pt; vertical-align:sub;\">0p </span><span style=\" font-size:14pt;\">=</span></p></body></html>", None))
        self.le_I0p.setText(QCoreApplication.translate("mainWindow", u"5.39", None))
        self.lb_Pst.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>P<span style=\" vertical-align:sub;\">\u0421\u0422</span> =</p></body></html>", None))
        self.le_Pst.setText(QCoreApplication.translate("mainWindow", u"449", None))
        self.lb_Pmeh.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>P<span style=\" vertical-align:sub;\">\u043c\u0435\u0445</span> =</p></body></html>", None))
        self.le_Pmeh.setText(QCoreApplication.translate("mainWindow", u"208", None))
        self.lb_r1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">r</span><span style=\" font-size:14pt; vertical-align:sub;\">1 </span><span style=\" font-size:14pt;\">=</span></p></body></html>", None))
        self.le_r1.setText(QCoreApplication.translate("mainWindow", u"0.6", None))
        self.lb_r2_shtrih.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>r'<span style=\" vertical-align:sub;\">2 </span>=</p></body></html>", None))
        self.le_r2_shtrih.setText(QCoreApplication.translate("mainWindow", u"0.38", None))
        self.lb_c1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>c<span style=\" vertical-align:sub;\">1 </span>=</p></body></html>", None))
        self.le_c1.setText(QCoreApplication.translate("mainWindow", u"1.029", None))
        self.lb_a_shtrih.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>a' =</p></body></html>", None))
        self.le_a_shtrih.setText(QCoreApplication.translate("mainWindow", u"1.06", None))
        self.lb_a.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>a =</p></body></html>", None))
        self.le_a.setText(QCoreApplication.translate("mainWindow", u"0.364", None))
        self.lb_b_shtrih.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>b' =</p></body></html>", None))
        self.le_b_shtrih.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.lb_b.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>b =</p></body></html>", None))
        self.le_b.setText(QCoreApplication.translate("mainWindow", u"4.17", None))
        self.bt_check_table_1.setText(QCoreApplication.translate("mainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430", None))
        self.bt_calculate_table1.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.bt_show_chart_1.setText(QCoreApplication.translate("mainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.bt_export_xl_1.setText(QCoreApplication.translate("mainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0432 \u044d\u043a\u0441\u0435\u043b\u044c", None))
        self.lb_error.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("mainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 1", None))
        ___qtablewidgetitem87 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0447\u0451\u0442\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0443\u043b\u0430", None));
        ___qtablewidgetitem88 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440\u043d\u043e\u0441\u0442\u044c", None));
        ___qtablewidgetitem89 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043a\u043e\u043b\u044c\u0436\u0435\u043d\u0438\u0435 s", None));
        ___qtablewidgetitem90 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("mainWindow", u"s \u043a\u0440", None));
        ___qtablewidgetitem91 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("mainWindow", u"1", None));
        ___qtablewidgetitem92 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("mainWindow", u"2", None));
        ___qtablewidgetitem93 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("mainWindow", u"3", None));
        ___qtablewidgetitem94 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("mainWindow", u"4", None));
        ___qtablewidgetitem95 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("mainWindow", u"5", None));
        ___qtablewidgetitem96 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("mainWindow", u"6", None));
        ___qtablewidgetitem97 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("mainWindow", u"7", None));
        ___qtablewidgetitem98 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("mainWindow", u"8", None));
        ___qtablewidgetitem99 = self.tableWidget_2.verticalHeaderItem(9)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("mainWindow", u"9", None));
        ___qtablewidgetitem100 = self.tableWidget_2.verticalHeaderItem(10)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("mainWindow", u"10", None));
        ___qtablewidgetitem101 = self.tableWidget_2.verticalHeaderItem(11)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("mainWindow", u"11", None));
        ___qtablewidgetitem102 = self.tableWidget_2.verticalHeaderItem(12)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("mainWindow", u"12", None));
        ___qtablewidgetitem103 = self.tableWidget_2.verticalHeaderItem(13)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("mainWindow", u"13", None));
        ___qtablewidgetitem104 = self.tableWidget_2.verticalHeaderItem(14)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("mainWindow", u"14", None));

        __sortingEnabled1 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem105 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("mainWindow", u"1", None));
        ___qtablewidgetitem106 = self.tableWidget_2.item(0, 3)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("mainWindow", u"0.8", None));
        ___qtablewidgetitem107 = self.tableWidget_2.item(0, 4)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("mainWindow", u"0.5", None));
        ___qtablewidgetitem108 = self.tableWidget_2.item(0, 5)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("mainWindow", u"0.2", None));
        ___qtablewidgetitem109 = self.tableWidget_2.item(0, 6)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("mainWindow", u"0.1", None));
        ___qtablewidgetitem110 = self.tableWidget_2.item(0, 7)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("mainWindow", u"0.19", None));
        ___qtablewidgetitem111 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("mainWindow", u"\u03be=63,61h_c*\u221as", None));
        ___qtablewidgetitem112 = self.tableWidget_2.item(1, 1)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem113 = self.tableWidget_2.item(1, 2)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("mainWindow", u"1.55", None));
        ___qtablewidgetitem114 = self.tableWidget_2.item(2, 0)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("mainWindow", u"\u03c6(\u03be)", None));
        ___qtablewidgetitem115 = self.tableWidget_2.item(2, 1)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem116 = self.tableWidget_2.item(2, 2)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("mainWindow", u"0.39", None));
        ___qtablewidgetitem117 = self.tableWidget_2.item(3, 0)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("mainWindow", u"h_r = h_c/(1-\u03c6)", None));
        ___qtablewidgetitem118 = self.tableWidget_2.item(3, 1)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("mainWindow", u"\u043c\u043c", None));
        ___qtablewidgetitem119 = self.tableWidget_2.item(3, 2)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("mainWindow", u"17.524", None));
        ___qtablewidgetitem120 = self.tableWidget_2.item(4, 0)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("mainWindow", u"k_r=q_c/q_r", None));
        ___qtablewidgetitem121 = self.tableWidget_2.item(4, 1)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem122 = self.tableWidget_2.item(4, 2)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("mainWindow", u"1.348", None));
        ___qtablewidgetitem123 = self.tableWidget_2.item(5, 0)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("mainWindow", u"K_R =1+(r_c/r_2)*(k_r-1)", None));
        ___qtablewidgetitem124 = self.tableWidget_2.item(5, 1)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem125 = self.tableWidget_2.item(5, 2)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("mainWindow", u"1.23", None));
        ___qtablewidgetitem126 = self.tableWidget_2.item(6, 0)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("mainWindow", u"r'_2_\u03be = K_R*r'_2", None));
        ___qtablewidgetitem127 = self.tableWidget_2.item(6, 1)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem128 = self.tableWidget_2.item(6, 2)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("mainWindow", u"0.48", None));
        ___qtablewidgetitem129 = self.tableWidget_2.item(7, 0)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("mainWindow", u"\u043a_\u0434 = \u03c6'(\u03be)", None));
        ___qtablewidgetitem130 = self.tableWidget_2.item(7, 1)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem131 = self.tableWidget_2.item(7, 2)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("mainWindow", u"0.85", None));
        ___qtablewidgetitem132 = self.tableWidget_2.item(8, 0)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("mainWindow", u"\u03bb_\u043f2\u03be = \u03bb_\u043f2 - \u0394\u03bb\u043f2\u03be", None));
        ___qtablewidgetitem133 = self.tableWidget_2.item(8, 1)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem134 = self.tableWidget_2.item(8, 2)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("mainWindow", u"1.9", None));
        ___qtablewidgetitem135 = self.tableWidget_2.item(9, 0)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("mainWindow", u"Kx = \u03a3\u03bb_2\u03be/\u03a3\u03bb_2", None));
        ___qtablewidgetitem136 = self.tableWidget_2.item(9, 1)
        ___qtablewidgetitem136.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem137 = self.tableWidget_2.item(9, 2)
        ___qtablewidgetitem137.setText(QCoreApplication.translate("mainWindow", u"0.972", None));
        ___qtablewidgetitem138 = self.tableWidget_2.item(10, 0)
        ___qtablewidgetitem138.setText(QCoreApplication.translate("mainWindow", u"x'2\u03be = Kx * x'_2", None));
        ___qtablewidgetitem139 = self.tableWidget_2.item(10, 1)
        ___qtablewidgetitem139.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem140 = self.tableWidget_2.item(10, 2)
        ___qtablewidgetitem140.setText(QCoreApplication.translate("mainWindow", u"2.058", None));
        ___qtablewidgetitem141 = self.tableWidget_2.item(11, 0)
        ___qtablewidgetitem141.setText(QCoreApplication.translate("mainWindow", u"R\u043f = r_1+c_1\u043f* (r'_2_\u03be/s)", None));
        ___qtablewidgetitem142 = self.tableWidget_2.item(11, 1)
        ___qtablewidgetitem142.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem143 = self.tableWidget_2.item(11, 2)
        ___qtablewidgetitem143.setText(QCoreApplication.translate("mainWindow", u"1.16", None));
        ___qtablewidgetitem144 = self.tableWidget_2.item(12, 0)
        ___qtablewidgetitem144.setText(QCoreApplication.translate("mainWindow", u"X\u043f = x_1+c_1\u043f*x'2\u03be", None));
        ___qtablewidgetitem145 = self.tableWidget_2.item(12, 1)
        ___qtablewidgetitem145.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem146 = self.tableWidget_2.item(12, 2)
        ___qtablewidgetitem146.setText(QCoreApplication.translate("mainWindow", u"3.667", None));
        ___qtablewidgetitem147 = self.tableWidget_2.item(13, 0)
        ___qtablewidgetitem147.setText(QCoreApplication.translate("mainWindow", u"I'_2\u043f = U/\u221a(R\u043f^2 + X\u043f^2)", None));
        ___qtablewidgetitem148 = self.tableWidget_2.item(13, 1)
        ___qtablewidgetitem148.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem149 = self.tableWidget_2.item(13, 2)
        ___qtablewidgetitem149.setText(QCoreApplication.translate("mainWindow", u"98.81", None));
        ___qtablewidgetitem150 = self.tableWidget_2.item(14, 0)
        ___qtablewidgetitem150.setText(QCoreApplication.translate("mainWindow", u"I_1\u043f=I'_2\u221a(R\u043f^2 + (X\u043f+x_12\u043f)^2)/(c_1\u043f*x_12\u043f)", None));
        ___qtablewidgetitem151 = self.tableWidget_2.item(14, 1)
        ___qtablewidgetitem151.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem152 = self.tableWidget_2.item(14, 2)
        ___qtablewidgetitem152.setText(QCoreApplication.translate("mainWindow", u"101.15", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled1)

        self.lb_h_c.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c </span>=</p></body></html>", None))
        self.le_h_c.setText(QCoreApplication.translate("mainWindow", u"29.62", None))
        self.lb_h_p_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">p2 </span>=</p></body></html>", None))
        self.le_h_p_2.setText(QCoreApplication.translate("mainWindow", u"30.62", None))
        self.lb_h_sh.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">\u0448</span> =</p></body></html>", None))
        self.le_h_sh.setText(QCoreApplication.translate("mainWindow", u"0.7", None))
        self.lb_h_sh_shtrih.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>h'<span style=\" vertical-align:sub;\">\u0448</span> =</p></body></html>", None))
        self.le_h_sh_shtrih.setText(QCoreApplication.translate("mainWindow", u"0.3", None))
        self.lb_b_1_r.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>b<span style=\" vertical-align:sub;\">1\u0440\u043e\u0442.</span>=</p></body></html>", None))
        self.le_b_1_r.setText(QCoreApplication.translate("mainWindow", u"8.36", None))
        self.lb_b_2_r.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>b<span style=\" vertical-align:sub;\">2\u0440\u043e\u0442.</span>=</p></body></html>", None))
        self.le_b_2_r.setText(QCoreApplication.translate("mainWindow", u"4.53", None))
        self.lb_h_0.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">0</span> =</p></body></html>", None))
        self.le_h_0.setText(QCoreApplication.translate("mainWindow", u"24.98", None))
        self.lb_b_sh_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>b<span style=\" vertical-align:sub;\">\u04482</span> =</p></body></html>", None))
        self.le_b_sh_2.setText(QCoreApplication.translate("mainWindow", u"1.5", None))
        self.lb_Lamda_d_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; font-weight:700; color:#202122; background-color:#ffffff;\">\u03bb</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; font-weight:700; color:#202122; background-color:#ffffff; vertical-align:sub;\">\u0434</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; color:#202122; background-color:#ffffff; vertical-align:sub;\">2</span>=</p></body></html>", None))
        self.le_Lamda_d_2.setText(QCoreApplication.translate("mainWindow", u"2.19", None))
        self.lb_X_2_shtrih.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>X'<span style=\" vertical-align:sub;\">2</span> =</p></body></html>", None))
        self.le_X_2_shtrih.setText(QCoreApplication.translate("mainWindow", u"2.03", None))
        self.lb_x_1_2_p.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u0445<span style=\" vertical-align:sub;\">12\u0440</span> =</p></body></html>", None))
        self.le_x_1_2_p.setText(QCoreApplication.translate("mainWindow", u"91.84", None))
        self.lb_c_1_p.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u0441<span style=\" vertical-align:sub;\">1\u0440</span> =</p></body></html>", None))
        self.le_c_1_p.setText(QCoreApplication.translate("mainWindow", u"1.02", None))
        self.lb_X_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u0425<span style=\" vertical-align:sub;\">1</span> =</p></body></html>", None))
        self.le_X_1.setText(QCoreApplication.translate("mainWindow", u"1.89", None))
        self.lb_h_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">1 </span>=</p></body></html>", None))
        self.le_h_1.setText(QCoreApplication.translate("mainWindow", u"23.17", None))
        self.lb_q_c.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>q<span style=\" vertical-align:sub;\">c</span> =</p></body></html>", None))
        self.le_q_c.setText(QCoreApplication.translate("mainWindow", u"184.94", None))
        self.lb_r_c.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>r<span style=\" vertical-align:sub;\">c</span> =</p></body></html>", None))
        self.le_r_c.setText(QCoreApplication.translate("mainWindow", u"38.3", None))
        self.lb_r_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>r<span style=\" vertical-align:sub;\">2</span> =</p></body></html>", None))
        self.le_r_2.setText(QCoreApplication.translate("mainWindow", u"57.3", None))
        self.lb_Lamda_p_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; font-weight:700; color:#202122; background-color:#ffffff;\">\u03bb</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; color:#202122; background-color:#ffffff; vertical-align:sub;\">p2</span>=</p></body></html>", None))
        self.le_Lamda_p_2.setText(QCoreApplication.translate("mainWindow", u"2.42", None))
        self.lb_Lamda_l_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; font-weight:700; color:#202122; background-color:#ffffff;\">\u03bb</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; font-weight:700; color:#202122; background-color:#ffffff; vertical-align:sub;\">\u043b</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; color:#202122; background-color:#ffffff; vertical-align:sub;\">2</span>=</p></body></html>", None))
        self.le_Lamda_l_2.setText(QCoreApplication.translate("mainWindow", u"0.678", None))
        self.bt_calculate_table2.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.bt_check_table_2.setText(QCoreApplication.translate("mainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430", None))
        self.bt_export_xl_table_2.setText(QCoreApplication.translate("mainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0432 \u044d\u043a\u0441\u0435\u043b\u044c", None))
        self.lb_error_2.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("mainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 2", None))
        self.bt_check_table_3.setText(QCoreApplication.translate("mainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430", None))
        self.bt_calculate_table3.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.bt_show_chart_table3.setText(QCoreApplication.translate("mainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.bt_export_xl_table_3.setText(QCoreApplication.translate("mainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0432 \u044d\u043a\u0441\u0435\u043b\u044c", None))
        ___qtablewidgetitem153 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem153.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0447\u0451\u0442\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0443\u043b\u0430", None));
        ___qtablewidgetitem154 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem154.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440\u043d\u043e\u0441\u0442\u044c", None));
        ___qtablewidgetitem155 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem155.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043a\u043e\u043b\u044c\u0436\u0435\u043d\u0438\u0435 s", None));
        ___qtablewidgetitem156 = self.tableWidget_3.horizontalHeaderItem(7)
        ___qtablewidgetitem156.setText(QCoreApplication.translate("mainWindow", u"s \u043a\u0440", None));
        ___qtablewidgetitem157 = self.tableWidget_3.verticalHeaderItem(1)
        ___qtablewidgetitem157.setText(QCoreApplication.translate("mainWindow", u"1", None));
        ___qtablewidgetitem158 = self.tableWidget_3.verticalHeaderItem(2)
        ___qtablewidgetitem158.setText(QCoreApplication.translate("mainWindow", u"2", None));
        ___qtablewidgetitem159 = self.tableWidget_3.verticalHeaderItem(3)
        ___qtablewidgetitem159.setText(QCoreApplication.translate("mainWindow", u"3", None));
        ___qtablewidgetitem160 = self.tableWidget_3.verticalHeaderItem(4)
        ___qtablewidgetitem160.setText(QCoreApplication.translate("mainWindow", u"4", None));
        ___qtablewidgetitem161 = self.tableWidget_3.verticalHeaderItem(5)
        ___qtablewidgetitem161.setText(QCoreApplication.translate("mainWindow", u"5", None));
        ___qtablewidgetitem162 = self.tableWidget_3.verticalHeaderItem(6)
        ___qtablewidgetitem162.setText(QCoreApplication.translate("mainWindow", u"6", None));
        ___qtablewidgetitem163 = self.tableWidget_3.verticalHeaderItem(7)
        ___qtablewidgetitem163.setText(QCoreApplication.translate("mainWindow", u"7", None));
        ___qtablewidgetitem164 = self.tableWidget_3.verticalHeaderItem(8)
        ___qtablewidgetitem164.setText(QCoreApplication.translate("mainWindow", u"8", None));
        ___qtablewidgetitem165 = self.tableWidget_3.verticalHeaderItem(9)
        ___qtablewidgetitem165.setText(QCoreApplication.translate("mainWindow", u"9", None));
        ___qtablewidgetitem166 = self.tableWidget_3.verticalHeaderItem(10)
        ___qtablewidgetitem166.setText(QCoreApplication.translate("mainWindow", u"10", None));
        ___qtablewidgetitem167 = self.tableWidget_3.verticalHeaderItem(11)
        ___qtablewidgetitem167.setText(QCoreApplication.translate("mainWindow", u"11", None));
        ___qtablewidgetitem168 = self.tableWidget_3.verticalHeaderItem(12)
        ___qtablewidgetitem168.setText(QCoreApplication.translate("mainWindow", u"12", None));
        ___qtablewidgetitem169 = self.tableWidget_3.verticalHeaderItem(13)
        ___qtablewidgetitem169.setText(QCoreApplication.translate("mainWindow", u"13", None));
        ___qtablewidgetitem170 = self.tableWidget_3.verticalHeaderItem(14)
        ___qtablewidgetitem170.setText(QCoreApplication.translate("mainWindow", u"14", None));
        ___qtablewidgetitem171 = self.tableWidget_3.verticalHeaderItem(15)
        ___qtablewidgetitem171.setText(QCoreApplication.translate("mainWindow", u"15", None));
        ___qtablewidgetitem172 = self.tableWidget_3.verticalHeaderItem(16)
        ___qtablewidgetitem172.setText(QCoreApplication.translate("mainWindow", u"16", None));
        ___qtablewidgetitem173 = self.tableWidget_3.verticalHeaderItem(17)
        ___qtablewidgetitem173.setText(QCoreApplication.translate("mainWindow", u"17", None));
        ___qtablewidgetitem174 = self.tableWidget_3.verticalHeaderItem(18)
        ___qtablewidgetitem174.setText(QCoreApplication.translate("mainWindow", u"18", None));
        ___qtablewidgetitem175 = self.tableWidget_3.verticalHeaderItem(19)
        ___qtablewidgetitem175.setText(QCoreApplication.translate("mainWindow", u"19", None));
        ___qtablewidgetitem176 = self.tableWidget_3.verticalHeaderItem(20)
        ___qtablewidgetitem176.setText(QCoreApplication.translate("mainWindow", u"20", None));

        __sortingEnabled2 = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        ___qtablewidgetitem177 = self.tableWidget_3.item(0, 2)
        ___qtablewidgetitem177.setText(QCoreApplication.translate("mainWindow", u"1", None));
        ___qtablewidgetitem178 = self.tableWidget_3.item(0, 3)
        ___qtablewidgetitem178.setText(QCoreApplication.translate("mainWindow", u"0.8", None));
        ___qtablewidgetitem179 = self.tableWidget_3.item(0, 4)
        ___qtablewidgetitem179.setText(QCoreApplication.translate("mainWindow", u"0.5", None));
        ___qtablewidgetitem180 = self.tableWidget_3.item(0, 5)
        ___qtablewidgetitem180.setText(QCoreApplication.translate("mainWindow", u"0.2", None));
        ___qtablewidgetitem181 = self.tableWidget_3.item(0, 6)
        ___qtablewidgetitem181.setText(QCoreApplication.translate("mainWindow", u"0.1", None));
        ___qtablewidgetitem182 = self.tableWidget_3.item(0, 7)
        ___qtablewidgetitem182.setText(QCoreApplication.translate("mainWindow", u"0.19", None));
        ___qtablewidgetitem183 = self.tableWidget_3.item(1, 0)
        ___qtablewidgetitem183.setText(QCoreApplication.translate("mainWindow", u"k_\u043d\u0430\u0441", None));
        ___qtablewidgetitem184 = self.tableWidget_3.item(1, 1)
        ___qtablewidgetitem184.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem185 = self.tableWidget_3.item(1, 2)
        ___qtablewidgetitem185.setText(QCoreApplication.translate("mainWindow", u"1.4", None));
        ___qtablewidgetitem186 = self.tableWidget_3.item(2, 0)
        ___qtablewidgetitem186.setText(QCoreApplication.translate("mainWindow", u"F\u043f.\u0441\u0440=0,7*((I_1*k_\u043d\u0430\u0441*u_\u043f)/a)(k'_beta+k_y1*k_\u043e\u04311*(Z1/Z2))", None));
        ___qtablewidgetitem187 = self.tableWidget_3.item(2, 1)
        ___qtablewidgetitem187.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem188 = self.tableWidget_3.item(2, 2)
        ___qtablewidgetitem188.setText(QCoreApplication.translate("mainWindow", u"4587.33", None));
        ___qtablewidgetitem189 = self.tableWidget_3.item(3, 0)
        ___qtablewidgetitem189.setText(QCoreApplication.translate("mainWindow", u"\u0412_\u0444\u0431 = F\u043f.\u0441\u0440 * 10^(-6)/(1,6\u03b4*\u0421_N)", None));
        ___qtablewidgetitem190 = self.tableWidget_3.item(3, 1)
        ___qtablewidgetitem190.setText(QCoreApplication.translate("mainWindow", u"\u0422\u043b", None));
        ___qtablewidgetitem191 = self.tableWidget_3.item(3, 2)
        ___qtablewidgetitem191.setText(QCoreApplication.translate("mainWindow", u"5.114", None));
        ___qtablewidgetitem192 = self.tableWidget_3.item(4, 0)
        ___qtablewidgetitem192.setText(QCoreApplication.translate("mainWindow", u"k_\u03b4 = f(\u0412_\u0444\u0431)", None));
        ___qtablewidgetitem193 = self.tableWidget_3.item(4, 1)
        ___qtablewidgetitem193.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem194 = self.tableWidget_3.item(4, 2)
        ___qtablewidgetitem194.setText(QCoreApplication.translate("mainWindow", u"0.481", None));
        ___qtablewidgetitem195 = self.tableWidget_3.item(5, 0)
        ___qtablewidgetitem195.setText(QCoreApplication.translate("mainWindow", u"\u0441_1 = (t_z1-b_\u04481)(1-k_\u03b4)", None));
        ___qtablewidgetitem196 = self.tableWidget_3.item(5, 1)
        ___qtablewidgetitem196.setText(QCoreApplication.translate("mainWindow", u"\u043c\u043c", None));
        ___qtablewidgetitem197 = self.tableWidget_3.item(5, 2)
        ___qtablewidgetitem197.setText(QCoreApplication.translate("mainWindow", u"5.114", None));
        ___qtablewidgetitem198 = self.tableWidget_3.item(6, 0)
        ___qtablewidgetitem198.setText(QCoreApplication.translate("mainWindow", u"\u03bb_\u043f1\u043d\u0430\u0441 = \u03bb\u043f1 - \u0394\u03bb_\u043f1\u043d\u0430\u0441", None));
        ___qtablewidgetitem199 = self.tableWidget_3.item(6, 1)
        ___qtablewidgetitem199.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem200 = self.tableWidget_3.item(6, 2)
        ___qtablewidgetitem200.setText(QCoreApplication.translate("mainWindow", u"1.26", None));
        ___qtablewidgetitem201 = self.tableWidget_3.item(7, 0)
        ___qtablewidgetitem201.setText(QCoreApplication.translate("mainWindow", u"\u03bb_\u04341\u043d\u0430\u0441 = k_\u03b4*\u03bb\u04341", None));
        ___qtablewidgetitem202 = self.tableWidget_3.item(7, 1)
        ___qtablewidgetitem202.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem203 = self.tableWidget_3.item(7, 2)
        ___qtablewidgetitem203.setText(QCoreApplication.translate("mainWindow", u"0.658", None));
        ___qtablewidgetitem204 = self.tableWidget_3.item(8, 0)
        ___qtablewidgetitem204.setText(QCoreApplication.translate("mainWindow", u"\u0445_1\u043d\u0430\u0441 = \u04451*\u03a3\u03bb_1\u043d\u0430\u0441/\u03a3\u03bb_1", None));
        ___qtablewidgetitem205 = self.tableWidget_3.item(8, 1)
        ___qtablewidgetitem205.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem206 = self.tableWidget_3.item(8, 2)
        ___qtablewidgetitem206.setText(QCoreApplication.translate("mainWindow", u"1.176", None));
        ___qtablewidgetitem207 = self.tableWidget_3.item(9, 0)
        ___qtablewidgetitem207.setText(QCoreApplication.translate("mainWindow", u"c_1_\u043f = 1 + x_1\u043d\u0430\u0441/ x_12\u043f", None));
        ___qtablewidgetitem208 = self.tableWidget_3.item(9, 1)
        ___qtablewidgetitem208.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem209 = self.tableWidget_3.item(9, 2)
        ___qtablewidgetitem209.setText(QCoreApplication.translate("mainWindow", u"1.013", None));
        ___qtablewidgetitem210 = self.tableWidget_3.item(10, 0)
        ___qtablewidgetitem210.setText(QCoreApplication.translate("mainWindow", u"\u0441_2 = (t_z2-b_\u04482)(1-k_\u03b4)", None));
        ___qtablewidgetitem211 = self.tableWidget_3.item(10, 1)
        ___qtablewidgetitem211.setText(QCoreApplication.translate("mainWindow", u"\u043c\u043c", None));
        ___qtablewidgetitem212 = self.tableWidget_3.item(10, 2)
        ___qtablewidgetitem212.setText(QCoreApplication.translate("mainWindow", u"9.098", None));
        ___qtablewidgetitem213 = self.tableWidget_3.item(11, 0)
        ___qtablewidgetitem213.setText(QCoreApplication.translate("mainWindow", u"\u03bb_\u043f2\u03be\u043d\u0430\u0441 = \u03bb_\u043f2\u03be - \u0394\u03bb_\u043f2\u043d\u0430\u0441", None));
        ___qtablewidgetitem214 = self.tableWidget_3.item(11, 1)
        ___qtablewidgetitem214.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem215 = self.tableWidget_3.item(11, 2)
        ___qtablewidgetitem215.setText(QCoreApplication.translate("mainWindow", u"1.729", None));
        ___qtablewidgetitem216 = self.tableWidget_3.item(12, 0)
        ___qtablewidgetitem216.setText(QCoreApplication.translate("mainWindow", u"\u03bb_\u04342\u043d\u0430\u0441 = k_\u03b4*\u03bb\u04342", None));
        ___qtablewidgetitem217 = self.tableWidget_3.item(12, 1)
        ___qtablewidgetitem217.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem218 = self.tableWidget_3.item(12, 2)
        ___qtablewidgetitem218.setText(QCoreApplication.translate("mainWindow", u"1.127", None));
        ___qtablewidgetitem219 = self.tableWidget_3.item(13, 0)
        ___qtablewidgetitem219.setText(QCoreApplication.translate("mainWindow", u"\u0445'_2\u03be\u043d\u0430\u0441 = x'2*\u03a3\u03bb_2\u03be\u043d\u0430\u0441/\u03a3\u03bb_2", None));
        ___qtablewidgetitem220 = self.tableWidget_3.item(13, 1)
        ___qtablewidgetitem220.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem221 = self.tableWidget_3.item(13, 2)
        ___qtablewidgetitem221.setText(QCoreApplication.translate("mainWindow", u"1.470", None));
        ___qtablewidgetitem222 = self.tableWidget_3.item(14, 0)
        ___qtablewidgetitem222.setText(QCoreApplication.translate("mainWindow", u"R\u043f.\u043d\u0430\u0441 = r_1 + c_1\u043f.\u043d\u0430\u0441 * r'_2\u03be / s", None));
        ___qtablewidgetitem223 = self.tableWidget_3.item(14, 1)
        ___qtablewidgetitem223.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem224 = self.tableWidget_3.item(14, 2)
        ___qtablewidgetitem224.setText(QCoreApplication.translate("mainWindow", u"1.157", None));
        ___qtablewidgetitem225 = self.tableWidget_3.item(15, 0)
        ___qtablewidgetitem225.setText(QCoreApplication.translate("mainWindow", u"\u0425\u043f.\u043d\u0430\u0441 = x_1\u043d\u0430\u0441 + c_1\u043f.\u043d\u0430\u0441 * \u0445'_2\u03be\u043d\u0430\u0441", None));
        ___qtablewidgetitem226 = self.tableWidget_3.item(15, 1)
        ___qtablewidgetitem226.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem227 = self.tableWidget_3.item(15, 2)
        ___qtablewidgetitem227.setText(QCoreApplication.translate("mainWindow", u"2.666", None));
        ___qtablewidgetitem228 = self.tableWidget_3.item(16, 0)
        ___qtablewidgetitem228.setText(QCoreApplication.translate("mainWindow", u"I'_2\u043d\u0430\u0441 = U/\u221a(R\u043f.\u043d\u0430\u0441^2+\u0425\u043f.\u043d\u0430\u0441^2)", None));
        ___qtablewidgetitem229 = self.tableWidget_3.item(16, 1)
        ___qtablewidgetitem229.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem230 = self.tableWidget_3.item(16, 2)
        ___qtablewidgetitem230.setText(QCoreApplication.translate("mainWindow", u"130.765", None));
        ___qtablewidgetitem231 = self.tableWidget_3.item(17, 0)
        ___qtablewidgetitem231.setText(QCoreApplication.translate("mainWindow", u"I_1\u043d\u0430\u0441=I'_2\u043d\u0430\u0441*((\u221a(R\u043f.\u043d\u0430\u0441^2+(\u0425\u043f.\u043d\u0430\u0441+\u0445_12\u043f)^2))/(\u0441_1\u043f.\u043d\u0430\u0441*\u0445_12\u043f))", None));
        ___qtablewidgetitem232 = self.tableWidget_3.item(17, 1)
        ___qtablewidgetitem232.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem233 = self.tableWidget_3.item(17, 2)
        ___qtablewidgetitem233.setText(QCoreApplication.translate("mainWindow", u"132.983", None));
        ___qtablewidgetitem234 = self.tableWidget_3.item(18, 0)
        ___qtablewidgetitem234.setText(QCoreApplication.translate("mainWindow", u"k'\u043d\u0430\u0441 = I_1\u043d\u0430\u0441/I_1\u043f", None));
        ___qtablewidgetitem235 = self.tableWidget_3.item(18, 1)
        ___qtablewidgetitem235.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem236 = self.tableWidget_3.item(18, 2)
        ___qtablewidgetitem236.setText(QCoreApplication.translate("mainWindow", u"1.315", None));
        ___qtablewidgetitem237 = self.tableWidget_3.item(19, 0)
        ___qtablewidgetitem237.setText(QCoreApplication.translate("mainWindow", u"I_i= I_1\u043d\u0430\u0441 / I_1\u043d\u043e\u043c", None));
        ___qtablewidgetitem238 = self.tableWidget_3.item(19, 1)
        ___qtablewidgetitem238.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem239 = self.tableWidget_3.item(19, 2)
        ___qtablewidgetitem239.setText(QCoreApplication.translate("mainWindow", u"5.582", None));
        ___qtablewidgetitem240 = self.tableWidget_3.item(20, 0)
        ___qtablewidgetitem240.setText(QCoreApplication.translate("mainWindow", u"\u041c*", None));
        ___qtablewidgetitem241 = self.tableWidget_3.item(20, 1)
        ___qtablewidgetitem241.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem242 = self.tableWidget_3.item(20, 2)
        ___qtablewidgetitem242.setText(QCoreApplication.translate("mainWindow", u"1.101", None));
        self.tableWidget_3.setSortingEnabled(__sortingEnabled2)

        self.le_C_N.setText(QCoreApplication.translate("mainWindow", u"0.975", None))
        self.lb_k_y_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>k<span style=\" vertical-align:sub;\">y1 </span>=</p></body></html>", None))
        self.le_k_y_1.setText(QCoreApplication.translate("mainWindow", u"1", None))
        self.lb_C_N.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u0421<span style=\" vertical-align:sub;\">N </span>=</p></body></html>", None))
        self.lb_u_p.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>u<span style=\" vertical-align:sub;\">p</span> =</p></body></html>", None))
        self.le_u_p.setText(QCoreApplication.translate("mainWindow", u"20", None))
        self.lb_k_ob.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>k<span style=\" vertical-align:sub;\">\u043e\u0431</span> =</p></body></html>", None))
        self.le_k_ob.setText(QCoreApplication.translate("mainWindow", u"0.91", None))
        self.lb_Z_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>Z<span style=\" vertical-align:sub;\">1 </span>=</p></body></html>", None))
        self.le_Z_1.setText(QCoreApplication.translate("mainWindow", u"48", None))
        self.lb_Z_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>Z<span style=\" vertical-align:sub;\">2</span> =</p></body></html>", None))
        self.le_Z_2.setText(QCoreApplication.translate("mainWindow", u"38", None))
        self.lb_sigma.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-weight:700; color:#202122; background-color:#ffffff;\">\u03b4 </span>=</p></body></html>", None))
        self.le_sigma.setText(QCoreApplication.translate("mainWindow", u"0.55", None))
        self.lb_t_z_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>t<span style=\" vertical-align:sub;\">z1</span> =</p></body></html>", None))
        self.le_t_z_1.setText(QCoreApplication.translate("mainWindow", u"0.0136", None))
        self.lb_b_sh.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>b<span style=\" vertical-align:sub;\">\u0448</span> =</p></body></html>", None))
        self.le_b_sh.setText(QCoreApplication.translate("mainWindow", u"3.7", None))
        self.lb_h_sh_r.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">\u0448 \u0440\u043e\u0442.</span> =</p></body></html>", None))
        self.le_h_sh_r.setText(QCoreApplication.translate("mainWindow", u"0.7", None))
        self.lb_Lamda_p_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; color:#202122; background-color:#ffffff;\">\u03bb</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; color:#202122; background-color:#ffffff; vertical-align:sub;\">p1</span>=</p></body></html>", None))
        self.le_Lamda_p_1.setText(QCoreApplication.translate("mainWindow", u"1.99", None))
        self.lb_Lamda_d_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; color:#202122; background-color:#ffffff;\">\u03bb</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; color:#202122; background-color:#ffffff; vertical-align:sub;\">\u04341</span>=</p></body></html>", None))
        self.le_Lamda_d_1.setText(QCoreApplication.translate("mainWindow", u"2.06", None))
        self.lb_Lamda_l_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; color:#202122; background-color:#ffffff;\">\u03bb</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; color:#202122; background-color:#ffffff; vertical-align:sub;\">\u043b1</span>=</p></body></html>", None))
        self.le_Lamda_l_1.setText(QCoreApplication.translate("mainWindow", u"1.1", None))
        self.lb_t_z_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>t<span style=\" vertical-align:sub;\">z2</span> =</p></body></html>", None))
        self.le_t_z_2.setText(QCoreApplication.translate("mainWindow", u"0.0171", None))
        self.lb_r_2_Ksi_shtrih.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>r'<span style=\" vertical-align:sub;\">2\u03be </span>=</p></body></html>", None))
        self.le_r_2_Ksi_shtrih.setText(QCoreApplication.translate("mainWindow", u"0.521", None))
        self.lb_I_1_p.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>I<span style=\" vertical-align:sub;\">1p</span> =</p></body></html>", None))
        self.le_I_1_p.setText(QCoreApplication.translate("mainWindow", u"103.993", None))
        self.lb_I_1_nom.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>I<span style=\" vertical-align:sub;\">1\u043d\u043e\u043c</span> =</p></body></html>", None))
        self.le_I_1_nom.setText(QCoreApplication.translate("mainWindow", u"23.715", None))
        self.lb_h_k.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">k</span> =</p></body></html>", None))
        self.le_h_k.setText(QCoreApplication.translate("mainWindow", u"3.43", None))
        self.lb_Lamda_p_2_Ksi.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u03bb<span style=\" vertical-align:sub;\">\u043f2\u03be </span>=</p></body></html>", None))
        self.le_Lamda_p_2_Ksi.setText(QCoreApplication.translate("mainWindow", u"2.2272", None))
        self.lb_K_R.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>K<span style=\" vertical-align:sub;\">R</span> =</p></body></html>", None))
        self.le_K_R.setText(QCoreApplication.translate("mainWindow", u"1.372", None))
        self.lb_error_3.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("mainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 3", None))
        self.lb_D.setText(QCoreApplication.translate("mainWindow", u"D=", None))
        self.le_D.setText(QCoreApplication.translate("mainWindow", u"0.208", None))
        self.lb_P_st_main.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>P<span style=\" vertical-align:sub;\">\u0441\u0442. \u043e\u0441\u043d</span><span style=\" vertical-align:super;\">=</span></p></body></html>", None))
        self.le_P_st_main.setText(QCoreApplication.translate("mainWindow", u"371.39", None))
        self.lb_l_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>l<span style=\" vertical-align:sub;\">1</span><span style=\" vertical-align:super;\">=</span></p></body></html>", None))
        self.le_l_1.setText(QCoreApplication.translate("mainWindow", u"0.145", None))
        self.lb_a_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>a<span style=\" vertical-align:sub;\">1</span><span style=\" vertical-align:super;\">=</span></p></body></html>", None))
        self.le_a_1.setText(QCoreApplication.translate("mainWindow", u"113", None))
        self.l_delta_nu_pov_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u0394<span style=\" font-size:20pt;\">\u03bd</span><span style=\" font-size:16pt; vertical-align:sub;\">\u043f\u043e\u04321</span> =</p></body></html>", None))
        self.lb_delta_nu_pov_1.setText("")
        self.l_delta_nu_iz_p_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u0394<span style=\" font-size:20pt;\">\u03bd</span><span style=\" font-size:16pt; vertical-align:sub;\">\u0438\u0437.\u043f</span><span style=\" font-size:16pt; vertical-align:sub;\">1</span> =</p></body></html>", None))
        self.lb_delta_nu_iz_p_1.setText("")
        self.l_delta_nu_iz_l_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u0394<span style=\" font-size:20pt;\">\u03bd</span><span style=\" font-size:16pt; vertical-align:sub;\">\u0438\u0437.\u043b1</span> =</p></body></html>", None))
        self.lb_delta_nu_iz_l_1.setText("")
        self.l_delta_nu_pov_l_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u0394<span style=\" font-size:20pt;\">\u03bd</span><span style=\" font-size:16pt; vertical-align:sub;\">\u043f\u043e\u0432.\u043b1</span> =</p></body></html>", None))
        self.lb_delta_nu_pov_l_1.setText("")
        self.l_Q_v.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u0394<span style=\" font-size:20pt;\">\u03bd</span><span style=\" font-size:16pt; vertical-align:sub;\">1</span><span style=\" font-size:22pt; vertical-align:super;\">'</span> =</p></body></html>", None))
        self.lb_delta_nu_1_shtrih.setText("")
        self.l_delta_nu_1_shtrih.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u0394<span style=\" font-size:20pt;\">\u03bd</span><span style=\" font-size:16pt; vertical-align:sub;\">\u0432</span> =</p></body></html>", None))
        self.lb_delta_gamma_v.setText("")
        self.l_teta_v_shtrih.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u0394<span style=\" font-size:20pt;\">\u03bd</span><span style=\" font-size:16pt; vertical-align:sub;\">1</span> =</p></body></html>", None))
        self.lb_delta_nu_1.setText("")
        self.l_delta_nu_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>Q<span style=\" font-size:16pt; vertical-align:sub;\">\u0432</span>= </p></body></html>", None))
        self.lb_Q_v.setText("")
        self.l_delta_gamma_v.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:20px; font-weight:500; color:#040c28; background-color:rgba(80,151,255,0.176471);\">\u03b8</span><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; font-weight:500; color:#040c28; background-color:rgba(80,151,255,0.176471); vertical-align:sub;\">\u0432</span><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:24pt; font-weight:500; color:#040c28; background-color:rgba(80,151,255,0.176471); vertical-align:super;\">'</span> =</p></body></html>", None))
        self.lb_teta_v_shtrih.setText("")
        self.lb_h_pk.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">\u043f\u043a</span><span style=\" vertical-align:super;\">=</span></p></body></html>", None))
        self.le_h_pk.setText(QCoreApplication.translate("mainWindow", u"26.03", None))
        self.lb_b_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>b<span style=\" vertical-align:sub;\">1</span><span style=\" vertical-align:super;\">=</span></p></body></html>", None))
        self.le_b_1.setText(QCoreApplication.translate("mainWindow", u"7.71", None))
        self.lb_b_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>b<span style=\" vertical-align:sub;\">2</span><span style=\" vertical-align:super;\">=</span></p></body></html>", None))
        self.le_b_2.setText(QCoreApplication.translate("mainWindow", u"11.11", None))
        self.lb_b_iz_p_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>b<span style=\" vertical-align:sub;\">\u0438\u0437. \u043f1</span><span style=\" vertical-align:super;\">=</span></p></body></html>", None))
        self.le_b_iz_p_1.setText(QCoreApplication.translate("mainWindow", u"0.4", None))
        self.lb_lambda_ekv_shtrih.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; color:#202122; background-color:#ffffff;\">\u03bb</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; color:#202122; background-color:#ffffff;\">'</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; color:#202122; background-color:#ffffff; vertical-align:sub;\">\u044d\u043a\u0432</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; color:#202122; background-color:#ffffff; vertical-align:super;\">=</span></p></body></html>", None))
        self.le_lambda_ekv_shtrih.setText(QCoreApplication.translate("mainWindow", u"1.2", None))
        self.lb_l_l_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>l<span style=\" vertical-align:sub;\">\u043b1</span><span style=\" vertical-align:super;\">=</span></p></body></html>", None))
        self.le_l_l_1.setText(QCoreApplication.translate("mainWindow", u"0.222", None))
        self.lb_b_iz_l_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>b<span style=\" vertical-align:sub;\">\u0438\u0437. \u043b1</span><span style=\" vertical-align:super;\">=</span></p></body></html>", None))
        self.le_b_iz_l_1.setText(QCoreApplication.translate("mainWindow", u"0.05", None))
        self.lb_h_p_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">\u043f1</span><span style=\" vertical-align:super;\">=</span></p></body></html>", None))
        self.le_h_p_1.setText(QCoreApplication.translate("mainWindow", u"26.03", None))
        self.lb_l_vbl.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>l<span style=\" vertical-align:sub;\">\u0432\u044b\u043b</span><span style=\" vertical-align:super;\">=</span></p></body></html>", None))
        self.le_l_vbl.setText(QCoreApplication.translate("mainWindow", u"0.0723", None))
        self.lb_l_avg_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>l<span style=\" vertical-align:sub;\">\u0441\u04401</span><span style=\" vertical-align:super;\">=</span></p></body></html>", None))
        self.le_l_avg_1.setText(QCoreApplication.translate("mainWindow", u"0.734", None))
        self.lb_a_v.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>a<span style=\" vertical-align:sub;\">\u0432</span><span style=\" vertical-align:super;\">=</span></p></body></html>", None))
        self.le_a_v.setText(QCoreApplication.translate("mainWindow", u"22.5", None))
        self.lb_D_a.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>D<span style=\" vertical-align:sub;\">a</span><span style=\" vertical-align:super;\">=</span></p></body></html>", None))
        self.le_D_a.setText(QCoreApplication.translate("mainWindow", u"0.32", None))
        self.lb_s_kor.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>s<span style=\" vertical-align:sub;\">\u043a\u043e\u0440</span><span style=\" vertical-align:super;\">=</span></p></body></html>", None))
        self.le_s_kor.setText(QCoreApplication.translate("mainWindow", u"1.12", None))
        self.bt_thermal_calc.setText(QCoreApplication.translate("mainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0441\u0442\u0438 \u0442\u0435\u043f\u043b\u043e\u0432\u043e\u0439 \u0440\u0430\u0441\u0447\u0451\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tb_thermal_calc), QCoreApplication.translate("mainWindow", u"\u0422\u0435\u043f\u043b\u043e\u0432\u043e\u0439 \u0440\u0430\u0441\u0447\u0451\u0442", None))
        self.lb_valueOfError.setText(QCoreApplication.translate("mainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u0438", None))
#if QT_CONFIG(whatsthis)
        self.sl_ValueOfError.setWhatsThis(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u0421\u041b\u0410\u0419\u0414\u0415\u0420</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tb_settings), QCoreApplication.translate("mainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043f\u0440\u0435\u0434\u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0430 \u0434\u043b\u044f \u043e\u0431\u043b\u0435\u0433\u0447\u0435\u043d\u0438\u044f \u043f\u043e\u0434\u0441\u0447\u0451\u0442\u043e\u0432 \u043f\u0440\u0438 \u043f\u0440\u043e\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0438 \u0430\u0441\u0438\u043d\u0445\u0440\u043e\u043d\u043d\u043e\u0433\u043e \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f \u0441 \u043a\u043e\u0440\u043e\u0442\u043a\u043e\u0437\u0430\u043c\u043a\u043d\u0443\u0442\u044b\u043c \u0440\u043e\u0442\u043e\u0440\u043e\u043c.</span><br/></p><p><span style=\" font-size:16pt; font-style:italic;\">\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e:</span></p><p><span style=\" font-size:16pt; font-style:italic;\">1) \u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0443 \u043d\u0435\u043e\u0431"
                        "\u0445\u043e\u0434\u0438\u043c\u043e \u043f\u043e\u0434\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u043b\u044f \u043d\u043e\u043c\u0438\u043d\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u0430.</span></p><p><span style=\" font-size:16pt; font-style:italic;\">2) \u0412\u0432\u0435\u0441\u0442\u0438 \u0432\u043e \u0432\u043a\u043b\u0430\u0434\u043a\u0435 \u00ab\u0412\u0432\u043e\u0434 \u0434\u0430\u043d\u043d\u044b\u0445\u00bb \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0437\u0430\u0434\u0430\u043d\u0438\u044f \u0438 \u043d\u0430\u0436\u0430\u0442\u044c \u043a\u043d\u043e\u043f\u043a\u0443 \u00ab\u0412\u0432\u0435\u0441\u0442\u0438 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f\u00bb.</span></p><p><span style=\" font-size:16pt; font-style:italic;\">3) \u0414\u0430\u043b\u0435\u0435 \u0432\u043e \u0432\u043a\u043b\u0430\u0434\u043a\u0435"
                        " \u00ab\u0422\u0430\u0431\u043b\u0438\u0446\u0430 1\u00bb \u0432\u0432\u0435\u0441\u0442\u0438 \u043f\u043e\u0434\u0441\u0447\u0438\u0442\u0430\u043d\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u043b\u044f \u043d\u043e\u043c\u0438\u043d\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u0430.</span></p><p><span style=\" font-size:16pt; font-style:italic;\">4) \u041f\u043e\u0441\u043b\u0435 \u0432\u0432\u043e\u0434\u0430 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u043d\u043e\u043c\u0438\u043d\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u0430 \u043d\u0430\u0436\u0430\u0442\u044c \u043a\u043d\u043e\u043f\u043a\u0443 \u00ab\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430\u00bb.</span></p><p><span style=\" font-size:16pt; font-style:italic;\">5) \u041f\u0440\u0438 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0435 \u043f\u043e\u0434\u0441\u0447\u0451\u0442\u043e\u0432 \u0441 \u043d\u043e\u043c"
                        "\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u043c \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u043e\u043c \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0443 \u0431\u0443\u0434\u0443\u0442 \u043e\u043a\u0440\u0430\u0448\u0435\u043d\u044b \u0437\u0435\u043b\u0451\u043d\u044b\u043c \u0446\u0432\u0435\u0442\u043e\u043c \u043f\u043e\u043b\u044f \u0441 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u043c\u0438 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f\u043c\u0438, \u0432 \u043f\u0440\u043e\u0442\u0438\u0432\u043d\u043e\u043c \u0441\u043b\u0443\u0447\u0430\u0435 \u043f\u043e\u043b\u044f \u0431\u0443\u0434\u0443\u0442 \u043a\u0440\u0430\u0441\u043d\u043e\u0433\u043e \u0446\u0432\u0435\u0442\u0430.</span></p><p><span style=\" font-size:16pt; font-style:italic;\">6) \u041f\u0440\u0438 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e\u043c \u0432\u0432\u043e\u0434\u0435 \u0432\u0441\u0435\u0445 \u043f\u043e\u043b\u0435\u0439 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0443 \u0431\u0443\u0434\u0435\u0442 "
                        "\u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0430 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0432\u0432\u043e\u0434\u0430 \u0434\u0430\u043d\u043d\u044b\u0445, \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0445 \u0434\u043b\u044f \u0440\u0430\u0441\u0447\u0451\u0442\u0430 \u0432\u0441\u0435\u0439 \u0442\u0430\u0431\u043b\u0438\u0446\u044b.</span></p><p><span style=\" font-size:16pt; font-style:italic;\">7) \u041f\u0440\u0438 \u043f\u043e\u043b\u043d\u043e\u043c \u0440\u0430\u0441\u0447\u0451\u0442\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u044b 1 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0443 \u0431\u0443\u0434\u0435\u0442 \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0430 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0432\u044b\u0432\u043e\u0434\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0430 \u0440\u0430\u0431\u043e\u0447\u0438\u0445 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438"
                        "\u0441\u0442\u0438\u043a \u0430.\u0434. </span></p><p><span style=\" font-size:16pt; font-style:italic;\">8) \u0410\u043d\u0430\u043b\u043e\u0433\u0438\u0447\u043d\u043e \u0437\u0430\u043f\u043e\u043b\u043d\u044f\u044e\u0442\u0441\u044f \u0442\u0430\u0431\u043b\u0438\u0446\u0430 2 \u0438 \u0442\u0430\u0431\u043b\u0438\u0446\u0430 3 \u0434\u043b\u044f \u0441\u043a\u043e\u043b\u044c\u0436\u0435\u043d\u0438\u044f, \u0440\u0430\u0432\u043d\u043e\u0433\u043e 1.</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("mainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
    # retranslateUi

