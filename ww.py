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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1435, 929)
        self.tabWidget = QTabWidget(mainWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(10, 0, 1411, 871))
        font = QFont()
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.Input = QLabel(self.tab_4)
        self.Input.setObjectName(u"Input")
        self.Input.setGeometry(QRect(20, 40, 111, 21))
        self.submitValues = QPushButton(self.tab_4)
        self.submitValues.setObjectName(u"submitValues")
        self.submitValues.setGeometry(QRect(20, 240, 441, 41))
        self.layoutWidget = QWidget(self.tab_4)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 70, 445, 159))
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

        self.lineSnom = QLineEdit(self.layoutWidget)
        self.lineSnom.setObjectName(u"lineSnom")

        self.verticalLayout.addWidget(self.lineSnom)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setEnabled(True)
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
        __qtablewidgetitem44.setFont(font1);
        __qtablewidgetitem44.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(3, 0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(3, 1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setFont(font1);
        __qtablewidgetitem46.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(4, 0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(4, 1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setFont(font1);
        __qtablewidgetitem48.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(5, 0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(5, 1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setFont(font1);
        __qtablewidgetitem50.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(6, 0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(6, 1, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setFont(font1);
        __qtablewidgetitem52.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(7, 0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(7, 1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setFont(font1);
        __qtablewidgetitem54.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(8, 0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(8, 1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setFont(font1);
        __qtablewidgetitem56.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(9, 0, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(9, 1, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setFont(font1);
        __qtablewidgetitem58.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(10, 0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(10, 1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setFont(font1);
        __qtablewidgetitem60.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(11, 0, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(11, 1, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setFont(font1);
        __qtablewidgetitem62.setFlags(Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsEnabled);
        self.tableWidget.setItem(12, 0, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(12, 1, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setFont(font1);
        __qtablewidgetitem64.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(13, 0, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(13, 1, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setFont(font1);
        __qtablewidgetitem66.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(14, 0, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(14, 1, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setFont(font1);
        __qtablewidgetitem68.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(15, 0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(15, 1, __qtablewidgetitem69)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Symbol"])
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setKerning(False)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setFont(font3);
        __qtablewidgetitem70.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(16, 0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(16, 1, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setFont(font1);
        __qtablewidgetitem72.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(17, 0, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(17, 1, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setFont(font1);
        __qtablewidgetitem74.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(18, 0, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(18, 1, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setFont(font1);
        __qtablewidgetitem76.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(19, 0, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(19, 1, __qtablewidgetitem77)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(False)
        self.tableWidget.setGeometry(QRect(0, 0, 971, 711))
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
        self.layoutWidget1 = QWidget(self.tab)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 720, 534, 36))
        self.hl_buttons = QHBoxLayout(self.layoutWidget1)
        self.hl_buttons.setObjectName(u"hl_buttons")
        self.hl_buttons.setContentsMargins(0, 0, 0, 0)
        self.bt_check_table_1 = QPushButton(self.layoutWidget1)
        self.bt_check_table_1.setObjectName(u"bt_check_table_1")
        self.bt_check_table_1.setEnabled(False)

        self.hl_buttons.addWidget(self.bt_check_table_1)

        self.bt_calculate_table1 = QPushButton(self.layoutWidget1)
        self.bt_calculate_table1.setObjectName(u"bt_calculate_table1")
        self.bt_calculate_table1.setEnabled(False)

        self.hl_buttons.addWidget(self.bt_calculate_table1)

        self.bt_show_chart_1 = QPushButton(self.layoutWidget1)
        self.bt_show_chart_1.setObjectName(u"bt_show_chart_1")
        self.bt_show_chart_1.setEnabled(False)

        self.hl_buttons.addWidget(self.bt_show_chart_1)

        self.bt_export_xl_1 = QPushButton(self.layoutWidget1)
        self.bt_export_xl_1.setObjectName(u"bt_export_xl_1")
        self.bt_export_xl_1.setEnabled(False)
        self.bt_export_xl_1.setAutoDefault(False)

        self.hl_buttons.addWidget(self.bt_export_xl_1)

        self.layoutWidget2 = QWidget(self.tab)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(970, 0, 255, 468))
        self.vl_variables = QVBoxLayout(self.layoutWidget2)
        self.vl_variables.setObjectName(u"vl_variables")
        self.vl_variables.setContentsMargins(0, 0, 0, 0)
        self.hl_I0a = QHBoxLayout()
        self.hl_I0a.setSpacing(6)
        self.hl_I0a.setObjectName(u"hl_I0a")
        self.hl_I0a.setContentsMargins(2, -1, -1, -1)
        self.lb_I0a = QLabel(self.layoutWidget2)
        self.lb_I0a.setObjectName(u"lb_I0a")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_I0a.sizePolicy().hasHeightForWidth())
        self.lb_I0a.setSizePolicy(sizePolicy)

        self.hl_I0a.addWidget(self.lb_I0a)

        self.le_I0a = QLineEdit(self.layoutWidget2)
        self.le_I0a.setObjectName(u"le_I0a")
        self.le_I0a.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_I0a.sizePolicy().hasHeightForWidth())
        self.le_I0a.setSizePolicy(sizePolicy1)
        self.le_I0a.setMinimumSize(QSize(100, 32))

        self.hl_I0a.addWidget(self.le_I0a)


        self.vl_variables.addLayout(self.hl_I0a)

        self.hl_I0p = QHBoxLayout()
        self.hl_I0p.setObjectName(u"hl_I0p")
        self.hl_I0p.setContentsMargins(0, -1, -1, -1)
        self.lb_I0p = QLabel(self.layoutWidget2)
        self.lb_I0p.setObjectName(u"lb_I0p")
        sizePolicy.setHeightForWidth(self.lb_I0p.sizePolicy().hasHeightForWidth())
        self.lb_I0p.setSizePolicy(sizePolicy)

        self.hl_I0p.addWidget(self.lb_I0p)

        self.le_I0p = QLineEdit(self.layoutWidget2)
        self.le_I0p.setObjectName(u"le_I0p")
        self.le_I0p.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_I0p.sizePolicy().hasHeightForWidth())
        self.le_I0p.setSizePolicy(sizePolicy1)

        self.hl_I0p.addWidget(self.le_I0p)


        self.vl_variables.addLayout(self.hl_I0p)

        self.hl_Pst = QHBoxLayout()
        self.hl_Pst.setObjectName(u"hl_Pst")
        self.hl_Pst.setContentsMargins(-1, -1, 6, -1)
        self.lb_Pst = QLabel(self.layoutWidget2)
        self.lb_Pst.setObjectName(u"lb_Pst")
        sizePolicy.setHeightForWidth(self.lb_Pst.sizePolicy().hasHeightForWidth())
        self.lb_Pst.setSizePolicy(sizePolicy)

        self.hl_Pst.addWidget(self.lb_Pst)

        self.le_Pst = QLineEdit(self.layoutWidget2)
        self.le_Pst.setObjectName(u"le_Pst")
        self.le_Pst.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_Pst.sizePolicy().hasHeightForWidth())
        self.le_Pst.setSizePolicy(sizePolicy1)

        self.hl_Pst.addWidget(self.le_Pst)


        self.vl_variables.addLayout(self.hl_Pst)

        self.hl_Pmeh = QHBoxLayout()
        self.hl_Pmeh.setSpacing(0)
        self.hl_Pmeh.setObjectName(u"hl_Pmeh")
        self.hl_Pmeh.setContentsMargins(-1, -1, 6, -1)
        self.lb_Pmeh = QLabel(self.layoutWidget2)
        self.lb_Pmeh.setObjectName(u"lb_Pmeh")
        sizePolicy.setHeightForWidth(self.lb_Pmeh.sizePolicy().hasHeightForWidth())
        self.lb_Pmeh.setSizePolicy(sizePolicy)

        self.hl_Pmeh.addWidget(self.lb_Pmeh)

        self.le_Pmeh = QLineEdit(self.layoutWidget2)
        self.le_Pmeh.setObjectName(u"le_Pmeh")
        self.le_Pmeh.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(100)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.le_Pmeh.sizePolicy().hasHeightForWidth())
        self.le_Pmeh.setSizePolicy(sizePolicy2)
        self.le_Pmeh.setMinimumSize(QSize(20, 20))
        self.le_Pmeh.setSizeIncrement(QSize(100, 0))

        self.hl_Pmeh.addWidget(self.le_Pmeh)


        self.vl_variables.addLayout(self.hl_Pmeh)

        self.hl_r1 = QHBoxLayout()
        self.hl_r1.setObjectName(u"hl_r1")
        self.lb_r1 = QLabel(self.layoutWidget2)
        self.lb_r1.setObjectName(u"lb_r1")
        sizePolicy.setHeightForWidth(self.lb_r1.sizePolicy().hasHeightForWidth())
        self.lb_r1.setSizePolicy(sizePolicy)

        self.hl_r1.addWidget(self.lb_r1)

        self.le_r1 = QLineEdit(self.layoutWidget2)
        self.le_r1.setObjectName(u"le_r1")
        self.le_r1.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_r1.sizePolicy().hasHeightForWidth())
        self.le_r1.setSizePolicy(sizePolicy1)
        self.le_r1.setLayoutDirection(Qt.LeftToRight)

        self.hl_r1.addWidget(self.le_r1)


        self.vl_variables.addLayout(self.hl_r1)

        self.hl_r2_shtrih = QHBoxLayout()
        self.hl_r2_shtrih.setObjectName(u"hl_r2_shtrih")
        self.hl_r2_shtrih.setContentsMargins(0, -1, -1, -1)
        self.lb_r2_shtrih = QLabel(self.layoutWidget2)
        self.lb_r2_shtrih.setObjectName(u"lb_r2_shtrih")
        sizePolicy.setHeightForWidth(self.lb_r2_shtrih.sizePolicy().hasHeightForWidth())
        self.lb_r2_shtrih.setSizePolicy(sizePolicy)
        self.lb_r2_shtrih.setFrameShape(QFrame.NoFrame)

        self.hl_r2_shtrih.addWidget(self.lb_r2_shtrih)

        self.le_r2_shtrih = QLineEdit(self.layoutWidget2)
        self.le_r2_shtrih.setObjectName(u"le_r2_shtrih")
        self.le_r2_shtrih.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_r2_shtrih.sizePolicy().hasHeightForWidth())
        self.le_r2_shtrih.setSizePolicy(sizePolicy1)

        self.hl_r2_shtrih.addWidget(self.le_r2_shtrih)


        self.vl_variables.addLayout(self.hl_r2_shtrih)

        self.hl_c1 = QHBoxLayout()
        self.hl_c1.setObjectName(u"hl_c1")
        self.lb_c1 = QLabel(self.layoutWidget2)
        self.lb_c1.setObjectName(u"lb_c1")
        sizePolicy.setHeightForWidth(self.lb_c1.sizePolicy().hasHeightForWidth())
        self.lb_c1.setSizePolicy(sizePolicy)

        self.hl_c1.addWidget(self.lb_c1)

        self.le_c1 = QLineEdit(self.layoutWidget2)
        self.le_c1.setObjectName(u"le_c1")
        self.le_c1.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_c1.sizePolicy().hasHeightForWidth())
        self.le_c1.setSizePolicy(sizePolicy1)

        self.hl_c1.addWidget(self.le_c1)


        self.vl_variables.addLayout(self.hl_c1)

        self.hl_a_shtrih = QHBoxLayout()
        self.hl_a_shtrih.setObjectName(u"hl_a_shtrih")
        self.lb_a_shtrih = QLabel(self.layoutWidget2)
        self.lb_a_shtrih.setObjectName(u"lb_a_shtrih")
        sizePolicy.setHeightForWidth(self.lb_a_shtrih.sizePolicy().hasHeightForWidth())
        self.lb_a_shtrih.setSizePolicy(sizePolicy)

        self.hl_a_shtrih.addWidget(self.lb_a_shtrih)

        self.le_a_shtrih = QLineEdit(self.layoutWidget2)
        self.le_a_shtrih.setObjectName(u"le_a_shtrih")
        self.le_a_shtrih.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_a_shtrih.sizePolicy().hasHeightForWidth())
        self.le_a_shtrih.setSizePolicy(sizePolicy1)

        self.hl_a_shtrih.addWidget(self.le_a_shtrih)


        self.vl_variables.addLayout(self.hl_a_shtrih)

        self.hl_a = QHBoxLayout()
        self.hl_a.setObjectName(u"hl_a")
        self.lb_a = QLabel(self.layoutWidget2)
        self.lb_a.setObjectName(u"lb_a")
        sizePolicy.setHeightForWidth(self.lb_a.sizePolicy().hasHeightForWidth())
        self.lb_a.setSizePolicy(sizePolicy)

        self.hl_a.addWidget(self.lb_a)

        self.le_a = QLineEdit(self.layoutWidget2)
        self.le_a.setObjectName(u"le_a")
        self.le_a.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_a.sizePolicy().hasHeightForWidth())
        self.le_a.setSizePolicy(sizePolicy1)

        self.hl_a.addWidget(self.le_a)


        self.vl_variables.addLayout(self.hl_a)

        self.hl_b_shtrih = QHBoxLayout()
        self.hl_b_shtrih.setObjectName(u"hl_b_shtrih")
        self.lb_b_shtrih = QLabel(self.layoutWidget2)
        self.lb_b_shtrih.setObjectName(u"lb_b_shtrih")
        sizePolicy.setHeightForWidth(self.lb_b_shtrih.sizePolicy().hasHeightForWidth())
        self.lb_b_shtrih.setSizePolicy(sizePolicy)

        self.hl_b_shtrih.addWidget(self.lb_b_shtrih)

        self.le_b_shtrih = QLineEdit(self.layoutWidget2)
        self.le_b_shtrih.setObjectName(u"le_b_shtrih")
        self.le_b_shtrih.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_b_shtrih.sizePolicy().hasHeightForWidth())
        self.le_b_shtrih.setSizePolicy(sizePolicy1)

        self.hl_b_shtrih.addWidget(self.le_b_shtrih)


        self.vl_variables.addLayout(self.hl_b_shtrih)

        self.hl_b = QHBoxLayout()
        self.hl_b.setObjectName(u"hl_b")
        self.lb_b = QLabel(self.layoutWidget2)
        self.lb_b.setObjectName(u"lb_b")
        sizePolicy.setHeightForWidth(self.lb_b.sizePolicy().hasHeightForWidth())
        self.lb_b.setSizePolicy(sizePolicy)

        self.hl_b.addWidget(self.lb_b)

        self.le_b = QLineEdit(self.layoutWidget2)
        self.le_b.setObjectName(u"le_b")
        self.le_b.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_b.sizePolicy().hasHeightForWidth())
        self.le_b.setSizePolicy(sizePolicy1)

        self.hl_b.addWidget(self.le_b)


        self.vl_variables.addLayout(self.hl_b)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setEnabled(False)
        self.tableWidget_2 = QTableWidget(self.tab_2)
        if (self.tableWidget_2.columnCount() < 8):
            self.tableWidget_2.setColumnCount(8)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem85)
        if (self.tableWidget_2.rowCount() < 15):
            self.tableWidget_2.setRowCount(15)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        __qtablewidgetitem101.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        __qtablewidgetitem102.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        __qtablewidgetitem103.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        __qtablewidgetitem104.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 3, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        __qtablewidgetitem105.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 4, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        __qtablewidgetitem106.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 5, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        __qtablewidgetitem107.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 6, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        __qtablewidgetitem108.setFont(font1);
        self.tableWidget_2.setItem(0, 7, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        __qtablewidgetitem109.setFont(font1);
        __qtablewidgetitem109.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        __qtablewidgetitem110.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        __qtablewidgetitem111.setFont(font1);
        __qtablewidgetitem111.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(2, 0, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        __qtablewidgetitem112.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(2, 1, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        __qtablewidgetitem113.setFont(font1);
        __qtablewidgetitem113.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(3, 0, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        __qtablewidgetitem114.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(3, 1, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        __qtablewidgetitem115.setFont(font1);
        __qtablewidgetitem115.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(4, 0, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        __qtablewidgetitem116.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(4, 1, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        __qtablewidgetitem117.setFont(font1);
        __qtablewidgetitem117.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(5, 0, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        __qtablewidgetitem118.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(5, 1, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        __qtablewidgetitem119.setFont(font1);
        __qtablewidgetitem119.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(6, 0, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        __qtablewidgetitem120.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(6, 1, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        __qtablewidgetitem121.setFont(font1);
        __qtablewidgetitem121.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(7, 0, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        __qtablewidgetitem122.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(7, 1, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        __qtablewidgetitem123.setFont(font1);
        __qtablewidgetitem123.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(8, 0, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        __qtablewidgetitem124.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(8, 1, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        __qtablewidgetitem125.setFont(font1);
        __qtablewidgetitem125.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(9, 0, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        __qtablewidgetitem126.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(9, 1, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        __qtablewidgetitem127.setFont(font1);
        __qtablewidgetitem127.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(10, 0, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        __qtablewidgetitem128.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(10, 1, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        __qtablewidgetitem129.setFont(font1);
        __qtablewidgetitem129.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(11, 0, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        __qtablewidgetitem130.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(11, 1, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        __qtablewidgetitem131.setFont(font1);
        __qtablewidgetitem131.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(12, 0, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        __qtablewidgetitem132.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(12, 1, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        __qtablewidgetitem133.setFont(font1);
        __qtablewidgetitem133.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(13, 0, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        __qtablewidgetitem134.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(13, 1, __qtablewidgetitem134)
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        __qtablewidgetitem135 = QTableWidgetItem()
        __qtablewidgetitem135.setFont(font4);
        __qtablewidgetitem135.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(14, 0, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        __qtablewidgetitem136.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(14, 1, __qtablewidgetitem136)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setEnabled(False)
        self.tableWidget_2.setGeometry(QRect(0, 0, 1031, 511))
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(170)
        self.layoutWidget3 = QWidget(self.tab_2)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(0, 510, 207, 36))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bt_check_table_2 = QPushButton(self.layoutWidget3)
        self.bt_check_table_2.setObjectName(u"bt_check_table_2")

        self.horizontalLayout_4.addWidget(self.bt_check_table_2)

        self.bt_calculate_table2 = QPushButton(self.layoutWidget3)
        self.bt_calculate_table2.setObjectName(u"bt_calculate_table2")

        self.horizontalLayout_4.addWidget(self.bt_calculate_table2)

        self.layoutWidget_2 = QWidget(self.tab_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(1050, 0, 266, 762))
        self.vl_variables_t2 = QVBoxLayout(self.layoutWidget_2)
        self.vl_variables_t2.setObjectName(u"vl_variables_t2")
        self.vl_variables_t2.setContentsMargins(0, 0, 0, 0)
        self.hl_h_c = QHBoxLayout()
        self.hl_h_c.setSpacing(6)
        self.hl_h_c.setObjectName(u"hl_h_c")
        self.hl_h_c.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.hl_h_c.setContentsMargins(2, -1, -1, -1)
        self.lb_h_c = QLabel(self.layoutWidget_2)
        self.lb_h_c.setObjectName(u"lb_h_c")
        sizePolicy.setHeightForWidth(self.lb_h_c.sizePolicy().hasHeightForWidth())
        self.lb_h_c.setSizePolicy(sizePolicy)

        self.hl_h_c.addWidget(self.lb_h_c)

        self.le_h_c = QLineEdit(self.layoutWidget_2)
        self.le_h_c.setObjectName(u"le_h_c")
        self.le_h_c.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_h_c.sizePolicy().hasHeightForWidth())
        self.le_h_c.setSizePolicy(sizePolicy1)
        self.le_h_c.setMinimumSize(QSize(50, 32))
        self.le_h_c.setSizeIncrement(QSize(0, 0))
        self.le_h_c.setBaseSize(QSize(0, 0))
        self.le_h_c.setLayoutDirection(Qt.LeftToRight)
        self.le_h_c.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.hl_h_c.addWidget(self.le_h_c)


        self.vl_variables_t2.addLayout(self.hl_h_c)

        self.hl_h_p_2 = QHBoxLayout()
        self.hl_h_p_2.setObjectName(u"hl_h_p_2")
        self.hl_h_p_2.setContentsMargins(0, -1, -1, -1)
        self.lb_h_p_2 = QLabel(self.layoutWidget_2)
        self.lb_h_p_2.setObjectName(u"lb_h_p_2")
        sizePolicy.setHeightForWidth(self.lb_h_p_2.sizePolicy().hasHeightForWidth())
        self.lb_h_p_2.setSizePolicy(sizePolicy)

        self.hl_h_p_2.addWidget(self.lb_h_p_2)

        self.le_h_p_2 = QLineEdit(self.layoutWidget_2)
        self.le_h_p_2.setObjectName(u"le_h_p_2")
        self.le_h_p_2.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_h_p_2.sizePolicy().hasHeightForWidth())
        self.le_h_p_2.setSizePolicy(sizePolicy1)

        self.hl_h_p_2.addWidget(self.le_h_p_2)


        self.vl_variables_t2.addLayout(self.hl_h_p_2)

        self.hl_h_sh = QHBoxLayout()
        self.hl_h_sh.setObjectName(u"hl_h_sh")
        self.hl_h_sh.setContentsMargins(-1, -1, 6, -1)
        self.lb_h_sh = QLabel(self.layoutWidget_2)
        self.lb_h_sh.setObjectName(u"lb_h_sh")
        sizePolicy.setHeightForWidth(self.lb_h_sh.sizePolicy().hasHeightForWidth())
        self.lb_h_sh.setSizePolicy(sizePolicy)

        self.hl_h_sh.addWidget(self.lb_h_sh)

        self.le_h_sh = QLineEdit(self.layoutWidget_2)
        self.le_h_sh.setObjectName(u"le_h_sh")
        self.le_h_sh.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_h_sh.sizePolicy().hasHeightForWidth())
        self.le_h_sh.setSizePolicy(sizePolicy1)

        self.hl_h_sh.addWidget(self.le_h_sh)


        self.vl_variables_t2.addLayout(self.hl_h_sh)

        self.hl_h_sh_shtrih = QHBoxLayout()
        self.hl_h_sh_shtrih.setSpacing(0)
        self.hl_h_sh_shtrih.setObjectName(u"hl_h_sh_shtrih")
        self.hl_h_sh_shtrih.setContentsMargins(-1, -1, 6, -1)
        self.lb_h_sh_shtrih = QLabel(self.layoutWidget_2)
        self.lb_h_sh_shtrih.setObjectName(u"lb_h_sh_shtrih")
        sizePolicy.setHeightForWidth(self.lb_h_sh_shtrih.sizePolicy().hasHeightForWidth())
        self.lb_h_sh_shtrih.setSizePolicy(sizePolicy)

        self.hl_h_sh_shtrih.addWidget(self.lb_h_sh_shtrih)

        self.le_h_sh_shtrih = QLineEdit(self.layoutWidget_2)
        self.le_h_sh_shtrih.setObjectName(u"le_h_sh_shtrih")
        self.le_h_sh_shtrih.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.le_h_sh_shtrih.sizePolicy().hasHeightForWidth())
        self.le_h_sh_shtrih.setSizePolicy(sizePolicy2)
        self.le_h_sh_shtrih.setMinimumSize(QSize(20, 20))
        self.le_h_sh_shtrih.setSizeIncrement(QSize(100, 0))

        self.hl_h_sh_shtrih.addWidget(self.le_h_sh_shtrih)


        self.vl_variables_t2.addLayout(self.hl_h_sh_shtrih)

        self.hl_b_1_r = QHBoxLayout()
        self.hl_b_1_r.setObjectName(u"hl_b_1_r")
        self.lb_b_1_r = QLabel(self.layoutWidget_2)
        self.lb_b_1_r.setObjectName(u"lb_b_1_r")
        sizePolicy.setHeightForWidth(self.lb_b_1_r.sizePolicy().hasHeightForWidth())
        self.lb_b_1_r.setSizePolicy(sizePolicy)

        self.hl_b_1_r.addWidget(self.lb_b_1_r)

        self.le_b_1_r = QLineEdit(self.layoutWidget_2)
        self.le_b_1_r.setObjectName(u"le_b_1_r")
        self.le_b_1_r.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_b_1_r.sizePolicy().hasHeightForWidth())
        self.le_b_1_r.setSizePolicy(sizePolicy1)
        self.le_b_1_r.setLayoutDirection(Qt.LeftToRight)

        self.hl_b_1_r.addWidget(self.le_b_1_r)


        self.vl_variables_t2.addLayout(self.hl_b_1_r)

        self.hl_b_2_r = QHBoxLayout()
        self.hl_b_2_r.setObjectName(u"hl_b_2_r")
        self.hl_b_2_r.setContentsMargins(0, -1, -1, -1)
        self.lb_b_2_r = QLabel(self.layoutWidget_2)
        self.lb_b_2_r.setObjectName(u"lb_b_2_r")
        sizePolicy.setHeightForWidth(self.lb_b_2_r.sizePolicy().hasHeightForWidth())
        self.lb_b_2_r.setSizePolicy(sizePolicy)
        self.lb_b_2_r.setFrameShape(QFrame.NoFrame)

        self.hl_b_2_r.addWidget(self.lb_b_2_r)

        self.le_b_2_r = QLineEdit(self.layoutWidget_2)
        self.le_b_2_r.setObjectName(u"le_b_2_r")
        self.le_b_2_r.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_b_2_r.sizePolicy().hasHeightForWidth())
        self.le_b_2_r.setSizePolicy(sizePolicy1)

        self.hl_b_2_r.addWidget(self.le_b_2_r)


        self.vl_variables_t2.addLayout(self.hl_b_2_r)

        self.hl_h_1 = QHBoxLayout()
        self.hl_h_1.setObjectName(u"hl_h_1")
        self.lb_h_1 = QLabel(self.layoutWidget_2)
        self.lb_h_1.setObjectName(u"lb_h_1")
        sizePolicy.setHeightForWidth(self.lb_h_1.sizePolicy().hasHeightForWidth())
        self.lb_h_1.setSizePolicy(sizePolicy)

        self.hl_h_1.addWidget(self.lb_h_1)

        self.le_h_1 = QLineEdit(self.layoutWidget_2)
        self.le_h_1.setObjectName(u"le_h_1")
        self.le_h_1.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_h_1.sizePolicy().hasHeightForWidth())
        self.le_h_1.setSizePolicy(sizePolicy1)

        self.hl_h_1.addWidget(self.le_h_1)


        self.vl_variables_t2.addLayout(self.hl_h_1)

        self.hl_q_c = QHBoxLayout()
        self.hl_q_c.setObjectName(u"hl_q_c")
        self.lb_q_c = QLabel(self.layoutWidget_2)
        self.lb_q_c.setObjectName(u"lb_q_c")
        sizePolicy.setHeightForWidth(self.lb_q_c.sizePolicy().hasHeightForWidth())
        self.lb_q_c.setSizePolicy(sizePolicy)

        self.hl_q_c.addWidget(self.lb_q_c)

        self.le_q_c = QLineEdit(self.layoutWidget_2)
        self.le_q_c.setObjectName(u"le_q_c")
        self.le_q_c.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_q_c.sizePolicy().hasHeightForWidth())
        self.le_q_c.setSizePolicy(sizePolicy1)

        self.hl_q_c.addWidget(self.le_q_c)


        self.vl_variables_t2.addLayout(self.hl_q_c)

        self.hl_r_c = QHBoxLayout()
        self.hl_r_c.setObjectName(u"hl_r_c")
        self.lb_r_c = QLabel(self.layoutWidget_2)
        self.lb_r_c.setObjectName(u"lb_r_c")
        sizePolicy.setHeightForWidth(self.lb_r_c.sizePolicy().hasHeightForWidth())
        self.lb_r_c.setSizePolicy(sizePolicy)

        self.hl_r_c.addWidget(self.lb_r_c)

        self.le_r_c = QLineEdit(self.layoutWidget_2)
        self.le_r_c.setObjectName(u"le_r_c")
        self.le_r_c.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_r_c.sizePolicy().hasHeightForWidth())
        self.le_r_c.setSizePolicy(sizePolicy1)

        self.hl_r_c.addWidget(self.le_r_c)


        self.vl_variables_t2.addLayout(self.hl_r_c)

        self.hl_r_2 = QHBoxLayout()
        self.hl_r_2.setObjectName(u"hl_r_2")
        self.lb_r_2 = QLabel(self.layoutWidget_2)
        self.lb_r_2.setObjectName(u"lb_r_2")
        sizePolicy.setHeightForWidth(self.lb_r_2.sizePolicy().hasHeightForWidth())
        self.lb_r_2.setSizePolicy(sizePolicy)

        self.hl_r_2.addWidget(self.lb_r_2)

        self.le_r_2 = QLineEdit(self.layoutWidget_2)
        self.le_r_2.setObjectName(u"le_r_2")
        self.le_r_2.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_r_2.sizePolicy().hasHeightForWidth())
        self.le_r_2.setSizePolicy(sizePolicy1)

        self.hl_r_2.addWidget(self.le_r_2)


        self.vl_variables_t2.addLayout(self.hl_r_2)

        self.hl_h_0 = QHBoxLayout()
        self.hl_h_0.setObjectName(u"hl_h_0")
        self.lb_h_0 = QLabel(self.layoutWidget_2)
        self.lb_h_0.setObjectName(u"lb_h_0")
        sizePolicy.setHeightForWidth(self.lb_h_0.sizePolicy().hasHeightForWidth())
        self.lb_h_0.setSizePolicy(sizePolicy)

        self.hl_h_0.addWidget(self.lb_h_0)

        self.le_h_0 = QLineEdit(self.layoutWidget_2)
        self.le_h_0.setObjectName(u"le_h_0")
        self.le_h_0.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_h_0.sizePolicy().hasHeightForWidth())
        self.le_h_0.setSizePolicy(sizePolicy1)

        self.hl_h_0.addWidget(self.le_h_0)


        self.vl_variables_t2.addLayout(self.hl_h_0)

        self.hl_b_sh_2 = QHBoxLayout()
        self.hl_b_sh_2.setObjectName(u"hl_b_sh_2")
        self.lb_b_sh_2 = QLabel(self.layoutWidget_2)
        self.lb_b_sh_2.setObjectName(u"lb_b_sh_2")
        sizePolicy.setHeightForWidth(self.lb_b_sh_2.sizePolicy().hasHeightForWidth())
        self.lb_b_sh_2.setSizePolicy(sizePolicy)

        self.hl_b_sh_2.addWidget(self.lb_b_sh_2)

        self.le_b_sh_2 = QLineEdit(self.layoutWidget_2)
        self.le_b_sh_2.setObjectName(u"le_b_sh_2")
        self.le_b_sh_2.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_b_sh_2.sizePolicy().hasHeightForWidth())
        self.le_b_sh_2.setSizePolicy(sizePolicy1)

        self.hl_b_sh_2.addWidget(self.le_b_sh_2)


        self.vl_variables_t2.addLayout(self.hl_b_sh_2)

        self.hl_Lamda_p_2 = QHBoxLayout()
        self.hl_Lamda_p_2.setObjectName(u"hl_Lamda_p_2")
        self.lb_Lamda_p_2 = QLabel(self.layoutWidget_2)
        self.lb_Lamda_p_2.setObjectName(u"lb_Lamda_p_2")
        sizePolicy.setHeightForWidth(self.lb_Lamda_p_2.sizePolicy().hasHeightForWidth())
        self.lb_Lamda_p_2.setSizePolicy(sizePolicy)

        self.hl_Lamda_p_2.addWidget(self.lb_Lamda_p_2)

        self.le_Lamda_p_2 = QLineEdit(self.layoutWidget_2)
        self.le_Lamda_p_2.setObjectName(u"le_Lamda_p_2")
        self.le_Lamda_p_2.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_Lamda_p_2.sizePolicy().hasHeightForWidth())
        self.le_Lamda_p_2.setSizePolicy(sizePolicy1)

        self.hl_Lamda_p_2.addWidget(self.le_Lamda_p_2)


        self.vl_variables_t2.addLayout(self.hl_Lamda_p_2)

        self.hl_Lamda_l_2 = QHBoxLayout()
        self.hl_Lamda_l_2.setObjectName(u"hl_Lamda_l_2")
        self.lb_Lamda_l_2 = QLabel(self.layoutWidget_2)
        self.lb_Lamda_l_2.setObjectName(u"lb_Lamda_l_2")
        sizePolicy.setHeightForWidth(self.lb_Lamda_l_2.sizePolicy().hasHeightForWidth())
        self.lb_Lamda_l_2.setSizePolicy(sizePolicy)

        self.hl_Lamda_l_2.addWidget(self.lb_Lamda_l_2)

        self.le_Lamda_l_2 = QLineEdit(self.layoutWidget_2)
        self.le_Lamda_l_2.setObjectName(u"le_Lamda_l_2")
        self.le_Lamda_l_2.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_Lamda_l_2.sizePolicy().hasHeightForWidth())
        self.le_Lamda_l_2.setSizePolicy(sizePolicy1)

        self.hl_Lamda_l_2.addWidget(self.le_Lamda_l_2)


        self.vl_variables_t2.addLayout(self.hl_Lamda_l_2)

        self.hl_Lamda_d_2 = QHBoxLayout()
        self.hl_Lamda_d_2.setObjectName(u"hl_Lamda_d_2")
        self.lb_Lamda_d_2 = QLabel(self.layoutWidget_2)
        self.lb_Lamda_d_2.setObjectName(u"lb_Lamda_d_2")
        sizePolicy.setHeightForWidth(self.lb_Lamda_d_2.sizePolicy().hasHeightForWidth())
        self.lb_Lamda_d_2.setSizePolicy(sizePolicy)

        self.hl_Lamda_d_2.addWidget(self.lb_Lamda_d_2)

        self.le_Lamda_d_2 = QLineEdit(self.layoutWidget_2)
        self.le_Lamda_d_2.setObjectName(u"le_Lamda_d_2")
        self.le_Lamda_d_2.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_Lamda_d_2.sizePolicy().hasHeightForWidth())
        self.le_Lamda_d_2.setSizePolicy(sizePolicy1)

        self.hl_Lamda_d_2.addWidget(self.le_Lamda_d_2)


        self.vl_variables_t2.addLayout(self.hl_Lamda_d_2)

        self.hl_X_2_shtrih = QHBoxLayout()
        self.hl_X_2_shtrih.setObjectName(u"hl_X_2_shtrih")
        self.lb_X_2_shtrih = QLabel(self.layoutWidget_2)
        self.lb_X_2_shtrih.setObjectName(u"lb_X_2_shtrih")
        sizePolicy.setHeightForWidth(self.lb_X_2_shtrih.sizePolicy().hasHeightForWidth())
        self.lb_X_2_shtrih.setSizePolicy(sizePolicy)

        self.hl_X_2_shtrih.addWidget(self.lb_X_2_shtrih)

        self.le_X_2_shtrih = QLineEdit(self.layoutWidget_2)
        self.le_X_2_shtrih.setObjectName(u"le_X_2_shtrih")
        self.le_X_2_shtrih.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_X_2_shtrih.sizePolicy().hasHeightForWidth())
        self.le_X_2_shtrih.setSizePolicy(sizePolicy1)

        self.hl_X_2_shtrih.addWidget(self.le_X_2_shtrih)


        self.vl_variables_t2.addLayout(self.hl_X_2_shtrih)

        self.hl_x_1_2_p = QHBoxLayout()
        self.hl_x_1_2_p.setObjectName(u"hl_x_1_2_p")
        self.lb_x_1_2_p = QLabel(self.layoutWidget_2)
        self.lb_x_1_2_p.setObjectName(u"lb_x_1_2_p")
        sizePolicy.setHeightForWidth(self.lb_x_1_2_p.sizePolicy().hasHeightForWidth())
        self.lb_x_1_2_p.setSizePolicy(sizePolicy)

        self.hl_x_1_2_p.addWidget(self.lb_x_1_2_p)

        self.le_x_1_2_p = QLineEdit(self.layoutWidget_2)
        self.le_x_1_2_p.setObjectName(u"le_x_1_2_p")
        self.le_x_1_2_p.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_x_1_2_p.sizePolicy().hasHeightForWidth())
        self.le_x_1_2_p.setSizePolicy(sizePolicy1)

        self.hl_x_1_2_p.addWidget(self.le_x_1_2_p)


        self.vl_variables_t2.addLayout(self.hl_x_1_2_p)

        self.hl_c_1_p = QHBoxLayout()
        self.hl_c_1_p.setObjectName(u"hl_c_1_p")
        self.lb_c_1_p = QLabel(self.layoutWidget_2)
        self.lb_c_1_p.setObjectName(u"lb_c_1_p")
        sizePolicy.setHeightForWidth(self.lb_c_1_p.sizePolicy().hasHeightForWidth())
        self.lb_c_1_p.setSizePolicy(sizePolicy)

        self.hl_c_1_p.addWidget(self.lb_c_1_p)

        self.le_c_1_p = QLineEdit(self.layoutWidget_2)
        self.le_c_1_p.setObjectName(u"le_c_1_p")
        self.le_c_1_p.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_c_1_p.sizePolicy().hasHeightForWidth())
        self.le_c_1_p.setSizePolicy(sizePolicy1)

        self.hl_c_1_p.addWidget(self.le_c_1_p)


        self.vl_variables_t2.addLayout(self.hl_c_1_p)

        self.hl_X_1 = QHBoxLayout()
        self.hl_X_1.setObjectName(u"hl_X_1")
        self.lb_X_1 = QLabel(self.layoutWidget_2)
        self.lb_X_1.setObjectName(u"lb_X_1")
        sizePolicy.setHeightForWidth(self.lb_X_1.sizePolicy().hasHeightForWidth())
        self.lb_X_1.setSizePolicy(sizePolicy)

        self.hl_X_1.addWidget(self.lb_X_1)

        self.le_X_1 = QLineEdit(self.layoutWidget_2)
        self.le_X_1.setObjectName(u"le_X_1")
        self.le_X_1.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_X_1.sizePolicy().hasHeightForWidth())
        self.le_X_1.setSizePolicy(sizePolicy1)

        self.hl_X_1.addWidget(self.le_X_1)


        self.vl_variables_t2.addLayout(self.hl_X_1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setEnabled(False)
        self.tableWidget_3 = QTableWidget(self.tab_3)
        if (self.tableWidget_3.columnCount() < 8):
            self.tableWidget_3.setColumnCount(8)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem143)
        __qtablewidgetitem144 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem144)
        if (self.tableWidget_3.rowCount() < 21):
            self.tableWidget_3.setRowCount(21)
        __qtablewidgetitem145 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(6, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(7, __qtablewidgetitem152)
        __qtablewidgetitem153 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(8, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(9, __qtablewidgetitem154)
        __qtablewidgetitem155 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(10, __qtablewidgetitem155)
        __qtablewidgetitem156 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(11, __qtablewidgetitem156)
        __qtablewidgetitem157 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(12, __qtablewidgetitem157)
        __qtablewidgetitem158 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(13, __qtablewidgetitem158)
        __qtablewidgetitem159 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(14, __qtablewidgetitem159)
        __qtablewidgetitem160 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(15, __qtablewidgetitem160)
        __qtablewidgetitem161 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(16, __qtablewidgetitem161)
        __qtablewidgetitem162 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(17, __qtablewidgetitem162)
        __qtablewidgetitem163 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(18, __qtablewidgetitem163)
        __qtablewidgetitem164 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(19, __qtablewidgetitem164)
        __qtablewidgetitem165 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(20, __qtablewidgetitem165)
        __qtablewidgetitem166 = QTableWidgetItem()
        __qtablewidgetitem166.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_3.setItem(0, 2, __qtablewidgetitem166)
        __qtablewidgetitem167 = QTableWidgetItem()
        __qtablewidgetitem167.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_3.setItem(0, 3, __qtablewidgetitem167)
        __qtablewidgetitem168 = QTableWidgetItem()
        __qtablewidgetitem168.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_3.setItem(0, 4, __qtablewidgetitem168)
        __qtablewidgetitem169 = QTableWidgetItem()
        __qtablewidgetitem169.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_3.setItem(0, 5, __qtablewidgetitem169)
        __qtablewidgetitem170 = QTableWidgetItem()
        __qtablewidgetitem170.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_3.setItem(0, 6, __qtablewidgetitem170)
        __qtablewidgetitem171 = QTableWidgetItem()
        __qtablewidgetitem171.setFont(font1);
        self.tableWidget_3.setItem(0, 7, __qtablewidgetitem171)
        __qtablewidgetitem172 = QTableWidgetItem()
        __qtablewidgetitem172.setFont(font1);
        __qtablewidgetitem172.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(1, 0, __qtablewidgetitem172)
        __qtablewidgetitem173 = QTableWidgetItem()
        __qtablewidgetitem173.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(1, 1, __qtablewidgetitem173)
        __qtablewidgetitem174 = QTableWidgetItem()
        __qtablewidgetitem174.setFont(font4);
        __qtablewidgetitem174.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(2, 0, __qtablewidgetitem174)
        __qtablewidgetitem175 = QTableWidgetItem()
        __qtablewidgetitem175.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(2, 1, __qtablewidgetitem175)
        __qtablewidgetitem176 = QTableWidgetItem()
        __qtablewidgetitem176.setFont(font4);
        __qtablewidgetitem176.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(3, 0, __qtablewidgetitem176)
        __qtablewidgetitem177 = QTableWidgetItem()
        __qtablewidgetitem177.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(3, 1, __qtablewidgetitem177)
        __qtablewidgetitem178 = QTableWidgetItem()
        __qtablewidgetitem178.setFont(font1);
        __qtablewidgetitem178.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(4, 0, __qtablewidgetitem178)
        __qtablewidgetitem179 = QTableWidgetItem()
        __qtablewidgetitem179.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(4, 1, __qtablewidgetitem179)
        __qtablewidgetitem180 = QTableWidgetItem()
        self.tableWidget_3.setItem(4, 2, __qtablewidgetitem180)
        __qtablewidgetitem181 = QTableWidgetItem()
        __qtablewidgetitem181.setFont(font1);
        __qtablewidgetitem181.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(5, 0, __qtablewidgetitem181)
        __qtablewidgetitem182 = QTableWidgetItem()
        __qtablewidgetitem182.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(5, 1, __qtablewidgetitem182)
        __qtablewidgetitem183 = QTableWidgetItem()
        __qtablewidgetitem183.setFont(font1);
        __qtablewidgetitem183.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(6, 0, __qtablewidgetitem183)
        __qtablewidgetitem184 = QTableWidgetItem()
        __qtablewidgetitem184.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(6, 1, __qtablewidgetitem184)
        __qtablewidgetitem185 = QTableWidgetItem()
        __qtablewidgetitem185.setFont(font1);
        __qtablewidgetitem185.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(7, 0, __qtablewidgetitem185)
        __qtablewidgetitem186 = QTableWidgetItem()
        __qtablewidgetitem186.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(7, 1, __qtablewidgetitem186)
        __qtablewidgetitem187 = QTableWidgetItem()
        __qtablewidgetitem187.setFont(font1);
        __qtablewidgetitem187.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(8, 0, __qtablewidgetitem187)
        __qtablewidgetitem188 = QTableWidgetItem()
        __qtablewidgetitem188.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(8, 1, __qtablewidgetitem188)
        __qtablewidgetitem189 = QTableWidgetItem()
        __qtablewidgetitem189.setFont(font1);
        __qtablewidgetitem189.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(9, 0, __qtablewidgetitem189)
        __qtablewidgetitem190 = QTableWidgetItem()
        __qtablewidgetitem190.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(9, 1, __qtablewidgetitem190)
        __qtablewidgetitem191 = QTableWidgetItem()
        __qtablewidgetitem191.setFont(font1);
        __qtablewidgetitem191.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(10, 0, __qtablewidgetitem191)
        __qtablewidgetitem192 = QTableWidgetItem()
        __qtablewidgetitem192.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(10, 1, __qtablewidgetitem192)
        __qtablewidgetitem193 = QTableWidgetItem()
        __qtablewidgetitem193.setFont(font1);
        __qtablewidgetitem193.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(11, 0, __qtablewidgetitem193)
        __qtablewidgetitem194 = QTableWidgetItem()
        __qtablewidgetitem194.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(11, 1, __qtablewidgetitem194)
        __qtablewidgetitem195 = QTableWidgetItem()
        __qtablewidgetitem195.setFont(font1);
        __qtablewidgetitem195.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(12, 0, __qtablewidgetitem195)
        __qtablewidgetitem196 = QTableWidgetItem()
        __qtablewidgetitem196.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(12, 1, __qtablewidgetitem196)
        __qtablewidgetitem197 = QTableWidgetItem()
        __qtablewidgetitem197.setFont(font1);
        __qtablewidgetitem197.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(13, 0, __qtablewidgetitem197)
        __qtablewidgetitem198 = QTableWidgetItem()
        __qtablewidgetitem198.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(13, 1, __qtablewidgetitem198)
        __qtablewidgetitem199 = QTableWidgetItem()
        __qtablewidgetitem199.setFont(font4);
        __qtablewidgetitem199.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(14, 0, __qtablewidgetitem199)
        __qtablewidgetitem200 = QTableWidgetItem()
        __qtablewidgetitem200.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(14, 1, __qtablewidgetitem200)
        __qtablewidgetitem201 = QTableWidgetItem()
        __qtablewidgetitem201.setFont(font4);
        __qtablewidgetitem201.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(15, 0, __qtablewidgetitem201)
        __qtablewidgetitem202 = QTableWidgetItem()
        __qtablewidgetitem202.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(15, 1, __qtablewidgetitem202)
        __qtablewidgetitem203 = QTableWidgetItem()
        __qtablewidgetitem203.setFont(font4);
        __qtablewidgetitem203.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(16, 0, __qtablewidgetitem203)
        __qtablewidgetitem204 = QTableWidgetItem()
        __qtablewidgetitem204.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(16, 1, __qtablewidgetitem204)
        __qtablewidgetitem205 = QTableWidgetItem()
        __qtablewidgetitem205.setFont(font4);
        __qtablewidgetitem205.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(17, 0, __qtablewidgetitem205)
        __qtablewidgetitem206 = QTableWidgetItem()
        __qtablewidgetitem206.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(17, 1, __qtablewidgetitem206)
        __qtablewidgetitem207 = QTableWidgetItem()
        __qtablewidgetitem207.setFont(font4);
        __qtablewidgetitem207.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(18, 0, __qtablewidgetitem207)
        __qtablewidgetitem208 = QTableWidgetItem()
        __qtablewidgetitem208.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(18, 1, __qtablewidgetitem208)
        __qtablewidgetitem209 = QTableWidgetItem()
        __qtablewidgetitem209.setFont(font1);
        __qtablewidgetitem209.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(19, 0, __qtablewidgetitem209)
        __qtablewidgetitem210 = QTableWidgetItem()
        __qtablewidgetitem210.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(19, 1, __qtablewidgetitem210)
        __qtablewidgetitem211 = QTableWidgetItem()
        __qtablewidgetitem211.setFont(font1);
        __qtablewidgetitem211.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(20, 0, __qtablewidgetitem211)
        __qtablewidgetitem212 = QTableWidgetItem()
        __qtablewidgetitem212.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_3.setItem(20, 1, __qtablewidgetitem212)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(0, 0, 1111, 681))
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(170)
        self.layoutWidget4 = QWidget(self.tab_3)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(0, 690, 369, 62))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bt_check_table_3 = QPushButton(self.layoutWidget4)
        self.bt_check_table_3.setObjectName(u"bt_check_table_3")

        self.horizontalLayout.addWidget(self.bt_check_table_3)

        self.bt_calculate_table3 = QPushButton(self.layoutWidget4)
        self.bt_calculate_table3.setObjectName(u"bt_calculate_table3")

        self.horizontalLayout.addWidget(self.bt_calculate_table3)

        self.bt_show_chart_table3 = QPushButton(self.layoutWidget4)
        self.bt_show_chart_table3.setObjectName(u"bt_show_chart_table3")
        self.bt_show_chart_table3.setEnabled(False)

        self.horizontalLayout.addWidget(self.bt_show_chart_table3)

        self.layoutWidget_3 = QWidget(self.tab_3)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(1120, 0, 266, 802))
        self.vl_variables_t3 = QVBoxLayout(self.layoutWidget_3)
        self.vl_variables_t3.setObjectName(u"vl_variables_t3")
        self.vl_variables_t3.setContentsMargins(0, 0, 0, 0)
        self.hl_C_N = QHBoxLayout()
        self.hl_C_N.setSpacing(6)
        self.hl_C_N.setObjectName(u"hl_C_N")
        self.hl_C_N.setContentsMargins(2, -1, -1, -1)
        self.lb_C_N = QLabel(self.layoutWidget_3)
        self.lb_C_N.setObjectName(u"lb_C_N")
        sizePolicy.setHeightForWidth(self.lb_C_N.sizePolicy().hasHeightForWidth())
        self.lb_C_N.setSizePolicy(sizePolicy)

        self.hl_C_N.addWidget(self.lb_C_N)

        self.le_C_N = QLineEdit(self.layoutWidget_3)
        self.le_C_N.setObjectName(u"le_C_N")
        self.le_C_N.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_C_N.sizePolicy().hasHeightForWidth())
        self.le_C_N.setSizePolicy(sizePolicy1)
        self.le_C_N.setMinimumSize(QSize(100, 32))

        self.hl_C_N.addWidget(self.le_C_N)


        self.vl_variables_t3.addLayout(self.hl_C_N)

        self.hl_k_y_1 = QHBoxLayout()
        self.hl_k_y_1.setObjectName(u"hl_k_y_1")
        self.hl_k_y_1.setContentsMargins(0, -1, -1, -1)
        self.lb_k_y_1 = QLabel(self.layoutWidget_3)
        self.lb_k_y_1.setObjectName(u"lb_k_y_1")
        sizePolicy.setHeightForWidth(self.lb_k_y_1.sizePolicy().hasHeightForWidth())
        self.lb_k_y_1.setSizePolicy(sizePolicy)

        self.hl_k_y_1.addWidget(self.lb_k_y_1)

        self.le_k_y_1 = QLineEdit(self.layoutWidget_3)
        self.le_k_y_1.setObjectName(u"le_k_y_1")
        self.le_k_y_1.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_k_y_1.sizePolicy().hasHeightForWidth())
        self.le_k_y_1.setSizePolicy(sizePolicy1)

        self.hl_k_y_1.addWidget(self.le_k_y_1)


        self.vl_variables_t3.addLayout(self.hl_k_y_1)

        self.hl_u_p = QHBoxLayout()
        self.hl_u_p.setObjectName(u"hl_u_p")
        self.hl_u_p.setContentsMargins(-1, -1, 6, -1)
        self.lb_u_p = QLabel(self.layoutWidget_3)
        self.lb_u_p.setObjectName(u"lb_u_p")
        sizePolicy.setHeightForWidth(self.lb_u_p.sizePolicy().hasHeightForWidth())
        self.lb_u_p.setSizePolicy(sizePolicy)

        self.hl_u_p.addWidget(self.lb_u_p)

        self.le_u_p = QLineEdit(self.layoutWidget_3)
        self.le_u_p.setObjectName(u"le_u_p")
        self.le_u_p.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_u_p.sizePolicy().hasHeightForWidth())
        self.le_u_p.setSizePolicy(sizePolicy1)

        self.hl_u_p.addWidget(self.le_u_p)


        self.vl_variables_t3.addLayout(self.hl_u_p)

        self.hl_k_ob = QHBoxLayout()
        self.hl_k_ob.setSpacing(0)
        self.hl_k_ob.setObjectName(u"hl_k_ob")
        self.hl_k_ob.setContentsMargins(-1, -1, 6, -1)
        self.lb_k_ob = QLabel(self.layoutWidget_3)
        self.lb_k_ob.setObjectName(u"lb_k_ob")
        sizePolicy.setHeightForWidth(self.lb_k_ob.sizePolicy().hasHeightForWidth())
        self.lb_k_ob.setSizePolicy(sizePolicy)

        self.hl_k_ob.addWidget(self.lb_k_ob)

        self.le_k_ob = QLineEdit(self.layoutWidget_3)
        self.le_k_ob.setObjectName(u"le_k_ob")
        self.le_k_ob.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.le_k_ob.sizePolicy().hasHeightForWidth())
        self.le_k_ob.setSizePolicy(sizePolicy2)
        self.le_k_ob.setMinimumSize(QSize(20, 20))
        self.le_k_ob.setSizeIncrement(QSize(100, 0))

        self.hl_k_ob.addWidget(self.le_k_ob)


        self.vl_variables_t3.addLayout(self.hl_k_ob)

        self.hl_Z_1 = QHBoxLayout()
        self.hl_Z_1.setObjectName(u"hl_Z_1")
        self.lb_Z_1 = QLabel(self.layoutWidget_3)
        self.lb_Z_1.setObjectName(u"lb_Z_1")
        sizePolicy.setHeightForWidth(self.lb_Z_1.sizePolicy().hasHeightForWidth())
        self.lb_Z_1.setSizePolicy(sizePolicy)

        self.hl_Z_1.addWidget(self.lb_Z_1)

        self.le_Z_1 = QLineEdit(self.layoutWidget_3)
        self.le_Z_1.setObjectName(u"le_Z_1")
        self.le_Z_1.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_Z_1.sizePolicy().hasHeightForWidth())
        self.le_Z_1.setSizePolicy(sizePolicy1)
        self.le_Z_1.setLayoutDirection(Qt.LeftToRight)

        self.hl_Z_1.addWidget(self.le_Z_1)


        self.vl_variables_t3.addLayout(self.hl_Z_1)

        self.hl_Z_2 = QHBoxLayout()
        self.hl_Z_2.setObjectName(u"hl_Z_2")
        self.hl_Z_2.setContentsMargins(0, -1, -1, -1)
        self.lb_Z_2 = QLabel(self.layoutWidget_3)
        self.lb_Z_2.setObjectName(u"lb_Z_2")
        sizePolicy.setHeightForWidth(self.lb_Z_2.sizePolicy().hasHeightForWidth())
        self.lb_Z_2.setSizePolicy(sizePolicy)
        self.lb_Z_2.setFrameShape(QFrame.NoFrame)

        self.hl_Z_2.addWidget(self.lb_Z_2)

        self.le_Z_2 = QLineEdit(self.layoutWidget_3)
        self.le_Z_2.setObjectName(u"le_Z_2")
        self.le_Z_2.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_Z_2.sizePolicy().hasHeightForWidth())
        self.le_Z_2.setSizePolicy(sizePolicy1)

        self.hl_Z_2.addWidget(self.le_Z_2)


        self.vl_variables_t3.addLayout(self.hl_Z_2)

        self.hl_sigma = QHBoxLayout()
        self.hl_sigma.setObjectName(u"hl_sigma")
        self.lb_sigma = QLabel(self.layoutWidget_3)
        self.lb_sigma.setObjectName(u"lb_sigma")
        sizePolicy.setHeightForWidth(self.lb_sigma.sizePolicy().hasHeightForWidth())
        self.lb_sigma.setSizePolicy(sizePolicy)

        self.hl_sigma.addWidget(self.lb_sigma)

        self.le_sigma = QLineEdit(self.layoutWidget_3)
        self.le_sigma.setObjectName(u"le_sigma")
        self.le_sigma.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_sigma.sizePolicy().hasHeightForWidth())
        self.le_sigma.setSizePolicy(sizePolicy1)

        self.hl_sigma.addWidget(self.le_sigma)


        self.vl_variables_t3.addLayout(self.hl_sigma)

        self.hl_t_z_1 = QHBoxLayout()
        self.hl_t_z_1.setObjectName(u"hl_t_z_1")
        self.lb_t_z_1 = QLabel(self.layoutWidget_3)
        self.lb_t_z_1.setObjectName(u"lb_t_z_1")
        sizePolicy.setHeightForWidth(self.lb_t_z_1.sizePolicy().hasHeightForWidth())
        self.lb_t_z_1.setSizePolicy(sizePolicy)

        self.hl_t_z_1.addWidget(self.lb_t_z_1)

        self.le_t_z_1 = QLineEdit(self.layoutWidget_3)
        self.le_t_z_1.setObjectName(u"le_t_z_1")
        self.le_t_z_1.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_t_z_1.sizePolicy().hasHeightForWidth())
        self.le_t_z_1.setSizePolicy(sizePolicy1)

        self.hl_t_z_1.addWidget(self.le_t_z_1)


        self.vl_variables_t3.addLayout(self.hl_t_z_1)

        self.hl_b_sh = QHBoxLayout()
        self.hl_b_sh.setObjectName(u"hl_b_sh")
        self.lb_b_sh = QLabel(self.layoutWidget_3)
        self.lb_b_sh.setObjectName(u"lb_b_sh")
        sizePolicy.setHeightForWidth(self.lb_b_sh.sizePolicy().hasHeightForWidth())
        self.lb_b_sh.setSizePolicy(sizePolicy)

        self.hl_b_sh.addWidget(self.lb_b_sh)

        self.le_b_sh = QLineEdit(self.layoutWidget_3)
        self.le_b_sh.setObjectName(u"le_b_sh")
        self.le_b_sh.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_b_sh.sizePolicy().hasHeightForWidth())
        self.le_b_sh.setSizePolicy(sizePolicy1)

        self.hl_b_sh.addWidget(self.le_b_sh)


        self.vl_variables_t3.addLayout(self.hl_b_sh)

        self.hl_h_sh_r = QHBoxLayout()
        self.hl_h_sh_r.setObjectName(u"hl_h_sh_r")
        self.lb_h_sh_r = QLabel(self.layoutWidget_3)
        self.lb_h_sh_r.setObjectName(u"lb_h_sh_r")
        sizePolicy.setHeightForWidth(self.lb_h_sh_r.sizePolicy().hasHeightForWidth())
        self.lb_h_sh_r.setSizePolicy(sizePolicy)

        self.hl_h_sh_r.addWidget(self.lb_h_sh_r)

        self.le_h_sh_r = QLineEdit(self.layoutWidget_3)
        self.le_h_sh_r.setObjectName(u"le_h_sh_r")
        self.le_h_sh_r.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_h_sh_r.sizePolicy().hasHeightForWidth())
        self.le_h_sh_r.setSizePolicy(sizePolicy1)

        self.hl_h_sh_r.addWidget(self.le_h_sh_r)


        self.vl_variables_t3.addLayout(self.hl_h_sh_r)

        self.hl_Lamda_p_1 = QHBoxLayout()
        self.hl_Lamda_p_1.setObjectName(u"hl_Lamda_p_1")
        self.lb_Lamda_p_1 = QLabel(self.layoutWidget_3)
        self.lb_Lamda_p_1.setObjectName(u"lb_Lamda_p_1")
        sizePolicy.setHeightForWidth(self.lb_Lamda_p_1.sizePolicy().hasHeightForWidth())
        self.lb_Lamda_p_1.setSizePolicy(sizePolicy)

        self.hl_Lamda_p_1.addWidget(self.lb_Lamda_p_1)

        self.le_Lamda_p_1 = QLineEdit(self.layoutWidget_3)
        self.le_Lamda_p_1.setObjectName(u"le_Lamda_p_1")
        self.le_Lamda_p_1.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_Lamda_p_1.sizePolicy().hasHeightForWidth())
        self.le_Lamda_p_1.setSizePolicy(sizePolicy1)

        self.hl_Lamda_p_1.addWidget(self.le_Lamda_p_1)


        self.vl_variables_t3.addLayout(self.hl_Lamda_p_1)

        self.hl_Lamda_d_1 = QHBoxLayout()
        self.hl_Lamda_d_1.setObjectName(u"hl_Lamda_d_1")
        self.lb_Lamda_d_1 = QLabel(self.layoutWidget_3)
        self.lb_Lamda_d_1.setObjectName(u"lb_Lamda_d_1")
        sizePolicy.setHeightForWidth(self.lb_Lamda_d_1.sizePolicy().hasHeightForWidth())
        self.lb_Lamda_d_1.setSizePolicy(sizePolicy)

        self.hl_Lamda_d_1.addWidget(self.lb_Lamda_d_1)

        self.le_Lamda_d_1 = QLineEdit(self.layoutWidget_3)
        self.le_Lamda_d_1.setObjectName(u"le_Lamda_d_1")
        self.le_Lamda_d_1.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_Lamda_d_1.sizePolicy().hasHeightForWidth())
        self.le_Lamda_d_1.setSizePolicy(sizePolicy1)

        self.hl_Lamda_d_1.addWidget(self.le_Lamda_d_1)


        self.vl_variables_t3.addLayout(self.hl_Lamda_d_1)

        self.hl_Lamda_l_1 = QHBoxLayout()
        self.hl_Lamda_l_1.setObjectName(u"hl_Lamda_l_1")
        self.lb_Lamda_l_1 = QLabel(self.layoutWidget_3)
        self.lb_Lamda_l_1.setObjectName(u"lb_Lamda_l_1")
        sizePolicy.setHeightForWidth(self.lb_Lamda_l_1.sizePolicy().hasHeightForWidth())
        self.lb_Lamda_l_1.setSizePolicy(sizePolicy)

        self.hl_Lamda_l_1.addWidget(self.lb_Lamda_l_1)

        self.le_Lamda_l_1 = QLineEdit(self.layoutWidget_3)
        self.le_Lamda_l_1.setObjectName(u"le_Lamda_l_1")
        self.le_Lamda_l_1.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_Lamda_l_1.sizePolicy().hasHeightForWidth())
        self.le_Lamda_l_1.setSizePolicy(sizePolicy1)

        self.hl_Lamda_l_1.addWidget(self.le_Lamda_l_1)


        self.vl_variables_t3.addLayout(self.hl_Lamda_l_1)

        self.hl_t_z_2 = QHBoxLayout()
        self.hl_t_z_2.setObjectName(u"hl_t_z_2")
        self.lb_t_z_2 = QLabel(self.layoutWidget_3)
        self.lb_t_z_2.setObjectName(u"lb_t_z_2")
        sizePolicy.setHeightForWidth(self.lb_t_z_2.sizePolicy().hasHeightForWidth())
        self.lb_t_z_2.setSizePolicy(sizePolicy)

        self.hl_t_z_2.addWidget(self.lb_t_z_2)

        self.le_t_z_2 = QLineEdit(self.layoutWidget_3)
        self.le_t_z_2.setObjectName(u"le_t_z_2")
        self.le_t_z_2.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_t_z_2.sizePolicy().hasHeightForWidth())
        self.le_t_z_2.setSizePolicy(sizePolicy1)

        self.hl_t_z_2.addWidget(self.le_t_z_2)


        self.vl_variables_t3.addLayout(self.hl_t_z_2)

        self.hl_r_2_Ksi_shtrih = QHBoxLayout()
        self.hl_r_2_Ksi_shtrih.setObjectName(u"hl_r_2_Ksi_shtrih")
        self.lb_r_2_Ksi_shtrih = QLabel(self.layoutWidget_3)
        self.lb_r_2_Ksi_shtrih.setObjectName(u"lb_r_2_Ksi_shtrih")
        sizePolicy.setHeightForWidth(self.lb_r_2_Ksi_shtrih.sizePolicy().hasHeightForWidth())
        self.lb_r_2_Ksi_shtrih.setSizePolicy(sizePolicy)

        self.hl_r_2_Ksi_shtrih.addWidget(self.lb_r_2_Ksi_shtrih)

        self.le_r_2_Ksi_shtrih = QLineEdit(self.layoutWidget_3)
        self.le_r_2_Ksi_shtrih.setObjectName(u"le_r_2_Ksi_shtrih")
        self.le_r_2_Ksi_shtrih.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_r_2_Ksi_shtrih.sizePolicy().hasHeightForWidth())
        self.le_r_2_Ksi_shtrih.setSizePolicy(sizePolicy1)

        self.hl_r_2_Ksi_shtrih.addWidget(self.le_r_2_Ksi_shtrih)


        self.vl_variables_t3.addLayout(self.hl_r_2_Ksi_shtrih)

        self.hl_I_1_p = QHBoxLayout()
        self.hl_I_1_p.setObjectName(u"hl_I_1_p")
        self.lb_I_1_p = QLabel(self.layoutWidget_3)
        self.lb_I_1_p.setObjectName(u"lb_I_1_p")
        sizePolicy.setHeightForWidth(self.lb_I_1_p.sizePolicy().hasHeightForWidth())
        self.lb_I_1_p.setSizePolicy(sizePolicy)

        self.hl_I_1_p.addWidget(self.lb_I_1_p)

        self.le_I_1_p = QLineEdit(self.layoutWidget_3)
        self.le_I_1_p.setObjectName(u"le_I_1_p")
        self.le_I_1_p.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_I_1_p.sizePolicy().hasHeightForWidth())
        self.le_I_1_p.setSizePolicy(sizePolicy1)

        self.hl_I_1_p.addWidget(self.le_I_1_p)


        self.vl_variables_t3.addLayout(self.hl_I_1_p)

        self.hl_I_1_nom = QHBoxLayout()
        self.hl_I_1_nom.setObjectName(u"hl_I_1_nom")
        self.lb_I_1_nom = QLabel(self.layoutWidget_3)
        self.lb_I_1_nom.setObjectName(u"lb_I_1_nom")
        sizePolicy.setHeightForWidth(self.lb_I_1_nom.sizePolicy().hasHeightForWidth())
        self.lb_I_1_nom.setSizePolicy(sizePolicy)

        self.hl_I_1_nom.addWidget(self.lb_I_1_nom)

        self.le_I_1_nom = QLineEdit(self.layoutWidget_3)
        self.le_I_1_nom.setObjectName(u"le_I_1_nom")
        self.le_I_1_nom.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_I_1_nom.sizePolicy().hasHeightForWidth())
        self.le_I_1_nom.setSizePolicy(sizePolicy1)

        self.hl_I_1_nom.addWidget(self.le_I_1_nom)


        self.vl_variables_t3.addLayout(self.hl_I_1_nom)

        self.hl_h_k = QHBoxLayout()
        self.hl_h_k.setObjectName(u"hl_h_k")
        self.lb_h_k = QLabel(self.layoutWidget_3)
        self.lb_h_k.setObjectName(u"lb_h_k")
        sizePolicy.setHeightForWidth(self.lb_h_k.sizePolicy().hasHeightForWidth())
        self.lb_h_k.setSizePolicy(sizePolicy)

        self.hl_h_k.addWidget(self.lb_h_k)

        self.le_h_k = QLineEdit(self.layoutWidget_3)
        self.le_h_k.setObjectName(u"le_h_k")
        self.le_h_k.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_h_k.sizePolicy().hasHeightForWidth())
        self.le_h_k.setSizePolicy(sizePolicy1)

        self.hl_h_k.addWidget(self.le_h_k)


        self.vl_variables_t3.addLayout(self.hl_h_k)

        self.hl_Lamda_p_2_Ksi = QHBoxLayout()
        self.hl_Lamda_p_2_Ksi.setObjectName(u"hl_Lamda_p_2_Ksi")
        self.lb_Lamda_p_2_Ksi = QLabel(self.layoutWidget_3)
        self.lb_Lamda_p_2_Ksi.setObjectName(u"lb_Lamda_p_2_Ksi")
        sizePolicy.setHeightForWidth(self.lb_Lamda_p_2_Ksi.sizePolicy().hasHeightForWidth())
        self.lb_Lamda_p_2_Ksi.setSizePolicy(sizePolicy)

        self.hl_Lamda_p_2_Ksi.addWidget(self.lb_Lamda_p_2_Ksi)

        self.le_Lamda_p_2_Ksi = QLineEdit(self.layoutWidget_3)
        self.le_Lamda_p_2_Ksi.setObjectName(u"le_Lamda_p_2_Ksi")
        self.le_Lamda_p_2_Ksi.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_Lamda_p_2_Ksi.sizePolicy().hasHeightForWidth())
        self.le_Lamda_p_2_Ksi.setSizePolicy(sizePolicy1)

        self.hl_Lamda_p_2_Ksi.addWidget(self.le_Lamda_p_2_Ksi)


        self.vl_variables_t3.addLayout(self.hl_Lamda_p_2_Ksi)

        self.hl_K_R = QHBoxLayout()
        self.hl_K_R.setObjectName(u"hl_K_R")
        self.lb_K_R = QLabel(self.layoutWidget_3)
        self.lb_K_R.setObjectName(u"lb_K_R")
        sizePolicy.setHeightForWidth(self.lb_K_R.sizePolicy().hasHeightForWidth())
        self.lb_K_R.setSizePolicy(sizePolicy)

        self.hl_K_R.addWidget(self.lb_K_R)

        self.le_K_R = QLineEdit(self.layoutWidget_3)
        self.le_K_R.setObjectName(u"le_K_R")
        self.le_K_R.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_K_R.sizePolicy().hasHeightForWidth())
        self.le_K_R.setSizePolicy(sizePolicy1)

        self.hl_K_R.addWidget(self.le_K_R)


        self.vl_variables_t3.addLayout(self.hl_K_R)

        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(mainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.linePower.setCurrentIndex(18)
        self.lineVoltage.setCurrentIndex(1)
        self.linePolarity.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0447\u0451\u0442\u043d\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("mainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.Input.setText(QCoreApplication.translate("mainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435:", None))
        self.submitValues.setText(QCoreApplication.translate("mainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        self.Power.setText(QCoreApplication.translate("mainWindow", u"\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f ", None))
        self.Voltage.setText(QCoreApplication.translate("mainWindow", u"\u041d\u043e\u043c\u0438\u043d\u0430\u043b\u044c\u043d\u043e\u0435 \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435", None))
        self.polarity.setText(QCoreApplication.translate("mainWindow", u"\u041f\u043e\u043b\u044f\u0440\u043d\u043e\u0441\u0442\u044c", None))
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
        ___qtablewidgetitem44.setText(QCoreApplication.translate("mainWindow", u"I_1\u043f = I_0\u043f+I'_2cos(\u03c6)'_2", None));
        ___qtablewidgetitem45 = self.tableWidget.item(8, 1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem46 = self.tableWidget.item(9, 0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("mainWindow", u"I_1\u0440 = I_0\u043f+I'_2sin(\u03c6)'_2", None));
        ___qtablewidgetitem47 = self.tableWidget.item(9, 1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem48 = self.tableWidget.item(10, 0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("mainWindow", u"I_1 = \u221a(I_1\u043f^2+I_1\u0440^2)", None));
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
        ___qtablewidgetitem58.setText(QCoreApplication.translate("mainWindow", u"P_\u0434\u043e\u0431 = 0,005P_1", None));
        ___qtablewidgetitem59 = self.tableWidget.item(15, 1)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("mainWindow", u"\u043a\u0412\u0442", None));
        ___qtablewidgetitem60 = self.tableWidget.item(16, 0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("mainWindow", u"\u03a3P=P\u0441\u0442+P\u043c\u0435\u0445+P\u044d2+P\u044d1+P\u044d.\u0449+P\u0434\u043e\u0431", None));
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

        self.bt_check_table_1.setText(QCoreApplication.translate("mainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430", None))
        self.bt_calculate_table1.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.bt_show_chart_1.setText(QCoreApplication.translate("mainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.bt_export_xl_1.setText(QCoreApplication.translate("mainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0432 \u044d\u043a\u0441\u0435\u043b\u044c", None))
        self.lb_I0a.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">I</span><span style=\" font-size:14pt; vertical-align:sub;\">0a </span><span style=\" font-size:14pt;\">=</span></p></body></html>", None))
        self.lb_I0p.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">I</span><span style=\" font-size:14pt; vertical-align:sub;\">0p </span><span style=\" font-size:14pt;\">=</span></p></body></html>", None))
        self.lb_Pst.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>P<span style=\" vertical-align:sub;\">\u0421\u0422</span> =</p></body></html>", None))
        self.lb_Pmeh.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>P<span style=\" vertical-align:sub;\">\u043c\u0435\u0445</span> =</p></body></html>", None))
        self.lb_r1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">r</span><span style=\" font-size:14pt; vertical-align:sub;\">1 </span><span style=\" font-size:14pt;\">=</span></p></body></html>", None))
        self.lb_r2_shtrih.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>r'<span style=\" vertical-align:sub;\">2 </span>=</p></body></html>", None))
        self.lb_c1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>c<span style=\" vertical-align:sub;\">1 </span>=</p></body></html>", None))
        self.lb_a_shtrih.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>a' =</p></body></html>", None))
        self.lb_a.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>a =</p></body></html>", None))
        self.lb_b_shtrih.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>b' =</p></body></html>", None))
        self.lb_b.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>b =</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("mainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 1", None))
        ___qtablewidgetitem68 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0447\u0451\u0442\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0443\u043b\u0430", None));
        ___qtablewidgetitem69 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440\u043d\u043e\u0441\u0442\u044c", None));
        ___qtablewidgetitem70 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043a\u043e\u043b\u044c\u0436\u0435\u043d\u0438\u0435 s", None));
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
        ___qtablewidgetitem104.setText(QCoreApplication.translate("mainWindow", u"\u043a_\u0434 = \u03c6'(\u03be)", None));
        ___qtablewidgetitem105 = self.tableWidget_2.item(7, 1)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem106 = self.tableWidget_2.item(8, 0)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("mainWindow", u"\u03bb_\u043f2\u03be = \u03bb_\u043f2 - \u0394\u03bb\u043f2\u03be", None));
        ___qtablewidgetitem107 = self.tableWidget_2.item(8, 1)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem108 = self.tableWidget_2.item(9, 0)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("mainWindow", u"Kx = \u03a3\u03bb_2\u03be/\u03a3\u03bb_2", None));
        ___qtablewidgetitem109 = self.tableWidget_2.item(9, 1)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem110 = self.tableWidget_2.item(10, 0)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("mainWindow", u"x'2\u03be = Kx * x'_2", None));
        ___qtablewidgetitem111 = self.tableWidget_2.item(10, 1)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem112 = self.tableWidget_2.item(11, 0)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("mainWindow", u"R\u043f = r_1+c_1\u043f* (r'_2_\u03be/s)", None));
        ___qtablewidgetitem113 = self.tableWidget_2.item(11, 1)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem114 = self.tableWidget_2.item(12, 0)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("mainWindow", u"X\u043f = x_1+c_1\u043f*x'2\u03be", None));
        ___qtablewidgetitem115 = self.tableWidget_2.item(12, 1)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem116 = self.tableWidget_2.item(13, 0)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("mainWindow", u"I'_2\u043f = U/\u221a(R\u043f^2 + X\u043f^2)", None));
        ___qtablewidgetitem117 = self.tableWidget_2.item(13, 1)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem118 = self.tableWidget_2.item(14, 0)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("mainWindow", u"I_1\u043f=I'_2\u221a(R\u043f^2 + (X\u043f+x_12\u043f)^2)/(c_1\u043f*x_12\u043f)", None));
        ___qtablewidgetitem119 = self.tableWidget_2.item(14, 1)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled1)

        self.bt_check_table_2.setText(QCoreApplication.translate("mainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430", None))
        self.bt_calculate_table2.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.lb_h_c.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c </span>=</p></body></html>", None))
        self.lb_h_p_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">p2 </span>=</p></body></html>", None))
        self.lb_h_sh.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">\u0448</span> =</p></body></html>", None))
        self.lb_h_sh_shtrih.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>h'<span style=\" vertical-align:sub;\">\u0448</span> =</p></body></html>", None))
        self.lb_b_1_r.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>b<span style=\" vertical-align:sub;\">1\u0440\u043e\u0442.</span>=</p></body></html>", None))
        self.lb_b_2_r.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>b<span style=\" vertical-align:sub;\">2\u0440\u043e\u0442.</span>=</p></body></html>", None))
        self.lb_h_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">1 </span>=</p></body></html>", None))
        self.lb_q_c.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>q<span style=\" vertical-align:sub;\">c</span> =</p></body></html>", None))
        self.lb_r_c.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>r<span style=\" vertical-align:sub;\">c</span> =</p></body></html>", None))
        self.lb_r_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>r<span style=\" vertical-align:sub;\">2</span> =</p></body></html>", None))
        self.lb_h_0.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">0</span> =</p></body></html>", None))
        self.lb_b_sh_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>b<span style=\" vertical-align:sub;\">\u04482</span> =</p></body></html>", None))
        self.lb_Lamda_p_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; font-weight:700; color:#202122; background-color:#ffffff;\">\u03bb</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; color:#202122; background-color:#ffffff; vertical-align:sub;\">p2</span>=</p></body></html>", None))
        self.lb_Lamda_l_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; font-weight:700; color:#202122; background-color:#ffffff;\">\u03bb</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; font-weight:700; color:#202122; background-color:#ffffff; vertical-align:sub;\">\u043b</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; color:#202122; background-color:#ffffff; vertical-align:sub;\">2</span>=</p></body></html>", None))
        self.lb_Lamda_d_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; font-weight:700; color:#202122; background-color:#ffffff;\">\u03bb</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; font-weight:700; color:#202122; background-color:#ffffff; vertical-align:sub;\">\u0434</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; color:#202122; background-color:#ffffff; vertical-align:sub;\">2</span>=</p></body></html>", None))
        self.lb_X_2_shtrih.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>X'<span style=\" vertical-align:sub;\">2</span> =</p></body></html>", None))
        self.lb_x_1_2_p.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u0445<span style=\" vertical-align:sub;\">12\u0440</span> =</p></body></html>", None))
        self.lb_c_1_p.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u0441<span style=\" vertical-align:sub;\">1\u0440</span> =</p></body></html>", None))
        self.lb_X_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u0425<span style=\" vertical-align:sub;\">1</span> =</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("mainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 2", None))
        ___qtablewidgetitem120 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0447\u0451\u0442\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0443\u043b\u0430", None));
        ___qtablewidgetitem121 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440\u043d\u043e\u0441\u0442\u044c", None));
        ___qtablewidgetitem122 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043a\u043e\u043b\u044c\u0436\u0435\u043d\u0438\u0435 s", None));
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
        ___qtablewidgetitem152.setText(QCoreApplication.translate("mainWindow", u"F\u043f.\u0441\u0440=0,7*((I_1*k_\u043d\u0430\u0441*u_\u043f)/a)(k'_beta+k_y1*k_\u043e\u04311*(Z1/Z2))", None));
        ___qtablewidgetitem153 = self.tableWidget_3.item(2, 1)
        ___qtablewidgetitem153.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem154 = self.tableWidget_3.item(3, 0)
        ___qtablewidgetitem154.setText(QCoreApplication.translate("mainWindow", u"\u0412_\u0444\u0431 = F\u043f.\u0441\u0440 * 10^(-6)/(1,6\u03b4*\u0421_N)", None));
        ___qtablewidgetitem155 = self.tableWidget_3.item(3, 1)
        ___qtablewidgetitem155.setText(QCoreApplication.translate("mainWindow", u"\u0422\u043b", None));
        ___qtablewidgetitem156 = self.tableWidget_3.item(4, 0)
        ___qtablewidgetitem156.setText(QCoreApplication.translate("mainWindow", u"k_\u03b4 = f(\u0412_\u0444\u0431)", None));
        ___qtablewidgetitem157 = self.tableWidget_3.item(4, 1)
        ___qtablewidgetitem157.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem158 = self.tableWidget_3.item(5, 0)
        ___qtablewidgetitem158.setText(QCoreApplication.translate("mainWindow", u"\u0441_1 = (t_z1-b_\u04481)(1-k_\u03b4)", None));
        ___qtablewidgetitem159 = self.tableWidget_3.item(5, 1)
        ___qtablewidgetitem159.setText(QCoreApplication.translate("mainWindow", u"\u043c\u043c", None));
        ___qtablewidgetitem160 = self.tableWidget_3.item(6, 0)
        ___qtablewidgetitem160.setText(QCoreApplication.translate("mainWindow", u"\u03bb_\u043f1\u043d\u0430\u0441 = \u03bb\u043f1 - \u0394\u03bb_\u043f1\u043d\u0430\u0441", None));
        ___qtablewidgetitem161 = self.tableWidget_3.item(6, 1)
        ___qtablewidgetitem161.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem162 = self.tableWidget_3.item(7, 0)
        ___qtablewidgetitem162.setText(QCoreApplication.translate("mainWindow", u"\u03bb_\u04341\u043d\u0430\u0441 = k_\u03b4*\u03bb\u04341", None));
        ___qtablewidgetitem163 = self.tableWidget_3.item(7, 1)
        ___qtablewidgetitem163.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem164 = self.tableWidget_3.item(8, 0)
        ___qtablewidgetitem164.setText(QCoreApplication.translate("mainWindow", u"\u0445_1\u043d\u0430\u0441 = \u04451*\u03a3\u03bb_1\u043d\u0430\u0441/\u03a3\u03bb_1", None));
        ___qtablewidgetitem165 = self.tableWidget_3.item(8, 1)
        ___qtablewidgetitem165.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem166 = self.tableWidget_3.item(9, 0)
        ___qtablewidgetitem166.setText(QCoreApplication.translate("mainWindow", u"c_1_\u043f = 1 + x_1\u043d\u0430\u0441/ x_12\u043f", None));
        ___qtablewidgetitem167 = self.tableWidget_3.item(9, 1)
        ___qtablewidgetitem167.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem168 = self.tableWidget_3.item(10, 0)
        ___qtablewidgetitem168.setText(QCoreApplication.translate("mainWindow", u"\u0441_2 = (t_z2-b_\u04482)(1-k_\u03b4)", None));
        ___qtablewidgetitem169 = self.tableWidget_3.item(10, 1)
        ___qtablewidgetitem169.setText(QCoreApplication.translate("mainWindow", u"\u043c\u043c", None));
        ___qtablewidgetitem170 = self.tableWidget_3.item(11, 0)
        ___qtablewidgetitem170.setText(QCoreApplication.translate("mainWindow", u"\u03bb_\u043f2\u03be\u043d\u0430\u0441 = \u03bb_\u043f2\u03be - \u0394\u03bb_\u043f2\u043d\u0430\u0441", None));
        ___qtablewidgetitem171 = self.tableWidget_3.item(11, 1)
        ___qtablewidgetitem171.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem172 = self.tableWidget_3.item(12, 0)
        ___qtablewidgetitem172.setText(QCoreApplication.translate("mainWindow", u"\u03bb_\u04342\u043d\u0430\u0441 = k_\u03b4*\u03bb\u04342", None));
        ___qtablewidgetitem173 = self.tableWidget_3.item(12, 1)
        ___qtablewidgetitem173.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem174 = self.tableWidget_3.item(13, 0)
        ___qtablewidgetitem174.setText(QCoreApplication.translate("mainWindow", u"\u0445'_2\u03be\u043d\u0430\u0441 = x'2*\u03a3\u03bb_2\u03be\u043d\u0430\u0441/\u03a3\u03bb_2", None));
        ___qtablewidgetitem175 = self.tableWidget_3.item(13, 1)
        ___qtablewidgetitem175.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem176 = self.tableWidget_3.item(14, 0)
        ___qtablewidgetitem176.setText(QCoreApplication.translate("mainWindow", u"R\u043f.\u043d\u0430\u0441 = r_1 + c_1\u043f.\u043d\u0430\u0441 * r'_2\u03be / s", None));
        ___qtablewidgetitem177 = self.tableWidget_3.item(14, 1)
        ___qtablewidgetitem177.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem178 = self.tableWidget_3.item(15, 0)
        ___qtablewidgetitem178.setText(QCoreApplication.translate("mainWindow", u"\u0425\u043f.\u043d\u0430\u0441 = x_1\u043d\u0430\u0441 + c_1\u043f.\u043d\u0430\u0441 * \u0445'_2\u03be\u043d\u0430\u0441", None));
        ___qtablewidgetitem179 = self.tableWidget_3.item(15, 1)
        ___qtablewidgetitem179.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem180 = self.tableWidget_3.item(16, 0)
        ___qtablewidgetitem180.setText(QCoreApplication.translate("mainWindow", u"I'_2\u043d\u0430\u0441 = U/\u221a(R\u043f.\u043d\u0430\u0441^2+\u0425\u043f.\u043d\u0430\u0441^2)", None));
        ___qtablewidgetitem181 = self.tableWidget_3.item(16, 1)
        ___qtablewidgetitem181.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem182 = self.tableWidget_3.item(17, 0)
        ___qtablewidgetitem182.setText(QCoreApplication.translate("mainWindow", u"I_1\u043d\u0430\u0441=I'_2\u043d\u0430\u0441*((\u221a(R\u043f.\u043d\u0430\u0441^2+(\u0425\u043f.\u043d\u0430\u0441+\u0445_12\u043f)^2))/(\u0441_1\u043f.\u043d\u0430\u0441*\u0445_12\u043f))", None));
        ___qtablewidgetitem183 = self.tableWidget_3.item(17, 1)
        ___qtablewidgetitem183.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem184 = self.tableWidget_3.item(18, 0)
        ___qtablewidgetitem184.setText(QCoreApplication.translate("mainWindow", u"k'\u043d\u0430\u0441 = I_1\u043d\u0430\u0441/I_1\u043f", None));
        ___qtablewidgetitem185 = self.tableWidget_3.item(18, 1)
        ___qtablewidgetitem185.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem186 = self.tableWidget_3.item(19, 0)
        ___qtablewidgetitem186.setText(QCoreApplication.translate("mainWindow", u"I_i= I_1\u043d\u0430\u0441 / I_1\u043d\u043e\u043c", None));
        ___qtablewidgetitem187 = self.tableWidget_3.item(19, 1)
        ___qtablewidgetitem187.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem188 = self.tableWidget_3.item(20, 0)
        ___qtablewidgetitem188.setText(QCoreApplication.translate("mainWindow", u"\u041c*", None));
        ___qtablewidgetitem189 = self.tableWidget_3.item(20, 1)
        ___qtablewidgetitem189.setText(QCoreApplication.translate("mainWindow", u"-", None));
        self.tableWidget_3.setSortingEnabled(__sortingEnabled2)

        self.bt_check_table_3.setText(QCoreApplication.translate("mainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430", None))
        self.bt_calculate_table3.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.bt_show_chart_table3.setText(QCoreApplication.translate("mainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.lb_C_N.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u0421<span style=\" vertical-align:sub;\">N </span>=</p></body></html>", None))
        self.lb_k_y_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>k<span style=\" vertical-align:sub;\">y1 </span>=</p></body></html>", None))
        self.lb_u_p.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>u<span style=\" vertical-align:sub;\">p</span> =</p></body></html>", None))
        self.lb_k_ob.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>k<span style=\" vertical-align:sub;\">\u043e\u0431</span> =</p></body></html>", None))
        self.lb_Z_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>Z<span style=\" vertical-align:sub;\">1 </span>=</p></body></html>", None))
        self.lb_Z_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>Z<span style=\" vertical-align:sub;\">2</span> =</p></body></html>", None))
        self.lb_sigma.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-weight:700; color:#202122; background-color:#ffffff;\">\u03b4 </span>=</p></body></html>", None))
        self.lb_t_z_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>t<span style=\" vertical-align:sub;\">z1</span> =</p></body></html>", None))
        self.lb_b_sh.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>b<span style=\" vertical-align:sub;\">\u0448</span> =</p></body></html>", None))
        self.lb_h_sh_r.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">\u0448 \u0440\u043e\u0442.</span> =</p></body></html>", None))
        self.lb_Lamda_p_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; color:#202122; background-color:#ffffff;\">\u03bb</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; color:#202122; background-color:#ffffff; vertical-align:sub;\">p1</span>=</p></body></html>", None))
        self.lb_Lamda_d_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; color:#202122; background-color:#ffffff;\">\u03bb</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; color:#202122; background-color:#ffffff; vertical-align:sub;\">\u04341</span>=</p></body></html>", None))
        self.lb_Lamda_l_1.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; color:#202122; background-color:#ffffff;\">\u03bb</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:16pt; color:#202122; background-color:#ffffff; vertical-align:sub;\">\u043b1</span>=</p></body></html>", None))
        self.lb_t_z_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>t<span style=\" vertical-align:sub;\">z2</span> =</p></body></html>", None))
        self.lb_r_2_Ksi_shtrih.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>r'<span style=\" vertical-align:sub;\">2\u03be </span>=</p></body></html>", None))
        self.lb_I_1_p.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>I<span style=\" vertical-align:sub;\">1p</span> =</p></body></html>", None))
        self.lb_I_1_nom.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>I<span style=\" vertical-align:sub;\">1\u043d\u043e\u043c</span> =</p></body></html>", None))
        self.lb_h_k.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">k</span> =</p></body></html>", None))
        self.lb_Lamda_p_2_Ksi.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u03bb<span style=\" vertical-align:sub;\">\u043f2\u03be </span>=</p></body></html>", None))
        self.lb_K_R.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>K<span style=\" vertical-align:sub;\">R</span> =</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("mainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 3", None))
    # retranslateUi


