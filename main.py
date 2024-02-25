import sys

import matplotlib.pyplot as plt
import pandas as pd

from calculate import MainProgram
from func import SplineCubicInterpolate
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QInputDialog
from PySide6.QtGui import QMovie


from GUI_output import *
from tables import table1, table2, table3
from thermal_calculation import ThermalCalculation

correct_color = QColor(216, 255, 218)
incorrect_color = QColor(255, 216, 216)


class MainWindow(QMainWindow):
    table_2_student = table_1_student = table_3_student = None
    calc_obj, table_1, table_2, table_3 = None, None, None, None
    dialog, layout, password_input, submit_button = None, None, None, None

    def __init__(self, parent=None):
        global P_NOM, U_NOM, _2p_nom
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.scrollArea)
        self.resizetables()
        self.ui.bt_calculate_table1.clicked.connect(self.calculate_table1)
        self.ui.bt_calculate_table2.clicked.connect(self.calculate_table2)
        self.ui.bt_calculate_table3.clicked.connect(self.calculate_table3)
        self.ui.bt_export_xl_1.clicked.connect(self.save_table_to_xl_1)
        self.ui.bt_show_chart_1.clicked.connect(self.show_chart_table_1)
        self.ui.bt_show_chart_table3.clicked.connect(self.show_chart_table_3)
        self.ui.submitValues.clicked.connect(self.submitValuesButton)
        self.ui.bt_check_table_1.clicked.connect(self.checkTable1)
        self.ui.bt_check_table_2.clicked.connect(self.checkTable2)
        self.ui.bt_check_table_3.clicked.connect(self.checkTable3)
        self.ui.sl_ValueOfError.valueChanged.connect(self.changeError)
        self.ui.linePower.currentTextChanged.connect(self.updateVoltage)
        self.ui.bt_thermal_calc.clicked.connect(self.thermalcalculate)
        self.ui.bt_export_xl_table_2.clicked.connect(self.save_table_2_to_xl)
        self.ui.bt_export_xl_table_3.clicked.connect(self.save_table_3_to_xl)

        self.ui.bt_for_teacher.clicked.connect(self.initUI)

        self.setgif()
        self.ui.lb_error_settings.setText(
            str(self.ui.sl_ValueOfError.value()) + "%")

    def checkPassword(self):
        entered_password = self.password_input.text()
        expected_password = 'Y9vV7pz6VS!O(VDI)vDQC8h'

        if entered_password == expected_password:
            self.dialog.accept()
            name = QFileDialog.getSaveFileName(
                self, 'Сохранить файл', '', 'txt (*.txt)', )
            self.calc_obj.RunWithComments(name)

            msgBox = QMessageBox()
            msgBox.setText("Файл создан")
            msgBox.exec()
        else:
            msgBox = QMessageBox()
            msgBox.setText("Неправильный пароль")
            msgBox.exec()
            self.dialog.reject()

    def initUI(self):
        self.dialog = QDialog()
        self.dialog.setWindowTitle('Ввод пароля')

        self.layout = QVBoxLayout()

        self.password_input = QLineEdit(self.dialog)
        self.password_input.setPlaceholderText('Введите пароль')
        self.layout.addWidget(self.password_input)

        self.submit_button = QPushButton('Ввести пароль', self.dialog)
        self.submit_button.clicked.connect(self.checkPassword)
        self.layout.addWidget(self.submit_button)

        self.dialog.setLayout(self.layout)
        self.dialog.exec()

    def showPasswordDialog(self):
        password, ok = QInputDialog.getText(
            self, 'Введите пароль', 'Пароль:', QInputDialog.Password)

        if ok:
            if password == "ваш_пароль":  # Замените "ваш_пароль" на фактический пароль
                print("Пароль верный")
            else:
                print("Неверный пароль")

    def updateVoltage(self):
        if 0 < float(self.ui.linePower.currentText()) < 22:
            self.ui.lineVoltage.setCurrentText("220")
        elif 22 <= float(self.ui.linePower.currentText()) < 100:
            self.ui.lineVoltage.setCurrentText("380")
        else:
            self.ui.lineVoltage.setCurrentText("660")

    def setgif(self):
        movie = QMovie('gif/gif1.gif')
        self.gif1 = QLabel(self.ui.tab_5)
        self.gif1.setObjectName(u"gif1")
        self.gif1.setMovie(movie)
        self.gif1.setGeometry(QRect(25, 415, 600, 500))
        movie.setScaledSize(QSize(550, 350))
        movie.start()
        movie = QMovie('gif/gif2.gif')
        self.gif2 = QLabel(self.ui.tab_4)
        self.gif2.setObjectName(u"gif2")
        self.gif2.setMovie(movie)
        self.gif2.setGeometry(QRect(550, -150, 1425, 823))
        movie.setScaledSize(QSize(900, 450))
        movie.start()

    def resizetables(self):
        self.ui.tableWidget.resizeColumnsToContents()
        # self.ui.tableWidget.setColumnWidth(0, 250)
        # self.ui.tableWidget.setColumnWidth(1, 80)
        # self.ui.tableWidget.setColumnWidth(2, 80)
        # self.ui.tableWidget.setColumnWidth(3, 80)
        # self.ui.tableWidget.setColumnWidth(4, 80)
        # self.ui.tableWidget.setColumnWidth(5, 120)
        # self.ui.tableWidget.setColumnWidth(6, 80)
        # self.ui.tableWidget.setColumnWidth(7, 80)
        # self.ui.tableWidget.setColumnWidth(8, 80)
        self.ui.tableWidget_2.setColumnWidth(0, 390)
        self.ui.tableWidget_2.setColumnWidth(1, 80)
        self.ui.tableWidget_2.setColumnWidth(2, 80)
        self.ui.tableWidget_2.setColumnWidth(3, 80)
        self.ui.tableWidget_2.setColumnWidth(4, 120)
        self.ui.tableWidget_2.setColumnWidth(5, 80)
        self.ui.tableWidget_2.setColumnWidth(6, 80)
        self.ui.tableWidget_2.setColumnWidth(7, 80)
        self.ui.tableWidget_3.setColumnWidth(0, 500)
        self.ui.tableWidget_3.setColumnWidth(1, 80)
        self.ui.tableWidget_3.setColumnWidth(2, 75)
        self.ui.tableWidget_3.setColumnWidth(3, 75)
        self.ui.tableWidget_3.setColumnWidth(4, 110)
        self.ui.tableWidget_3.setColumnWidth(5, 75)
        self.ui.tableWidget_3.setColumnWidth(6, 75)
        self.ui.tableWidget_3.setColumnWidth(7, 75)

    def clearTables(self):
        for i in range(2, 8):
            for j in range(1, 20 + 1):
                self.ui.tableWidget.setItem(j, i, QTableWidgetItem(""))

        for i in range(3, 7 + 1):
            for j in range(1, 14 + 1):
                self.ui.tableWidget_2.setItem(j, i, QTableWidgetItem(""))

        for i in range(3, 7 + 1):
            for j in range(1, 20 + 1):
                self.ui.tableWidget_3.setItem(j, i, QTableWidgetItem(""))

    def checkTable1(self):
        try:
            self.table_1_student = table1(float(self.ui.le_a.text()), float(self.ui.le_a_shtrih.text()),
                                          float(self.ui.le_r2_shtrih.text()), float(
                                              self.ui.le_b.text()),
                                          float(self.ui.le_b_shtrih.text(
                                          )), self.calc_obj.U, float(self.ui.le_I0a.text()), float(self.ui.le_I0p.text()),
                                          float(self.ui.le_c1.text()), float(
                                              self.ui.le_r1.text()),
                                          float(self.ui.le_Pst.text()), float(self.ui.le_Pmeh.text()),
                                          float(self.ui.le_n1.text()))
        except Exception as e:
            msgBox = QMessageBox()
            msgBox.setText(
                "Неправильно введены значения")
            msgBox.exec()
        count = 0
        for i in range(1, 20 + 1):
            self.ui.tableWidget.item(i, 8).setBackground(incorrect_color)

            try:
                curr_value = float(self.ui.tableWidget.item(i, 8).text())
            except Exception as e:
                continue

            self.ui.tableWidget.item(i, 8).setFlags(
                self.ui.tableWidget.item(i, 8).flags() & ~Qt.ItemIsSelectable)
            if (
                self.table_1_student.calculateTable(i, self.calc_obj.s_nom) * (1 - (self.ui.sl_ValueOfError.value() / 100)) < curr_value < self.table_1_student.calculateTable(i,self.calc_obj.s_nom) * (1 + (self.ui.sl_ValueOfError.value() / 100))
                ):
                self.ui.tableWidget.item(i, 8).setBackground(correct_color)
                count += 1

        if (count == 20):
            self.ui.bt_calculate_table1.setEnabled(True)


    def checkTable2(self):

        try:
            self.table_2_student = table2(
                float(self.ui.le_h_c.text()), float(
                    self.ui.le_h_p_2.text()), float(self.ui.le_h_sh.text()),
                float(self.ui.le_h_sh_shtrih.text()), float(
                    self.ui.le_b_1_r.text()), float(self.ui.le_b_2_r.text()),
                float(self.ui.le_h_1.text()), float(self.ui.le_q_c.text()
                                                    ), float(self.ui.le_r_c.text()), self.calc_obj.U,
                float(self.ui.le_r1.text()), float(
                    self.ui.le_r_2.text()), float(self.ui.le_r2_shtrih.text()), float(self.ui.le_h_0.text()),
                float(self.ui.le_b_sh_2.text()),
                float(self.ui.le_Lamda_p_2.text()), float(
                    self.ui.le_Lamda_l_2.text()),
                float(self.ui.le_Lamda_d_2.text()), float(
                    self.ui.le_X_2_shtrih.text()),
                float(self.ui.le_x_1_2_p.text()), float(
                    self.ui.le_c_1_p.text()), float(self.ui.le_X_1.text())
            )
        except Exception as e:
            msgBox = QMessageBox()
            msgBox.setText(
                "Неправильно введены значения")
            msgBox.exec()

        count = 0
        for i in range(1, 14 + 1):
            self.ui.tableWidget_2.item(i, 2).setBackground(incorrect_color)

            try:
                curr_value = float(self.ui.tableWidget_2.item(i, 2).text())
            except Exception as e:
                continue

            self.ui.tableWidget_2.item(i, 2).setFlags(
                self.ui.tableWidget_2.item(i, 2).flags() & ~Qt.ItemIsSelectable)

            if (
                self.table_2_student.calculateTable(i, 1) * (1 - (self.ui.sl_ValueOfError.value() / 100)) < curr_value < self.table_2_student.calculateTable(i, 1) * (1 + (self.ui.sl_ValueOfError.value() / 100))
                ):
                self.ui.tableWidget_2.item(i, 2).setBackground(correct_color)
                count += 1

        if count == 14:
            self.ui.bt_calculate_table2.setEnabled(True)


    def checkTable3(self):

        try:
            self.table_3_student = table3(
                float(self.ui.le_C_N.text()), float(
                    self.ui.le_k_y_1.text()), float(self.ui.le_u_p.text()),
                float(self.ui.le_k_ob.text()), float(self.ui.le_X_1.text()), float(
                    self.ui.le_Z_1.text()), float(self.ui.le_Z_2.text()),
                float(self.ui.le_delta.text()), float(self.ui.le_t_z_1.text()),
                float(self.ui.le_b_sh.text()), float(
                    self.ui.le_h_sh_r.text()), float(self.ui.le_Lamda_p_1.text()),
                float(self.ui.le_Lamda_d_1.text()), float(
                    self.ui.le_Lamda_l_1.text()),
                float(self.ui.le_x_1_2_p.text()), float(
                    self.ui.le_t_z_2.text()), float(self.ui.le_b_sh_2.text()),
                float(self.ui.le_Lamda_p_2.text()), float(
                    self.ui.le_Lamda_l_2.text()),
                float(self.ui.le_Lamda_d_2.text()), float(
                    self.ui.le_h_sh_shtrih.text()),
                float(self.ui.le_X_2_shtrih.text()), float(
                    self.ui.le_r1.text()),
                float(self.ui.le_r_2_Ksi_shtrih.text()), self.calc_obj.U, float(
                    self.ui.le_I_1_p.text()),
                float(self.ui.le_I_1_nom.text()), self.table_1_student.calculateTable(
                    11, self.calc_obj.s_nom),
                self.calc_obj.s_nom, float(self.ui.le_h_k.text()), float(
                    self.ui.le_Lamda_p_2_Ksi.text()),
                float(self.ui.le_K_R.text()), self.table_2_student
            )
        except Exception as e:
            msgBox = QMessageBox()
            msgBox.setText(
                "Неправильно введены значения")
            msgBox.exec()

        count = 0
        for i in range(1, 20 + 1):
            self.ui.tableWidget_3.item(i, 2).setBackground(incorrect_color)

            try:
                curr_value = float(self.ui.tableWidget_3.item(i, 2).text())
            except Exception as e:
                continue

            self.ui.tableWidget_3.item(i, 2).setFlags(
                self.ui.tableWidget_3.item(i, 2).flags() & ~Qt.ItemIsSelectable)

            if (
                self.table_3_student.calculateTable(i, 1) * (1 - (self.ui.sl_ValueOfError.value() / 100)) < curr_value < self.table_3_student.calculateTable(i, 1) * (1 + (self.ui.sl_ValueOfError.value() / 100))
                ):
                self.ui.tableWidget_3.item(i, 2).setBackground(correct_color)
                count += 1

        if count == 20:
            self.ui.bt_calculate_table3.setEnabled(True)


    def submitValuesButton(self):
        P_2 = float(self.ui.linePower.currentText())
        U = int(self.ui.lineVoltage.currentText())
        _2p = int(self.ui.linePolarity.currentText())
        heatClass = self.ui.cmb_heatClass.currentText()

        try:
            S_nom = float(self.ui.lineSnom.text())
            if (not (0 < S_nom <= 1)):
                raise KeyError()
        except ValueError:
            msgBox = QMessageBox()
            msgBox.setText(
                "Введены недопустимые символы")
            msgBox.exec()
            return
        except KeyError:
            msgBox = QMessageBox()
            msgBox.setText("Некорректно введено S_nom (0;1]")
            msgBox.exec()
            return
        try:
            self.calc_obj = MainProgram(P_2, U, _2p, heatClass, S_nom)
            #self.calc_obj.Run()
        except KeyError:
            msgBox = QMessageBox()
            msgBox.setText(
                "Неккоректно введена полярность")
            msgBox.exec()
            return
        except Exception:
            msgBox = QMessageBox()
            msgBox.setText(
                "Напряжение не соответствует мощности, попробуйте снова")
            msgBox.exec()
            return

        self.ui.tableWidget.item(0, 2).setText(str(round(S_nom / 7, 3)))
        self.ui.tableWidget.item(0, 3).setText(str(round(2 * S_nom / 7, 3)))
        self.ui.tableWidget.item(0, 4).setText(str(round(3 * S_nom / 7, 3)))
        self.ui.tableWidget.item(0, 5).setText(str(round(4 * S_nom / 7, 3)))
        self.ui.tableWidget.item(0, 6).setText(str(round(5 * S_nom / 7, 3)))
        self.ui.tableWidget.item(0, 7).setText(str(round(6 * S_nom / 7, 3)))
        self.ui.tableWidget.item(0, 8).setText(str(round(S_nom, 3)))

        # self.table_1 = table1(
        #     self.calc_obj.a, self.calc_obj.a_shtrih, self.calc_obj.r_2_shtrih, self.calc_obj.b, self.calc_obj.b_shtrih, self.calc_obj.U,
        #     self.calc_obj.I_0_a, self.calc_obj.I_nu, self.calc_obj.C_1, self.calc_obj.r_1, self.calc_obj.P_st, self.calc_obj.P_meh
        # )
        # self.table_2 = table2(
        #     self.calc_obj.h_c, self.calc_obj.h_p_2, self.calc_obj.h_sh, self.calc_obj.h_sh_shtrih, self.calc_obj.b_1_r,
        #     self.calc_obj.b_2_r, self.calc_obj.h_1, self.calc_obj.q_c, self.calc_obj.r_c, self.calc_obj.U, self.calc_obj.r_1,
        #     self.calc_obj.r_2, self.calc_obj.r_2_shtrih, self.calc_obj.h_0,
        #     self.calc_obj.b_sh_2, self.calc_obj.Lamda_p_2, self.calc_obj.Lamda_l_2, self.calc_obj.Lamda_d_2,
        #     self.calc_obj.X_2_shtrih, self.calc_obj.x_1_2_p, self.calc_obj.c_1_p, self.calc_obj.X_1
        # )
        # self.table_3 = table3(
        #     self.calc_obj.C_N, self.calc_obj.k_y_1, self.calc_obj.u_p, self.calc_obj.k_ob, self.calc_obj.X_1, self.calc_obj.Z_1,
        #     self.calc_obj.Z_2,
        #     self.calc_obj.delta, self.calc_obj.t_z_1, self.calc_obj.b_sh, self.calc_obj.h_sh_r,
        #     self.calc_obj.Lamda_p_1, self.calc_obj.Lamda_d_1, self.calc_obj.Lamda_l_1, self.calc_obj.x_1_2_p, self.calc_obj.t_z_2,
        #     self.calc_obj.b_sh_2, self.calc_obj.Lamda_p_2, self.calc_obj.Lamda_l_2, self.calc_obj.Lamda_d_2,
        #     self.calc_obj.h_sh_shtrih, self.calc_obj.X_2_shtrih, self.calc_obj.r_1, self.calc_obj.r_2_Ksi_shtrih, self.calc_obj.U,
        #     self.calc_obj.I_1_p, self.calc_obj.I_1_nom, self.table_1.calculateTable(
        #         11, self.calc_obj.s_nom), self.calc_obj.s_nom,
        #     self.calc_obj.h_k, self.calc_obj.Lamda_p_2_Ksi, self.calc_obj.K_R, self.table_2
        # )

        self.ui.tab.setEnabled(True)
        self.ui.tab_2.setEnabled(True)
        self.ui.tab_3.setEnabled(True)
        self.ui.tableWidget.setEnabled(True)
        self.ui.tableWidget_2.setEnabled(True)
        self.ui.tableWidget_3.setEnabled(True)

        self.ui.bt_check_table_1.setEnabled(True)
        self.ui.bt_calculate_table1.setEnabled(False)
        self.ui.bt_show_chart_1.setEnabled(False)
        self.ui.bt_export_xl_1.setEnabled(False)
        self.ui.bt_calculate_table2.setEnabled(False)
        self.ui.bt_export_xl_table_2.setEnabled(False)
        self.ui.bt_export_xl_table_3.setEnabled(False)
        self.ui.bt_calculate_table3.setEnabled(False)
        self.ui.bt_show_chart_table3.setEnabled(False)
        self.ui.bt_thermal_calc.setEnabled(False)

        self.ui.bt_for_teacher.setEnabled(True)

        self.clearTables()
        self.ui.tabWidget.setCurrentWidget(self.ui.tab)

        self.ui.lb_error.setText(
            "Допустимая погрешность при проверке = " + str(self.ui.sl_ValueOfError.value()) + "%")
        self.ui.lb_error_2.setText(
            "Допустимая погрешность при проверке = " + str(self.ui.sl_ValueOfError.value()) + "%")
        self.ui.lb_error_3.setText(
            "Допустимая погрешность при проверке = " + str(self.ui.sl_ValueOfError.value()) + "%")

        for i in range(1, 19 + 1):
            for j in range(0, 9):
                if (i % 2):
                    self.ui.tableWidget.item(i, j).setBackground(
                        QColor(230, 230, 230))
                else:
                    self.ui.tableWidget.item(i, j).setBackground(
                        QColor(255, 255, 255))
                if (j < 9 - 1):
                    self.ui.tableWidget.item(i, j).setFlags(~Qt.ItemIsEditable)

        for i in range(1, 14 + 1):
            for j in range(0, 8):
                if (i % 2):
                    self.ui.tableWidget_2.item(
                        i, j).setBackground(QColor(230, 230, 230))
                else:
                    self.ui.tableWidget.item(i, j).setBackground(
                        QColor(255, 255, 255))
                if (j > 2):
                    self.ui.tableWidget_2.item(
                        i, j).setFlags(~Qt.ItemIsEditable)

        for i in range(1, 20 + 1):
            for j in range(0, 8):
                if (i % 2):
                    self.ui.tableWidget_3.item(
                        i, j).setBackground(QColor(230, 230, 230))
                #else:
                    # self.ui.tableWidget.item(i, j).setBackground(
                    #     QColor(255, 255, 255))
                if (j > 2):
                    self.ui.tableWidget_3.item(
                        i, j).setFlags(~Qt.ItemIsEditable)

        self.ui.le_Pst.setEnabled(True)
        self.ui.le_Pmeh.setEnabled(True)
        self.ui.le_a.setEnabled(True)
        self.ui.le_a_shtrih.setEnabled(True)
        self.ui.le_b.setEnabled(True)
        self.ui.le_b_shtrih.setEnabled(True)
        self.ui.le_I0p.setEnabled(True)
        self.ui.le_I0a.setEnabled(True)
        self.ui.le_r1.setEnabled(True)
        self.ui.le_r2_shtrih.setEnabled(True)
        self.ui.le_c1.setEnabled(True)

        self.ui.le_h_c.setEnabled(True)
        self.ui.le_h_p_2.setEnabled(True)
        self.ui.le_h_sh.setEnabled(True)
        self.ui.le_h_sh_shtrih.setEnabled(True)
        self.ui.le_b_1_r.setEnabled(True)
        self.ui.le_b_2_r.setEnabled(True)
        self.ui.le_h_1.setEnabled(True)
        self.ui.le_q_c.setEnabled(True)
        self.ui.le_r_2.setEnabled(True)
        self.ui.le_h_0.setEnabled(True)
        self.ui.le_b_sh_2.setEnabled(True)
        self.ui.le_Lamda_p_2.setEnabled(True)
        self.ui.le_Lamda_d_2.setEnabled(True)
        self.ui.le_Lamda_l_2.setEnabled(True)
        self.ui.le_X_2_shtrih.setEnabled(True)
        self.ui.le_x_1_2_p.setEnabled(True)
        self.ui.le_c_1_p.setEnabled(True)
        self.ui.le_X_1.setEnabled(True)
        self.ui.le_r_c.setEnabled(True)

        self.ui.le_C_N.setEnabled(True)
        self.ui.le_k_y_1.setEnabled(True)
        self.ui.le_u_p.setEnabled(True)
        self.ui.le_k_ob.setEnabled(True)
        self.ui.le_Z_1.setEnabled(True)
        self.ui.le_Z_2.setEnabled(True)
        self.ui.le_delta.setEnabled(True)
        self.ui.le_t_z_1.setEnabled(True)
        self.ui.le_b_sh.setEnabled(True)
        self.ui.le_h_sh_r.setEnabled(True)
        self.ui.le_Lamda_l_1.setEnabled(True)
        self.ui.le_Lamda_p_1.setEnabled(True)
        self.ui.le_Lamda_d_1.setEnabled(True)
        self.ui.le_t_z_2.setEnabled(True)
        self.ui.le_r_2_Ksi_shtrih.setEnabled(True)
        self.ui.le_I_1_p.setEnabled(True)
        self.ui.le_I_1_nom.setEnabled(True)
        self.ui.le_Lamda_p_2_Ksi.setEnabled(True)
        self.ui.le_h_k.setEnabled(True)
        self.ui.le_K_R.setEnabled(True)
        self.ui.le_n1.setEnabled(True)

    def save_table_to_xl_1(self):
        col_count = self.ui.tableWidget.columnCount()
        row_count = self.ui.tableWidget.rowCount()
        df_list = []

        headers = [str(self.ui.tableWidget.horizontalHeaderItem(i).text())
                   for i in range(col_count)]

        # df indexing is slow, so use lists

        for row in range(row_count):
            df_list2 = []
            for col in range(col_count):
                if col <= 1:
                    table_item = self.ui.tableWidget.item(row, col)
                    df_list2.append(
                        '' if table_item is None else str(table_item.text()))
                else:
                    table_item = self.ui.tableWidget.item(row, col)
                    df_list2.append(
                        '' if table_item is None else float(table_item.text()))
            df_list.append(df_list2)

        df_list.append(list([]))

        df_list.append(list(
            [f'P_2 = {self.calc_obj.P_2}', f'U = {self.calc_obj.U}', f'2p = {self.calc_obj._2p}',
             f'I0a = {round(self.table_1_student.I_0_a, 3)}', f'I0p = {round(self.table_1_student.I_nu, 3)}',
             f'Pст+Pмех = {round(self.table_1_student.P_st + self.table_1_student.P_meh, 3)}',
             f'r1 = {round(self.table_1_student.r_1, 3)}', f"r'2 = {round(self.table_1_student.r_2_shtrih, 3)}",
             f'c1 = {round(self.table_1_student.C_1, 3)}']))
        df_list.append(list(
            [f" a' = {round(self.table_1_student.a_shtrih, 3)}", f'a = {round(self.table_1_student.a, 3)}',
             f"b' = {round(self.table_1_student.b_shtrih, 3)}", f'b = {round(self.table_1_student.b, 3)}']))

        df = pd.DataFrame(df_list, columns=headers)
        name = QFileDialog.getSaveFileName(
            self, 'Сохранить файл', '', 'XLSX File (*.xlsx)',)
        if name[0] != '':
            writer = pd.ExcelWriter(name[0], mode='w')
            df.to_excel(writer, f'Двигатель {len(writer.sheets)}')
            writer._save()

    def save_table_2_to_xl(self):
        col_count = self.ui.tableWidget_2.columnCount()
        row_count = self.ui.tableWidget_2.rowCount()
        df_list = []
        headers = [str(self.ui.tableWidget.horizontalHeaderItem(i).text())
                   for i in range(col_count)]

        # df indexing is slow, so use lists

        for row in range(row_count):
            df_list2 = []
            for col in range(col_count):
                if col <= 1:
                    table_item = self.ui.tableWidget_2.item(row, col)
                    df_list2.append(
                        '' if table_item is None else str(table_item.text()))
                else:
                    table_item = self.ui.tableWidget_2.item(row, col)
                    df_list2.append(
                        '' if table_item is None else float(table_item.text()))
            df_list.append(df_list2)

        df_list.append(list([]))

        df_list.append(list(
            [f'P_2 = {self.calc_obj.P_2}', f'U = {self.calc_obj.U}', f'2p = {self.calc_obj._2p}',
             f"I'2ном = {round(self.table_1_student.calculateTable(11,self.calc_obj.s_nom), 3)}",
             f'x1 = {round(self.table_2_student.X_1, 3)}', f"x'2 = {round(self.table_2_student.X_2_shtrih, 3)}",
             f'r1 = {round(self.table_2_student.r_1, 3)}', f"r'2 = {round(self.table_2_student.r_2_shtrih, 3)}"
             ]))
        df_list.append(list(
            [f'c1п = {round(self.table_2_student.c_1_p, 3)}', f" x12п = {round(self.table_2_student.x_1_2_p, 3)}", f'sном = {round(self.calc_obj.s_nom, 3)}']))

        df = pd.DataFrame(df_list, columns=headers)
        name = QFileDialog.getSaveFileName(
            self, 'Сохранить файл', '', 'XLSX File (*.xlsx)', )
        if name[0] != '':
            writer = pd.ExcelWriter(name[0], mode='w')
            df.to_excel(writer, f'Двигатель {len(writer.sheets)}')
            writer._save()

    def save_table_3_to_xl(self):
        col_count = self.ui.tableWidget_3.columnCount()
        row_count = self.ui.tableWidget_3.rowCount()
        df_list = []
        headers = [str(self.ui.tableWidget.horizontalHeaderItem(i).text())
                   for i in range(col_count)]

        # df indexing is slow, so use lists

        for row in range(row_count):
            df_list2 = []
            for col in range(col_count):
                if col <= 1:
                    table_item = self.ui.tableWidget_3.item(row, col)
                    df_list2.append(
                        '' if table_item is None else str(table_item.text()))
                else:
                    table_item = self.ui.tableWidget_3.item(row, col)
                    df_list2.append(
                        '' if table_item is None else float(table_item.text()))
            df_list.append(df_list2)

        df_list.append(list([]))

        df_list.append(list(
            [f'P_2 = {self.calc_obj.P_2}', f'U = {self.calc_obj.U}', f'2p = {self.calc_obj._2p}', f"I1ном = {round(self.table_3_student.I_1_nom, 3)}",
             f"I'2ном = {round(self.table_1_student.calculateTable(11,self.calc_obj.s_nom), 3)}",
             f'x1 = {round(self.table_3_student.X_1, 3)}', f"x'2 = {round(self.table_3_student.X_2_shtrih, 3)}",
             f'r1 = {round(self.table_3_student.r_1, 3)}',
             ]))
        df_list.append(list(
            [f"r'2 = {round(self.table_2_student.r_2_shtrih, 3)}",
             f" x12п = {round(self.table_3_student.x_1_2_p, 3)}", f'sном = {round(self.calc_obj.s_nom, 3)}',
             f"C_N = {round(self.table_3_student.C_N, 3)}"]))

        df = pd.DataFrame(df_list, columns=headers)
        name = QFileDialog.getSaveFileName(
            self, 'Сохранить файл', '', 'XLSX File (*.xlsx)', )
        if name[0] != '':
            writer = pd.ExcelWriter(name[0], mode='w')
            df.to_excel(writer, f'Двигатель {len(writer.sheets)}')
            writer._save()

    def show_chart_table_1(self):
        x_arr = [0]
        y_arr_1 = [0]
        y_arr_2 = [0]
        y_arr_3 = [0]
        y_arr_4 = [0]
        y_arr_5 = [0]

        S_nom = float(self.ui.tableWidget.item(0, 8).text())

        length_of_s_nom = 10_000

        for i in range(round(length_of_s_nom * (S_nom / 7)), round(length_of_s_nom * S_nom)):
            x_arr.append(
                round(self.table_1_student.calculateTable(12, i / length_of_s_nom), 3))
        for i in range(round(length_of_s_nom * (S_nom / 7)), round(length_of_s_nom * S_nom)):
            y_arr_1.append(
                round(self.table_1_student.calculateTable(19, i / length_of_s_nom), 3))
        for i in range(round(length_of_s_nom * (S_nom / 7)), round(length_of_s_nom * S_nom)):
            y_arr_2.append(
                round(self.table_1_student.calculateTable(18, i / length_of_s_nom), 3))
        for i in range(round(length_of_s_nom * (S_nom / 7)), round(length_of_s_nom * S_nom)):
            y_arr_3.append(i / length_of_s_nom)
        for i in range(round(length_of_s_nom * (S_nom / 7)), round(length_of_s_nom * S_nom)):
            y_arr_4.append(
                round(self.table_1_student.calculateTable(10, i / length_of_s_nom), 3))
        for i in range(round(length_of_s_nom * (S_nom / 7)), round(length_of_s_nom * S_nom)):
            y_arr_5.append(
                round(self.table_1_student.calculateTable(20, i / length_of_s_nom), 3))

        y_arr_1[0] = y_arr_1[1] * 0.1
        y_arr_4[0] = y_arr_4[1] * 0.75

        fig = plt.figure()

        cosPhi_chart = fig.add_subplot(2, 3, 1)
        kpd_chart = fig.add_subplot(2, 3, 2)
        s_chart = fig.add_subplot(2, 3, 3)
        I_1_chart = fig.add_subplot(2, 3, 4)
        n_chart = fig.add_subplot(2, 3, 5)

        x_list = [x / 50 for x in range(0, round(x_arr[-1] * 50))]

        cosPhi_chart.plot(x_list, [SplineCubicInterpolate(x, x_arr, y_arr_1)
                                   for x in x_list], color='red', marker='o', markersize=0.5, linewidth=1)
        cosPhi_chart.minorticks_on()
        cosPhi_chart.grid(which='major',
                          color='k',
                          linewidth=1)
        cosPhi_chart.grid(which='minor',
                          color='k',
                          linestyle=':')
        cosPhi_chart.set_ylabel('cos(φ)', size=16)
        cosPhi_chart.set_xlabel('P_квт', size=16)
        cosPhi_chart.set_ylim(0, 1)

        kpd_chart.plot(x_list, [SplineCubicInterpolate(x, x_arr, y_arr_2)
                                for x in x_list], color='red', marker='o', markersize=0.5, linewidth=1)
        kpd_chart.minorticks_on()
        kpd_chart.grid(which='major',
                       color='k',
                       linewidth=1)
        kpd_chart.grid(which='minor',
                       color='k',
                       linestyle=':')
        kpd_chart.set_ylabel('η', size=16)
        kpd_chart.set_xlabel('P_квт', size=16)
        kpd_chart.set_ylim(0, 1)

        s_chart.plot(x_list, [SplineCubicInterpolate(x, x_arr, y_arr_3)
                              for x in x_list], color='red', marker='o', markersize=0.5, linewidth=1)
        s_chart.minorticks_on()
        s_chart.grid(which='major',
                     color='k',
                     linewidth=1)
        s_chart.grid(which='minor',
                     color='k',
                     linestyle=':')
        s_chart.set_ylabel('s', size=16)
        s_chart.set_xlabel('P_квт', size=16)

        I_1_chart.plot(x_list, [SplineCubicInterpolate(x, x_arr, y_arr_4)
                                for x in x_list], color='red', marker='o', markersize=0.5, linewidth=1)
        I_1_chart.minorticks_on()
        I_1_chart.grid(which='major',
                       color='k',
                       linewidth=1)
        I_1_chart.grid(which='minor',
                       color='k',
                       linestyle=':')
        I_1_chart.set_ylabel('I₁', size=16)
        I_1_chart.set_xlabel('P_квт', size=16)

        n_chart.plot(x_list, [SplineCubicInterpolate(x, x_arr, y_arr_5)
                                   for x in x_list], color='red', marker='o', markersize=0.5, linewidth=1)
        n_chart.minorticks_on()
        n_chart.grid(which='major',
                          color='k',
                          linewidth=1)
        n_chart.grid(which='minor',
                          color='k',
                          linestyle=':')
        n_chart.set_ylabel('n', size=16)
        n_chart.set_xlabel('P_квт', size=16)

        fig.set_figwidth(16)
        fig.set_figheight(9)

        plt.show()

    def show_chart_table_3(self):

        x_arr = [0]
        y_arr_1 = [0]
        y_arr_2 = [0]

        fig = plt.figure()

        length_of_s_nom = 10

        for i in range(round(0.1 * length_of_s_nom), length_of_s_nom):
            x_arr.append(i / length_of_s_nom)
        for i in range(round(0.1 * length_of_s_nom), length_of_s_nom):
            y_arr_1.append(
                round(self.table_3_student.calculateTable(19, i / length_of_s_nom), 3))
        for i in range(round(0.1 * length_of_s_nom), length_of_s_nom):
            y_arr_2.append(
                round(self.table_3_student.calculateTable(20, i / length_of_s_nom), 3))

        # x_arr.sort()
        # y_arr_1.sort()
        # y_arr_2.reverse()
        # y_arr_2.remove(0)
        # y_arr_2.insert(0, 0)
        # print(y_arr_1)
        # print(x_arr)
        # print(y_arr_2)

        I_dot = fig.add_subplot(1, 2, 1)
        M_star = fig.add_subplot(1, 2, 2)

        x_list = [x / 1000 for x in range(0, round(x_arr[-1] * 1000))]

        I_dot.plot(x_list, [SplineCubicInterpolate(x, x_arr, y_arr_1)
                            for x in x_list], color='red', marker='o', markersize=0.5, linewidth=1)
        I_dot.minorticks_on()
        I_dot.grid(which='major',
                   color='k',
                   linewidth=1)
        I_dot.grid(which='minor',
                   color='k',
                   linestyle=':')
        I_dot.set_ylabel('I.', size=16)
        I_dot.set_xlabel('s', size=16)

        M_star.plot(x_list, [SplineCubicInterpolate(x, x_arr, y_arr_2)
                             for x in x_list], color='red', marker='o', markersize=0.5, linewidth=1)
        M_star.minorticks_on()
        M_star.grid(which='major',
                    color='k',
                    linewidth=1)
        M_star.grid(which='minor',
                    color='k',
                    linestyle=':')
        M_star.set_ylabel('M*', size=16)
        M_star.set_xlabel('s', size=16)

        fig.set_figwidth(10)
        fig.set_figheight(6)

        plt.show()

    def calculate_table1(self):
        self.ui.bt_show_chart_1.setEnabled(True)
        self.ui.bt_export_xl_1.setEnabled(True)

        for i in range(2, 8):
            for j in range(1, 20 + 1):
                self.ui.tableWidget.item(j, i).setText(
                    str(round(self.table_1_student.calculateTable(j, float(self.ui.tableWidget.item(0, i).text())), 3)))
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.reset()

    def calculate_table2(self):


        for i in range(3, 7 + 1):
            for j in range(1, 14 + 1):
                self.ui.tableWidget_2.item(j, i).setText(str(round(self.table_2_student.calculateTable(
                    j, float(self.ui.tableWidget_2.item(0, i).text())), 3)))
        self.ui.tableWidget_2.reset()
        self.ui.bt_export_xl_table_2.setEnabled(True)

    def calculate_table3(self):


        try:
            for i in range(3, 7 + 1):
                for j in range(1, 20 + 1):
                    self.ui.tableWidget_3.item(j, i).setText(
                        str(round(self.table_3_student.calculateTable(j, float(self.ui.tableWidget_3.item(0, i).text())),
                                  2)))
            self.ui.bt_export_xl_table_3.setEnabled(True)
            self.ui.bt_show_chart_table3.setEnabled(True)
            self.ui.tableWidget_3.reset()
        except Exception as e:
            msgBox = QMessageBox()
            msgBox.setText(
                "Необходимо посчитать прошлые таблицы")
            msgBox.exec()

        self.ui.bt_thermal_calc.setEnabled(True)

    def changeError(self):
        self.ui.lb_error.setText(
            "Погрешность при проверке = " + str(self.ui.sl_ValueOfError.value()) + "%")
        self.ui.lb_error_2.setText(
            "Погрешность при проверке = " + str(self.ui.sl_ValueOfError.value()) + "%")
        self.ui.lb_error_3.setText(
            "Погрешность при проверке = " + str(self.ui.sl_ValueOfError.value()) + "%")
        self.ui.lb_error_settings.setText(
            str(self.ui.sl_ValueOfError.value()) + "%")

        self.ui.bt_calculate_table1.setEnabled(False)
        self.clearTables()

    def thermalcalculate(self):
        k_ro = {"F": 1.07, "B": 1.15, "H": 1.45}
        if (self.calc_obj.h <= 132):
            m_shtrih = 1.8
        else:
            m_shtrih = 2.5
        try:
            tc = ThermalCalculation(self.calc_obj.K, k_ro[self.calc_obj.heatClass],
                                    self.table_1_student.calculateTable(
                                        13, self.calc_obj.s_nom),
                                    float(self.ui.le_P_st_main.text()),
                                    float(self.ui.le_D.text()), float(
                                        self.ui.le_l_1.text()), float(self.ui.le_a_1.text()),
                                    float(self.ui.le_Z_1.text()), float(
                                        self.ui.le_h_pk.text()),
                                    float(self.ui.le_b_iz_p_1.text()),
                                    float(self.ui.le_b_1.text()), float(
                                        self.ui.le_b_2.text()),
                                    float(self.ui.le_lambda_ekv_shtrih.text()),
                                    float(self.ui.le_l_l_1.text()), float(
                                        self.ui.le_b_iz_l_1.text()),
                                    float(self.ui.le_h_p_1.text()),
                                    float(self.ui.le_l_vbl.text()), float(
                                        self.ui.le_l_avg_1.text()),
                                    self.table_1_student.calculateTable(
                                        16, self.calc_obj.s_nom),
                                    self.table_1_student.calculateTable(
                                        14, self.calc_obj.s_nom),
                                    float(self.ui.le_Pmeh.text()),
                                    float(self.ui.le_s_kor.text()), float(
                                        self.ui.le_a_v.text()), m_shtrih, self.calc_obj.n,
                                    float(self.ui.le_D_a.text()))
            self.ui.lb_delta_nu_pov_1.setText(
                str(round(tc.delta_nu_pov_1, 3)) + " \u00b0C")
            self.ui.lb_delta_nu_iz_p_1.setText(
                str(round(tc.delta_nu_iz_p_1, 3)) + " \u00b0C")
            self.ui.lb_delta_nu_iz_l_1.setText(
                str(round(tc.delta_nu_iz_l_1, 3)) + " \u00b0C")
            self.ui.lb_delta_nu_pov_l_1.setText(
                str(round(tc.delta_nu_pov_l_1, 3)) + " \u00b0C")
            self.ui.lb_delta_gamma_v.setText(
                str(round(tc.delta_gamma_v, 3)) + " \u00b0C")
            self.ui.lb_teta_v_shtrih.setText(
                str(round(tc.teta_v_shtrih, 3)) + " м^3/c")
            self.ui.lb_Q_v.setText(str(round(tc.Q_v, 3)) + " м^3/c")
            self.ui.lb_delta_nu_1_shtrih.setText(
                str(round(tc.delta_nu_1_shtrih, 3)) + " \u00b0C")
            self.ui.lb_delta_nu_1.setText(
                str(round(tc.delta_nu_1, 3)) + " \u00b0C")
        except Exception as e:
            msgBox = QMessageBox()
            msgBox.setText(
                "Необходимо посчитать таблицы")
            msgBox.exec()


app = QApplication()
window = MainWindow()
window.show()
sys.exit(app.exec())

