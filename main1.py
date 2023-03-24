import math

from colorama import *

init(autoreset=True)

import matplotlib.pyplot as plt

from dict import *
from func import *

####* __ТЗ__
a_harmonic = 1  # гармоника 1 порядка
n_el = 2 # 17 пункт
P_2 = 1.5
U = 220
n = 1500
_2p = 4
m = 3
f = 50
beta_shtrih = 0.833
k_uk = math.sin((math.pi / 2) * beta_shtrih)
cosPhi = cosPhi_func(_2p, P_2)
kpd = kpd_func(_2p, P_2)
print(Back.BLUE + "Пункт: ТЗ")
print("a_gor =", a_harmonic)
print("m =", m)
print("f =", f)
print("coef_ukorochenia =", k_uk)
print("P_2 =", P_2)
print("U =", U)
print("cosPhi =", cosPhi)
print("kpd =", kpd)
print("2p =", _2p, end='\n\n')

####* __1__
h_shtrih = {
    # 2: (p2_up(P_2) + p2_down(P_2)) / 2,
    4: (p6_down__p4_up(P_2) + p4_down(P_2)) / 2,
    # 6: (p8_down__p6_up(P_2) + p6_down__p4_up(P_2) / 2),
    # 8: (p8_up(P_2) + p8_down__p6_up(P_2)) / 2,
    10: 0,
    12: 0
}[_2p]
h = FindApproximateWithinBounds(
    [56, 63, 71, 80, 90, 100, 112, 132, 160, 180, 200, 225, 250, 280, 315, 355],
    h_shtrih
)
D_a = {
    56: 0.088,
    63: 0.104,
    71: 0.116,
    80: 0.131,
    90: 0.153,
    100: 0.173,
    112: 0.194,
    132: 0.229,
    160: 0.2785,
    180: 0.32,
    200: 0.354,
    225: 0.399,
    250: 0.437,
    280: 0.525,
    315: 0.59,
    355: 0.66
}[h]

####* __2__
# k_D = {
#     2: 0.56,
#     4: 0.65,
#     6: 0.71,
#     8: 0.735,
#     10: 0.76,
#     12: 0.76
# }[_2p]

k_D = {
    2: 0.56,
    4: 0.62,
    6: 0.71,
    8: 0.73,
    10: 0.76,
    12: 0.76
}[_2p]
sumator = 0.005
sumator_D_a = 0.001
# НЦ
print(h)
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
while D_a !=D_a_max[h]+sumator_D_a:
    k_D = 0.62
    while (k_D != 0.685):

        D = round(k_D * D_a, 3)

        ####* __3__
        tau = (math.pi * D) / _2p

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
        # }[_2p][D_a]
        k_e = K_e_func(D_a)
        P_shtrih = (P_2 * 1000) * (k_e / (kpd * cosPhi))

        ####* __5__
        A_shtrih = (A__up(_2p, D_a) + A__down(_2p, D_a)) / 2
        B_sig_shtrih = (B_sig__up(_2p, D_a) + B_sig__down(_2p, D_a)) / 2

        ####* __6__
        t_z_1_max = round(t_z1__2_max(tau), 3)
        t_z_1_min = round(t_z1__2_min(tau), 3)

        Z_1_min = round((math.pi * D) / t_z_1_max)
        Z_1_max = round((math.pi * D) / t_z_1_min)

        Z_1 = {  # АЛГОРИТМ РАБОТАЕТ, НО ЕСТЬ НЬЮАНС
            2: FindMaxInBounds([12, 18, 24, 30, 36, 42, 48], Z_1_min, Z_1_max),
            4: FindMaxInBounds([12, 18, 24, 36, 42, 48, 60, 72], Z_1_min, Z_1_max),
            6: FindMaxInBounds([36, 54, 72, 90], Z_1_min, Z_1_max),
            8: FindMaxInBounds([48, 72, 84, 96], Z_1_min, Z_1_max),
            10: FindMaxInBounds([60, 90, 120], Z_1_min, Z_1_max),
            12: FindMaxInBounds([72, 90, 108, 144], Z_1_min, Z_1_max)
        }[_2p]

        q_1 = math.ceil(Z_1 / (_2p * m))
        k_ras = (math.sin(math.pi / (2 * m))) / (q_1 * math.sin(math.pi / (2 * m * q_1)))

        k_ob = k_ras * k_uk

        ####* __7__
        p = _2p / 2
        k_B = math.pi / (2 * math.sqrt(2))
        omega = math.pi * 2 * f / p
        l_sig = (P_shtrih / (k_B * D ** 2 * omega * k_ob * A_shtrih * B_sig_shtrih))

        ####? __8__
        lamda = l_sig / tau

        ####* __9__

        ####* __10__

        ####* __11__
        t_z_1 = (math.pi * D) / (_2p * q_1 * m)

        ####* __12__
        I_1_nom = (P_2 * 1000) / (m * U * cosPhi * kpd)
        u_shtrih_p = (math.pi * D * A_shtrih) / (I_1_nom * Z_1)

        ####* __13__
        u_p = round(a_harmonic * u_shtrih_p)

        ####? __14__
        w_1 = (u_p * Z_1) / (2 * a_harmonic * m)
        A = (2 * I_1_nom * w_1 * m) / (math.pi * D)
        Ph = (k_e * U) / (4 * k_B * w_1 * k_ob * f)
        B_sig = ((_2p / 2) * Ph) / (D * l_sig)

        ####* __15__
        J_1_shtrih = ((AJ__up(_2p, D_a) + AJ__down(_2p, D_a)) / 2) / A

        ####* __16__
        q_ef_shtrih = (I_1_nom / (a_harmonic * J_1_shtrih)) * 10 ** 6

        ####* __17__

        q_el_shtrih = q_ef_shtrih / n_el
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
        q_ef = n_el * q_el

        ####* __18__
        J_1 = I_1_nom / (a_harmonic * q_el * n_el)

        ####* __19__
        B_z_1 = {
            2: 1.75,
            4: 1.7,
            6: 1.75,
            8: 1.75,
            10: 1.7,
            12: 1.7
        }[_2p]
        B_a = {
            2: 1.5,
            4: 1.5,
            6: 1.5,
            8: 1.25,
            10: 1.15,
            12: 1.15
        }[_2p]
        k_c = 0.97
        l_st_1 = l_sig
        b_z_1 = ((B_sig * t_z_1 * l_sig) / (B_z_1 * l_sig * k_c)) * 10 ** 3
        h_a = Ph / (2 * B_a * l_sig * k_c)

        ####* __20__
        b_sh = {50: 1.8, 63: 1.8, 71: 2, 80: 3, 90: 3, 100: 3.5, 112: 3.5, 132: 3.5, 160: 3.7, 180: 3.7, 200: 3.7, 225: 3.7,
                250: 3.7, 280: 3.7, 315: 3.7, 355: 3.7}
        h_sh = 0.8
        h_p = ((D_a - D) / 2 - h_a) * 10 ** 3
        b_1 = (math.pi * ((D * 10 ** 3) + 2 * h_sh - b_sh[h]) - Z_1 * b_z_1) / (Z_1 - math.pi)
        b_2 = ((math.pi * ((D * 10 ** 3) + 2 * h_p)) / Z_1) - b_z_1
        h_p_k = h_p - (h_sh + ((b_1 - b_sh[h]) / 2))

        ####* __21__
        delta_b = 0
        delta_h = 0
        if (50 <= h <= 132):
            delta_b = 0.1
            delta_h = 0.1
        elif (160 <= h <= 250):
            delta_b = 0.2
            delta_h = 0.2
        elif (280 <= h <= 355):
            delta_b = 0.3
            delta_h = 0.3
        elif (400 <= h <= 500):
            delta_b = 0.4
            delta_h = 0.3

        b_1_shtrih = b_1 - delta_b
        b_2_shtrih = b_2 - delta_b
        h_p_k_shtrih = h_p_k - delta_h
        S_pr = 0
        if (180 <= h <= 250):
            S_pr = 0.6 * (b_1 + b_2)
        elif (h >= 280):
            S_pr = 0.9 * b_1 + 0.4 * b_2
        b_iz = 0
        if (50 <= h <= 80):
            b_iz = 0.2
        elif (90 <= h <= 132):
            b_iz = 0.25
        elif (h == 160):
            b_iz = 0.4
        elif (180 <= h <= 250):
            b_iz = 0.4
        S_iz = b_iz * (2 * h_p + b_1 + b_2)
        S_p_shtrih = ((b_1_shtrih + b_2_shtrih) / 2) * h_p_k_shtrih - (S_iz + S_pr)

        ####? __22__
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
        k_z = round((d_iz ** 2 * u_p * n_el) / S_p_shtrih, 2)
        print(Back.YELLOW + "Пункт: 22")
        print("d_iz =", d_iz)
        if (0.7 <= k_z <= 0.75):
            print("k_D = " + str(k_D))
            print("D_a = " + str(D_a))
            print(Back.GREEN + "k_z = " + str(k_z), end='\n\n')
            break
        else:
            print("k_D = " + str(k_D), end='\n\n')
            print(Back.RED + "k_z = " + str(k_z), end='\n\n')
            k_D += sumator
    if (0.7 <= k_z <= 0.75):
        print("k_D = " + str(k_D))
        print("D_a = " + str(D_a))
        print(Back.GREEN + "k_z = " + str(k_z), end='\n\n')

        break
    else:
        print("D_a = " + str(D_a), end='\n\n')
        print(Back.RED + "k_z = " + str(k_z), end='\n\n')
        D_a += sumator_D_a

# КЦ
if (0.7 > k_z or k_z > 0.75):
    print(Back.RED + "k_z = " + str(k_z), end='\n\n')
    exit(1)
print(Back.BLUE + "Пункт: 1")
print("h_shtrih =", h_shtrih)
print("h =", h)
print("D_a =", D_a, end='\n\n')
print(Back.BLUE + "Пункт: 2")
print("k_D =", k_D)
print("D =", D, end='\n\n')
print(Back.BLUE + "Пункт: 3")
print("tau =", tau, end='\n\n')
print(Back.BLUE + "Пункт: 4")
print("k_e =", k_e)
print("P_shtrih =", P_shtrih, end='\n\n')
print(Back.BLUE + "Пункт: 5")
print("A_shtrih =", A_shtrih)
print("B_sig_shtrih =", B_sig_shtrih, end='\n\n')
print(Back.BLUE + "Пункт: 6")
print("k_ras =", k_ras)
print("k_uk =", k_uk)
print("k_ob =", k_ob, end='\n\n')
print(Back.BLUE + "Пункт: 7")
print("p =", p)
print("k_B =", k_B)
print("omega =", omega)
print("l_sig =", l_sig, end='\n\n')
print(Back.YELLOW + "Пункт: 8")
print("lamda =", lamda, end='\n\n')
print(Back.BLUE + "Пункт: 9")
print("t_z_1_max =", t_z_1_max)
print("t_z_1_min =", t_z_1_min, end='\n\n')
print(Back.BLUE + "Пункт: 10")
print("Z_1_min =", (math.pi * D) / t_z_1_max)
print("Z_1_max =", (math.pi * D) / t_z_1_min)
print("Z_1 =", Z_1)
print("q1 =", q_1, end='\n\n')
print(Back.BLUE + "Пункт: 11")
print("t_z_1 =", t_z_1, end='\n\n')
print(Back.BLUE + "Пункт: 12")
print("I_1_nom =", I_1_nom)
print("u_shtrih_p =", u_shtrih_p, end='\n\n')
print(Back.BLUE + "Пункт: 13")
print("u_p =", u_p, end='\n\n')
print(Back.YELLOW + "Пункт: 14")
print("w_1 =", w_1)
print("Ph =", Ph)
if (A_shtrih * 0.9 < A < A_shtrih * 1.1 or B_sig_shtrih * 0.9 < B_sig < B_sig_shtrih * 1.1):
    print(Back.GREEN + "A = " + str(A))
    print(Back.GREEN + "B_sig = " + str(B_sig), end='\n\n')
else:
    print(Back.RED + "A = " + str(A))
    print(Back.RED + "B_sig = " + str(B_sig), end='\n\n')
    exit()
print(Back.BLUE + "Пункт: 15")
print("AJ =", (AJ__up(_2p, D_a) + AJ__down(_2p, D_a)) / 2)
print("J_1_shtrih =", J_1_shtrih, end='\n\n')
print(Back.BLUE + "Пункт: 16")
print("q_ef_shtrih =", q_ef_shtrih, end='\n\n')
print(Back.BLUE + "Пункт: 17")
print("n_el =", n_el)
print("q_el_shtrih =", q_el_shtrih)
print("q_el =", q_el)
print("q_ef =", q_ef, end='\n\n')
print(Back.BLUE + "Пункт: 18")
if ((J_1_shtrih * 0.9) * 10 ** -6 < J_1 < (J_1_shtrih * 1.1) * 10 ** -6):
    print(Back.GREEN + "J_1 = " + str(J_1), end='\n\n')
else:
    print(Back.RED + "J_1 = " + str(J_1), end='\n\n')
    exit()
print(Back.BLUE + "Пункт: 19")
print("B_z_1 =", B_z_1)
print("B_a =", B_a)
print("k_c =", k_c)
print("b_z_1 =", b_z_1)
print("h_a =", h_a, end='\n\n')
print(Back.BLUE + "Пункт: 20")
print("b_sh =", b_sh[h])
print("h_sh =", h_sh)
print("h_p =", h_p)
print("b_1 =", b_1)
print("b_2 =", b_2)
print("h_p_k =", h_p_k, end='\n\n')
print(Back.BLUE + "Пункт: 21")
print("delta_b =", delta_b)
print("delta_h =", delta_h)
print("b_1_shtrih =", b_1_shtrih)
print("b_2_shtrih =", b_2_shtrih)
print("h_p_k_shtrih =", h_p_k_shtrih)
print("b_iz =", b_iz)
print("S_pr =", S_pr)
print("S_iz =", S_iz)
print("S_p_shtrih =", S_p_shtrih, end='\n\n')

####* __23__
sigma = Sigma(h)[_2p](D)
print(Back.BLUE + "Пункт: 23")
print("sigma =", sigma, end='\n\n')

####* __24__
Z_2 = findTheNumberOfRotorSlots(P_2, Z_1)
print(Back.BLUE + "Пункт: 24")
print("Z_2 =", Z_2, end='\n\n')

####* __25__
D_2 = D - (2 * (sigma * 10 ** (-3)))
print(Back.BLUE + "Пункт: 25")
print("D_2 =", D_2, end='\n\n')

####* __26__
l_2 = l_1 = l_sig
print(Back.BLUE + "Пункт: 26")
print("l_2 = l_1 =", l_2, end='\n\n')

####* __27__
t_z_2 = (math.pi * D_2) / Z_2
print(Back.BLUE + "Пункт: 27")
print("t_z_2 =", t_z_2, end='\n\n')

####* __28__
k_B = 0
if (50 <= h <= 63):
    k_B = 0.19
elif (71 <= h <= 250):
    k_B = 0.23
elif (280 <= h <= 355):
    if (_2p == 2):
        k_B = 0.22
    elif (4 <= _2p <= 12):
        k_B = 0.23
elif (400 <= h <= 500):
    if (_2p == 4):
        k_B = 0.2
    elif (_2p == 6):
        k_B = 0.23
    elif (8 <= _2p <= 12):
        k_B = 0.25
D_j = D_b = k_B * D_a
print(Back.BLUE + "Пункт: 28")
print("k_B__punkt_24 =", k_B)
print("D_j =", D_j, end='\n\n')

####* __29__
k_sk = 1
v_i = (2 * m * w_1 * k_ob) / (Z_2 * k_sk)
k_i = 0.2 + 0.8 * cosPhi
I_2 = k_i * I_1_nom * v_i
print(Back.BLUE + "Пункт: 29")
print("k_sk =", k_sk)
print("v_i =", v_i)
print("k_i =", k_i)
print("I_2 =", I_2, end='\n\n')

####* __30__
J_2 = 3 * 10 ** 6
q_p = I_2 / J_2
print(Back.BLUE + "Пункт: 30")
print("J_2 =", J_2)
print("q_p =", q_p, end='\n\n')

####* __31__
b_sh_2 = {50: 1.0, 63: 1.0, 71: 1.0, 80: 1.0, 90: 1.0, 100: 1.0, 112: 1.5, 132: 1.5, 160: 1.5, 180: 1.5, 200: 1.5,
          225: 1.5,
          250: 1.5, 280:1.5,315:1.5,355:1.5}
h_sh_shtrih = 0.3  # это для 2p >= 4, для 2p=2 см стр 380
h_sh_r = {50: 0.5, 63: 0.5, 71: 0.5, 80: 0.5, 90: 0.5, 100: 0.5, 112: 0.75, 132: 0.75, 160: 0.7, 180: 0.7, 200: 0.7,
          225: 0.7,
          250: 0.7, 280:0.7,315:0.7,355:0.7}
B_z_2 = 1.95 #от 1.7 до 1.95
l_st_2 = l_st_1
b_z_2 = ((B_sig * t_z_2 * l_sig) / (B_z_2 * l_st_1 * k_c)) * 10 ** 3
b_1_r = (math.pi * (D_2 * 10 ** 3 - 2 * h_sh_r[h] - 2 * h_sh_shtrih) - Z_2 * b_z_2) / (math.pi + Z_2)
b_2_r = math.sqrt((b_1_r ** 2 * (Z_2 / math.pi + math.pi / 2) - 4 * q_p*10**6) / (Z_2 / math.pi + math.pi / 2))
h_1 = (b_1_r - b_2_r) * (Z_2 / (2 * math.pi))
print(Back.BLUE + "Пункт: 31")
print("b_sh_2 =", b_sh_2[h])
print("h_sh_shtrih =", h_sh_shtrih)
print("l_st_2 = l_st_1 =", l_st_2)
print("b_z_2 =", b_z_2)
print("b_1_r =", b_1_r)
print("b_2_r =", b_2_r)
print("h_1 =", h_1, end='\n\n')

####* __32__
b_z_2_shtrih = math.pi * ((D_2 * 10 ** 3 - 2 * (h_sh_r[h] + h_sh_shtrih) * b_1_r) / (Z_2)) - b_1_r
b_z_2_shtrih_shtrih = math.pi * ((D_2 * 10 ** 3 - 2 * h_p + b_2_r) / (Z_2)) - b_2_r
h_p_2 = h_sh_shtrih + h_sh_r[h] + (b_1_r / 2) + h_1 + (b_2_r / 2)
print(Back.BLUE + "Пункт: 32")
print("b_z_2_shtrih =", b_z_2_shtrih)
print("b_z_2'_shtrih =", b_z_2_shtrih_shtrih)
print("h_p_2 =", h_p_2, end='\n\n')

####* __33__
q_c = (math.pi / 8) * (b_1_r ** 2 + b_2_r ** 2) + (1 / 2) * (b_1_r + b_2_r) * h_1
J_2 = (I_2 / q_c) * 10 ** 6
print(Back.BLUE + "Пункт: 33")
print("q_c =", q_c)
print("J_2 =", J_2, end='\n\n')

####* __34__
delta = round(2 * math.sin((math.pi * p) / Z_2), 3)
I_kl = I_2 / delta
j_kl = 0.85 * J_2
q_kl_shtrih = (I_kl / j_kl) * 10 ** 6
h_kl = 1.25 * h_p_2
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
print("D_k_avg =", D_k_avg, end='\n\n')

####* __35__
nu_0 = 4 * math.pi * 10 ** -7
gamma_1 = (b_sh[h] / sigma) ** 2 / (5 + b_sh[h] / sigma)
k_sig = (t_z_1 * 10 ** 3) / ((t_z_1 * 10 ** 3) - gamma_1 * sigma)
F_sig = (2 / nu_0) * B_sig * sigma * k_sig * 10 ** -3
print(Back.BLUE + "Пункт: 35")
print("nu_0 =", nu_0)
print("gamma_1 =", gamma_1)
print("k_sig =", k_sig)
print("F_sig =", F_sig, end='\n\n')

####* __36__
h_Z_1 = h_p
B_Z_1_shtrih = round(((B_sig * (t_z_1 * 10 ** 3) * l_sig) / (b_z_1 * l_st_1 * k_c)), 2)

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
print("F_Z_1 =", F_Z_1, end='\n\n')

####* __37__
h_Z_2 = h_p_2 - 0.1 * b_2
B_Z_2_shtrih = round(((B_sig * t_z_2 * l_sig) / (b_z_2 * l_st_2 * k_c)) * 10 ** 3, 2)

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
print("F_Z_2 =", F_Z_2, end='\n\n')

####* __38__
k_Z = 1 + (F_Z_1 + F_Z_2) / F_sig
print(Back.BLUE + "Пункт: 38")
print("k_Z =", k_Z, end='\n\n')

####* __39__
h_a = (D_a - D) / 2 - h_p * 10 ** -3
L_a = math.pi * (D_a - h_a) / _2p
B_a = round(Ph / (2 * h_a * l_st_1 * k_c), 2)
H_a = H_a_dict[int(B_a * 10) / 10][int(B_a * 100 % 10)]
F_a = L_a * H_a
print(Back.BLUE + "Пункт: 39")
print("h_a =", h_a)
print("L_a =", L_a)
print("B_a =", B_a)
print("H_a =", H_a)
print("F_a =", F_a, end='\n\n')

####* __40__
h_j = (D_2 - D_j) / 2 - h_p_2 * 10 ** -3
h_j_shtrih = (2 + _2p / 2) / (3.2 * (_2p / 2)) * (D_2 / 2 - h_p_2 * 10 ** -3)
B_j = Ph / (2 * h_j_shtrih * l_st_2 * k_c)
H_j = H_a_dict[int(B_j * 10) / 10][int(B_j * 100 % 10)]
L_j = (math.pi * (D_j + h_j)) / _2p
F_j = L_j * H_j
print(Back.BLUE + "Пункт: 40")
print("h_j =", h_j)
print("h_j_shtrih =", h_j_shtrih)
print("B_j =", B_j)
print("L_j =", L_j)
print("F_j =", F_j)
print("H_j =", H_j, end='\n\n')

####* __41__
F_c = F_sig + F_Z_1 + F_Z_2 + F_a + F_j
print(Back.BLUE + "Пункт: 41")
print("F_c =", F_c, end='\n\n')

####* __42__
k_nu = F_c / F_sig
print(Back.BLUE + "Пункт: 42")
print("k_nu =", k_nu, end='\n\n')

####* __43__
I_nu = ((_2p / 2) * F_c) / (0.9 * m * w_1 * k_ob)
I_nu_star = I_nu / I_1_nom
print(Back.YELLOW + "Пункт: 43")
print("I_nu =", I_nu)
print("I_nu_star =", I_nu_star, end='\n\n')

####* __44__
k_R = 1
ro_115_cuprum = (10 ** -6) / 41
l_p_1 = l_1
b_k_m = ((math.pi * ((D + h_p) / _2p)) * beta_shtrih) * 10 ** -2
B = 0.01
k_l = {
    2: 1.2,
    4: 1.3,
    6: 1.4,
    8: 1.5,
    10: 1.5,
    12: 1.5,
}[_2p]
k_vil = {
    2: 0.26,
    4: 0.4,
    6: 0.5,
    8: 0.5,
    10: 0.5,
    12: 0.5,
}[_2p]
l_l_1 = k_l * b_k_m + 2 * B
l_avg_1 = 2 * (l_p_1 + l_l_1)
L_1 = l_avg_1 * w_1
r_1 = (k_R * ro_115_cuprum * (L_1 / (q_ef * a_harmonic))) * 10 ** 6
r_1_star = r_1 * (I_1_nom / U)
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
print("r_1 =", r_1)
print("r_1_star =", r_1_star)
print("l_vil =", l_vil, end='\n\n')

####* __45__
ro_115_al = (10 ** -6) / 20.5
r_c = ro_115_al * (l_2 / (q_c * 10 ** -6))
l_c = l_2
r_kl = ro_115_al * (math.pi * D_k_avg * 10 ** -3) / (Z_2 * q_kl * 10 ** -6)
r_2 = r_c + (2 * r_kl) / (delta ** 2)
r_2_shtrih = r_2 * (4 * m * (w_1 * k_ob) ** 2) / (Z_2 * k_sk ** 2)
r_2_shtrih_star = r_2_shtrih * (I_1_nom / U)
print(Back.BLUE + "Пункт: 45")
print("ro_115_al =", ro_115_al)
print("r_c =", r_c)
print("l_c =", l_c)
print("r_kl =", r_kl)
print("r_2 =", r_2)
print("r_2_shtrih =", r_2_shtrih)
print("r_2_shtrih_star =", r_2_shtrih_star, end='\n\n')

####* __46__
h_2 = h_p_k - 2 * b_iz
h_k = 0.5 * (b_1 - b_sh_2[h])
k_B_shtrih = 0.25 * (1 + 3 * beta_shtrih)
k_B = 0.25 * (1 + 3 * k_B_shtrih)
h_1_temp = 0
Lamda_p_1 = h_2 / (3 * b_1) * k_B + (
        h_1_temp / b_1 + (3 * h_k) / (b_1 + 2 * b_sh_2[h]) + h_sh_shtrih / b_sh_2[h]) * k_B_shtrih
Lamda_l_1 = 0.34 * (q_1 / l_sig) * (l_l_1 - 0.64 * beta_shtrih * tau)
B_sk = 0
k_sk_shtrih = k_sk_shtrih_func(t_z_2 / t_z_1)
Ksi = 2 * k_sk_shtrih * k_B_shtrih - k_ob ** 2 * ((t_z_2 * 10 ** 3) / (t_z_1 * 10 ** 3)) ** 2 * (1 + B_sk ** 2)
Lamda_d_1 = (t_z_1 * 10 ** 3) / (12 * sigma * k_sig) * Ksi
X_1 = 15.8 * (f / 100) * (w_1 / 100) ** 2 * (l_sig / ((_2p / 2) * q_1)) * (Lamda_p_1 + Lamda_l_1 + Lamda_d_1)
X_1_star = X_1 * (I_1_nom / U)
print(Back.BLUE + "Пункт: 46")
print("h_2 =", h_2)
print("h_k =", h_k)
print("k_B_shtrih =", k_B_shtrih)
print("k_B =", k_B)
print("Lamda_p_1 =", Lamda_p_1)
print("Lamda_l_1 =", Lamda_l_1)
print("B_sk =", B_sk)
print("k_sk_shtrih =", k_sk_shtrih)
print("Ksi =", Ksi)
print("Lamda_d_1 =", Lamda_d_1)
print("X_1 =", X_1)
print("X_1_star =", X_1_star, end='\n\n')

####* __47__
h_0 = h_1 + 0.4 * b_2_r
k_d = 1
Lamda_p_2 = (h_0 / (3 * b_1_r) * (1 - (math.pi * b_1_r ** 2) / (8 * q_c)) ** 2 + 0.66 - b_sh_2[h] / (
        2 * b_1_r)) * k_d + h_sh_r[h] / b_sh_2[h] + 1.12 * (h_sh_shtrih * 10 ** -3 * 10 ** 6) / I_2
Lamda_l_2 = (2.3 * (D_k_avg * 10 ** -3)) / (Z_2 * l_sig * delta ** 2) * math.log10(
    (4.7 * D_k_avg * 10 ** -3) / (h_kl * 10 ** -3 + 2 * b_kl * 10 ** -3))
delta_z = 0
Ksi = 1 + (1 / 5) * ((math.pi * (_2p / 2)) / Z_2) ** 2 - (delta_z / (1 - ((_2p / 2) / Z_1)))
Lamda_d_2 = (t_z_2 * 10 ** 3) / (12 * sigma * k_sig) * Ksi
Lamda_sk = 0
X_2 = 7.9 * f * l_sig * (Lamda_p_2 + Lamda_l_2 + Lamda_d_2 + Lamda_sk) * 10 ** -6
X_2_shtrih = X_2 * (4 * m * (w_1 * k_ob) ** 2) / (Z_2 * k_sk ** 2)
X_2_shtrih_star = X_2_shtrih * (I_1_nom / U)
print(Back.BLUE + "Пункт: 47")
print("h_0 =", h_0)
print("k_d =", k_d)
print("Lamda_p_2 =", Lamda_p_2)
print("Lamda_l_2 =", Lamda_l_2)
print("delta_z =", delta_z)
print("Ksi =", Ksi)
print("Lamda_d_2 =", Lamda_d_2)
print("Lamda_sk =", Lamda_sk)
print("X_2 =", X_2)
print("X_2_shtrih =", X_2_shtrih)
print("X_2_shtrih_star =", X_2_shtrih_star, end='\n\n')

####* __48__
P_1_a_150 = 2.5
gamma_c = 7.8 * 10 ** 3
m_a = math.pi * (D_a - h_a) * h_a * l_st_1 * gamma_c
m_z_1 = (h_Z_1 * 10 ** -3) * (b_z_1 * 10 ** -3) * Z_1 * l_st_1 * k_sk * gamma_c
if (P_2 < 250):
    k_d_a = 1.6
    k_d_z = 1.8
elif (P_2 > 250):
    k_d_a = 1.4
    k_d_z = 1.7

P_st_main = P_1_a_150 * (f / 50) ** beta_shtrih * (k_d_a * B_a ** 2 * m_a + k_d_z * B_z_1 ** 2 * m_z_1)
print(Back.BLUE + "Пункт: 48")
print("P_1_a_150 =", P_1_a_150)
print("gamma_c =", gamma_c)
print("m_a =", m_a)
print("m_z_1 =", m_z_1)
print("k_d_a =", k_d_a)
print("k_d_z =", k_d_z)
print("P_st_main =", P_st_main, end='\n\n')

####* __49__
k_02 = 1.5
betta_02 = beta_0_func(b_sh[h] / sigma)
B_02 = betta_02 * k_sig * B_sig
p_pov_2 = 0.5 * k_02 * ((Z_1 * n) / 10_000) ** 1.5 * (B_02 * t_z_1 * 10 ** 3) ** 2
P_pov_2 = p_pov_2 * ((t_z_2 * 10 ** 3) - b_sh_2[h]) * Z_2 * l_st_2 * 10 ** -3
print(Back.BLUE + "Пункт: 49")
print("k_02 =", k_02)
print("betta_02 =", betta_02)
print("B_02 =", B_02)
print("p_pov_2 =", p_pov_2)
print("P_pov_2 =", P_pov_2, end='\n\n')

####* __50__
b_z_2_avg = (b_z_2_shtrih + b_z_2_shtrih_shtrih) / 2
m_z_2 = Z_2 * h_Z_2 * 10 ** -3 * b_z_2_avg * 10 ** -3 * l_st_2 * k_c * gamma_c
B_z_2_avg = (B_Z_2_shtrih + B_z_2) / 2
B_pul_2 = (gamma_1 * sigma) / (2 * t_z_2 * 10 ** 3) * B_z_2_avg
P_pul_2 = 0.11 * (((Z_1 * n) / 1000) * B_pul_2) ** 2 * m_z_2
print(Back.BLUE + "Пункт: 50")
print("b_z_2_avg =", m_z_2)
print("m_z_2 =", m_z_2)
print("B_pul_2 =", B_pul_2)
print("P_pul_2 =", P_pul_2, end='\n\n')

####* __51__
P_st_dob = P_pov_2 + P_pul_2
print(Back.BLUE + "Пункт: 51")
print("P_st_dob =", P_st_dob, end='\n\n')

####* __52__
P_st = P_st_main + P_st_dob
print(Back.BLUE + "Пункт: 52")
print("P_st =", P_st, end='\n\n')

####* __53__
K_t = 1.3 * (1 - D_a)
P_meh = K_t * (n / 10) ** 2 * D_a ** 4
print(Back.BLUE + "Пункт: 53")
print("K_t =", K_t)
print("P_meh =", P_meh, end='\n\n')

####* __54__
P_el_x_x = 3 * I_nu ** 2 * r_1
I_x_x_a = (P_st + P_meh + P_el_x_x) / (m * U)
I_x_x = math.sqrt(I_x_x_a ** 2 + I_nu ** 2)
cosPhi_x_x = I_x_x_a / I_x_x
print(Back.BLUE + "Пункт: 54")
print("P_el_x_x =", P_el_x_x)
print("I_x_x_a =", I_x_x_a)
print("I_x_x =", I_x_x)
print("cosPhi_x_x =", cosPhi_x_x, end='\n\n')

####* __55__
r_1_2 = P_st_main / (m * I_nu ** 2)
X_1_2 = U / I_nu - X_1
C_1 = 1 + (X_1 / X_1_2)
gamma = math.degrees(math.atan((r_1 * X_1_2 - r_1_2 * X_1) / (r_1_2 * (r_1 + r_1_2) + X_1_2 * (X_1 + X_1_2))))
I_0_a = (P_st_main + 3 * I_nu ** 2) / (3 * U)
a_shtrih = C_1 ** 2
b_shtrih = 0
a = C_1 * r_1
b = C_1 * (X_1 + C_1 * X_2_shtrih)
P = (P_st + P_meh) * 10 ** -3
print(Back.BLUE + "Пункт: 55")
print("r_1_2 =", r_1_2)
print("X_1_2 =", X_1_2)
print("C_1 =", C_1)
print("gamma =", gamma)
print("I_0_a =", I_0_a)
print("a_shtrih =", a_shtrih)
print("b_shtrih =", b_shtrih)
print("a =", a)
print("b =", b)
print("P =", P, end='\n\n')

s_nom = 0.0244

####* __56__
print(Back.BLUE + "Таблица 1")


def calculate_Table_1(numeration, s):
    def f1():
        return (a_shtrih * r_2_shtrih) / s_shtrih

    def f2():
        R = a + ((a_shtrih * r_2_shtrih) / s_shtrih)
        return R

    def f3():
        X = b + ((b_shtrih * r_2_shtrih) / s_shtrih)
        return X

    def f4():
        Z = math.sqrt(f2() * f2() + f3() * f3())
        return Z

    def f5():
        I2_2shtriha = U / f4()
        return I2_2shtriha

    def f6():
        cosPhi2_shtrih = f2() / f4()
        return cosPhi2_shtrih

    def f7():
        sinPhi2_shtrih = f3() / f4()
        return sinPhi2_shtrih

    def f8():
        I_1a = I_0_a + f5() * f6()
        return I_1a

    def f9():
        I_1p = I_nu + f5() * f7()
        return I_1p

    def f10():
        I1 = math.sqrt(f8() * f8() + f9() * f9())
        return I1

    def f11():
        global I2_shtrih
        I2_shtrih = C_1 * f5()
        return I2_shtrih

    def f12():
        P1 = 3 * U * f8() * 0.001
        return P1

    def f13():
        P_e1 = 3 * f10() * f10() * r_1 * 0.001
        return P_e1

    def f14():
        P_e2 = 3 * f11() * f11() * r_2_shtrih * 0.001
        return P_e2

    def f15():
        P_dob = 0.005 * f12()
        return P_dob

    def f16():
        sumP = f15() + f13() + f14() + (P_st + P_meh) * 10 ** -3
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
    print(i, "|\t", calculate_Table_1(i, s_nom))

####* __57__
s_kr = 1
nu_rasch = 115
ro_115 = ro_115_al
b_c__na__b_p = 1
f_1 = f
h_c = h_p_2 - (h_sh_r[h] + h_sh_shtrih)
Ksi = 63.61 * h_c * 10 ** -3 * math.sqrt(s_kr)
phi = phi_func(Ksi)
h_r = h_c / (1 + phi)
b_r = b_1_r - ((b_1_r - b_2_r) / h_1) * h_r
q_r = (math.pi * b_1_r ** 2) / 8 + ((b_1_r + b_r) / 2) * (h_r - (b_1_r / 2))
k_r = q_c / q_r
r_c_shtrih = r_c
K_R = 1 + (r_c_shtrih / r_2) * (k_r - 1)
r_2_Ksi_shtrih = K_R * r_2_shtrih
print(Back.BLUE + "Пункт: 57")
print("nu_rasch =", nu_rasch)
print("ro_115 =", ro_115)
print("b_c__na__b_p =", b_c__na__b_p)
print("f_1 =", f_1)
print("h_c =", h_c)
print("Ksi =", Ksi)
print("phi =", phi)
print("h_r =", h_r)
print("b_r =", b_r)
print("q_r =", q_r)
print("k_r =", k_r)
print("r_c_shtrih =", r_c_shtrih)
print("K_R =", K_R)
print("r_2_Ksi_shtrih =", r_2_Ksi_shtrih, end='\n\n')

####* __58__
K_d = phi_shtrih_func(Ksi)
delta_Lambda_p_2_Ksi = (h_0 / (3 * b_1_r) * (1 - (math.pi * b_1_r ** 2) / (8 * q_c)) ** 2 + 0.66 - b_sh_2[h] / (
        2 * b_1_r)) * (1 - K_d)
Lamda_p_2_Ksi = Lamda_p_2 - delta_Lambda_p_2_Ksi
K_x = (Lamda_p_2_Ksi + Lamda_l_2 + Lamda_d_2) / (Lamda_p_2 + Lamda_l_2 + Lamda_d_2)
X_2__Ksi_shtrih = X_2_shtrih * K_x
print(Back.BLUE + "Пункт: 58")
print("K_d =", K_d)
print("delta_Lambda_p_2_Ksi =", delta_Lambda_p_2_Ksi)
print("Lamda_p_2_Ksi =", Lamda_p_2_Ksi)
print("K_x =", K_x)
print("X_2__Ksi_shtrih =", X_2__Ksi_shtrih, end='\n\n')

####* __59__
x_1_2_p = k_nu * X_1_2
c_1_p = 1 + (X_1 / x_1_2_p)
print(Back.BLUE + "Пункт: 59")
print("x_1_2_p =", x_1_2_p)
print("c_1_p =", c_1_p, end='\n\n')

####* __60__
R_p = r_1 + c_1_p * (r_2_Ksi_shtrih / s_kr)
X_p = X_1 + c_1_p * X_2__Ksi_shtrih
I_2_p_shtrih = U / math.sqrt(R_p ** 2 + X_p ** 2)
I_1_p = I_2_p_shtrih * (math.sqrt(R_p ** 2 + (X_p + x_1_2_p) ** 2) / (c_1_p * x_1_2_p))
print(Back.BLUE + "Пункт: 60")
print("R_p =", R_p)
print("X_p =", X_p)
print("I_2_p_shtrih =", I_2_p_shtrih)
print("I_1_p =", I_1_p, end='\n\n')

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
        return K_R

    def f6():
        return r_2_Ksi_shtrih

    def f7():
        return K_d

    def f8():
        return Lamda_p_2_Ksi

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
        return I_1_p

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
    print(i, "|\t", calculate_Table_2(i, s_nom))

####* __61__
k_beta_shtrih = 1
C_N = 0.64 + 2.5 * math.sqrt(sigma / ((t_z_1 + t_z_2) * 10 ** 3))
k_y_1 = math.sin(beta_shtrih * (math.pi / 2))
print(Back.BLUE + "Пункт: 61")
print("k_beta_shtrih =", k_beta_shtrih)
print("C_N =", C_N)
print("k_y_1 =", k_y_1, end='\n\n')

####* Таблица 3
print(Back.BLUE + "Таблица 3")


def calculate_Table_3(numeration, s):
    def f1():
        return 1.4

    def f2():
        global F_p_avg
        F_p_avg = 0.7 * (((I_1_p * f1() * u_p) / a_harmonic) * (k_beta_shtrih + k_y_1 * k_ob * (Z_1 / Z_2)))
        return F_p_avg

    def f3():
        global B_Ph_sig
        B_Ph_sig = (f2() * 10 ** -6) / (1.6 * sigma * 10 ** -3 * C_N)
        return B_Ph_sig

    def f4():
        k_sig = k_sig_func(f3())
        return k_sig

    def f5():
        c_1 = (t_z_1 * 10 ** 3 - b_sh[h]) * (1 - f4())
        return c_1

    def f6():
        global Lamda_p_1_nas
        Lamda_p_1_nas = Lamda_p_1 - (((h_sh + 0.58 * h_k) / b_sh[h]) * (f5() / (f5() + 1.5 * b_sh[h])))
        return Lamda_p_1_nas

    def f7():
        global Lamda_d_1_nas
        Lamda_d_1_nas = f4() * Lamda_d_1
        return Lamda_d_1_nas

    def f8():
        global x_1_nas
        x_1_nas = X_1 * (Lamda_p_1_nas + Lamda_d_1_nas + Lamda_l_1) / (Lamda_p_1 + Lamda_d_1 + Lamda_l_1)
        return x_1_nas

    def f9():
        c_1_p = 1 + (f8() / x_1_2_p)
        return c_1_p

    def f10():
        global c_2
        c_2 = (t_z_2 * 10 ** 3 - b_sh_2[h]) * (1 - f4())
        return c_2

    def f11():
        global Lamda_p_2_Ksi_nas
        Lamda_p_2_Ksi_nas = Lamda_p_2_Ksi - (h_sh_shtrih / b_sh_2[h]) * (f10() / (f10() + b_sh_2[h]))
        return Lamda_p_2_Ksi_nas

    def f12():
        global Lamda_d_2_nas
        Lamda_d_2_nas = f4() * Lamda_d_2
        return Lamda_d_2_nas

    def f13():
        global x_2_Ksi_nas_shtrih
        x_2_Ksi_nas_shtrih = X_2_shtrih * (f11() + f12() + Lamda_l_2) / (Lamda_p_2 + Lamda_d_2 + Lamda_l_2)
        return x_2_Ksi_nas_shtrih

    def f14():
        global R_p_nas
        R_p_nas = r_1 + (1 + (f8() / x_1_2_p)) * (r_2_Ksi_shtrih / s_shtrih)
        return R_p_nas

    def f15():
        global X_p_nas
        X_p_nas = f8() + (1 + (f8() / x_1_2_p)) * f13()
        return X_p_nas

    def f16():
        global I_2_nas_shtrih
        I_2_nas_shtrih = U / math.sqrt(f14() ** 2 + f15())
        return I_2_nas_shtrih

    def f17():
        global I_1_nas
        I_1_nas = f16() * (math.sqrt(f14() ** 2 + (f15() + x_1_2_p) ** 2)) / ((1 + (f8() / x_1_2_p)) * x_1_2_p)
        return I_1_nas

    def f18():
        global k_nas_shtrih
        k_nas_shtrih = f17() / I_1_p
        return k_nas_shtrih

    def f19():
        global I_1_star
        I_1_star = f17() / I_1_nom
        return I_1_star

    def f20():
        global M_dot
        M_dot = (f16() / I2_shtrih) ** 2 * K_R * (s_nom / s_shtrih)
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

####################################################################################?
# print('h =', h)
# print("(15000 * k_e[4][0.2785]) / (kpd_4(15) * cosPhi_4(15)) =", (15000 * k_e[4][0.2785]) / (kpd_4(15) * cosPhi_4(15)))
# print("k_e[4][0.2785] =", k_e[4][0.2785])
# print("kpd_4(15) =", kpd_4(15))
# print("cosPhi_4(15) =", cosPhi_4(15))
# print("induction_4(D_a[160]) =", induction_4(0.272))
# print("A_4(D_a[160]) =", A_4(0.272))

# x_list = [x/1000 for x in range(-500000, 500000)]

# plt.plot(x_list, [p8_up(x) for x in x_list], color='blue', marker='o', markersize=3)
# plt.plot(x_list, [p8_down__p6_up(x) for x in x_list], color='brown', marker='o', markersize=3)
# plt.plot(x_list, [p6_down__p4_up(x) for x in x_list], color='gray', marker='o', markersize=3)
# plt.plot(x_list, [p2_up(x) for x in x_list], color='orange', marker='o', markersize=3)
# plt.plot(x_list, [p4_down(x) for x in x_list], color='blue', marker='o', markersize=3)
# plt.plot(x_list, [p2_down(x) for x in x_list], color='green', marker='o', markersize=3)

# plt.plot(x_list, [cosPHI_4(x) for x in x_list], color='red', marker='o', markersize=3)
# plt.plot(x_list, [induction_4(x) for x in x_list], color='red', marker='o', markersize=3)
# plt.plot(x_list, [KPD_4(x) for x in x_list], color='green', marker='o', markersize=3)

# plt.plot(x_list, [A_4(x) for x in x_list], color='green', marker='o', markersize=3)

# plt.plot(x_list, [t_z1__2_max(x) for x in x_list], color='green', marker='o', markersize=3)
# plt.plot(x_list, [t_z1__2_min(x) for x in x_list], color='green', marker='o', markersize=3)

# plt.plot(x_list, [AJ_4(x) for x in x_list], color='green', marker='o', markersize=3)

# plt.plot(x_list, [k_sk_shtrih_func(x) for x in x_list], color='blue', marker='o', markersize=3)

# plt.plot(x_list, [k_sig_func(x) for x in x_list], color='blue', marker='o', markersize=3)

plt.show()
####################################################################################?
