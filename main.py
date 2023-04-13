import sys

import matplotlib.pyplot as plt
from PyQt6 import uic
import pandas as pd
from main1 import *
from func import Lagrange,LinearInterpolation
from PySide6.QtWidgets import QApplication, QMainWindow
from ww import *
from tables import table1, table2, table3
from scipy import interpolate
from openpyxl import Workbook
table_1 = table1(a, a_shtrih, r_2_shtrih, b, b_shtrih, U, I_0_a, I_nu, C_1, r_1, P_st, P_meh)
table_2 = table2(h_c, h_p_2, h_sh, h_sh_shtrih, b_1_r, b_2_r, h_1, q_c, r_c, r_2, h_0, b_sh_2, Lamda_p_2, Lamda_l_2,
                Lamda_d_2, X_2_shtrih, x_1_2_p, c_1_p, X_1)
table_3 = table3(C_N, k_y_1, u_p, k_ob, Z_1, Z_2, sigma, t_z_1, b_sh[h], h_sh_r[h], Lamda_p_1, Lamda_d_1, Lamda_l_1, x_1_2_p,
                t_z_2, b_sh_2[h], Lamda_p_2, Lamda_l_2, Lamda_d_2, h_sh_shtrih, X_2_shtrih, r_1, r_2_Ksi_shtrih, U, I_1_p,
                I_1_nom, table_1.calculateTable(11, s_nom), s_nom, h_k, Lamda_p_2_Ksi, K_R)
@staticmethod
def write_qtable_to_df(table):
    col_count = table.columnCount()
    row_count = table.rowCount()
    headers = [str(table.horizontalHeaderItem(i).text()) for i in range(col_count)]

    # df indexing is slow, so use lists
    df_list = []
    for row in range(row_count):
        df_list2 = []
        for col in range(col_count):
            if col <= 1:
                table_item = table.item(row, col)
                df_list2.append('' if table_item is None else str(table_item.text()))
            else:
                table_item = table.item(row, col)
                df_list2.append('' if table_item is None else float(table_item.text()))
        df_list.append(df_list2)
    df_list.append(list([]))
    df_list.append(list([f'P_2 = {P_2}', f'U = {U}', f'λ = {lamda}', f'A = {round(A, 3)}', f'B =  {round(B_sig, 3)}', f"J1' = {round(J_1_shtrih, 3)}", f"J1 = {round(J_1, 3)}", f'k_з = {k_z}', f'I_nu* = {round(I_nu_star, 3)}']))
    df_list.append(list([f'n_эл = {n_el}', f'I0a = {round(I_0_a,3)}', f'I0p = {round(I_nu,3)}', f'Pст+Pмех = {round(P_st+P_meh,3)}', f'r1 = {round(r_1,3)}', f"r'2 = {round(r_2_shtrih,3)}", f'c1 = {round(c_1_p,3)}', f" a' = {round(a_shtrih,3)}", f'a = {round(a,3)}']))
    df_list.append(list([f"b' = {round(b_shtrih,3)}", f'b = {round(b,3)}', f'u_p = {u_p}', f'I_1_nom = {round(I_1_nom,3)}', f'KPD = {kpd}', f'cos(phi) = {cosPhi}']))
    df = pd.DataFrame(df_list, columns=headers)

    return df
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        global P_NOM,U_NOM,_2p_nom
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.resizetables()
        self.ui.bt_calculate_table1.clicked.connect(self.calculate_table1)
        self.ui.bt_calculate_table2.clicked.connect(self.calculate_table2)
        self.ui.bt_calculate_table3.clicked.connect(self.calculate_table3)
        self.ui.bt_export_xl_1.clicked.connect(self.save_table_to_xl_1)
        self.ui.bt_show_chart_1.clicked.connect(self.show_chart_table_1)
        self.ui.bt_show_chart_table3.clicked.connect(self.show_chart_table_3)


    def resizetables(self):
        self.ui.tableWidget.setColumnWidth(0, 250)
        self.ui.tableWidget.setColumnWidth(1, 80)
        self.ui.tableWidget.setColumnWidth(2, 80)
        self.ui.tableWidget.setColumnWidth(3, 80)
        self.ui.tableWidget.setColumnWidth(4, 80)
        self.ui.tableWidget.setColumnWidth(5, 120)
        self.ui.tableWidget.setColumnWidth(6, 80)
        self.ui.tableWidget.setColumnWidth(7, 80)
        self.ui.tableWidget.setColumnWidth(8, 80)
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
    def save_table_to_xl_1(self):
        df = write_qtable_to_df(self.ui.tableWidget)
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
            x_arr.append(round(table_1.calculateTable(12, float(self.ui.tableWidget.item(0, i).text())), 3))
        for i in range(2, 8 + 1):
            y_arr_1.append(round(table_1.calculateTable(19, float(self.ui.tableWidget.item(0, i).text())), 3))
        for i in range(2, 8 + 1):
            y_arr_2.append(round(table_1.calculateTable(18, float(self.ui.tableWidget.item(0, i).text())), 3))
        for i in range(2, 8 + 1):
            y_arr_3.append(float(self.ui.tableWidget.item(0, i).text()))
        for i in range(2, 8 + 1):
            y_arr_4.append(round(table_1.calculateTable(10, float(self.ui.tableWidget.item(0, i).text())), 3))
        x_arr.sort()
        y_arr_3.sort()
        y_arr_4.sort()
        y_arr_4[0] = y_arr_4[1]*0.75
        fig = plt.figure()


        cosPhi_chart = fig.add_subplot(2, 2, 1)
        kpd_chart = fig.add_subplot(2, 2, 2)
        s_chart = fig.add_subplot(2,2,3)
        I_1_chart = fig.add_subplot(2,2,4)

        x_list = [x / 1000 for x in range(0, int(x_arr[-1]) * 1000)]

        cosPhi_chart.plot(x_list, [Lagrange(x, x_arr, y_arr_1) for x in x_list], color='red', marker='o', markersize=3)
        cosPhi_chart.minorticks_on()
        cosPhi_chart.grid(which='major',
                          color='k',
                          linewidth=2)
        cosPhi_chart.grid(which='minor',
                          color='k',
                          linestyle=':')
        cosPhi_chart.set_ylabel('cos(φ)',size=16)
        cosPhi_chart.set_xlabel('P_квт',size=16)
        cosPhi_chart.set_ylim(0,1)

        kpd_chart.plot(x_list, [Lagrange(x, x_arr, y_arr_2) for x in x_list], color='red', marker='o', markersize=3)
        kpd_chart.minorticks_on()
        kpd_chart.grid(which='major',
                          color='k',
                          linewidth=2)
        kpd_chart.grid(which='minor',
                          color='k',
                          linestyle=':')
        kpd_chart.set_ylabel('η',size=16)
        kpd_chart.set_xlabel('P_квт',size=16)
        kpd_chart.set_ylim(0, 1)

        s_chart.plot(x_list, [Lagrange(x, x_arr, y_arr_3) for x in x_list], color='red', marker='o', markersize=3)
        s_chart.minorticks_on()
        s_chart.grid(which='major',
                       color='k',
                       linewidth=2)
        s_chart.grid(which='minor',
                       color='k',
                       linestyle=':')
        s_chart.set_ylabel('s',size=16)
        s_chart.set_xlabel('P_квт',size=16)

        I_1_chart.plot(x_list, [Lagrange(x, x_arr, y_arr_4) for x in x_list], color='red', marker='o', markersize=3)
        I_1_chart.minorticks_on()
        I_1_chart.grid(which='major',
                     color='k',
                     linewidth=2)
        I_1_chart.grid(which='minor',
                     color='k',
                     linestyle=':')
        I_1_chart.set_ylabel('I₁',size=16)
        I_1_chart.set_xlabel('P_квт',size=16)

        fig.set_figwidth(12)
        fig.set_figheight(12)


        plt.show()
    def show_chart_table_3(self):

        x_arr = [0]
        y_arr_1 = [0]
        y_arr_2 = [0]

        fig = plt.figure()

        for i in range(2, 7 ):
             x_arr.append(float(self.ui.tableWidget_3.item(0, i).text()))
        for i in range(2, 7 ):
            y_arr_1.append(round(table_3.calculateTable(19, float(self.ui.tableWidget_3.item(0, i).text())), 3))
        for i in range(2, 7 ):
            y_arr_2.append(round(table_3.calculateTable(20, float(self.ui.tableWidget_3.item(0, i).text())), 3))
        x_arr.sort()
        y_arr_1.sort()
        y_arr_2.reverse()
        y_arr_2.remove(0)
        y_arr_2.insert(0,0)
        print(y_arr_1)
        print(x_arr)
        print(y_arr_2)


        I_dot = fig.add_subplot(1, 2, 1)
        M_star = fig.add_subplot(1, 2, 2)

        x_list = [x / 1000 for x in range(0, int(x_arr[-1]) * 1000)]

        I_dot.plot(x_list, [LinearInterpolation(x, x_arr, y_arr_1) for x in x_list], color='red', marker='o', markersize=3)
        I_dot.minorticks_on()
        I_dot.grid(which='major',
                          color='k',
                          linewidth=2)
        I_dot.grid(which='minor',
                          color='k',
                          linestyle=':')
        I_dot.set_ylabel('I.',size=16)
        I_dot.set_xlabel('s',size=16)

        M_star.plot(x_list, [LinearInterpolation(x, x_arr, y_arr_2) for x in x_list], color='red', marker='o', markersize=3)
        M_star.minorticks_on()
        M_star.grid(which='major',
                   color='k',
                   linewidth=2)
        M_star.grid(which='minor',
                   color='k',
                   linestyle=':')
        M_star.set_ylabel('M*',size=16)
        M_star.set_xlabel('s',size=16)

        fig.set_figwidth(12)
        fig.set_figheight(12)

        plt.show()

    def calculate_table1(self):
        for i in range(2, 8 + 1):
            for j in range(1, 19 + 1):
                self.ui.tableWidget.setItem(j, i, QTableWidgetItem(
                    str(round(table_1.calculateTable(j, float(self.ui.tableWidget.item(0, i).text())), 3))))

    def calculate_table2(self):
        for i in range(2, 7 + 1):
            for j in range(1, 14 + 1):
                self.ui.tableWidget_2.setItem(j, i, QTableWidgetItem(
                    str(round(table_2.calculateTable(j, float(self.ui.tableWidget_2.item(0, i).text())), 3))))

    def calculate_table3(self):
        for i in range(2, 7 + 1):
            for j in range(1, 20 + 1):
                self.ui.tableWidget_3.setItem(j, i, QTableWidgetItem(
                    str(round(table_3.calculateTable(j, float(self.ui.tableWidget_3.item(0, i).text())), 2))))


app = QApplication()
window = MainWindow()
window.show()
sys.exit(app.exec())
