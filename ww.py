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
    QLabel, QPushButton, QSizePolicy, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1268, 794)
        self.tabWidget = QTabWidget(mainWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 1251, 771))
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
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget.setItem(0, 8, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
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
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget.setItem(4, 1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget.setItem(5, 1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget.setItem(6, 1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget.setItem(7, 1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget.setItem(8, 1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget.setItem(9, 1, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget.setItem(10, 1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget.setItem(11, 1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget.setItem(12, 1, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget.setItem(13, 1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget.setItem(14, 1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget.setItem(15, 1, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget.setItem(16, 1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget.setItem(17, 1, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget.setItem(18, 1, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget.setItem(19, 1, __qtablewidgetitem58)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 100, 1111, 511))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.verticalHeader().setDefaultSectionSize(24)
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(740, 620, 369, 31))
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
        self.label_5.setGeometry(QRect(10, 10, 331, 101))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tableWidget_2 = QTableWidget(self.tab_2)
        if (self.tableWidget_2.columnCount() < 8):
            self.tableWidget_2.setColumnCount(8)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem66)
        if (self.tableWidget_2.rowCount() < 15):
            self.tableWidget_2.setRowCount(15)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        __qtablewidgetitem82.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        __qtablewidgetitem83.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        __qtablewidgetitem84.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 3, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        __qtablewidgetitem86.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 4, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        __qtablewidgetitem87.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 5, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        __qtablewidgetitem88.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 6, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 7, __qtablewidgetitem89)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(0, 10, 1231, 481))
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(150)
        self.bt_calculate_table2 = QPushButton(self.tab_2)
        self.bt_calculate_table2.setObjectName(u"bt_calculate_table2")
        self.bt_calculate_table2.setGeometry(QRect(1000, 630, 75, 24))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tableWidget_3 = QTableWidget(self.tab_3)
        if (self.tableWidget_3.columnCount() < 8):
            self.tableWidget_3.setColumnCount(8)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem97)
        if (self.tableWidget_3.rowCount() < 21):
            self.tableWidget_3.setRowCount(21)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(6, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(7, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(8, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(9, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(10, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(11, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(12, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(13, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(14, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(15, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(16, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(17, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(18, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(19, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(20, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 2, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 3, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 4, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 5, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 6, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 7, __qtablewidgetitem124)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(0, 0, 1241, 661))
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(150)
        self.layoutWidget1 = QWidget(self.tab_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(1134, 670, 103, 56))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bt_calculate_table3 = QPushButton(self.layoutWidget1)
        self.bt_calculate_table3.setObjectName(u"bt_calculate_table3")

        self.verticalLayout_4.addWidget(self.bt_calculate_table3)

        self.bt_show_chart_table3 = QPushButton(self.layoutWidget1)
        self.bt_show_chart_table3.setObjectName(u"bt_show_chart_table3")

        self.verticalLayout_4.addWidget(self.bt_show_chart_table3)

        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(mainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0447\u0451\u0442\u043d\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
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
        ___qtablewidgetitem30 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem31 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem32 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem33 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043c", None));
        ___qtablewidgetitem34 = self.tableWidget.item(5, 1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem35 = self.tableWidget.item(6, 1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem36 = self.tableWidget.item(7, 1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem37 = self.tableWidget.item(8, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem38 = self.tableWidget.item(9, 1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem39 = self.tableWidget.item(10, 1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem40 = self.tableWidget.item(11, 1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("mainWindow", u"\u0410", None));
        ___qtablewidgetitem41 = self.tableWidget.item(12, 1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("mainWindow", u"\u043a\u0412\u0442", None));
        ___qtablewidgetitem42 = self.tableWidget.item(13, 1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("mainWindow", u"\u043a\u0412\u0442", None));
        ___qtablewidgetitem43 = self.tableWidget.item(14, 1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("mainWindow", u"\u043a\u0412\u0442", None));
        ___qtablewidgetitem44 = self.tableWidget.item(15, 1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("mainWindow", u"\u043a\u0412\u0442", None));
        ___qtablewidgetitem45 = self.tableWidget.item(16, 1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("mainWindow", u"\u043a\u0412\u0442", None));
        ___qtablewidgetitem46 = self.tableWidget.item(17, 1)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("mainWindow", u"\u043a\u0412\u0442", None));
        ___qtablewidgetitem47 = self.tableWidget.item(18, 1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("mainWindow", u"-", None));
        ___qtablewidgetitem48 = self.tableWidget.item(19, 1)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("mainWindow", u"-", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.bt_calculate_table1.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.bt_show_chart_1.setText(QCoreApplication.translate("mainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.bt_export_xl_1.setText(QCoreApplication.translate("mainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0432 \u044d\u043a\u0441\u0435\u043b\u044c", None))
        self.label_5.setText(QCoreApplication.translate("mainWindow", u"P_2 = 22; U = 380/660 ; 2p = 4; I_0_a = 0,37; I_0_p = 5,39\n"
"P_st + P_tr_sh + P_mex = 0,67; r_1 = 0,6; r'_2 = 0,38\n"
"c_1 = 1,029; a' = 1,06; a = 0,364; b' = 0\n"
"b = 4,17; p_st = 0,44928; P_mex = 0,20854; P_e_1 = 1,012\n"
"P_e_m = 0,559; P_dob = 0,121; SUMMA p= 2,349; P_2 = 21,908\n"
"", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("mainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 1", None))
        ___qtablewidgetitem49 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0447\u0451\u0442\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0443\u043b\u0430", None));
        ___qtablewidgetitem50 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440\u043d\u043e\u0441\u0442\u044c", None));
        ___qtablewidgetitem51 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043a\u043e\u043b\u044c\u0436\u0435\u043d\u0438\u0435 s", None));
        ___qtablewidgetitem52 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("mainWindow", u"s \u043a\u0440", None));
        ___qtablewidgetitem53 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("mainWindow", u"1", None));
        ___qtablewidgetitem54 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("mainWindow", u"2", None));
        ___qtablewidgetitem55 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("mainWindow", u"3", None));
        ___qtablewidgetitem56 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("mainWindow", u"4", None));
        ___qtablewidgetitem57 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("mainWindow", u"5", None));
        ___qtablewidgetitem58 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("mainWindow", u"6", None));
        ___qtablewidgetitem59 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("mainWindow", u"7", None));
        ___qtablewidgetitem60 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("mainWindow", u"8", None));
        ___qtablewidgetitem61 = self.tableWidget_2.verticalHeaderItem(9)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("mainWindow", u"9", None));
        ___qtablewidgetitem62 = self.tableWidget_2.verticalHeaderItem(10)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("mainWindow", u"10", None));
        ___qtablewidgetitem63 = self.tableWidget_2.verticalHeaderItem(11)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("mainWindow", u"11", None));
        ___qtablewidgetitem64 = self.tableWidget_2.verticalHeaderItem(12)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("mainWindow", u"12", None));
        ___qtablewidgetitem65 = self.tableWidget_2.verticalHeaderItem(13)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("mainWindow", u"13", None));
        ___qtablewidgetitem66 = self.tableWidget_2.verticalHeaderItem(14)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("mainWindow", u"14", None));

        __sortingEnabled1 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem67 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("mainWindow", u"1", None));
        ___qtablewidgetitem68 = self.tableWidget_2.item(0, 3)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("mainWindow", u"0.8", None));
        ___qtablewidgetitem69 = self.tableWidget_2.item(0, 4)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("mainWindow", u"0.5", None));
        ___qtablewidgetitem70 = self.tableWidget_2.item(0, 5)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("mainWindow", u"0.2", None));
        ___qtablewidgetitem71 = self.tableWidget_2.item(0, 6)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("mainWindow", u"0.1", None));
        ___qtablewidgetitem72 = self.tableWidget_2.item(0, 7)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("mainWindow", u"0.19", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled1)

        self.bt_calculate_table2.setText(QCoreApplication.translate("mainWindow", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("mainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 2", None))
        ___qtablewidgetitem73 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0447\u0451\u0442\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0443\u043b\u0430", None));
        ___qtablewidgetitem74 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440\u043d\u043e\u0441\u0442\u044c", None));
        ___qtablewidgetitem75 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043a\u043e\u043b\u044c\u0436\u0435\u043d\u0438\u0435 s", None));
        ___qtablewidgetitem76 = self.tableWidget_3.horizontalHeaderItem(7)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("mainWindow", u"s \u043a\u0440", None));
        ___qtablewidgetitem77 = self.tableWidget_3.verticalHeaderItem(1)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("mainWindow", u"1", None));
        ___qtablewidgetitem78 = self.tableWidget_3.verticalHeaderItem(2)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("mainWindow", u"2", None));
        ___qtablewidgetitem79 = self.tableWidget_3.verticalHeaderItem(3)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("mainWindow", u"3", None));
        ___qtablewidgetitem80 = self.tableWidget_3.verticalHeaderItem(4)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("mainWindow", u"4", None));
        ___qtablewidgetitem81 = self.tableWidget_3.verticalHeaderItem(5)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("mainWindow", u"5", None));
        ___qtablewidgetitem82 = self.tableWidget_3.verticalHeaderItem(6)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("mainWindow", u"6", None));
        ___qtablewidgetitem83 = self.tableWidget_3.verticalHeaderItem(7)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("mainWindow", u"7", None));
        ___qtablewidgetitem84 = self.tableWidget_3.verticalHeaderItem(8)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("mainWindow", u"8", None));
        ___qtablewidgetitem85 = self.tableWidget_3.verticalHeaderItem(9)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("mainWindow", u"9", None));
        ___qtablewidgetitem86 = self.tableWidget_3.verticalHeaderItem(10)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("mainWindow", u"10", None));
        ___qtablewidgetitem87 = self.tableWidget_3.verticalHeaderItem(11)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("mainWindow", u"11", None));
        ___qtablewidgetitem88 = self.tableWidget_3.verticalHeaderItem(12)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("mainWindow", u"12", None));
        ___qtablewidgetitem89 = self.tableWidget_3.verticalHeaderItem(13)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("mainWindow", u"13", None));
        ___qtablewidgetitem90 = self.tableWidget_3.verticalHeaderItem(14)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("mainWindow", u"14", None));
        ___qtablewidgetitem91 = self.tableWidget_3.verticalHeaderItem(15)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("mainWindow", u"15", None));
        ___qtablewidgetitem92 = self.tableWidget_3.verticalHeaderItem(16)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("mainWindow", u"16", None));
        ___qtablewidgetitem93 = self.tableWidget_3.verticalHeaderItem(17)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("mainWindow", u"17", None));
        ___qtablewidgetitem94 = self.tableWidget_3.verticalHeaderItem(18)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("mainWindow", u"18", None));
        ___qtablewidgetitem95 = self.tableWidget_3.verticalHeaderItem(19)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("mainWindow", u"19", None));
        ___qtablewidgetitem96 = self.tableWidget_3.verticalHeaderItem(20)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("mainWindow", u"20", None));

        __sortingEnabled2 = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        ___qtablewidgetitem97 = self.tableWidget_3.item(0, 2)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("mainWindow", u"1", None));
        ___qtablewidgetitem98 = self.tableWidget_3.item(0, 3)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("mainWindow", u"0.8", None));
        ___qtablewidgetitem99 = self.tableWidget_3.item(0, 4)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("mainWindow", u"0.5", None));
        ___qtablewidgetitem100 = self.tableWidget_3.item(0, 5)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("mainWindow", u"0.2", None));
        ___qtablewidgetitem101 = self.tableWidget_3.item(0, 6)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("mainWindow", u"0.1", None));
        ___qtablewidgetitem102 = self.tableWidget_3.item(0, 7)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("mainWindow", u"0.19", None));
        self.tableWidget_3.setSortingEnabled(__sortingEnabled2)

        self.bt_calculate_table3.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.bt_show_chart_table3.setText(QCoreApplication.translate("mainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("mainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 3", None))
    # retranslateUi

