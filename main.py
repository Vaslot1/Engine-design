import sys

import matplotlib.pyplot as plt
from PyQt6 import uic
import pandas as pd
from main2 import MainProgram
from func import Lagrange, LinearInterpolation, SplineCubicInterpolate
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ww import *
from tables import table1, table2, table3
from scipy import interpolate
from openpyxl import Workbook

correct_color = QColor(216, 255, 218)
incorrect_color = QColor(255, 216, 216)


class MainWindow(QMainWindow):
    table_student_2 = table_student_1 = table_student_3 = None
    aboba, table_1, table_2, table_3 = None, None, None, None

    def __init__(self, parent=None):
        global P_NOM, U_NOM, _2p_nom
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.tabWidget)
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
            for j in range(1, 19 + 1):
                self.ui.tableWidget.setItem(j, i, QTableWidgetItem(""))

        for i in range(2, 7 + 1):
            for j in range(1, 14 + 1):
                self.ui.tableWidget_2.setItem(j, i, QTableWidgetItem(""))

        for i in range(2, 7 + 1):
            for j in range(1, 20 + 1):
                self.ui.tableWidget_3.setItem(j, i, QTableWidgetItem(""))

    def checkTable1(self):

        count = 0
        for i in range(1, 19 + 1):
            self.ui.tableWidget.item(i, 8).setBackground(incorrect_color)

            try:
                curr_value = float(self.ui.tableWidget.item(i, 8).text())
            except Exception as e:
                continue

            self.ui.tableWidget.item(i, 8).setFlags(self.ui.tableWidget.item(i, 8).flags() & ~Qt.ItemIsSelectable)

            if (self.table_1.calculateTable(i, self.aboba.s_nom) * 0.9 < curr_value < self.table_1.calculateTable(i,
                                                                                                                  self.aboba.s_nom) * 1.1):
                self.ui.tableWidget.item(i, 8).setBackground(correct_color)
                count += 1

        if (count == 19):
            self.ui.bt_calculate_table1.setEnabled(True)
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

    def checkTable2(self):

        count = 0
        for i in range(1, 14 + 1):
            self.ui.tableWidget_2.item(i, 2).setBackground(incorrect_color)

            try:
                curr_value = float(self.ui.tableWidget_2.item(i, 2).text())
            except Exception as e:
                continue

            self.ui.tableWidget_2.item(i, 2).setFlags(self.ui.tableWidget_2.item(i, 2).flags() & ~Qt.ItemIsSelectable)

            if self.table_2.calculateTable(i, 1) * 0.9 < curr_value < self.table_2.calculateTable(i, 1) * 1.1:
                self.ui.tableWidget_2.item(i, 2).setBackground(correct_color)
                count += 1

        if count == 14:
            self.ui.bt_calculate_table2.setEnabled(True)
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

    def checkTable3(self):

        count = 0
        for i in range(1, 20 + 1):
            self.ui.tableWidget_3.item(i, 2).setBackground(incorrect_color)

            try:
                curr_value = float(self.ui.tableWidget_3.item(i, 2).text())
            except Exception as e:
                continue

            self.ui.tableWidget_3.item(i, 2).setFlags(self.ui.tableWidget_3.item(i, 2).flags() & ~Qt.ItemIsSelectable)

            if self.table_3.calculateTable(i, 1) * 0.9 < curr_value < self.table_3.calculateTable(i, 1) * 1.1:
                self.ui.tableWidget_3.item(i, 2).setBackground(correct_color)
                count += 1

        if count == 20:
            self.ui.bt_calculate_table3.setEnabled(True)
            self.ui.le_C_N.setEnabled(True)
            self.ui.le_k_y_1.setEnabled(True)
            self.ui.le_u_p.setEnabled(True)
            self.ui.le_k_ob.setEnabled(True)
            self.ui.le_Z_1.setEnabled(True)
            self.ui.le_Z_2.setEnabled(True)
            self.ui.le_sigma.setEnabled(True)
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

    def submitValuesButton(self):

        P_2 = float(self.ui.linePower.currentText())
        U = int(self.ui.lineVoltage.currentText())
        _2p = int(self.ui.linePolarity.currentText())

        try:
            S_nom = float(self.ui.lineSnom.text())
            if (not (0 < S_nom <= 1)):
                raise KeyError()
        except ValueError:
            msgBox = QMessageBox()
            msgBox.setText("Введены недопустимые символы")
            msgBox.exec()
            return
        except KeyError:
            msgBox = QMessageBox()
            msgBox.setText("Некорректно введено S_nom (0;1]")
            msgBox.exec()
            return

        self.aboba = MainProgram(P_2, U, _2p, S_nom)
        self.aboba.Run()

        self.ui.tableWidget.item(0, 8).setText(str(S_nom))

        self.table_1 = table1(
            self.aboba.a, self.aboba.a_shtrih, self.aboba.r_2_shtrih, self.aboba.b, self.aboba.b_shtrih, self.aboba.U,
            self.aboba.I_0_a, self.aboba.I_nu, self.aboba.C_1, self.aboba.r_1, self.aboba.P_st, self.aboba.P_meh
        )
        self.table_2 = table2(
            self.aboba.h_c, self.aboba.h_p_2, self.aboba.h_sh, self.aboba.h_sh_shtrih, self.aboba.b_1_r,
            self.aboba.b_2_r, self.aboba.h_1, self.aboba.q_c, self.aboba.r_c, self.aboba.r_2, self.aboba.h_0,
            self.aboba.b_sh_2, self.aboba.Lamda_p_2, self.aboba.Lamda_l_2, self.aboba.Lamda_d_2,
            self.aboba.X_2_shtrih, self.aboba.x_1_2_p, self.aboba.c_1_p, self.aboba.X_1
        )
        self.table_3 = table3(
            self.aboba.C_N, self.aboba.k_y_1, self.aboba.u_p, self.aboba.k_ob, self.aboba.Z_1, self.aboba.Z_2,
            self.aboba.sigma, self.aboba.t_z_1, self.aboba.b_sh[self.aboba.h], self.aboba.h_sh_r[self.aboba.h],
            self.aboba.Lamda_p_1, self.aboba.Lamda_d_1, self.aboba.Lamda_l_1, self.aboba.x_1_2_p, self.aboba.t_z_2,
            self.aboba.b_sh_2[self.aboba.h], self.aboba.Lamda_p_2, self.aboba.Lamda_l_2, self.aboba.Lamda_d_2,
            self.aboba.h_sh_shtrih, self.aboba.X_2_shtrih, self.aboba.r_1, self.aboba.r_2_Ksi_shtrih, self.aboba.U,
            self.aboba.I_1_p, self.aboba.I_1_nom, self.table_1.calculateTable(11, self.aboba.s_nom), self.aboba.s_nom,
            self.aboba.h_k, self.aboba.Lamda_p_2_Ksi, self.aboba.K_R, self.table_2
        )

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
        self.ui.bt_calculate_table3.setEnabled(False)
        self.ui.bt_show_chart_table3.setEnabled(False)

        self.clearTables()
        self.ui.tabWidget.setCurrentWidget(self.ui.tab)

        for i in range(1, 19 + 1):
            for j in range(0, 9):
                if (i % 2):
                    self.ui.tableWidget.item(i, j).setBackground(QColor(230, 230, 230))
                else:
                    self.ui.tableWidget.item(i, j).setBackground(QColor(255, 255, 255))
                if (j < 9 - 1):
                    self.ui.tableWidget.item(i, j).setFlags(~Qt.ItemIsEditable)

        for i in range(1, 14 + 1):
            for j in range(0, 8):
                if (i % 2):
                    self.ui.tableWidget_2.item(i, j).setBackground(QColor(230, 230, 230))
                else:
                    self.ui.tableWidget.item(i, j).setBackground(QColor(255, 255, 255))
                if (j > 2):
                    self.ui.tableWidget_2.item(i, j).setFlags(~Qt.ItemIsEditable)

        for i in range(1, 20 + 1):
            for j in range(0, 8):
                if (i % 2):
                    self.ui.tableWidget_3.item(i, j).setBackground(QColor(230, 230, 230))
                else:
                    self.ui.tableWidget.item(i, j).setBackground(QColor(255, 255, 255))
                if (j > 2):
                    self.ui.tableWidget_3.item(i, j).setFlags(~Qt.ItemIsEditable)

    def save_table_to_xl_1(self):
        col_count = self.ui.tableWidget.columnCount()
        row_count = self.ui.tableWidget.rowCount()
        headers = [str(self.ui.tableWidget.horizontalHeaderItem(i).text()) for i in range(col_count)]

        # df indexing is slow, so use lists
        df_list = []
        for row in range(row_count):
            df_list2 = []
            for col in range(col_count):
                if col <= 1:
                    table_item = self.ui.tableWidget.item(row, col)
                    df_list2.append('' if table_item is None else str(table_item.text()))
                else:
                    table_item = self.ui.tableWidget.item(row, col)
                    df_list2.append('' if table_item is None else float(table_item.text()))
            df_list.append(df_list2)
        df_list.append(list([]))
        df_list.append(list(
            [f'P_2 = {P_2}', f'U = {U}', f'λ = {lamda}', f'A = {round(A, 3)}', f'B =  {round(B_sig, 3)}',
             f"J1' = {round(J_1_shtrih, 3)}", f"J1 = {round(J_1, 3)}", f'k_з = {k_z}',
             f'I_nu* = {round(I_nu_star, 3)}']))
        df_list.append(list([f'n_эл = {n_el}', f'I0a = {round(I_0_a, 3)}', f'I0p = {round(I_nu, 3)}',
                             f'Pст+Pмех = {round(P_st + P_meh, 3)}', f'r1 = {round(r_1, 3)}',
                             f"r'2 = {round(r_2_shtrih, 3)}", f'c1 = {round(c_1_p, 3)}', f" a' = {round(a_shtrih, 3)}",
                             f'a = {round(a, 3)}']))
        df_list.append(list(
            [f"b' = {round(b_shtrih, 3)}", f'b = {round(b, 3)}', f'u_p = {u_p}', f'I_1_nom = {round(I_1_nom, 3)}',
             f'KPD = {kpd}', f'cos(phi) = {cosPhi}']))

        df = pd.DataFrame(df_list, columns=headers)
        print(df)
        writer = pd.ExcelWriter('example.xlsx', mode='a')
        df.to_excel(writer, f'Двигатель {len(writer.sheets)}')
        writer.save()

    def show_chart_table_1(self):

        x_arr = [0]
        y_arr_1 = [0.1]
        y_arr_2 = [0]
        y_arr_3 = [0]
        y_arr_4 = [0]

        for i in range(2, 8 + 1):
            x_arr.append(round(self.table_1_student.calculateTable(12, float(self.ui.tableWidget.item(0, i).text())), 3))
        for i in range(2, 8 + 1):
            y_arr_1.append(round(self.table_1_student.calculateTable(19, float(self.ui.tableWidget.item(0, i).text())), 3))
        for i in range(2, 8 + 1):
            y_arr_2.append(round(self.table_1_student.calculateTable(18, float(self.ui.tableWidget.item(0, i).text())), 3))
        for i in range(2, 8 + 1):
            y_arr_3.append(float(self.ui.tableWidget.item(0, i).text()))
        for i in range(2, 8 + 1):
            y_arr_4.append(round(self.table_1_student.calculateTable(10, float(self.ui.tableWidget.item(0, i).text())), 3))
        x_arr.sort()
        y_arr_3.sort()
        y_arr_4.sort()
        y_arr_4[0] = y_arr_4[1] * 0.75
        fig = plt.figure()

        cosPhi_chart = fig.add_subplot(2, 2, 1)
        kpd_chart = fig.add_subplot(2, 2, 2)
        s_chart = fig.add_subplot(2, 2, 3)
        I_1_chart = fig.add_subplot(2, 2, 4)

        x_list = [x / 1000 for x in range(0, int(x_arr[-1]) * 1000)]

        cosPhi_chart.plot(x_list, [SplineCubicInterpolate(x, x_arr, y_arr_1) for x in x_list], color='red', marker='o',
                          markersize=3)
        cosPhi_chart.minorticks_on()
        cosPhi_chart.grid(which='major',
                          color='k',
                          linewidth=2)
        cosPhi_chart.grid(which='minor',
                          color='k',
                          linestyle=':')
        cosPhi_chart.set_ylabel('cos(φ)', size=16)
        cosPhi_chart.set_xlabel('P_квт', size=16)
        cosPhi_chart.set_ylim(0, 1)

        kpd_chart.plot(x_list, [SplineCubicInterpolate(x, x_arr, y_arr_2) for x in x_list], color='red', marker='o',
                       markersize=3)
        kpd_chart.minorticks_on()
        kpd_chart.grid(which='major',
                       color='k',
                       linewidth=2)
        kpd_chart.grid(which='minor',
                       color='k',
                       linestyle=':')
        kpd_chart.set_ylabel('η', size=16)
        kpd_chart.set_xlabel('P_квт', size=16)
        kpd_chart.set_ylim(0, 1)

        s_chart.plot(x_list, [SplineCubicInterpolate(x, x_arr, y_arr_3) for x in x_list], color='red', marker='o',
                     markersize=3)
        s_chart.minorticks_on()
        s_chart.grid(which='major',
                     color='k',
                     linewidth=2)
        s_chart.grid(which='minor',
                     color='k',
                     linestyle=':')
        s_chart.set_ylabel('s', size=16)
        s_chart.set_xlabel('P_квт', size=16)

        I_1_chart.plot(x_list, [SplineCubicInterpolate(x, x_arr, y_arr_4) for x in x_list], color='red', marker='o',
                       markersize=3)
        I_1_chart.minorticks_on()
        I_1_chart.grid(which='major',
                       color='k',
                       linewidth=2)
        I_1_chart.grid(which='minor',
                       color='k',
                       linestyle=':')
        I_1_chart.set_ylabel('I₁', size=16)
        I_1_chart.set_xlabel('P_квт', size=16)

        fig.set_figwidth(12)
        fig.set_figheight(12)

        plt.show()

    def show_chart_table_3(self):

        x_arr = [0]
        y_arr_1 = [0]
        y_arr_2 = [0]

        fig = plt.figure()

        for i in range(2, 7):
            x_arr.append(float(self.ui.tableWidget_3.item(0, i).text()))
        for i in range(2, 7):
            y_arr_1.append(round(self.table_3.calculateTable(19, float(self.ui.tableWidget_3.item(0, i).text())), 3))
        for i in range(2, 7):
            y_arr_2.append(round(self.table_3.calculateTable(20, float(self.ui.tableWidget_3.item(0, i).text())), 3))
        x_arr.sort()
        y_arr_1.sort()
        y_arr_2.reverse()
        y_arr_2.remove(0)
        y_arr_2.insert(0, 0)
        print(y_arr_1)
        print(x_arr)
        print(y_arr_2)

        I_dot = fig.add_subplot(1, 2, 1)
        M_star = fig.add_subplot(1, 2, 2)

        x_list = [x / 1000 for x in range(0, int(x_arr[-1]) * 1000)]

        I_dot.plot(x_list, [SplineCubicInterpolate(x, x_arr, y_arr_1) for x in x_list], color='red', marker='o',
                   markersize=3)
        I_dot.minorticks_on()
        I_dot.grid(which='major',
                   color='k',
                   linewidth=2)
        I_dot.grid(which='minor',
                   color='k',
                   linestyle=':')
        I_dot.set_ylabel('I.', size=16)
        I_dot.set_xlabel('s', size=16)

        M_star.plot(x_list, [SplineCubicInterpolate(x, x_arr, y_arr_2) for x in x_list], color='red', marker='o',
                    markersize=3)
        M_star.minorticks_on()
        M_star.grid(which='major',
                    color='k',
                    linewidth=2)
        M_star.grid(which='minor',
                    color='k',
                    linestyle=':')
        M_star.set_ylabel('M*', size=16)
        M_star.set_xlabel('s', size=16)

        fig.set_figwidth(12)
        fig.set_figheight(12)

        plt.show()

    def calculate_table1(self):
        self.ui.bt_show_chart_1.setEnabled(True)
        self.ui.bt_export_xl_1.setEnabled(True)
        try:
            self.table_1_student = table1(float(self.ui.le_a.text()), float(self.ui.le_a_shtrih.text()),
                                     float(self.ui.le_r2_shtrih.text()), float(self.ui.le_b.text()),
                                     float(self.ui.le_b_shtrih.text()), self.aboba.U, float(self.ui.le_I0a.text()),
                                     float(self.ui.le_I0p.text()), float(self.ui.le_c1.text()),
                                     float(self.ui.le_r1.text()), float(self.ui.le_Pst.text()),
                                     float(self.ui.le_Pmeh.text()))
        except Exception as e:
            msgBox = QMessageBox()
            msgBox.setText("Неправильно введены значения")
            msgBox.exec()
        for i in range(2, 8):
            for j in range(1, 19 + 1):
                self.ui.tableWidget.item(j, i).setText(
                    str(round(self.table_1_student.calculateTable(j, float(self.ui.tableWidget.item(0, i).text())), 3)))
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.tableWidget.reset()

    def calculate_table2(self):
        try:
            self.table_2_student = table2(
                float(self.ui.le_h_c.text()), float(self.ui.le_h_p_2.text()), float(self.ui.le_h_sh.text()),
                float(self.ui.le_h_sh_shtrih.text()), float(self.ui.le_b_1_r.text()), float(self.ui.le_b_2_r.text()),
                float(self.ui.le_h_1.text()), float(self.ui.le_q_c.text()), float(self.ui.le_r_c.text()),
                float(self.ui.le_r_2.text()), float(self.ui.le_h_0.text()), float(self.ui.le_b_sh_2.text()),
                float(self.ui.le_Lamda_p_2.text()), float(self.ui.le_Lamda_l_2.text()),
                float(self.ui.le_Lamda_d_2.text()), float(self.ui.le_X_2_shtrih.text()),
                float(self.ui.le_x_1_2_p.text()), float(self.ui.le_c_1_p.text()), float(self.ui.le_X_1.text())
            )
        except Exception as e:
            msgBox = QMessageBox()
            msgBox.setText("Неправильно введены значения")
            msgBox.exec()
        for i in range(3, 7 + 1):
            for j in range(2, 14 + 1):
                self.ui.tableWidget_2.item(j, i).setText(
                    str(round(self.table_2_student.calculateTable(j, float(self.ui.tableWidget_2.item(0, i).text())),
                              3)))
        self.ui.tableWidget_2.reset()

    def calculate_table3(self):
        self.ui.bt_show_chart_table3.setEnabled(True)
        try:
            self.table_3_student = table3(
                float(self.ui.le_C_N.text()), float(self.ui.le_k_y_1.text()), float(self.ui.le_u_p.text()),
                float(self.ui.le_k_ob.text()), float(self.ui.le_Z_1.text()), float(self.ui.le_Z_2.text()),
                float(self.ui.le_sigma.text()), float(self.ui.le_t_z_1.text()),
                float(self.ui.le_b_sh.text()), float(self.ui.le_h_sh_r.text()), float(self.ui.le_Lamda_p_1.text()),
                float(self.ui.le_Lamda_d_1.text()), float(self.ui.le_Lamda_l_1.text()),
                float(self.ui.le_x_1_2_p.text()), float(self.ui.le_t_z_2.text()), float(self.ui.le_b_sh_2.text()),
                float(self.ui.le_Lamda_p_2.text()), float(self.ui.le_Lamda_l_2.text()),
                float(self.ui.le_Lamda_d_2.text()), float(self.ui.le_h_sh_shtrih.text()),
                float(self.ui.le_X_2_shtrih.text()), float(self.ui.le_r1.text()),
                float(self.ui.le_r_2_Ksi_shtrih.text()), self.aboba.U, float(self.ui.le_I_1_p.text()),
                float(self.ui.le_I_1_nom.text()), self.table_1.calculateTable(11, self.aboba.s_nom),
                self.aboba.s_nom, float(self.ui.le_h_k.text()), float(self.ui.le_Lamda_p_2_Ksi.text()),
                float(self.ui.le_K_R.text()), self.table_2_student
            )
        except Exception as e:
            msgBox = QMessageBox()
            msgBox.setText("Неправильно введены значения")
            msgBox.exec()
        for i in range(3, 7 + 1):
            for j in range(1, 20 + 1):
                self.ui.tableWidget_3.item(j, i).setText(
                    str(round(self.table_3_student.calculateTable(j, float(self.ui.tableWidget_3.item(0, i).text())), 2)))
        self.ui.tableWidget_3.reset()


app = QApplication()
window = MainWindow()
window.show()
sys.exit(app.exec())
