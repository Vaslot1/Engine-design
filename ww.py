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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
                               QLabel, QLineEdit, QPushButton, QSizePolicy,
                               QTabWidget, QTableWidget, QTableWidgetItem, QWidget)


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1407, 929)
        self.tabWidget = QTabWidget(mainWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 10, 1411, 871))
        font = QFont()
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.Power = QLabel(self.tab_4)
        self.Power.setObjectName(u"Power")
        self.Power.setGeometry(QRect(20, 70, 191, 21))
        self.Input = QLabel(self.tab_4)
        self.Input.setObjectName(u"Input")
        self.Input.setGeometry(QRect(20, 40, 111, 21))
        self.Voltage = QLabel(self.tab_4)
        self.Voltage.setObjectName(u"Voltage")
        self.Voltage.setGeometry(QRect(20, 100, 241, 21))
        self.polarity = QLabel(self.tab_4)
        self.polarity.setObjectName(u"polarity")
        self.polarity.setGeometry(QRect(20, 130, 111, 16))
        self.linePower = QLineEdit(self.tab_4)
        self.linePower.setObjectName(u"linePower")
        self.linePower.setGeometry(QRect(300, 70, 113, 22))
        self.lineVoltage = QLineEdit(self.tab_4)
        self.lineVoltage.setObjectName(u"lineVoltage")
        self.lineVoltage.setGeometry(QRect(300, 100, 113, 22))
        self.linePolarity = QLineEdit(self.tab_4)
        self.linePolarity.setObjectName(u"linePolarity")
        self.linePolarity.setGeometry(QRect(300, 130, 113, 22))
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
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
        __qtablewidgetitem29.setFlags(Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFlags(Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable);
        self.tableWidget.setItem(0, 1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFlags(Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable);
        self.tableWidget.setItem(0, 2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFlags(Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable);
        self.tableWidget.setItem(0, 3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFlags(Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable);
        self.tableWidget.setItem(0, 4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFlags(Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable);
        self.tableWidget.setItem(0, 5, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFlags(Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable);
        self.tableWidget.setItem(0, 6, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFlags(Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable);
        self.tableWidget.setItem(0, 7, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget.setItem(0, 8, __qtablewidgetitem37)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font1);
        __qtablewidgetitem38.setFlags(Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem39)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        brush1 = QBrush(QColor(255, 0, 0, 120))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setBackground(brush1);
        __qtablewidgetitem40.setForeground(brush);
        self.tableWidget.setItem(1, 8, __qtablewidgetitem40)
        font2 = QFont()
        font2.setBold(True)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setFont(font2);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setFont(font2);
        self.tableWidget.setItem(3, 0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setFont(font2);
        self.tableWidget.setItem(4, 0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget.setItem(4, 1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setFont(font2);
        self.tableWidget.setItem(5, 0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget.setItem(5, 1, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setFont(font2);
        self.tableWidget.setItem(6, 0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget.setItem(6, 1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setFont(font2);
        self.tableWidget.setItem(7, 0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget.setItem(7, 1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setFont(font2);
        self.tableWidget.setItem(8, 0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget.setItem(8, 1, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setFont(font2);
        self.tableWidget.setItem(9, 0, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget.setItem(9, 1, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setFont(font2);
        self.tableWidget.setItem(10, 0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget.setItem(10, 1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setFont(font2);
        self.tableWidget.setItem(11, 0, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget.setItem(11, 1, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setFont(font2);
        self.tableWidget.setItem(12, 0, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget.setItem(12, 1, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setFont(font2);
        self.tableWidget.setItem(13, 0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget.setItem(13, 1, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setFont(font2);
        self.tableWidget.setItem(14, 0, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableWidget.setItem(14, 1, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setFont(font2);
        self.tableWidget.setItem(15, 0, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableWidget.setItem(15, 1, __qtablewidgetitem68)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Symbol"])
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setKerning(False)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setFont(font3);
        self.tableWidget.setItem(16, 0, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableWidget.setItem(16, 1, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setFont(font2);
        self.tableWidget.setItem(17, 0, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableWidget.setItem(17, 1, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setFont(font2);
        self.tableWidget.setItem(18, 0, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tableWidget.setItem(18, 1, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setFont(font2);
        self.tableWidget.setItem(19, 0, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableWidget.setItem(19, 1, __qtablewidgetitem76)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 70, 1391, 711))
        self.tableWidget.setFont(font)
        self.tableWidget.setInputMethodHints(Qt.ImhNone)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(34)
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 780, 429, 36))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_calculate_table1 = QPushButton(self.layoutWidget)
        self.bt_calculate_table1.setObjectName(u"bt_calculate_table1")

        self.horizontalLayout_2.addWidget(self.bt_calculate_table1)

        self.bt_show_chart_1 = QPushButton(self.layoutWidget)
        self.bt_show_chart_1.setObjectName(u"bt_show_chart_1")

        self.horizontalLayout_2.addWidget(self.bt_show_chart_1)

        self.bt_export_xl_1 = QPushButton(self.layoutWidget)
        self.bt_export_xl_1.setObjectName(u"bt_export_xl_1")
        self.bt_export_xl_1.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.bt_export_xl_1)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 1011, 61))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tableWidget_2 = QTableWidget(self.tab_2)
        if (self.tableWidget_2.columnCount() < 8):
            self.tableWidget_2.setColumnCount(8)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem84)
        if (self.tableWidget_2.rowCount() < 15):
            self.tableWidget_2.setRowCount(15)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        __qtablewidgetitem100.setFlags(Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        __qtablewidgetitem101.setFlags(Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        __qtablewidgetitem102.setFlags(Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        __qtablewidgetitem103.setFlags(Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 3, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        __qtablewidgetitem104.setFlags(Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 4, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        __qtablewidgetitem105.setFlags(Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 5, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        __qtablewidgetitem106.setFlags(Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 6, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 7, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        __qtablewidgetitem108.setFont(font2);
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        __qtablewidgetitem110.setFont(font2);
        self.tableWidget_2.setItem(2, 0, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 1, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        __qtablewidgetitem112.setFont(font2);
        self.tableWidget_2.setItem(3, 0, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 1, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        __qtablewidgetitem114.setFont(font2);
        self.tableWidget_2.setItem(4, 0, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 1, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        __qtablewidgetitem116.setFont(font2);
        self.tableWidget_2.setItem(5, 0, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 1, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        __qtablewidgetitem118.setFont(font2);
        self.tableWidget_2.setItem(6, 0, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tableWidget_2.setItem(6, 1, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        __qtablewidgetitem120.setFont(font2);
        self.tableWidget_2.setItem(7, 0, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tableWidget_2.setItem(7, 1, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        __qtablewidgetitem122.setFont(font2);
        self.tableWidget_2.setItem(8, 0, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tableWidget_2.setItem(8, 1, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        __qtablewidgetitem124.setFont(font2);
        self.tableWidget_2.setItem(9, 0, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.tableWidget_2.setItem(9, 1, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        __qtablewidgetitem126.setFont(font2);
        self.tableWidget_2.setItem(10, 0, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.tableWidget_2.setItem(10, 1, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        __qtablewidgetitem128.setFont(font2);
        self.tableWidget_2.setItem(11, 0, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.tableWidget_2.setItem(11, 1, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        __qtablewidgetitem130.setFont(font2);
        self.tableWidget_2.setItem(12, 0, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        self.tableWidget_2.setItem(12, 1, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        __qtablewidgetitem132.setFont(font2);
        self.tableWidget_2.setItem(13, 0, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.tableWidget_2.setItem(13, 1, __qtablewidgetitem133)
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        __qtablewidgetitem134 = QTableWidgetItem()
        __qtablewidgetitem134.setFont(font4);
        self.tableWidget_2.setItem(14, 0, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.tableWidget_2.setItem(14, 1, __qtablewidgetitem135)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(0, 110, 1391, 511))
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(170)
        self.bt_calculate_table2 = QPushButton(self.tab_2)
        self.bt_calculate_table2.setObjectName(u"bt_calculate_table2")
        self.bt_calculate_table2.setGeometry(QRect(0, 630, 111, 24))
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 911, 111))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tableWidget_3 = QTableWidget(self.tab_3)
        if (self.tableWidget_3.columnCount() < 8):
            self.tableWidget_3.setColumnCount(8)
        __qtablewidgetitem136 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem143)
        if (self.tableWidget_3.rowCount() < 21):
            self.tableWidget_3.setRowCount(21)
        __qtablewidgetitem144 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(6, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(7, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(8, __qtablewidgetitem152)
        __qtablewidgetitem153 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(9, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(10, __qtablewidgetitem154)
        __qtablewidgetitem155 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(11, __qtablewidgetitem155)
        __qtablewidgetitem156 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(12, __qtablewidgetitem156)
        __qtablewidgetitem157 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(13, __qtablewidgetitem157)
        __qtablewidgetitem158 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(14, __qtablewidgetitem158)
        __qtablewidgetitem159 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(15, __qtablewidgetitem159)
        __qtablewidgetitem160 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(16, __qtablewidgetitem160)
        __qtablewidgetitem161 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(17, __qtablewidgetitem161)
        __qtablewidgetitem162 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(18, __qtablewidgetitem162)
        __qtablewidgetitem163 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(19, __qtablewidgetitem163)
        __qtablewidgetitem164 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(20, __qtablewidgetitem164)
        __qtablewidgetitem165 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 2, __qtablewidgetitem165)
        __qtablewidgetitem166 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 3, __qtablewidgetitem166)
        __qtablewidgetitem167 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 4, __qtablewidgetitem167)
        __qtablewidgetitem168 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 5, __qtablewidgetitem168)
        __qtablewidgetitem169 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 6, __qtablewidgetitem169)
        __qtablewidgetitem170 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 7, __qtablewidgetitem170)
        __qtablewidgetitem171 = QTableWidgetItem()
        __qtablewidgetitem171.setFont(font2);
        self.tableWidget_3.setItem(1, 0, __qtablewidgetitem171)
        __qtablewidgetitem172 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 1, __qtablewidgetitem172)
        __qtablewidgetitem173 = QTableWidgetItem()
        __qtablewidgetitem173.setFont(font4);
        self.tableWidget_3.setItem(2, 0, __qtablewidgetitem173)
        __qtablewidgetitem174 = QTableWidgetItem()
        self.tableWidget_3.setItem(2, 1, __qtablewidgetitem174)
        __qtablewidgetitem175 = QTableWidgetItem()
        __qtablewidgetitem175.setFont(font4);
        self.tableWidget_3.setItem(3, 0, __qtablewidgetitem175)
        __qtablewidgetitem176 = QTableWidgetItem()
        self.tableWidget_3.setItem(3, 1, __qtablewidgetitem176)
        __qtablewidgetitem177 = QTableWidgetItem()
        __qtablewidgetitem177.setFont(font2);
        self.tableWidget_3.setItem(4, 0, __qtablewidgetitem177)
        __qtablewidgetitem178 = QTableWidgetItem()
        self.tableWidget_3.setItem(4, 1, __qtablewidgetitem178)
        __qtablewidgetitem179 = QTableWidgetItem()
        self.tableWidget_3.setItem(4, 2, __qtablewidgetitem179)
        __qtablewidgetitem180 = QTableWidgetItem()
        __qtablewidgetitem180.setFont(font2);
        self.tableWidget_3.setItem(5, 0, __qtablewidgetitem180)
        __qtablewidgetitem181 = QTableWidgetItem()
        self.tableWidget_3.setItem(5, 1, __qtablewidgetitem181)
        __qtablewidgetitem182 = QTableWidgetItem()
        __qtablewidgetitem182.setFont(font2);
        self.tableWidget_3.setItem(6, 0, __qtablewidgetitem182)
        __qtablewidgetitem183 = QTableWidgetItem()
        self.tableWidget_3.setItem(6, 1, __qtablewidgetitem183)
        __qtablewidgetitem184 = QTableWidgetItem()
        __qtablewidgetitem184.setFont(font2);
        self.tableWidget_3.setItem(7, 0, __qtablewidgetitem184)
        __qtablewidgetitem185 = QTableWidgetItem()
        self.tableWidget_3.setItem(7, 1, __qtablewidgetitem185)
        __qtablewidgetitem186 = QTableWidgetItem()
        __qtablewidgetitem186.setFont(font2);
        self.tableWidget_3.setItem(8, 0, __qtablewidgetitem186)
        __qtablewidgetitem187 = QTableWidgetItem()
        self.tableWidget_3.setItem(8, 1, __qtablewidgetitem187)
        __qtablewidgetitem188 = QTableWidgetItem()
        __qtablewidgetitem188.setFont(font2);
        self.tableWidget_3.setItem(9, 0, __qtablewidgetitem188)
        __qtablewidgetitem189 = QTableWidgetItem()
        self.tableWidget_3.setItem(9, 1, __qtablewidgetitem189)
        __qtablewidgetitem190 = QTableWidgetItem()
        __qtablewidgetitem190.setFont(font2);
        self.tableWidget_3.setItem(10, 0, __qtablewidgetitem190)
        __qtablewidgetitem191 = QTableWidgetItem()
        self.tableWidget_3.setItem(10, 1, __qtablewidgetitem191)
        __qtablewidgetitem192 = QTableWidgetItem()
        __qtablewidgetitem192.setFont(font2);
        self.tableWidget_3.setItem(11, 0, __qtablewidgetitem192)
        __qtablewidgetitem193 = QTableWidgetItem()
        self.tableWidget_3.setItem(11, 1, __qtablewidgetitem193)
        __qtablewidgetitem194 = QTableWidgetItem()
        __qtablewidgetitem194.setFont(font2);
        self.tableWidget_3.setItem(12, 0, __qtablewidgetitem194)
        __qtablewidgetitem195 = QTableWidgetItem()
        self.tableWidget_3.setItem(12, 1, __qtablewidgetitem195)
        __qtablewidgetitem196 = QTableWidgetItem()
        __qtablewidgetitem196.setFont(font2);
        self.tableWidget_3.setItem(13, 0, __qtablewidgetitem196)
        __qtablewidgetitem197 = QTableWidgetItem()
        self.tableWidget_3.setItem(13, 1, __qtablewidgetitem197)
        __qtablewidgetitem198 = QTableWidgetItem()
        __qtablewidgetitem198.setFont(font4);
        self.tableWidget_3.setItem(14, 0, __qtablewidgetitem198)
        __qtablewidgetitem199 = QTableWidgetItem()
        self.tableWidget_3.setItem(14, 1, __qtablewidgetitem199)
        __qtablewidgetitem200 = QTableWidgetItem()
        __qtablewidgetitem200.setFont(font4);
        self.tableWidget_3.setItem(15, 0, __qtablewidgetitem200)
        __qtablewidgetitem201 = QTableWidgetItem()
        self.tableWidget_3.setItem(15, 1, __qtablewidgetitem201)
        __qtablewidgetitem202 = QTableWidgetItem()
        __qtablewidgetitem202.setFont(font4);
        self.tableWidget_3.setItem(16, 0, __qtablewidgetitem202)
        __qtablewidgetitem203 = QTableWidgetItem()
        self.tableWidget_3.setItem(16, 1, __qtablewidgetitem203)
        __qtablewidgetitem204 = QTableWidgetItem()
        __qtablewidgetitem204.setFont(font4);
        self.tableWidget_3.setItem(17, 0, __qtablewidgetitem204)
        __qtablewidgetitem205 = QTableWidgetItem()
        self.tableWidget_3.setItem(17, 1, __qtablewidgetitem205)
        __qtablewidgetitem206 = QTableWidgetItem()
        __qtablewidgetitem206.setFont(font4);
        self.tableWidget_3.setItem(18, 0, __qtablewidgetitem206)
        __qtablewidgetitem207 = QTableWidgetItem()
        self.tableWidget_3.setItem(18, 1, __qtablewidgetitem207)
        __qtablewidgetitem208 = QTableWidgetItem()
        __qtablewidgetitem208.setFont(font2);
        self.tableWidget_3.setItem(19, 0, __qtablewidgetitem208)
        __qtablewidgetitem209 = QTableWidgetItem()
        self.tableWidget_3.setItem(19, 1, __qtablewidgetitem209)
        __qtablewidgetitem210 = QTableWidgetItem()
        __qtablewidgetitem210.setFont(font2);
        self.tableWidget_3.setItem(20, 0, __qtablewidgetitem210)
        __qtablewidgetitem211 = QTableWidgetItem()
        self.tableWidget_3.setItem(20, 1, __qtablewidgetitem211)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(0, 90, 1391, 681))
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(170)
        self.layoutWidget1 = QWidget(self.tab_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 770, 258, 36))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bt_calculate_table3 = QPushButton(self.layoutWidget1)
        self.bt_calculate_table3.setObjectName(u"bt_calculate_table3")

        self.horizontalLayout.addWidget(self.bt_calculate_table3)

        self.bt_show_chart_table3 = QPushButton(self.layoutWidget1)
        self.bt_show_chart_table3.setObjectName(u"bt_show_chart_table3")

        self.horizontalLayout.addWidget(self.bt_show_chart_table3)

        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(mainWindow)

        self.tabWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(mainWindow)

    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow",
                                                             u"\u0420\u0430\u0441\u0447\u0451\u0442\u043d\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430",
                                                             None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("mainWindow",
                                                                                                 u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435",
                                                                                                 None))
        self.Power.setText(QCoreApplication.translate("mainWindow",
                                                      u"\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f ",
                                                      None))
        self.Input.setText(
            QCoreApplication.translate("mainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435:", None))
        self.Voltage.setText(QCoreApplication.translate("mainWindow",
                                                        u"\u041d\u043e\u043c\u0438\u043d\u0430\u043b\u044c\u043d\u043e\u0435 \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435",
                                                        None))
        self.polarity.setText(
            QCoreApplication.translate("mainWindow", u"\u041f\u043e\u043b\u044f\u0440\u043d\u043e\u0441\u0442\u044c",
                                       None))
        self.linePower.setText(QCoreApplication.translate("mainWindow", u"22", None))
        self.lineVoltage.setText(QCoreApplication.translate("mainWindow", u"380", None))
        self.linePolarity.setText(QCoreApplication.translate("mainWindow", u"4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("mainWindow",
                                                                                                 u"\u0412\u0432\u043e\u0434 \u0434\u0430\u043d\u043d\u044b\u0445",
                                                                                                 None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mainWindow",
                                                               u"\u0420\u0430\u0441\u0447\u0451\u0442\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0443\u043b\u0430",
                                                               None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mainWindow",
                                                                u"\u0420\u0430\u0437\u043c\u0435\u0440\u043d\u043e\u0441\u0442\u044c",
                                                                None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("mainWindow", u"\u0421\u043a\u043e\u043b\u044c\u0436\u0435\u043d\u0438\u0435 s",
                                       None));
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
        ___qtablewidgetitem32 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("mainWindow", u"R = a+a'r'_2/s", None));
        ___qtablewidgetitem33 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem34 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("mainWindow", u"X = b+b'r'_2/s", None));
        ___qtablewidgetitem35 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem36 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("mainWindow", u"Z = \u221a(R^2+X^2)", None));
        ___qtablewidgetitem37 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem38 = self.tableWidget.item(5, 0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("mainWindow", u"I'_2 = U/Z", None));
        ___qtablewidgetitem39 = self.tableWidget.item(5, 1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem40 = self.tableWidget.item(6, 0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("mainWindow", u"cos(\u03c6)'_2 = R/Z", None));
        ___qtablewidgetitem41 = self.tableWidget.item(6, 1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem42 = self.tableWidget.item(7, 0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("mainWindow", u"sin(\u03c6)'_2 = X/Z", None));
        ___qtablewidgetitem43 = self.tableWidget.item(7, 1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem44 = self.tableWidget.item(8, 0)
        ___qtablewidgetitem44.setText(
            QCoreApplication.translate("mainWindow", u"I_1\u043f = I_0\u043f+I'_2cos(\u03c6)'_2", None));
        ___qtablewidgetitem45 = self.tableWidget.item(8, 1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem46 = self.tableWidget.item(9, 0)
        ___qtablewidgetitem46.setText(
            QCoreApplication.translate("mainWindow", u"I_1\u0440 = I_0\u043f+I'_2sin(\u03c6)'_2", None));
        ___qtablewidgetitem47 = self.tableWidget.item(9, 1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem48 = self.tableWidget.item(10, 0)
        ___qtablewidgetitem48.setText(
            QCoreApplication.translate("mainWindow", u"I_1 = \u221a(I_1\u043f^2+I_1\u0440^2)", None));
        ___qtablewidgetitem49 = self.tableWidget.item(10, 1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem50 = self.tableWidget.item(11, 0)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("mainWindow", u"I'_2 = c_1 I'_2", None));
        ___qtablewidgetitem51 = self.tableWidget.item(11, 1)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem52 = self.tableWidget.item(12, 0)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("mainWindow", u"P_1 = 3U I_1a * 10^-3", None));
        ___qtablewidgetitem53 = self.tableWidget.item(12, 1)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("mainWindow", u"\u043a\u0412\u0442", None));
        ___qtablewidgetitem54 = self.tableWidget.item(13, 0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("mainWindow", u"P_\u044d1 = 3I_1^2*r_1*10^-3", None));
        ___qtablewidgetitem55 = self.tableWidget.item(13, 1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("mainWindow", u"\u043a\u0412\u0442", None));
        ___qtablewidgetitem56 = self.tableWidget.item(14, 0)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("mainWindow", u"P_\u044d2=3I'_2^2*r'_2*10^-3", None));
        ___qtablewidgetitem57 = self.tableWidget.item(14, 1)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("mainWindow", u"\u043a\u0412\u0442", None));
        ___qtablewidgetitem58 = self.tableWidget.item(15, 0)
        ___qtablewidgetitem58.setText(
            QCoreApplication.translate("mainWindow", u"P_\u0434\u043e\u0431 = 0,005P_1", None));
        ___qtablewidgetitem59 = self.tableWidget.item(15, 1)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("mainWindow", u"\u043a\u0412\u0442", None));
        ___qtablewidgetitem60 = self.tableWidget.item(16, 0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("mainWindow",
                                                                 u"\u03a3P=P\u0441\u0442+P\u043c\u0435\u0445+P\u044d2+P\u044d1+P\u044d.\u0449+P\u0434\u043e\u0431",
                                                                 None));
        ___qtablewidgetitem61 = self.tableWidget.item(16, 1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("mainWindow", u"\u043a\u0412\u0442", None));
        ___qtablewidgetitem62 = self.tableWidget.item(17, 0)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("mainWindow", u"P_2 = P_1 - \u03a3P", None));
        ___qtablewidgetitem63 = self.tableWidget.item(17, 1)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("mainWindow", u"\u043a\u0412\u0442", None));
        ___qtablewidgetitem64 = self.tableWidget.item(18, 0)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("mainWindow", u"\u03b7 = 1 - \u03a3P/P_1", None));
        ___qtablewidgetitem65 = self.tableWidget.item(18, 1)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem66 = self.tableWidget.item(19, 0)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("mainWindow", u"cos(\u03c6) = I_1a/I_1", None));
        ___qtablewidgetitem67 = self.tableWidget.item(19, 1)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("mainWindow", u"-", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.bt_calculate_table1.setText(
            QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c",
                                       None))
        self.bt_show_chart_1.setText(QCoreApplication.translate("mainWindow",
                                                                u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a",
                                                                None))
        self.bt_export_xl_1.setText(QCoreApplication.translate("mainWindow",
                                                               u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0432 \u044d\u043a\u0441\u0435\u043b\u044c",
                                                               None))
        self.label_5.setText(QCoreApplication.translate("mainWindow",
                                                        u"<html><head/><body><p><span style=\" font-size:14pt;\">P</span><span style=\" font-size:14pt; vertical-align:sub;\">2\u043d</span><span style=\" font-size:14pt;\"> = 22; U = 380/660 ; 2p = 4; I</span><span style=\" font-size:14pt; vertical-align:sub;\">0a</span><span style=\" font-size:14pt;\"> = 0,37; I</span><span style=\" font-size:14pt; vertical-align:sub;\">0p</span><span style=\" font-size:14pt;\"> = 5,39; P</span><span style=\" font-size:14pt; vertical-align:sub;\">\u0441\u0442</span><span style=\" font-size:14pt;\"> + P</span><span style=\" font-size:14pt; vertical-align:sub;\">\u0442\u0440.\u0449</span><span style=\" font-size:14pt;\"> + P</span><span style=\" font-size:14pt; vertical-align:sub;\">\u043c\u0435\u0445</span><span style=\" font-size:14pt;\"> = 0,67; r</span><span style=\" font-size:14pt; vertical-align:sub;\">1 </span><span style=\" font-size:14pt;\">= 0,6; r'</span><span style=\" font-size:14pt; vertical-align:sub;\">2</span><span style=\" font-size:14pt;\"> = 0,38; c</span><span style="
                                                        "\" font-size:14pt; vertical-align:sub;\">1 </span><span style=\" font-size:14pt;\">= 1,029;</span></p><p><span style=\" font-size:14pt;\">a' = 1,06; a = 0,364; b' = 0; b = 4,17; P</span><span style=\" font-size:14pt; vertical-align:sub;\">\u0441\u0442</span><span style=\" font-size:14pt;\"> = 0,44928; P</span><span style=\" font-size:14pt; vertical-align:sub;\">\u043c\u0435\u0445</span><span style=\" font-size:14pt;\"> = 0,20854; P</span><span style=\" font-size:14pt; vertical-align:sub;\">\u044d1</span><span style=\" font-size:14pt;\"> = 1,012; P</span><span style=\" font-size:14pt; vertical-align:sub;\">\u044d\u0449</span><span style=\" font-size:14pt;\"> = 0,559;</span></p><p><span style=\" font-size:14pt;\"><br/></span></p></body></html>",
                                                        None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("mainWindow",
                                                                                               u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 1",
                                                                                               None))
        ___qtablewidgetitem68 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("mainWindow",
                                                                 u"\u0420\u0430\u0441\u0447\u0451\u0442\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0443\u043b\u0430",
                                                                 None));
        ___qtablewidgetitem69 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("mainWindow",
                                                                 u"\u0420\u0430\u0437\u043c\u0435\u0440\u043d\u043e\u0441\u0442\u044c",
                                                                 None));
        ___qtablewidgetitem70 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem70.setText(
            QCoreApplication.translate("mainWindow", u"\u0421\u043a\u043e\u043b\u044c\u0436\u0435\u043d\u0438\u0435 s",
                                       None));
        ___qtablewidgetitem71 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("mainWindow", u"s \u043a\u0440", None));
        ___qtablewidgetitem72 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("mainWindow", u"1", None));
        ___qtablewidgetitem73 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("mainWindow", u"2", None));
        ___qtablewidgetitem74 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("mainWindow", u"3", None));
        ___qtablewidgetitem75 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("mainWindow", u"4", None));
        ___qtablewidgetitem76 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("mainWindow", u"5", None));
        ___qtablewidgetitem77 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("mainWindow", u"6", None));
        ___qtablewidgetitem78 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("mainWindow", u"7", None));
        ___qtablewidgetitem79 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("mainWindow", u"8", None));
        ___qtablewidgetitem80 = self.tableWidget_2.verticalHeaderItem(9)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("mainWindow", u"9", None));
        ___qtablewidgetitem81 = self.tableWidget_2.verticalHeaderItem(10)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("mainWindow", u"10", None));
        ___qtablewidgetitem82 = self.tableWidget_2.verticalHeaderItem(11)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("mainWindow", u"11", None));
        ___qtablewidgetitem83 = self.tableWidget_2.verticalHeaderItem(12)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("mainWindow", u"12", None));
        ___qtablewidgetitem84 = self.tableWidget_2.verticalHeaderItem(13)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("mainWindow", u"13", None));
        ___qtablewidgetitem85 = self.tableWidget_2.verticalHeaderItem(14)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("mainWindow", u"14", None));

        __sortingEnabled1 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem86 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("mainWindow", u"1", None));
        ___qtablewidgetitem87 = self.tableWidget_2.item(0, 3)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("mainWindow", u"0.8", None));
        ___qtablewidgetitem88 = self.tableWidget_2.item(0, 4)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("mainWindow", u"0.5", None));
        ___qtablewidgetitem89 = self.tableWidget_2.item(0, 5)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("mainWindow", u"0.2", None));
        ___qtablewidgetitem90 = self.tableWidget_2.item(0, 6)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("mainWindow", u"0.1", None));
        ___qtablewidgetitem91 = self.tableWidget_2.item(0, 7)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("mainWindow", u"0.19", None));
        ___qtablewidgetitem92 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("mainWindow", u"\u03be=63,61h_c*\u221as", None));
        ___qtablewidgetitem93 = self.tableWidget_2.item(1, 1)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem94 = self.tableWidget_2.item(2, 0)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("mainWindow", u"\u03c6(\u03be)", None));
        ___qtablewidgetitem95 = self.tableWidget_2.item(2, 1)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem96 = self.tableWidget_2.item(3, 0)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("mainWindow", u"h_r = h_c/(1-\u03c6)", None));
        ___qtablewidgetitem97 = self.tableWidget_2.item(3, 1)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("mainWindow", u"\u043c\u043c", None));
        ___qtablewidgetitem98 = self.tableWidget_2.item(4, 0)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("mainWindow", u"k_r=q_c/q_r", None));
        ___qtablewidgetitem99 = self.tableWidget_2.item(4, 1)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem100 = self.tableWidget_2.item(5, 0)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("mainWindow", u"K_R =1+(r_c/r_2)*(k_r-1)", None));
        ___qtablewidgetitem101 = self.tableWidget_2.item(5, 1)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem102 = self.tableWidget_2.item(6, 0)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("mainWindow", u"r'_2_\u03be = K_R*r'_2", None));
        ___qtablewidgetitem103 = self.tableWidget_2.item(6, 1)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem104 = self.tableWidget_2.item(7, 0)
        ___qtablewidgetitem104.setText(
            QCoreApplication.translate("mainWindow", u"\u043a_\u0434 = \u03c6'(\u03be)", None));
        ___qtablewidgetitem105 = self.tableWidget_2.item(7, 1)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem106 = self.tableWidget_2.item(8, 0)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("mainWindow",
                                                                  u"\u03bb_\u043f2\u03be = \u03bb_\u043f2 - \u0394\u03bb\u043f2\u03be",
                                                                  None));
        ___qtablewidgetitem107 = self.tableWidget_2.item(8, 1)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem108 = self.tableWidget_2.item(9, 0)
        ___qtablewidgetitem108.setText(
            QCoreApplication.translate("mainWindow", u"Kx = \u03a3\u03bb_2\u03be/\u03a3\u03bb_2", None));
        ___qtablewidgetitem109 = self.tableWidget_2.item(9, 1)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem110 = self.tableWidget_2.item(10, 0)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("mainWindow", u"x'2\u03be = Kx * x'_2", None));
        ___qtablewidgetitem111 = self.tableWidget_2.item(10, 1)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem112 = self.tableWidget_2.item(11, 0)
        ___qtablewidgetitem112.setText(
            QCoreApplication.translate("mainWindow", u"R\u043f = r_1+c_1\u043f* (r'_2_\u03be/s)", None));
        ___qtablewidgetitem113 = self.tableWidget_2.item(11, 1)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem114 = self.tableWidget_2.item(12, 0)
        ___qtablewidgetitem114.setText(
            QCoreApplication.translate("mainWindow", u"X\u043f = x_1+c_1\u043f*x'2\u03be", None));
        ___qtablewidgetitem115 = self.tableWidget_2.item(12, 1)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem116 = self.tableWidget_2.item(13, 0)
        ___qtablewidgetitem116.setText(
            QCoreApplication.translate("mainWindow", u"I'_2\u043f = U/\u221a(R\u043f^2 + X\u043f^2)", None));
        ___qtablewidgetitem117 = self.tableWidget_2.item(13, 1)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem118 = self.tableWidget_2.item(14, 0)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("mainWindow",
                                                                  u"I_1\u043f=I'_2\u221a(R\u043f^2 + (X\u043f+x_12\u043f)^2)/(c_1\u043f*x_12\u043f)",
                                                                  None));
        ___qtablewidgetitem119 = self.tableWidget_2.item(14, 1)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled1)

        self.bt_calculate_table2.setText(
            QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c",
                                       None))
        self.label.setText(QCoreApplication.translate("mainWindow",
                                                      u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                      "p, li { white-space: pre-wrap; }\n"
                                                      "hr { height: 1px; border-width: 0; }\n"
                                                      "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                      "li.checked::marker { content: \"\\2612\"; }\n"
                                                      "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                      "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">P</span><span style=\" font-size:14pt; vertical-align:sub;\">2</span><span style=\" font-size:14pt;\"> = 22; U = 380/660; 2p = 4 ; I</span><span style=\" font-size:14pt; vertical-align:sub;\">1\u043d\u043e\u043c</span><span style=\" font-size:14pt;\"> = 23,715;I'</span><span style=\" font-size:14pt; vertical-align:sub;\">2\u043d\u043e\u043c</span><span style=\" font-"
                                                      "size:14pt;\"> = 22,158; x</span><span style=\" font-size:14pt; vertical-align:sub;\">1</span><span style=\" font-size:14pt;\"> = 1,89; x'</span><span style=\" font-size:14pt; vertical-align:sub;\">2</span><span style=\" font-size:14pt;\"> = 2,03; x</span><span style=\" font-size:14pt; vertical-align:sub;\">12\u043f</span><span style=\" font-size:14pt;\"> = 91,84; r</span><span style=\" font-size:14pt; vertical-align:sub;\">1</span><span style=\" font-size:14pt;\"> = 0,6; r'</span><span style=\" font-size:14pt; vertical-align:sub;\">2</span><span style=\" font-size:14pt;\"> = 0,38;</span></p>\n"
                                                      "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">s</span><span style=\" font-size:14pt; vertical-align:sub;\">\u043d\u043e\u043c</span><span style=\" font-size:14pt;\"> = 0,0244; C</span><span style=\" font-size:14pt; vertical-align:sub;\">1\u043f</span><span style=\" font-size:14pt;\"> = 1,02; h</span><span style"
                                                      "=\" font-size:14pt; vertical-align:sub;\">c</span><span style=\" font-size:14pt;\"> = 29,62; q</span><span style=\" font-size:14pt; vertical-align:sub;\">c</span><span style=\" font-size:14pt;\"> = 184,94; q</span><span style=\" font-size:14pt; vertical-align:sub;\">r</span><span style=\" font-size:14pt;\"> = 112,074; r</span><span style=\" font-size:14pt; vertical-align:sub;\">c</span><span style=\" font-size:14pt;\"> = 38,3 * 10</span><span style=\" font-size:14pt; vertical-align:super;\">-6 </span><span style=\" font-size:14pt;\">; r</span><span style=\" font-size:14pt; vertical-align:sub;\">2</span><span style=\" font-size:14pt;\"> = 57,3 * 10</span><span style=\" font-size:14pt; vertical-align:super;\">-6</span><span style=\" font-size:14pt;\">;  x'</span><span style=\" font-size:14pt; vertical-align:sub;\">2\u03be </span><span style=\" font-size:14pt;\">= 1,624</span></p>\n"
                                                      "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span s"
                                                      "tyle=\" font-family:'sans-serif'; font-size:14pt; color:#202122; background-color:#ffffff;\">\u03bb</span><span style=\" font-family:'sans-serif'; font-size:14pt; color:#202122; background-color:#ffffff; vertical-align:sub;\">\u043f2</span><span style=\" font-size:14pt;\"> = 2,42; </span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:14pt; font-weight:700; color:#202122; background-color:#ffffff;\">\u0394</span><span style=\" font-family:'sans-serif'; font-size:14pt; color:#202122; background-color:#ffffff;\">\u03bb</span><span style=\" font-family:'sans-serif'; font-size:14pt; color:#202122; background-color:#ffffff; vertical-align:sub;\">\u043f2</span><span style=\" font-size:14pt; vertical-align:sub;\">\u03be</span><span style=\" font-size:14pt;\"> = 0,148; </span><span style=\" font-family:'sans-serif'; font-size:14pt; color:#202122; background-color:#ffffff;\">\u03bb</span><span style=\" font-family:'sans-serif'; font-size:14pt; color:#"
                                                      "202122; background-color:#ffffff; vertical-align:sub;\">\u043b2</span><span style=\" font-size:14pt;\"> = 0,678; </span><span style=\" font-family:'sans-serif'; font-size:14pt; color:#202122; background-color:#ffffff;\">\u03bb</span><span style=\" font-family:'sans-serif'; font-size:14pt; color:#202122; background-color:#ffffff; vertical-align:sub;\">\u04342</span><span style=\" font-size:14pt;\"> = 2,19</span></p>\n"
                                                      "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\"><br /></span></p></body></html>",
                                                      None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("mainWindow",
                                                                                                 u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 2",
                                                                                                 None))
        ___qtablewidgetitem120 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("mainWindow",
                                                                  u"\u0420\u0430\u0441\u0447\u0451\u0442\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0443\u043b\u0430",
                                                                  None));
        ___qtablewidgetitem121 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("mainWindow",
                                                                  u"\u0420\u0430\u0437\u043c\u0435\u0440\u043d\u043e\u0441\u0442\u044c",
                                                                  None));
        ___qtablewidgetitem122 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem122.setText(
            QCoreApplication.translate("mainWindow", u"\u0421\u043a\u043e\u043b\u044c\u0436\u0435\u043d\u0438\u0435 s",
                                       None));
        ___qtablewidgetitem123 = self.tableWidget_3.horizontalHeaderItem(7)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("mainWindow", u"s \u043a\u0440", None));
        ___qtablewidgetitem124 = self.tableWidget_3.verticalHeaderItem(1)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("mainWindow", u"1", None));
        ___qtablewidgetitem125 = self.tableWidget_3.verticalHeaderItem(2)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("mainWindow", u"2", None));
        ___qtablewidgetitem126 = self.tableWidget_3.verticalHeaderItem(3)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("mainWindow", u"3", None));
        ___qtablewidgetitem127 = self.tableWidget_3.verticalHeaderItem(4)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("mainWindow", u"4", None));
        ___qtablewidgetitem128 = self.tableWidget_3.verticalHeaderItem(5)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("mainWindow", u"5", None));
        ___qtablewidgetitem129 = self.tableWidget_3.verticalHeaderItem(6)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("mainWindow", u"6", None));
        ___qtablewidgetitem130 = self.tableWidget_3.verticalHeaderItem(7)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("mainWindow", u"7", None));
        ___qtablewidgetitem131 = self.tableWidget_3.verticalHeaderItem(8)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("mainWindow", u"8", None));
        ___qtablewidgetitem132 = self.tableWidget_3.verticalHeaderItem(9)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("mainWindow", u"9", None));
        ___qtablewidgetitem133 = self.tableWidget_3.verticalHeaderItem(10)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("mainWindow", u"10", None));
        ___qtablewidgetitem134 = self.tableWidget_3.verticalHeaderItem(11)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("mainWindow", u"11", None));
        ___qtablewidgetitem135 = self.tableWidget_3.verticalHeaderItem(12)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("mainWindow", u"12", None));
        ___qtablewidgetitem136 = self.tableWidget_3.verticalHeaderItem(13)
        ___qtablewidgetitem136.setText(QCoreApplication.translate("mainWindow", u"13", None));
        ___qtablewidgetitem137 = self.tableWidget_3.verticalHeaderItem(14)
        ___qtablewidgetitem137.setText(QCoreApplication.translate("mainWindow", u"14", None));
        ___qtablewidgetitem138 = self.tableWidget_3.verticalHeaderItem(15)
        ___qtablewidgetitem138.setText(QCoreApplication.translate("mainWindow", u"15", None));
        ___qtablewidgetitem139 = self.tableWidget_3.verticalHeaderItem(16)
        ___qtablewidgetitem139.setText(QCoreApplication.translate("mainWindow", u"16", None));
        ___qtablewidgetitem140 = self.tableWidget_3.verticalHeaderItem(17)
        ___qtablewidgetitem140.setText(QCoreApplication.translate("mainWindow", u"17", None));
        ___qtablewidgetitem141 = self.tableWidget_3.verticalHeaderItem(18)
        ___qtablewidgetitem141.setText(QCoreApplication.translate("mainWindow", u"18", None));
        ___qtablewidgetitem142 = self.tableWidget_3.verticalHeaderItem(19)
        ___qtablewidgetitem142.setText(QCoreApplication.translate("mainWindow", u"19", None));
        ___qtablewidgetitem143 = self.tableWidget_3.verticalHeaderItem(20)
        ___qtablewidgetitem143.setText(QCoreApplication.translate("mainWindow", u"20", None));

        __sortingEnabled2 = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        ___qtablewidgetitem144 = self.tableWidget_3.item(0, 2)
        ___qtablewidgetitem144.setText(QCoreApplication.translate("mainWindow", u"1", None));
        ___qtablewidgetitem145 = self.tableWidget_3.item(0, 3)
        ___qtablewidgetitem145.setText(QCoreApplication.translate("mainWindow", u"0.8", None));
        ___qtablewidgetitem146 = self.tableWidget_3.item(0, 4)
        ___qtablewidgetitem146.setText(QCoreApplication.translate("mainWindow", u"0.5", None));
        ___qtablewidgetitem147 = self.tableWidget_3.item(0, 5)
        ___qtablewidgetitem147.setText(QCoreApplication.translate("mainWindow", u"0.2", None));
        ___qtablewidgetitem148 = self.tableWidget_3.item(0, 6)
        ___qtablewidgetitem148.setText(QCoreApplication.translate("mainWindow", u"0.1", None));
        ___qtablewidgetitem149 = self.tableWidget_3.item(0, 7)
        ___qtablewidgetitem149.setText(QCoreApplication.translate("mainWindow", u"0.19", None));
        ___qtablewidgetitem150 = self.tableWidget_3.item(1, 0)
        ___qtablewidgetitem150.setText(QCoreApplication.translate("mainWindow", u"k_\u043d\u0430\u0441", None));
        ___qtablewidgetitem151 = self.tableWidget_3.item(1, 1)
        ___qtablewidgetitem151.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem152 = self.tableWidget_3.item(2, 0)
        ___qtablewidgetitem152.setText(QCoreApplication.translate("mainWindow",
                                                                  u"F\u043f.\u0441\u0440=0,7*((I_1*k_\u043d\u0430\u0441*u_\u043f)/a)(k'_beta+k_y1*k_\u043e\u04311*(Z1/Z2))",
                                                                  None));
        ___qtablewidgetitem153 = self.tableWidget_3.item(2, 1)
        ___qtablewidgetitem153.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem154 = self.tableWidget_3.item(3, 0)
        ___qtablewidgetitem154.setText(QCoreApplication.translate("mainWindow",
                                                                  u"\u0412_\u0444\u0431 = F\u043f.\u0441\u0440 * 10^(-6)/(1,6\u03b4*\u0421_N)",
                                                                  None));
        ___qtablewidgetitem155 = self.tableWidget_3.item(3, 1)
        ___qtablewidgetitem155.setText(QCoreApplication.translate("mainWindow", u"\u0422\u043b", None));
        ___qtablewidgetitem156 = self.tableWidget_3.item(4, 0)
        ___qtablewidgetitem156.setText(
            QCoreApplication.translate("mainWindow", u"k_\u03b4 = f(\u0412_\u0444\u0431)", None));
        ___qtablewidgetitem157 = self.tableWidget_3.item(4, 1)
        ___qtablewidgetitem157.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem158 = self.tableWidget_3.item(5, 0)
        ___qtablewidgetitem158.setText(
            QCoreApplication.translate("mainWindow", u"\u0441_1 = (t_z1-b_\u04481)(1-k_\u03b4)", None));
        ___qtablewidgetitem159 = self.tableWidget_3.item(5, 1)
        ___qtablewidgetitem159.setText(QCoreApplication.translate("mainWindow", u"\u043c\u043c", None));
        ___qtablewidgetitem160 = self.tableWidget_3.item(6, 0)
        ___qtablewidgetitem160.setText(QCoreApplication.translate("mainWindow",
                                                                  u"\u03bb_\u043f1\u043d\u0430\u0441 = \u03bb\u043f1 - \u0394\u03bb_\u043f1\u043d\u0430\u0441",
                                                                  None));
        ___qtablewidgetitem161 = self.tableWidget_3.item(6, 1)
        ___qtablewidgetitem161.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem162 = self.tableWidget_3.item(7, 0)
        ___qtablewidgetitem162.setText(
            QCoreApplication.translate("mainWindow", u"\u03bb_\u04341\u043d\u0430\u0441 = k_\u03b4*\u03bb\u04341",
                                       None));
        ___qtablewidgetitem163 = self.tableWidget_3.item(7, 1)
        ___qtablewidgetitem163.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem164 = self.tableWidget_3.item(8, 0)
        ___qtablewidgetitem164.setText(QCoreApplication.translate("mainWindow",
                                                                  u"\u0445_1\u043d\u0430\u0441 = \u04451*\u03a3\u03bb_1\u043d\u0430\u0441/\u03a3\u03bb_1",
                                                                  None));
        ___qtablewidgetitem165 = self.tableWidget_3.item(8, 1)
        ___qtablewidgetitem165.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem166 = self.tableWidget_3.item(9, 0)
        ___qtablewidgetitem166.setText(
            QCoreApplication.translate("mainWindow", u"c_1_\u043f = 1 + x_1\u043d\u0430\u0441/ x_12\u043f", None));
        ___qtablewidgetitem167 = self.tableWidget_3.item(9, 1)
        ___qtablewidgetitem167.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem168 = self.tableWidget_3.item(10, 0)
        ___qtablewidgetitem168.setText(
            QCoreApplication.translate("mainWindow", u"\u0441_2 = (t_z2-b_\u04482)(1-k_\u03b4)", None));
        ___qtablewidgetitem169 = self.tableWidget_3.item(10, 1)
        ___qtablewidgetitem169.setText(QCoreApplication.translate("mainWindow", u"\u043c\u043c", None));
        ___qtablewidgetitem170 = self.tableWidget_3.item(11, 0)
        ___qtablewidgetitem170.setText(QCoreApplication.translate("mainWindow",
                                                                  u"\u03bb_\u043f2\u03be\u043d\u0430\u0441 = \u03bb_\u043f2\u03be - \u0394\u03bb_\u043f2\u043d\u0430\u0441",
                                                                  None));
        ___qtablewidgetitem171 = self.tableWidget_3.item(11, 1)
        ___qtablewidgetitem171.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem172 = self.tableWidget_3.item(12, 0)
        ___qtablewidgetitem172.setText(
            QCoreApplication.translate("mainWindow", u"\u03bb_\u04342\u043d\u0430\u0441 = k_\u03b4*\u03bb\u04342",
                                       None));
        ___qtablewidgetitem173 = self.tableWidget_3.item(12, 1)
        ___qtablewidgetitem173.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem174 = self.tableWidget_3.item(13, 0)
        ___qtablewidgetitem174.setText(QCoreApplication.translate("mainWindow",
                                                                  u"\u0445'_2\u03be\u043d\u0430\u0441 = x'2*\u03a3\u03bb_2\u03be\u043d\u0430\u0441/\u03a3\u03bb_2",
                                                                  None));
        ___qtablewidgetitem175 = self.tableWidget_3.item(13, 1)
        ___qtablewidgetitem175.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem176 = self.tableWidget_3.item(14, 0)
        ___qtablewidgetitem176.setText(QCoreApplication.translate("mainWindow",
                                                                  u"R\u043f.\u043d\u0430\u0441 = r_1 + c_1\u043f.\u043d\u0430\u0441 * r'_2\u03be / s",
                                                                  None));
        ___qtablewidgetitem177 = self.tableWidget_3.item(14, 1)
        ___qtablewidgetitem177.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem178 = self.tableWidget_3.item(15, 0)
        ___qtablewidgetitem178.setText(QCoreApplication.translate("mainWindow",
                                                                  u"\u0425\u043f.\u043d\u0430\u0441 = x_1\u043d\u0430\u0441 + c_1\u043f.\u043d\u0430\u0441 * \u0445'_2\u03be\u043d\u0430\u0441",
                                                                  None));
        ___qtablewidgetitem179 = self.tableWidget_3.item(15, 1)
        ___qtablewidgetitem179.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem180 = self.tableWidget_3.item(16, 0)
        ___qtablewidgetitem180.setText(QCoreApplication.translate("mainWindow",
                                                                  u"I'_2\u043d\u0430\u0441 = U/\u221a(R\u043f.\u043d\u0430\u0441^2+\u0425\u043f.\u043d\u0430\u0441^2)",
                                                                  None));
        ___qtablewidgetitem181 = self.tableWidget_3.item(16, 1)
        ___qtablewidgetitem181.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem182 = self.tableWidget_3.item(17, 0)
        ___qtablewidgetitem182.setText(QCoreApplication.translate("mainWindow",
                                                                  u"I_1\u043d\u0430\u0441=I'_2\u043d\u0430\u0441*((\u221a(R\u043f.\u043d\u0430\u0441^2+(\u0425\u043f.\u043d\u0430\u0441+\u0445_12\u043f)^2))/(\u0441_1\u043f.\u043d\u0430\u0441*\u0445_12\u043f))",
                                                                  None));
        ___qtablewidgetitem183 = self.tableWidget_3.item(17, 1)
        ___qtablewidgetitem183.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem184 = self.tableWidget_3.item(18, 0)
        ___qtablewidgetitem184.setText(
            QCoreApplication.translate("mainWindow", u"k'\u043d\u0430\u0441 = I_1\u043d\u0430\u0441/I_1\u043f", None));
        ___qtablewidgetitem185 = self.tableWidget_3.item(18, 1)
        ___qtablewidgetitem185.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem186 = self.tableWidget_3.item(19, 0)
        ___qtablewidgetitem186.setText(
            QCoreApplication.translate("mainWindow", u"I_i= I_1\u043d\u0430\u0441 / I_1\u043d\u043e\u043c", None));
        ___qtablewidgetitem187 = self.tableWidget_3.item(19, 1)
        ___qtablewidgetitem187.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem188 = self.tableWidget_3.item(20, 0)
        ___qtablewidgetitem188.setText(QCoreApplication.translate("mainWindow", u"\u041c*", None));
        ___qtablewidgetitem189 = self.tableWidget_3.item(20, 1)
        ___qtablewidgetitem189.setText(QCoreApplication.translate("mainWindow", u"-", None));
        self.tableWidget_3.setSortingEnabled(__sortingEnabled2)

        self.bt_calculate_table3.setText(
            QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.bt_show_chart_table3.setText(QCoreApplication.translate("mainWindow",
                                                                     u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a",
                                                                     None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("mainWindow",
                                                                                                 u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 3",
                                                                                                 None))

