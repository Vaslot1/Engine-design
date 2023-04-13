import math
import time
from colorama import *
init(autoreset=True)

import matplotlib.pyplot as plt
from dict import *
from func import *

class MainProgram:
    a_harmonic = 1  # гармоника 1 порядка
    P_2 = 250
    U = 660
    _2p = 4
    h = 0
    
    n = 1500
    m = 3
    f = 50
    beta_shtrih = 0.833
    
    # 1 Таблица
    a = 0
    a_shtrih = 0
    r_2_shtrih = 0
    b = 0
    b_shtrih = 0
    I_0_a = 0
    I_nu = 0
    C_1 = 0
    r_1 = 0
    P_st = 0
    P_meh = 0
    
    # 2 Таблица
    h_c = 0
    h_p_2 = 0
    h_sh = 0
    h_sh_shtrih = 0
    b_1_r = 0
    b_2_r = 0
    h_1 = 0
    q_c = 0
    r_c = 0
    r_2 = 0
    h_0 = 0
    b_sh_2 = 0
    Lamda_p_2 = 0
    Lamda_l_2 = 0
    Lamda_d_2 = 0
    X_2_shtrih = 0
    x_1_2_p = 0
    c_1_p = 0
    X_1 = 0
    
    # 3 Таблица
    C_N = 0
    k_y_1 = 0
    u_p = 0
    k_ob = 0
    Z_1 = 0
    Z_2 = 0
    sigma = 0
    t_z_1 = 0
    b_sh = 0
    h_sh_r = 0
    Lamda_p_1 = 0
    Lamda_d_1 = 0
    Lamda_l_1 = 0
    x_1_2_p = 0
    t_z_2 = 0
    b_sh_2 = 0
    h_sh_shtrih = 0
    X_2_shtrih = 0
    r_1 = 0
    r_2_Ksi_shtrih = 0
    I_1_p = 0
    I_1_nom = 0
    s_nom = 0
    I2_shtrih = 0
    h_k = 0
    Lamda_p_2_Ksi = 0
    K_R = 0

    def __init__(self, P_2, U, _2p, s_nom):
        self.P_2 = P_2
        self.U = U
        self._2p = _2p
        self.s_nom = s_nom

    def Run(self):
        k_uk = math.sin((math.pi / 2) * self.beta_shtrih)
        cosPhi = cosPhi_func(self._2p, self.P_2)
        kpd = kpd_func(self._2p, self.P_2)
        
        print(Back.BLUE + "Пункт: ТЗ")
        print("a_gor =", self.a_harmonic)
        print("m =", self.m)
        print("f =", self.f)
        print("P_2 =", self.P_2)
        print("U =", self.U)
        print("coef_ukorochenia =", k_uk)
        print("cosPhi =", cosPhi)
        print("kpd =", kpd)
        print("2p =", self._2p, end='\n\n')
        
        ####* __1__
        h_shtrih = {
            # 2: (p2_up(self.P_2) + p2_down(self.P_2)) / 2,
            4: (p6_down__p4_up(self.P_2) + p4_down(self.P_2)) / 2,
            # 6: (p8_down__p6_up(self.P_2) + p6_down__p4_up(self.P_2) / 2),
            # 8: (p8_up(self.P_2) + p8_down__p6_up(self.P_2)) / 2,
            10: 0,
            12: 0
        }[self._2p]
        self.h = FindApproximateWithinBounds(
            [56, 63, 71, 80, 90, 100, 112, 132, 160, 180, 200, 225, 250, 280, 315, 355],
            h_shtrih
        )
        print(h_shtrih)
        print(self.h)
        D_a = {
            56: 0.08,
            63: 0.1,
            71: 0.116,
            80: 0.131,
            90: 0.149,
            100: 0.168,
            112: 0.191,
            132: 0.225,
            160: 0.272,
            180: 0.313,
            200: 0.349,
            225: 0.392,
            250: 0.437,
            280: 0.52,
            315: 0.59,
            355: 0.66
        }[self.h]

        ####* __2__
        # k_D = {
        #     2: 0.56,
        #     4: 0.65,
        #     6: 0.71,
        #     8: 0.735,
        #     10: 0.76,
        #     12: 0.76
        # }[self._2p]

        k_D = {
            2: 0.56,
            4: 0.62,
            6: 0.71,
            8: 0.73,
            10: 0.76,
            12: 0.76
        }[self._2p]
        k_D = 0.62
        sumator = 0.005
        sumator_D_a = 0.001
        # НЦ
        print(self.h)
        print(D_a)
        D_a_max = {
            56: 0.096,
            63: 0.108,
            71: 0.122,
            80: 0.139,
            90: 0.157,
            100: 0.175,
            112: 0.197,
            132: 0.233,
            160: 0.285,
            180: 0.322,
            200: 0.359,
            225: 0.406,
            250: 0.452,
            280: 0.53,
            315: 0.59,
            355: 0.66
        }

        step_h = 0
        exit_from_inf_while = False
        number_of_iteration = 1
        print("======================Начало цикла перебора значений=========================")
        while step_h <= 300:
            print(f"==================                {number_of_iteration}                     =====================")
            self.h = FindApproximateWithinBounds(
                [56, 63, 71, 80, 90, 100, 112, 132, 160, 180, 200, 225, 250, 280, 315, 355],
                h_shtrih + step_h
            )

            while D_a != D_a_max[self.h] + sumator_D_a:
                print("---------------------")
                print("D_a =", D_a)
                print("k_D =", k_D)
                print(f"D_a_max[{self.h}] =", D_a_max[self.h] + sumator_D_a)
                print("---------------------", end='\n')
                D_a = round(D_a, 3)
                k_D = 0.62
                while (k_D != 0.685):
                    D = round(k_D * D_a, 3)

                    ####* __3__
                    tau = (math.pi * D) / self._2p

                    ####* __4__
                    # k_e = {
                    #     4: {
                    #         0.08: 0.948,
                    #         0.104: 0.952,
                    #         0.119: 0.956,
                    #         0.135: 0.96,
                    #         0.153: 0.963,
                    #         0.171: 0.965,
                    #         0.194: 0.968,
                    #         0.229: 0.972,
                    #         0.2785: 0.975,
                    #         0.32: 0.976,
                    #         0.354: 0.978,
                    #         0.399: 0.98,
                    #         0.444: 0.981,
                    #         0.525: 0.983,
                    #         0.59: 0.985,
                    #         0.66: 0.986
                    #     }
                    # }[self._2p][D_a]
                    k_e = K_e_func(D_a)
                    P_shtrih = (self.P_2 * 1000) * (k_e / (kpd * cosPhi))

                    ####* __5__
                    A_shtrih = (A__down(self._2p, D_a) + A__up(self._2p, D_a)) / 2
                    B_sig_shtrih = (B_sig__down(self._2p, D_a) + B_sig__up(self._2p, D_a)) / 2.1
                    print(tau)
                    ####* __6__
                    if self.h <= 90:  # пока не сделали,костыль
                        t_z_1_max = round(t_z1__1_max(tau), 3)
                        t_z_1_min = round(t_z1__1_max(tau), 3)
                    elif 90 < self.h <= 250:
                        t_z_1_max = round(t_z1__2_max(tau), 3)
                        t_z_1_min = round(t_z1__2_min(tau), 3)
                    elif self.h >= 280:
                        t_z_1_max = round(t_z1__3_max(tau), 3)
                        t_z_1_min = round(t_z1__3_min(tau), 3)

                    Z_1_min = round((math.pi * D) / t_z_1_max)
                    Z_1_max = round((math.pi * D) / t_z_1_min)

                    self.Z_1 = {  # АЛГОРИТМ РАБОТАЕТ, НО ЕСТЬ НЬЮАНС
                        2: FindMaxInBounds([12, 18, 24, 30, 36, 42, 48], Z_1_min, Z_1_max),
                        4: FindMaxInBounds([12, 18, 24, 36, 42, 48, 60, 72], Z_1_min, Z_1_max),
                        6: FindMaxInBounds([36, 54, 72, 90], Z_1_min, Z_1_max),
                        8: FindMaxInBounds([48, 72, 84, 96], Z_1_min, Z_1_max),
                        10: FindMaxInBounds([60, 90, 120], Z_1_min, Z_1_max),
                        12: FindMaxInBounds([72, 90, 108, 144], Z_1_min, Z_1_max)
                    }[self._2p]

                    q_1 = math.ceil(self.Z_1 / (self._2p * self.m))
                    k_ras = (math.sin(math.pi / (2 * self.m))) / (q_1 * math.sin(math.pi / (2 * self.m * q_1)))

                    self.k_ob = k_ras * k_uk

                    ####* __7__
                    p = self._2p / 2
                    k_B = math.pi / (2 * math.sqrt(2))
                    omega = math.pi * 2 * self.f / p
                    l_sig = (P_shtrih / (k_B * D ** 2 * omega * self.k_ob * A_shtrih * B_sig_shtrih))

                    ####? __8__
                    lamda = round(l_sig / tau, 1)

                    ####* __9__

                    ####* __10__

                    ####* __11__
                    self.t_z_1 = (math.pi * D) / (self._2p * q_1 * self.m)

                    ####* __12__
                    self.I_1_nom = (self.P_2 * 1000) / (self.m * self.U * cosPhi * kpd)
                    u_shtrih_p = (math.pi * D * A_shtrih) / (self.I_1_nom * self.Z_1)

                    ####* __13__
                    if self.P_2 <= 15:
                        self.u_p = round(self.a_harmonic * u_shtrih_p)
                    else:
                        if math.floor(self.a_harmonic * u_shtrih_p) % 2 == 0:
                            self.u_p = math.floor(self.a_harmonic * u_shtrih_p)
                        elif math.ceil(self.a_harmonic * u_shtrih_p) % 2 == 0:
                            self.u_p = math.ceil(self.a_harmonic * u_shtrih_p)


                    ####? __14__
                    w_1 = (self.u_p * self.Z_1) / (2 * self.a_harmonic * self.m)
                    A = (2 * self.I_1_nom * w_1 * self.m) / (math.pi * D)
                    Ph = (k_e * self.U) / (4 * k_B * w_1 * self.k_ob * self.f)
                    B_sig = ((self._2p / 2) * Ph) / (D * l_sig)

                    ####* __15__
                    J_1_shtrih = ((AJ__up(self._2p, D_a) + AJ__down(self._2p, D_a)) / 2) / A

                    ####* __16__
                    q_ef_shtrih = (self.I_1_nom / (self.a_harmonic * J_1_shtrih)) * 10 ** 6

                    ####* __17__
                    n_el = 0
                    if (0 < self.P_2 <= 15):
                        n_el = 3
                    elif (15 < self.P_2 <= 90):
                        n_el = 5
                    elif (90 < self.P_2 <= 132):
                        n_el = 1
                    elif (132 < self.P_2 < 315):
                        n_el = 2
                    elif (self.P_2 == 315):
                        n_el = 4
                    q_el_shtrih = q_ef_shtrih / n_el
                    if (self.P_2 < 110):
                        q_el = FindApproximateWithinBounds(
                            [0.00502, 0.00636, 0.00785, 0.00985, 0.01227, 0.01368, 0.01539,
                            0.01767, 0.0201, 0.0227, 0.0255, 0.0284, 0.0314, 0.0353, 0.0394,
                            0.0437, 0.0491, 0.0552, 0.0616, 0.0707, 0.0779, 0.0881, 0.099,
                            0.1104, 0.1257, 0.1419, 0.159, 0.1772, 0.1963, 0.221, 0.246,
                            0.283, 0.312, 0.353, 0.396, 0.442, 0.503, 0.567, 0.636, 0.709,
                            0.785, 0.883, 0.985, 1.094, 1.227, 1.368, 1.539, 1.767, 2.011,
                            2.27, 2.54, 2.83, 3.14, 3.53, 3.94, 4.36, 4.91],
                            q_el_shtrih
                        )
                    else:
                        q_el = FindApproximateWithinBounds(
                            [3.369, 3.561, 3.785, 3.887, 4.025, 4.397, 4.585, 4.825, 4.992, 5.14, 5.465,
                            5.672, 5.785, 6.185, 6.437, 6.585, 6.985, 7.287, 7.385, 7.785, 8.137, 8.265,
                            9.157, 9.745, 9.385, 9.865, 10.35, 10.51, 11.15, 11.71, 11.79, 12.59, 13.24, 13.39
                                , 14.19, 14.94, 14.99, 15.79, 16.75, 16.64, 17.71, 18.67, 18.68, 19.79, 20.89],
                            q_el_shtrih
                        )
                    q_ef = n_el * q_el

                    print("q_ef_shtrih =", q_ef_shtrih)
                    print("q_el =", q_el, end='\n')

                    ####* __18__
                    J_1 = self.I_1_nom / (self.a_harmonic * q_el * n_el)

                    ####* __19__
                    B_z_1 = {
                        2: 1.75,
                        4: 1.7,
                        6: 1.75,
                        8: 1.75,
                        10: 1.7,
                        12: 1.7
                    }[self._2p]
                    B_a = {
                        2: 1.5,
                        4: 1.5,
                        6: 1.5,
                        8: 1.25,
                        10: 1.15,
                        12: 1.15
                    }[self._2p]
                    k_c = 0.97
                    l_st_1 = l_sig
                    b_z_1 = ((B_sig * self.t_z_1 * l_sig) / (B_z_1 * l_sig * k_c)) * 10 ** 3
                    h_a = Ph / (2 * B_a * l_sig * k_c)

                    ####* __20__
                    self.b_sh = {56: 1.8, 63: 1.8, 71: 2, 80: 3, 90: 3, 100: 3.5, 112: 3.5, 132: 3.5, 160: 3.7, 180: 3.7, 200: 3.7,
                            225: 3.7,
                            250: 3.7, 280: 3.7, 315: 3.7, 355: 3.7}
                    self.h_sh = 0.8
                    h_p = ((D_a - D) / 2 - h_a) * 10 ** 3
                    b_1 = (math.pi * ((D * 10 ** 3) + 2 * self.h_sh - self.b_sh[self.h]) - self.Z_1 * b_z_1) / (self.Z_1 - math.pi)
                    b_2 = ((math.pi * ((D * 10 ** 3) + 2 * h_p)) / self.Z_1) - b_z_1
                    h_p_k = h_p - (self.h_sh + ((b_1 - self.b_sh[self.h]) / 2))

                    ####* __21__
                    delta_b = 0
                    delta_h = 0
                    if (56 <= self.h <= 132):
                        delta_b = 0.1
                        delta_h = 0.1
                    elif (160 <= self.h <= 250):
                        delta_b = 0.2
                        delta_h = 0.2
                    elif (280 <= self.h <= 355):
                        delta_b = 0.3
                        delta_h = 0.3
                    elif (400 <= self.h <= 500):
                        delta_b = 0.4
                        delta_h = 0.3

                    b_1_shtrih = b_1 - delta_b
                    b_2_shtrih = b_2 - delta_b
                    h_p_k_shtrih = h_p_k - delta_h
                    S_pr = 0
                    if (180 <= self.h <= 250):
                        S_pr = 0.6 * (b_1 + b_2)
                    elif (self.h >= 280):
                        S_pr = 0.9 * b_1 + 0.4 * b_2
                    b_iz = 0
                    if (50 <= self.h <= 80):
                        b_iz = 0.2
                    elif (90 <= self.h <= 132):
                        b_iz = 0.25
                    elif (self.h == 160):
                        b_iz = 0.4
                    elif (180 <= self.h <= 250):
                        b_iz = 0.4
                    elif (280 <= self.h <= 355):
                        b_iz = 0.55
                    S_iz = b_iz * (2 * h_p + b_1 + b_2)
                    S_p_shtrih = ((b_1_shtrih + b_2_shtrih) / 2) * h_p_k_shtrih - (S_iz + S_pr)

                    ####? __22__
                    if (self.P_2 < 110):
                        d_iz = {
                            0.00502: 0.1,
                            0.00636: 0.11,
                            0.00785: 0.122,
                            0.00985: 0.134,
                            0.01227: 0.147,
                            0.01368: 0.154,
                            0.01539: 0.162,
                            0.01767: 0.18,
                            0.0201: 0.19,
                            0.0227: 0.2,
                            0.0255: 0.21,
                            0.0284: 0.22,
                            0.0314: 0.23,
                            0.0353: 0.242,
                            0.0394: 0.259,
                            0.0437: 0.271,
                            0.0491: 0.285,
                            0.0552: 0.3,
                            0.0616: 0.315,
                            0.0707: 0.335,
                            0.0779: 0.35,
                            0.0881: 0.37,
                            0.099: 0.395,
                            0.1104: 0.415,
                            0.1257: 0.44,
                            0.1419: 0.565,
                            0.159: 0.49,
                            0.1772: 0.515,
                            0.1963: 0.545,
                            0.221: 0.585,
                            0.246: 0.615,
                            0.283: 0.655,
                            0.312: 0.69,
                            0.353: 0.73,
                            0.396: 0.77,
                            0.442: 0.815,
                            0.503: 0.865,
                            0.567: 0.915,
                            0.636: 0.965,
                            0.709: 1.015,
                            0.785: 1.08,
                            0.883: 1.14,
                            0.985: 1.2,
                            1.094: 1.26,
                            1.227: 1.33,
                            1.368: 1.405,
                            1.539: 1.485,
                            1.767: 1.585,
                            2.011: 1.685,
                            2.27: 1.785,
                            2.54: 1.895,
                            2.83: 1.995,
                            3.14: 2.095,
                            3.53: 2.22,
                            3.94: 2.34,
                            4.36: 2.16,
                            4.91: 2.6
                        }[q_el]
                        k_z = round((d_iz ** 2 * self.u_p * n_el) / S_p_shtrih, 2)
                    else:
                        d_iz = 0
                        k_z = 0
                    print(Back.YELLOW + "Пункт: 22")
                    print("d_iz =", d_iz)
                    if (0.7 <= k_z <= 0.75 and 0.7 <= lamda <= 1.3) or (0.6 <= lamda <= 1 and self.h >= 280):
                        print("k_D = " + str(k_D))
                        print("D_a = " + str(D_a))
                        print("lamda = " + str(lamda))
                        print(Back.GREEN + "k_z = " + str(k_z), end='\n')
                        exit_from_inf_while = True
                        break
                    else:
                        print("k_D = " + str(k_D), end='\n')
                        print("lamda = " + str(lamda))
                        print("D_a = " + str(D_a))
                        print(Back.RED + "k_z = " + str(k_z), end='\n')
                        k_D += sumator
                if (0.7 <= k_z <= 0.75) or (self.P_2 > 100 and A_shtrih * 0.9 < A < A_shtrih * 1.1):
                    if (0.7 <= lamda <= 1.3 and self.h <= 250) or (0.6 <= lamda <= 1 and self.h >= 280):
                        print("k_D = " + str(k_D))
                        print("D_a = " + str(D_a))
                        print("lamda = " + str(lamda))
                        print(Back.GREEN + "k_z = " + str(k_z), end='\n')
                        exit_from_inf_while = True
                        break
                else:
                    print("D_a = " + str(D_a), end='\n')
                    print("lamda = " + str(lamda))
                    print(Back.RED + "k_z = " + str(k_z), end='\n')
                    D_a += sumator_D_a

            if exit_from_inf_while:
                break
            else:
                step_h += 10
                number_of_iteration += 1
        print("======================Конец цикла перебора значений=========================")

        if (0.7 > k_z > 0.75 or ((lamda < 0.7 or lamda > 1.3) and self.h <= 250) or (
                (lamda < 0.6 or lamda > 1) and self.h >= 280)) and self.P_2 < 100:
            print(Back.RED + "k_z = " + str(k_z), end='\n')
            exit(1)
        print(Back.BLUE + "Пункт: 1")
        print("h_shtrih =", h_shtrih)
        print("self.h =", self.h)
        print("D_a =", D_a, end='\n')
        print(Back.BLUE + "Пункт: 2")
        print("k_D =", k_D)
        print("D =", D, end='\n')
        print(Back.BLUE + "Пункт: 3")
        print("tau =", tau, end='\n')
        print(Back.BLUE + "Пункт: 4")
        print("k_e =", k_e)
        print("P_shtrih =", P_shtrih, end='\n')
        print(Back.BLUE + "Пункт: 5")
        print("A_shtrih =", A_shtrih)
        print("B_sig_shtrih =", B_sig_shtrih, end='\n')
        print(Back.BLUE + "Пункт: 6")
        print("k_ras =", k_ras)
        print("k_uk =", k_uk)
        print("self.k_ob =", self.k_ob, end='\n')
        print(Back.BLUE + "Пункт: 7")
        print("p =", p)
        print("k_B =", k_B)
        print("omega =", omega)
        print("l_sig =", l_sig, end='\n')
        print(Back.YELLOW + "Пункт: 8")
        print("lamda =", lamda, end='\n')
        if (0.7 <= lamda <= 1.3):
            print(Back.GREEN + "lamda =" + str(lamda), end='\n')
        else:
            print(Back.RED + "lamda =" + str(lamda), end='\n')
            exit()
        print(Back.BLUE + "Пункт: 9")
        print("t_z_1_max =", t_z_1_max)
        print("t_z_1_min =", t_z_1_min, end='\n')
        print(Back.BLUE + "Пункт: 10")
        print("Z_1_min =", (math.pi * D) / t_z_1_max)
        print("Z_1_max =", (math.pi * D) / t_z_1_min)
        print("self.Z_1 =", self.Z_1)
        print("q1 =", q_1, end='\n')
        print(Back.BLUE + "Пункт: 11")
        print("self.t_z_1 =", self.t_z_1, end='\n')
        print(Back.BLUE + "Пункт: 12")
        print("self.I_1_nom =", self.I_1_nom)
        print("u_shtrih_p =", u_shtrih_p, end='\n')
        print(Back.BLUE + "Пункт: 13")
        print("self.u_p =", self.u_p, end='\n')
        print(Back.YELLOW + "Пункт: 14")
        print("w_1 =", w_1)
        print("Ph =", Ph)
        if (A_shtrih * 0.9 < A < A_shtrih * 1.1 or B_sig_shtrih * 0.9 < B_sig < B_sig_shtrih * 1.1):
            print(Back.GREEN + "A = " + str(A))
            print(Back.GREEN + "B_sig = " + str(B_sig), end='\n')
        else:
            print(Back.RED + "A = " + str(A))
            print(Back.RED + "B_sig = " + str(B_sig), end='\n')
            exit()
        print(Back.BLUE + "Пункт: 15")
        print("AJ =", (AJ__up(self._2p, D_a) + AJ__down(self._2p, D_a)) / 2)
        print("J_1_shtrih =", J_1_shtrih, end='\n')
        print(Back.BLUE + "Пункт: 16")
        print("q_ef_shtrih =", q_ef_shtrih, end='\n')
        print(Back.BLUE + "Пункт: 17")
        print("n_el =", n_el)
        print("q_el_shtrih =", q_el_shtrih)
        print("q_el =", q_el)
        print("q_ef =", q_ef, end='\n')
        print(Back.BLUE + "Пункт: 18")
        if ((J_1_shtrih * 0.9) * 10 ** -6 < J_1 < (J_1_shtrih * 1.1) * 10 ** -6):
            print(Back.GREEN + "J_1 = " + str(J_1), end='\n')
        else:
            print(Back.RED + "J_1 = " + str(J_1), end='\n')
            exit()
        print(Back.BLUE + "Пункт: 19")
        print("B_z_1 =", B_z_1)
        print("B_a =", B_a)
        print("k_c =", k_c)
        print("b_z_1 =", b_z_1)
        print("h_a =", h_a, end='\n')
        print(Back.BLUE + "Пункт: 20")
        print("self.b_sh =", self.b_sh[self.h])
        print("self.h_sh =", self.h_sh)
        print("h_p =", h_p)
        print("b_1 =", b_1)
        print("b_2 =", b_2)
        print("h_p_k =", h_p_k, end='\n')
        print(Back.BLUE + "Пункт: 21")
        print("delta_b =", delta_b)
        print("delta_h =", delta_h)
        print("b_1_shtrih =", b_1_shtrih)
        print("b_2_shtrih =", b_2_shtrih)
        print("h_p_k_shtrih =", h_p_k_shtrih)
        print("b_iz =", b_iz)
        print("S_pr =", S_pr)
        print("S_iz =", S_iz)
        print("S_p_shtrih =", S_p_shtrih, end='\n')

        ####* __23__
        self.sigma = Sigma(self.h)[self._2p](D)
        print(Back.BLUE + "Пункт: 23")
        print("self.sigma =", self.sigma, end='\n')

        ####* __24__
        self.Z_2 = findTheNumberOfRotorSlots(self.P_2, self.Z_1)
        print(Back.BLUE + "Пункт: 24")
        print("self.Z_2 =", self.Z_2, end='\n')

        ####* __25__
        D_2 = D - (2 * (self.sigma * 10 ** (-3)))
        print(Back.BLUE + "Пункт: 25")
        print("D_2 =", D_2, end='\n')

        ####* __26__
        l_2 = l_1 = l_sig
        print(Back.BLUE + "Пункт: 26")
        print("l_2 = l_1 =", l_2, end='\n')

        ####* __27__
        self.t_z_2 = (math.pi * D_2) / self.Z_2
        print(Back.BLUE + "Пункт: 27")
        print("self.t_z_2 =", self.t_z_2, end='\n')

        ####* __28__
        k_B = 0
        if (50 <= self.h <= 63):
            k_B = 0.19
        elif (71 <= self.h <= 250):
            k_B = 0.23
        elif (280 <= self.h <= 355):
            if (self._2p == 2):
                k_B = 0.22
            elif (4 <= self._2p <= 12):
                k_B = 0.23
        elif (400 <= self.h <= 500):
            if (self._2p == 4):
                k_B = 0.2
            elif (self._2p == 6):
                k_B = 0.23
            elif (8 <= self._2p <= 12):
                k_B = 0.25
        D_j = D_b = k_B * D_a
        print(Back.BLUE + "Пункт: 28")
        print("k_B__punkt_24 =", k_B)
        print("D_j =", D_j, end='\n')

        ####* __29__
        k_sk = 1
        v_i = (2 * self.m * w_1 * self.k_ob) / (self.Z_2 * k_sk)
        k_i = 0.2 + 0.8 * cosPhi
        I_2 = k_i * self.I_1_nom * v_i
        print(Back.BLUE + "Пункт: 29")
        print("k_sk =", k_sk)
        print("v_i =", v_i)
        print("k_i =", k_i)
        print("I_2 =", I_2, end='\n')

        ####* __30__
        J_2 = 3.5 * 10 ** 6
        q_p = I_2 / J_2
        print(Back.BLUE + "Пункт: 30")
        print("J_2 =", J_2)
        print("q_p =", q_p, end='\n')

        ####* __31__
        self.b_sh_2 = {56: 1.0, 63: 1.0, 71: 1.0, 80: 1.0, 90: 1.0, 100: 1.0, 112: 1.5, 132: 1.5, 160: 1.5, 180: 1.5, 200: 1.5,
                225: 1.5,
                250: 1.5, 280: 1.5, 315: 1.5, 355: 1.5}
        self.h_sh_shtrih = 0.3  # это для 2p >= 4, для 2p=2 см стр 380
        self.h_sh_r = {56: 0.5, 63: 0.5, 71: 0.5, 80: 0.5, 90: 0.5, 100: 0.5, 112: 0.75, 132: 0.75, 160: 0.7, 180: 0.7, 200: 0.7,
                225: 0.7,
                250: 0.7, 280: 0.7, 315: 0.7, 355: 0.7}
        B_z_2 = 1.95  # от 1.7 до 1.95
        l_st_2 = l_st_1
        b_z_2 = ((B_sig * self.t_z_2 * l_sig) / (B_z_2 * l_st_1 * k_c)) * 10 ** 3
        self.b_1_r = (math.pi * (D_2 * 10 ** 3 - 2 * self.h_sh_r[self.h] - 2 * self.h_sh_shtrih) - self.Z_2 * b_z_2) / (math.pi + self.Z_2)
        self.b_2_r = math.sqrt((self.b_1_r ** 2 * (self.Z_2 / math.pi + math.pi / 2) - 4 * q_p * 10 ** 6) / (self.Z_2 / math.pi + math.pi / 2))
        self.h_1 = (self.b_1_r - self.b_2_r) * (self.Z_2 / (2 * math.pi))
        print(Back.BLUE + "Пункт: 31")
        print("self.b_sh_2 =", self.b_sh_2[self.h])
        print("self.h_sh_shtrih =", self.h_sh_shtrih)
        print("l_st_2 = l_st_1 =", l_st_2)
        print("b_z_2 =", b_z_2)
        print("self.b_1_r =", self.b_1_r)
        print("self.b_2_r =", self.b_2_r)
        print("self.h_1 =", self.h_1, end='\n')

        ####* __32__
        b_z_2_shtrih = math.pi * ((D_2 * 10 ** 3 - 2 * (self.h_sh_r[self.h] + self.h_sh_shtrih) * self.b_1_r) / (self.Z_2)) - self.b_1_r
        b_z_2_shtrih_shtrih = math.pi * ((D_2 * 10 ** 3 - 2 * h_p + self.b_2_r) / (self.Z_2)) - self.b_2_r
        self.h_p_2 = self.h_sh_shtrih + self.h_sh_r[self.h] + (self.b_1_r / 2) + self.h_1 + (self.b_2_r / 2)
        print(Back.BLUE + "Пункт: 32")
        print("b_z_2_shtrih =", b_z_2_shtrih)
        print("b_z_2'_shtrih =", b_z_2_shtrih_shtrih)
        print("self.h_p_2 =", self.h_p_2, end='\n')

        ####* __33__
        self.q_c = (math.pi / 8) * (self.b_1_r ** 2 + self.b_2_r ** 2) + (1 / 2) * (self.b_1_r + self.b_2_r) * self.h_1
        J_2 = (I_2 / self.q_c) * 10 ** 6
        print(Back.BLUE + "Пункт: 33")
        print("self.q_c =", self.q_c)
        print("J_2 =", J_2, end='\n')

        ####* __34__
        delta = round(2 * math.sin((math.pi * p) / self.Z_2), 3)
        I_kl = I_2 / delta
        j_kl = 0.85 * J_2
        q_kl_shtrih = (I_kl / j_kl) * 10 ** 6
        h_kl = 1.25 * self.h_p_2
        b_kl = q_kl_shtrih / h_kl
        q_kl = h_kl * b_kl
        D_k_avg = (D_2 * 10 ** 3) - h_kl
        print(Back.BLUE + "Пункт: 34")
        print("delta =", delta)
        print("I_kl =", I_kl)
        print("j_kl =", j_kl)
        print("q_kl_shtrih =", q_kl_shtrih)
        print("h_kl =", h_kl)
        print("b_kl =", b_kl)
        print("q_kl =", q_kl)
        print("D_k_avg =", D_k_avg, end='\n')

        ####* __35__
        nu_0 = 4 * math.pi * 10 ** -7
        gamma_1 = (self.b_sh[self.h] / self.sigma) ** 2 / (5 + self.b_sh[self.h] / self.sigma)
        k_sig = (self.t_z_1 * 10 ** 3) / ((self.t_z_1 * 10 ** 3) - gamma_1 * self.sigma)
        F_sig = (2 / nu_0) * B_sig * self.sigma * k_sig * 10 ** -3
        print(Back.BLUE + "Пункт: 35")
        print("nu_0 =", nu_0)
        print("gamma_1 =", gamma_1)
        print("k_sig =", k_sig)
        print("F_sig =", F_sig, end='\n')

        ####* __36__
        h_Z_1 = h_p
        B_Z_1_shtrih = round(((B_sig * (self.t_z_1 * 10 ** 3) * l_sig) / (b_z_1 * l_st_1 * k_c)), 2)
        b_p = self.t_z_1 * 10 ** 3 - B_Z_1_shtrih

        if (B_Z_1_shtrih > 1.8):
            h_Z_1 = 0.5 * h_Z_1

        b_px_1 = (b_1 + b_2) / 2
        k_px_1 = (b_px_1 * l_sig) / (b_z_1 * l_st_1 * k_c)
        H_Z_1 = H_Z_1_dict[int(B_Z_1_shtrih * 10) / 10][int(B_Z_1_shtrih * 100 % 10)]
        F_Z_1 = 2 * h_Z_1 * 10 ** -3 * H_Z_1
        print(Back.BLUE + "Пункт: 36")
        print("h_Z_1 =", h_Z_1)
        print("b_px_1 =", b_px_1)
        print("k_px_1 =", k_px_1)
        print("H_Z_1 =", H_Z_1)
        print("B_Z_1 =", round(B_Z_1_shtrih - nu_0 * H_Z_1 * k_px_1, 1))
        print("B_Z_1_shtrih =", B_Z_1_shtrih)
        print("F_Z_1 =", F_Z_1, end='\n')

        ####* __37__
        h_Z_2 = self.h_p_2 - 0.1 * b_2
        B_Z_2_shtrih = round(((B_sig * self.t_z_2 * l_sig) / (b_z_2 * l_st_2 * k_c)) * 10 ** 3, 2)

        if (B_Z_2_shtrih > 1.8):
            h_Z_2 = 0.5 * h_Z_2

        b_px_2 = (b_1 + b_2) / 2
        k_px_2 = (b_px_2 * l_sig) / (b_z_2 * l_st_2 * k_c)
        H_Z_2 = H_Z_1_dict[int(B_Z_2_shtrih * 10) / 10][int(B_Z_2_shtrih * 100 % 10)]
        F_Z_2 = 2 * h_Z_2 * 10 ** -3 * H_Z_2
        print(Back.BLUE + "Пункт: 37")
        print("h_Z_2 =", h_Z_2)
        print("b_px_2 =", b_px_2)
        print("k_px_2 =", k_px_2)
        print("H_Z_2 =", H_Z_2)
        print("B_Z_2 =", round(B_Z_2_shtrih - nu_0 * H_Z_2 * k_px_2, 1))
        print("B_Z_2_shtrih =", B_Z_2_shtrih)
        print("F_Z_2 =", F_Z_2, end='\n')

        ####* __38__
        k_Z = 1 + (F_Z_1 + F_Z_2) / F_sig
        print(Back.BLUE + "Пункт: 38")
        print("k_Z =", k_Z, end='\n')

        ####* __39__
        h_a = (D_a - D) / 2 - h_p * 10 ** -3
        L_a = math.pi * (D_a - h_a) / self._2p
        B_a = round(Ph / (2 * h_a * l_st_1 * k_c), 2)
        H_a = H_a_dict[int(B_a * 10) / 10][int(B_a * 100 % 10)]
        F_a = L_a * H_a
        print(Back.BLUE + "Пункт: 39")
        print("h_a =", h_a)
        print("L_a =", L_a)
        print("B_a =", B_a)
        print("H_a =", H_a)
        print("F_a =", F_a, end='\n')

        ####* __40__
        h_j = (D_2 - D_j) / 2 - self.h_p_2 * 10 ** -3
        h_j_shtrih = (2 + self._2p / 2) / (3.2 * (self._2p / 2)) * (D_2 / 2 - self.h_p_2 * 10 ** -3)
        B_j = Ph / (2 * h_j_shtrih * l_st_2 * k_c)
        H_j = H_a_dict[int(B_j * 10) / 10][int(B_j * 100 % 10)]
        L_j = (math.pi * (D_j + h_j)) / self._2p
        F_j = L_j * H_j
        print(Back.BLUE + "Пункт: 40")
        print("h_j =", h_j)
        print("h_j_shtrih =", h_j_shtrih)
        print("B_j =", B_j)
        print("L_j =", L_j)
        print("F_j =", F_j)
        print("H_j =", H_j, end='\n')

        ####* __41__
        F_c = round(F_sig, 3) + round(F_Z_1, 3) + round(F_Z_2, 3) + round(F_a, 3) + round(F_j, 3)
        print(Back.BLUE + "Пункт: 41")
        print("F_c =", F_c, end='\n')

        ####* __42__
        k_nu = F_c / F_sig
        print(Back.BLUE + "Пункт: 42")
        print("k_nu =", k_nu, end='\n')

        ####* __43__
        self.I_nu = ((self._2p / 2) * F_c) / (0.9 * self.m * w_1 * self.k_ob)
        I_nu_star = self.I_nu / self.I_1_nom
        print(Back.YELLOW + "Пункт: 43")
        print("self.I_nu =", self.I_nu)
        print("I_nu_star =", I_nu_star, end='\n')

        ####* __44__
        k_R = 1
        ro_115_cuprum = (10 ** -6) / 41
        l_p_1 = l_1
        b_k_m = ((math.pi * ((D + h_p) / self._2p)) * self.beta_shtrih) * 10 ** -2
        B = 0.01
        k_l = {
            2: 1.2,
            4: 1.3,
            6: 1.4,
            8: 1.5,
            10: 1.5,
            12: 1.5,
        }[self._2p]
        k_vil = {
            2: 0.26,
            4: 0.4,
            6: 0.5,
            8: 0.5,
            10: 0.5,
            12: 0.5,
        }[self._2p]
        l_l_1 = k_l * b_k_m + 2 * B
        l_avg_1 = 2 * (l_p_1 + l_l_1)
        L_1 = l_avg_1 * w_1
        self.r_1 = (k_R * ro_115_cuprum * (L_1 / (q_ef * self.a_harmonic))) * 10 ** 6
        r_1_star = self.r_1 * (self.I_1_nom / self.U)
        l_vil = k_vil * b_k_m + B
        print(Back.BLUE + "Пункт: 44")
        print("k_R =", k_R)
        print("ro_115_cuprum =", ro_115_cuprum)
        print("l_p_1 =", l_p_1)
        print("b_k_m =", b_k_m)
        print("B =", B)
        print("k_l =", k_l)
        print("k_vil =", k_vil)
        print("l_l_1 =", l_l_1)
        print("l_avg_1 =", l_avg_1)
        print("L_1 =", L_1)
        print("self.r_1 =", self.r_1)
        print("r_1_star =", r_1_star)
        print("l_vil =", l_vil, end='\n')

        ####* __45__
        ro_115_al = (10 ** -6) / 20.5
        self.r_c = ro_115_al * (l_2 / (self.q_c * 10 ** -6))
        l_c = l_2
        r_kl = ro_115_al * (math.pi * D_k_avg * 10 ** -3) / (self.Z_2 * q_kl * 10 ** -6)
        self.r_2 = self.r_c + (2 * r_kl) / (delta ** 2)
        self.r_2_shtrih = self.r_2 * (4 * self.m * (w_1 * self.k_ob) ** 2) / (self.Z_2 * k_sk ** 2)
        r_2_shtrih_star = self.r_2_shtrih * (self.I_1_nom / self.U)
        print(Back.BLUE + "Пункт: 45")
        print("ro_115_al =", ro_115_al)
        print("self.r_c =", self.r_c)
        print("l_c =", l_c)
        print("r_kl =", r_kl)
        print("self.r_2 =", self.r_2)
        print("self.r_2_shtrih =", self.r_2_shtrih)
        print("r_2_shtrih_star =", r_2_shtrih_star, end='\n')

        ####* __46__
        h_2 = h_p_k - 2 * b_iz
        self.h_k = 0.5 * (b_1 - self.b_sh_2[self.h])
        k_B_shtrih = 0.25 * (1 + 3 * self.beta_shtrih)
        k_B = 0.25 * (1 + 3 * k_B_shtrih)
        h_1_temp = 0

        if (self.P_2 < 15):
            self.Lamda_p_1 = (h_2 / (3 * b_p)) + (self.h_k / b_p)
        else:
            self.Lamda_p_1 = h_2 / (3 * b_1) * k_B + (h_1_temp / b_1 + (3 * self.h_k) / (b_1 + 2 * self.b_sh_2[self.h]) + self.h_sh_shtrih / self.b_sh_2[self.h]) * k_B_shtrih

        self.Lamda_l_1 = 0.34 * (q_1 / l_sig) * (l_l_1 - 0.64 * self.beta_shtrih * tau)
        B_sk = 0
        k_sk_shtrih = k_sk_shtrih_func(self.t_z_2 / self.t_z_1)
        Ksi = 2 * k_sk_shtrih * k_B_shtrih - self.k_ob ** 2 * ((self.t_z_2 * 10 ** 3) / (self.t_z_1 * 10 ** 3)) ** 2 * (1 + B_sk ** 2)
        self.Lamda_d_1 = (self.t_z_1 * 10 ** 3) / (12 * self.sigma * k_sig) * Ksi
        self.X_1 = 15.8 * (self.f / 100) * (w_1 / 100) ** 2 * (l_sig / ((self._2p / 2) * q_1)) * (self.Lamda_p_1 + self.Lamda_l_1 + self.Lamda_d_1)
        X_1_star = self.X_1 * (self.I_1_nom / self.U)
        print(Back.BLUE + "Пункт: 46")
        print("h_2 =", h_2)
        print("self.h_k =", self.h_k)
        print("k_B_shtrih =", k_B_shtrih)
        print("k_B =", k_B)
        print("self.Lamda_p_1 =", self.Lamda_p_1)
        print("self.Lamda_l_1 =", self.Lamda_l_1)
        print("B_sk =", B_sk)
        print("k_sk_shtrih =", k_sk_shtrih)
        print("Ksi =", Ksi)
        print("self.Lamda_d_1 =", self.Lamda_d_1)
        print("self.X_1 =", self.X_1)
        print("X_1_star =", X_1_star, end='\n')

        ####* __47__
        self.h_0 = self.h_1 + 0.4 * self.b_2_r
        k_d = 1
        self.Lamda_p_2 = (self.h_0 / (3 * self.b_1_r) * (1 - (math.pi * self.b_1_r ** 2) / (8 * self.q_c)) ** 2 + 0.66 - self.b_sh_2[self.h] / (
                2 * self.b_1_r)) * k_d + self.h_sh_r[self.h] / self.b_sh_2[self.h] + 1.12 * (self.h_sh_shtrih * 10 ** -3 * 10 ** 6) / I_2
        self.Lamda_l_2 = (2.3 * (D_k_avg * 10 ** -3)) / (self.Z_2 * l_sig * delta ** 2) * math.log10(
            (4.7 * D_k_avg * 10 ** -3) / (h_kl * 10 ** -3 + 2 * b_kl * 10 ** -3))
        delta_z = 0
        Ksi = 1 + (1 / 5) * ((math.pi * (self._2p / 2)) / self.Z_2) ** 2 - (delta_z / (1 - ((self._2p / 2) / self.Z_1)))
        self.Lamda_d_2 = (self.t_z_2 * 10 ** 3) / (12 * self.sigma * k_sig) * Ksi
        Lamda_sk = 0
        X_2 = 7.9 * self.f * l_sig * (self.Lamda_p_2 + self.Lamda_l_2 + self.Lamda_d_2 + Lamda_sk) * 10 ** -6
        self.X_2_shtrih = X_2 * (4 * self.m * (w_1 * self.k_ob) ** 2) / (self.Z_2 * k_sk ** 2)
        X_2_shtrih_star = self.X_2_shtrih * (self.I_1_nom / self.U)
        print(Back.BLUE + "Пункт: 47")
        print("self.h_0 =", self.h_0)
        print("k_d =", k_d)
        print("self.Lamda_p_2 =", self.Lamda_p_2)
        print("self.Lamda_l_2 =", self.Lamda_l_2)
        print("delta_z =", delta_z)
        print("Ksi =", Ksi)
        print("self.Lamda_d_2 =", self.Lamda_d_2)
        print("Lamda_sk =", Lamda_sk)
        print("X_2 =", X_2)
        print("self.X_2_shtrih =", self.X_2_shtrih)
        print("X_2_shtrih_star =", X_2_shtrih_star, end='\n')

        ####* __48__
        P_1_a_150 = 2.5
        gamma_c = 7.8 * 10 ** 3
        m_a = math.pi * (D_a - h_a) * h_a * l_st_1 * gamma_c
        m_z_1 = (h_Z_1 * 10 ** -3) * (b_z_1 * 10 ** -3) * self.Z_1 * l_st_1 * k_sk * gamma_c
        if (self.P_2 < 250):
            k_d_a = 1.6
            k_d_z = 1.8
        elif (self.P_2 >= 250):
            k_d_a = 1.4
            k_d_z = 1.7

        P_st_main = P_1_a_150 * (self.f / 50) ** self.beta_shtrih * (k_d_a * B_a ** 2 * m_a + k_d_z * B_z_1 ** 2 * m_z_1)
        print(Back.BLUE + "Пункт: 48")
        print("P_1_a_150 =", P_1_a_150)
        print("gamma_c =", gamma_c)
        print("m_a =", m_a)
        print("m_z_1 =", m_z_1)
        print("k_d_a =", k_d_a)
        print("k_d_z =", k_d_z)
        print("P_st_main =", P_st_main, end='\n')

        ####* __49__
        k_02 = 1.5
        betta_02 = beta_0_func(self.b_sh[self.h] / self.sigma)
        B_02 = betta_02 * k_sig * B_sig
        p_pov_2 = 0.5 * k_02 * ((self.Z_1 * self.n) / 10_000) ** 1.5 * (B_02 * self.t_z_1 * 10 ** 3) ** 2
        P_pov_2 = p_pov_2 * ((self.t_z_2 * 10 ** 3) - self.b_sh_2[self.h]) * self.Z_2 * l_st_2 * 10 ** -3
        print(Back.BLUE + "Пункт: 49")
        print("k_02 =", k_02)
        print("betta_02 =", betta_02)
        print("B_02 =", B_02)
        print("p_pov_2 =", p_pov_2)
        print("P_pov_2 =", P_pov_2, end='\n')

        ####* __50__
        b_z_2_avg = (b_z_2_shtrih + b_z_2_shtrih_shtrih) / 2
        m_z_2 = self.Z_2 * h_Z_2 * 10 ** -3 * b_z_2_avg * 10 ** -3 * l_st_2 * k_c * gamma_c
        B_z_2_avg = (B_Z_2_shtrih + B_z_2) / 2
        B_pul_2 = (gamma_1 * self.sigma) / (2 * self.t_z_2 * 10 ** 3) * B_z_2_avg
        P_pul_2 = 0.11 * (((self.Z_1 * self.n) / 1000) * B_pul_2) ** 2 * m_z_2
        print(Back.BLUE + "Пункт: 50")
        print("b_z_2_avg =", m_z_2)
        print("m_z_2 =", m_z_2)
        print("B_pul_2 =", B_pul_2)
        print("P_pul_2 =", P_pul_2, end='\n')

        ####* __51__
        P_st_dob = P_pov_2 + P_pul_2
        print(Back.BLUE + "Пункт: 51")
        print("P_st_dob =", P_st_dob, end='\n')

        ####* __52__
        self.P_st = P_st_main + P_st_dob
        print(Back.BLUE + "Пункт: 52")
        print("self.P_st =", self.P_st, end='\n')

        ####* __53__
        K_t = 1.3 * (1 - D_a)
        self.P_meh = K_t * (self.n / 10) ** 2 * D_a ** 4
        print(Back.BLUE + "Пункт: 53")
        print("K_t =", K_t)
        print("self.P_meh =", self.P_meh, end='\n')

        ####* __54__
        P_el_x_x = 3 * self.I_nu ** 2 * self.r_1
        I_x_x_a = (self.P_st + self.P_meh + P_el_x_x) / (self.m * self.U)
        I_x_x = math.sqrt(I_x_x_a ** 2 + self.I_nu ** 2)
        cosPhi_x_x = I_x_x_a / I_x_x
        print(Back.BLUE + "Пункт: 54")
        print("P_el_x_x =", P_el_x_x)
        print("I_x_x_a =", I_x_x_a)
        print("I_x_x =", I_x_x)
        print("cosPhi_x_x =", cosPhi_x_x, end='\n')

        ####* __55__
        r_1_2 = P_st_main / (self.m * self.I_nu ** 2)
        X_1_2 = self.U / self.I_nu - self.X_1
        self.C_1 = 1 + (self.X_1 / X_1_2)
        gamma = math.degrees(math.atan((self.r_1 * X_1_2 - r_1_2 * self.X_1) / (r_1_2 * (self.r_1 + r_1_2) + X_1_2 * (self.X_1 + X_1_2))))
        self.I_0_a = (P_st_main + 3 * self.I_nu ** 2) / (3 * self.U)
        self.a_shtrih = self.C_1 ** 2
        self.b_shtrih = 0
        self.a = self.C_1 * self.r_1
        self.b = self.C_1 * (self.X_1 + self.C_1 * self.X_2_shtrih)
        P = (self.P_st + self.P_meh) * 10 ** -3
        print(Back.BLUE + "Пункт: 55")
        print("r_1_2 =", r_1_2)
        print("X_1_2 =", X_1_2)
        print("self.C_1 =", self.C_1)
        print("gamma =", gamma)
        print("self.I_0_a =", self.I_0_a)
        print("self.a_shtrih =", self.a_shtrih)
        print("self.b_shtrih =", self.b_shtrih)
        print("self.a =", self.a)
        print("self.b =", self.b)
        print("P =", P, end='\n')

        ####* __56__
        print(Back.BLUE + "Таблица 1")


        def calculate_Table_1(numeration, s):
            def f1():
                return (self.a_shtrih * self.r_2_shtrih) / s_shtrih

            def f2():
                R = self.a + ((self.a_shtrih * self.r_2_shtrih) / s_shtrih)
                return R

            def f3():
                X = self.b + ((self.b_shtrih * self.r_2_shtrih) / s_shtrih)
                return X

            def f4():
                Z = math.sqrt(f2() * f2() + f3() * f3())
                return Z

            def f5():
                I2_2shtriha = self.U / f4()
                return I2_2shtriha

            def f6():
                cosPhi2_shtrih = f2() / f4()
                return cosPhi2_shtrih

            def f7():
                sinPhi2_shtrih = f3() / f4()
                return sinPhi2_shtrih

            def f8():
                I_1a = self.I_0_a + f5() * f6()
                return I_1a

            def f9():
                I_1p = self.I_nu + f5() * f7()
                return I_1p

            def f10():
                I1 = math.sqrt(f8() * f8() + f9() * f9())
                return I1

            def f11():
                self.I2_shtrih = self.C_1 * f5()
                return self.I2_shtrih

            def f12():
                P1 = 3 * self.U * f8() * 0.001
                return P1

            def f13():
                P_e1 = 3 * f10() * f10() * self.r_1 * 0.001
                return P_e1

            def f14():
                P_e2 = 3 * f11() * f11() * self.r_2_shtrih * 0.001
                return P_e2

            def f15():
                P_dob = 0.005 * f12()
                return P_dob

            def f16():
                sumP = f15() + f13() + f14() + (self.P_st + self.P_meh) * 10 ** -3
                return sumP

            def f17():
                P2 = f12() - f16()
                return P2

            def f18():
                eta = 1 - (f16() / f12())
                return eta

            def f19():
                cosPhi = f8() / f10()
                return cosPhi

            def setS(s: float):
                global s_shtrih
                s_shtrih = s

            setS(s)
            alert = ""

            if numeration == 1:
                result = f1()
                if (result * 0.9 < 16.783 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 2:
                result = f2()
                if (result * 0.9 < 17.147 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 3:
                result = f3()
                if (result * 0.9 < 4.17 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 4:
                result = f4()
                if (result * 0.9 < 17.646 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 5:
                result = f5()
                if (result * 0.9 < 21.534 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 6:
                result = f6()
                if (result * 0.9 < 0.971 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 7:
                result = f7()
                if (result * 0.9 < 0.236 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 8:
                result = f8()
                if (result * 0.9 < 21.279 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 9:
                result = f9()
                if (result * 0.9 < 10.47 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 10:
                result = f10()
                if (result * 0.9 < 23.715 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 11:
                result = f11()
                if (result * 0.9 < 22.158 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 12:
                result = f12()
                if (result * 0.9 < 24.258 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 13:
                result = f13()
                if (result * 0.9 < 1.012 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 14:
                result = f14()
                if (result * 0.9 < 0.559 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 15:
                result = f15()
                if (result * 0.9 < 0.121 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 16:
                result = f16()
                if (result * 0.9 < 2.349 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 17:
                result = f17()
                if (result * 0.9 < 21.908 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 18:
                result = f18()
                if (result * 0.9 < 0.903 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 19:
                result = f19()
                if (result * 0.9 < 0.897 < result * 1.1):
                    pass
                else:
                    alert = Back.RED

            return alert + "{:.3f}".format(result * 0.9) + Style.RESET_ALL + "\t-\t" + alert + "{:.3f}".format(
                result) + Style.RESET_ALL + "\t+\t" + alert + "{:.3f}".format(result * 1.1)


        for i in range(1, 19 + 1):
            print(i, "|\t", calculate_Table_1(i, self.s_nom))

        ####* __57__
        s_kr = 1
        nu_rasch = 115
        ro_115 = ro_115_al
        b_c__na__b_p = 1
        f_1 = self.f
        self.h_c = self.h_p_2 - (self.h_sh_r[self.h] + self.h_sh_shtrih)
        Ksi = 63.61 * self.h_c * 10 ** -3 * math.sqrt(s_kr)
        phi = phi_func(Ksi)
        h_r = self.h_c / (1 + phi)
        b_r = self.b_1_r - ((self.b_1_r - self.b_2_r) / self.h_1) * h_r
        q_r = (math.pi * self.b_1_r ** 2) / 8 + ((self.b_1_r + b_r) / 2) * (h_r - (self.b_1_r / 2))
        k_r = self.q_c / q_r
        r_c_shtrih = self.r_c
        self.K_R = 1 + (r_c_shtrih / self.r_2) * (k_r - 1)
        self.r_2_Ksi_shtrih = self.K_R * self.r_2_shtrih
        print(Back.BLUE + "Пункт: 57")
        print("nu_rasch =", nu_rasch)
        print("ro_115 =", ro_115)
        print("b_c__na__b_p =", b_c__na__b_p)
        print("f_1 =", f_1)
        print("self.h_c =", self.h_c)
        print("Ksi =", Ksi)
        print("phi =", phi)
        print("h_r =", h_r)
        print("b_r =", b_r)
        print("q_r =", q_r)
        print("k_r =", k_r)
        print("r_c_shtrih =", r_c_shtrih)
        print("self.K_R =", self.K_R)
        print("self.r_2_Ksi_shtrih =", self.r_2_Ksi_shtrih, end='\n')

        ####* __58__
        K_d = phi_shtrih_func(Ksi)
        delta_Lambda_p_2_Ksi = (self.h_0 / (3 * self.b_1_r) * (1 - (math.pi * self.b_1_r ** 2) / (8 * self.q_c)) ** 2 + 0.66 - self.b_sh_2[self.h] / (
                2 * self.b_1_r)) * (1 - K_d)
        self.Lamda_p_2_Ksi = self.Lamda_p_2 - delta_Lambda_p_2_Ksi
        K_x = (self.Lamda_p_2_Ksi + self.Lamda_l_2 + self.Lamda_d_2) / (self.Lamda_p_2 + self.Lamda_l_2 + self.Lamda_d_2)
        X_2__Ksi_shtrih = self.X_2_shtrih * K_x
        print(Back.BLUE + "Пункт: 58")
        print("K_d =", K_d)
        print("delta_Lambda_p_2_Ksi =", delta_Lambda_p_2_Ksi)
        print("self.Lamda_p_2_Ksi =", self.Lamda_p_2_Ksi)
        print("K_x =", K_x)
        print("X_2__Ksi_shtrih =", X_2__Ksi_shtrih, end='\n')

        ####* __59__
        self.x_1_2_p = k_nu * X_1_2
        self.c_1_p = 1 + (self.X_1 / self.x_1_2_p)
        print(Back.BLUE + "Пункт: 59")
        print("self.x_1_2_p =", self.x_1_2_p)
        print("self.c_1_p =", self.c_1_p, end='\n')

        ####* __60__
        R_p = self.r_1 + self.c_1_p * (self.r_2_Ksi_shtrih / s_kr)
        X_p = self.X_1 + self.c_1_p * X_2__Ksi_shtrih
        I_2_p_shtrih = self.U / math.sqrt(R_p ** 2 + X_p ** 2)
        self.I_1_p = I_2_p_shtrih * (math.sqrt(R_p ** 2 + (X_p + self.x_1_2_p) ** 2) / (self.c_1_p * self.x_1_2_p))
        print(Back.BLUE + "Пункт: 60")
        print("R_p =", R_p)
        print("X_p =", X_p)
        print("I_2_p_shtrih =", I_2_p_shtrih)
        print("self.I_1_p =", self.I_1_p, end='\n')

        ####* Таблица 2
        print(Back.BLUE + "Таблица 2")


        def calculate_Table_2(numeration, s):
            def f1():
                return Ksi

            def f2():
                return phi

            def f3():
                return h_r

            def f4():
                return k_r

            def f5():
                return self.K_R

            def f6():
                return self.r_2_Ksi_shtrih

            def f7():
                return K_d

            def f8():
                return self.Lamda_p_2_Ksi

            def f9():
                return K_x

            def f10():
                return X_2__Ksi_shtrih

            def f11():
                return R_p

            def f12():
                return X_p

            def f13():
                return I_2_p_shtrih

            def f14():
                return self.I_1_p

            def setS(s: float):
                global s_shtrih
                s_shtrih = s

            setS(s)
            alert = ""

            if numeration == 1:
                result = f1()
                if (result * 0.9 < 1.884 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 2:
                result = f2()
                if (result * 0.9 < 0.78 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 3:
                result = f3()
                if (result * 0.9 < 16.64 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 4:
                result = f4()
                if (result * 0.9 < 1.557 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 5:
                result = f5()
                if (result * 0.9 < 1.372 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 6:
                result = f6()
                if (result * 0.9 < 0.521 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 7:
                result = f7()
                if (result * 0.9 < 0.8 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 8:
                result = f8()
                if (result * 0.9 < 2.272 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 9:
                result = f9()
                if (result * 0.9 < 0.8 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 10:
                result = f10()
                if (result * 0.9 < 1.624 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 11:
                result = f11()
                if (result * 0.9 < 1.130 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 12:
                result = f12()
                if (result * 0.9 < 3.546 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 13:
                result = f13()
                if (result * 0.9 < 102.123 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 14:
                result = f14()
                if (result * 0.9 < 103.993 < result * 1.1):
                    pass
                else:
                    alert = Back.RED

            return alert + "{:.3f}".format(result * 0.9) + Style.RESET_ALL + "\t-\t" + alert + "{:.3f}".format(
                result) + Style.RESET_ALL + "\t+\t" + alert + "{:.3f}".format(result * 1.1)


        for i in range(1, 14 + 1):
            print(i, "|\t", calculate_Table_2(i, self.s_nom))

        ####* __61__
        k_beta_shtrih = 1
        self.C_N = 0.64 + 2.5 * math.sqrt(self.sigma / ((self.t_z_1 + self.t_z_2) * 10 ** 3))
        self.k_y_1 = math.sin(self.beta_shtrih * (math.pi / 2))
        print(Back.BLUE + "Пункт: 61")
        print("k_beta_shtrih =", k_beta_shtrih)
        print("self.C_N =", self.C_N)
        print("self.k_y_1 =", self.k_y_1, end='\n')

        ####* Таблица 3
        print(Back.BLUE + "Таблица 3")


        def calculate_Table_3(numeration, s):
            def f1():
                return 1.4

            def f2():
                global F_p_avg
                F_p_avg = 0.7 * (((self.I_1_p * f1() * self.u_p) / self.a_harmonic) * (k_beta_shtrih + self.k_y_1 * self.k_ob * (self.Z_1 / self.Z_2)))
                return F_p_avg

            def f3():
                global B_Ph_sig
                B_Ph_sig = (f2() * 10 ** -6) / (1.6 * self.sigma * 10 ** -3 * self.C_N)
                return B_Ph_sig

            def f4():
                k_sig = k_sig_func(f3())
                return k_sig

            def f5():
                c_1 = (self.t_z_1 * 10 ** 3 - self.b_sh[self.h]) * (1 - f4())
                return c_1

            def f6():
                global Lamda_p_1_nas
                Lamda_p_1_nas = self.Lamda_p_1 - (((self.h_sh + 0.58 * self.h_k) / self.b_sh[self.h]) * (f5() / (f5() + 1.5 * self.b_sh[self.h])))
                return Lamda_p_1_nas

            def f7():
                global Lamda_d_1_nas
                Lamda_d_1_nas = f4() * self.Lamda_d_1
                return Lamda_d_1_nas

            def f8():
                global x_1_nas
                x_1_nas = self.X_1 * (Lamda_p_1_nas + Lamda_d_1_nas + self.Lamda_l_1) / (self.Lamda_p_1 + self.Lamda_d_1 + self.Lamda_l_1)
                return x_1_nas

            def f9():
                self.c_1_p = 1 + (f8() / self.x_1_2_p)
                return self.c_1_p

            def f10():
                global c_2
                c_2 = (self.t_z_2 * 10 ** 3 - self.b_sh_2[self.h]) * (1 - f4())
                return c_2

            def f11():
                global Lamda_p_2_Ksi_nas
                Lamda_p_2_Ksi_nas = self.Lamda_p_2_Ksi - (self.h_sh_shtrih / self.b_sh_2[self.h]) * (f10() / (f10() + self.b_sh_2[self.h]))
                return Lamda_p_2_Ksi_nas

            def f12():
                global Lamda_d_2_nas
                Lamda_d_2_nas = f4() * self.Lamda_d_2
                return Lamda_d_2_nas

            def f13():
                global x_2_Ksi_nas_shtrih
                x_2_Ksi_nas_shtrih = self.X_2_shtrih * (f11() + f12() + self.Lamda_l_2) / (self.Lamda_p_2 + self.Lamda_d_2 + self.Lamda_l_2)
                return x_2_Ksi_nas_shtrih

            def f14():
                global R_p_nas
                R_p_nas = self.r_1 + (1 + (f8() / self.x_1_2_p)) * (self.r_2_Ksi_shtrih / s_shtrih)
                return R_p_nas

            def f15():
                global X_p_nas
                X_p_nas = f8() + (1 + (f8() / self.x_1_2_p)) * f13()
                return X_p_nas

            def f16():
                global I_2_nas_shtrih
                I_2_nas_shtrih = self.U / math.sqrt(f14() ** 2 + f15() ** 2)
                return I_2_nas_shtrih

            def f17():
                global I_1_nas
                I_1_nas = f16() * (math.sqrt(f14() ** 2 + (f15() + self.x_1_2_p) ** 2)) / ((1 + (f8() / self.x_1_2_p)) * self.x_1_2_p)
                return I_1_nas

            def f18():
                global k_nas_shtrih
                k_nas_shtrih = f17() / self.I_1_p
                return k_nas_shtrih

            def f19():
                global I_1_star
                I_1_star = f17() / self.I_1_nom
                return I_1_star

            def f20():
                global M_dot
                M_dot = (f16() / self.I2_shtrih) ** 2 * self.K_R * (self.s_nom / s_shtrih)
                return M_dot

            def setS(s: float):
                global s_shtrih
                s_shtrih = s

            setS(s)
            alert = ""

            if numeration == 1:
                result = f1()
                if (result * 0.9 < 1.4 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 2:
                result = f2()
                if (result * 0.9 < 4339.46 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 3:
                result = f3()
                if (result * 0.9 < 5.057 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 4:
                result = f4()
                if (result * 0.9 < 0.48 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 5:
                result = f5()
                if (result * 0.9 < 5.148 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 6:
                result = f6()
                if (result * 0.9 < 1.587 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 7:
                result = f7()
                if (result * 0.9 < 0.988 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 8:
                result = f8()
                if (result * 0.9 < 1.378 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 9:
                result = f9()
                if (result * 0.9 < 1.02 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 10:
                result = f10()
                if (result * 0.9 < 8.117 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 11:
                result = f11()
                if (result * 0.9 < 1.71 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 12:
                result = f12()
                if (result * 0.9 < 1.051 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 13:
                result = f13()
                if (result * 0.9 < 1.32 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 14:
                result = f14()
                if (result * 0.9 < 1.129 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 15:
                result = f15()
                if (result * 0.9 < 2.717 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 16:
                result = f16()
                if (result * 0.9 < 129.163 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 17:
                result = f17()
                if (result * 0.9 < 131.718 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 18:
                result = f18()
                if (result * 0.9 < 1.266 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 19:
                result = f19()
                if (result * 0.9 < 5.4 < result * 1.1):
                    pass
                else:
                    alert = Back.RED
            elif numeration == 20:
                result = f20()
                if (result * 0.9 < 1.13 < result * 1.1):
                    pass
                else:
                    alert = Back.RED

            return alert + "{:.3f}".format(result * 0.9) + Style.RESET_ALL + "\t-\t" + alert + "{:.3f}".format(
                result) + Style.RESET_ALL + "\t+\t" + alert + "{:.3f}".format(result * 1.1)


        for i in range(1, 20 + 1):
            print(i, "|\t", calculate_Table_3(i, s_kr))