import math

from matplotlib import pyplot as plt

from calculate import ro_115_al, f, k_beta_shtrih, a_harmonic
from func import phi_func, phi_shtrih_func, k_del_func, LinearInterpolation, SplineCubicInterpolate, Lagrange

class table1:
    a_shtrih = a = b = b_shtrih = r_2_shtrih = U = I_0_a = I_nu = C_1 = r_1 = P_st = P_meh = 0
    s_shtrih = 0

    def __init__(self, _a, _a_shtrih, _r_2_shtrih, _b, _b_shtrih, _U, _I_0_a, _I_nu, _C_1, _r_1, _P_st, _P_meh):
        self.a_shtrih = _a_shtrih
        self.a = _a
        self.b = _b
        self.b_shtrih = _b_shtrih
        self.r_2_shtrih = _r_2_shtrih
        self.U = _U
        self.I_0_a = _I_0_a
        self.I_nu = _I_nu
        self.C_1 = _C_1
        self.r_1 = _r_1
        self.P_st = _P_st
        self.P_meh = _P_meh

    def setS(self, s):
        self.s_shtrih = s

    def f1_1(self):
        return (self.a_shtrih * self.r_2_shtrih) / self.s_shtrih

    def f2_1(self):
        R = self.a + ((self.a_shtrih * self.r_2_shtrih) / self.s_shtrih)
        return R

    def f3_1(self):
        X = self.b + ((self.b_shtrih * self.r_2_shtrih) / self.s_shtrih)
        return X

    def f4_1(self):
        Z = math.sqrt(self.f2_1() * self.f2_1() + self.f3_1() * self.f3_1())
        return Z

    def f5_1(self):
        I2_2shtriha = self.U / self.f4_1()
        return I2_2shtriha

    def f6_1(self):
        cosPhi2_shtrih = self.f2_1() / self.f4_1()
        return cosPhi2_shtrih

    def f7_1(self):
        sinPhi2_shtrih = self.f3_1() / self.f4_1()
        return sinPhi2_shtrih

    def f8_1(self):
        I_1a = self.I_0_a + self.f5_1() * self.f6_1()
        return I_1a

    def f9_1(self):
        I_1p = self.I_nu + self.f5_1() * self.f7_1()
        return I_1p

    def f10_1(self):
        I1 = math.sqrt(self.f8_1() * self.f8_1() + self.f9_1() * self.f9_1())
        return I1

    def f11_1(self):
        global I2_shtrih
        I2_shtrih = self.C_1 * self.f5_1()
        return I2_shtrih

    def f12_1(self):
        P1 = 3 * self.U * self.f8_1() * 0.001
        return P1

    def f13_1(self):
        P_e1 = 3 * self.f10_1() * self.f10_1() * self.r_1 * 0.001
        return P_e1

    def f14_1(self):
        P_e2 = 3 * self.f11_1() * self.f11_1() * self.r_2_shtrih * 0.001
        return P_e2

    def f15_1(self):
        P_dob = 0.005 * self.f12_1()
        return P_dob

    def f16_1(self):
        sumP = self.f15_1() + self.f13_1() + self.f14_1() + (self.P_st + self.P_meh) * 10 ** -3
        return sumP

    def f17_1(self):
        P2 = self.f12_1() - self.f16_1()
        return P2

    def f18_1(self):
        eta = 1 - (self.f16_1() / self.f12_1())
        return eta

    def f19_1(self):
        cosPhi = self.f8_1() / self.f10_1()
        return cosPhi

    def calculateTable(self, numeration, s):
        self.s_shtrih = s
        if numeration == 1:
            return self.f1_1()
        else:
            pass
        if numeration == 2:
            return self.f2_1()

        else:
            pass
        if numeration == 3:
            return self.f3_1()
        else:
            pass
        if numeration == 4:
            return self.f4_1()
        else:
            pass
        if numeration == 5:
            return self.f5_1()
        else:
            pass
        if numeration == 6:
            return self.f6_1()
        else:
            pass
        if numeration == 7:
            return self.f7_1()
        else:
            pass
        if numeration == 8:
            return self.f8_1()
        else:
            pass
        if numeration == 9:
            return self.f9_1()
        else:
            pass
        if numeration == 10:
            return self.f10_1()
        else:
            pass
        if numeration == 11:
            return self.f11_1()
        else:
            pass
        if numeration == 12:
            return self.f12_1()
        else:
            pass
        if numeration == 13:
            return self.f13_1()
        else:
            pass
        if numeration == 14:
            return self.f14_1()
        else:
            pass
        if numeration == 15:
            return self.f15_1()
        else:
            pass
        if numeration == 16:
            return self.f16_1()
        else:
            pass
        if numeration == 17:
            return self.f17_1()
        else:
            pass
        if numeration == 18:
            return self.f18_1()
        else:
            pass
        if numeration == 19:
            return self.f19_1()
        return -1


class table2:
    h_c = h_p_2 = h_sh = h_sh_shtrih = b_1_r = b_2_r = h_1 = q_c = r_c = U = r_1 = r_2 = r_2_shtrih = h_0 = b_sh_2 = Lamda_p_2 = Lamda_l_2 = Lamda_d_2 = X_2_shtrih = x_1_2_p = c_1_p = X_1 = 0
    s_shtrih = 0

    def __init__(self, _h_c, _h_p_2, _h_sh, _h_sh_shtrih, _b_1_r, _b_2_r, _h_1, _q_c, _r_c, _U, _r_1, _r_2, _r_2_shtrih, _h_0, _b_sh_2, _Lamda_p_2, _Lamda_l_2, _Lamda_d_2, _X_2_shtrih, _x_1_2_p, _c_1_p, _X_1):
        self.h_p_2 = _h_p_2
        self.h_sh = _h_sh
        self.h_sh_shtrih = _h_sh_shtrih
        self.b_1_r = _b_1_r
        self.b_2_r = _b_2_r
        self.h_1 = _h_1
        self.q_c = _q_c
        self.r_c = _r_c
        self.U = _U
        self.r_1 = _r_1
        self.r_2 = _r_2
        self.r_2_shtrih = _r_2_shtrih
        self.h_0 = _h_0
        self.b_sh_2 = _b_sh_2
        self.Lamda_p_2 = _Lamda_p_2
        self.Lamda_l_2 = _Lamda_l_2
        self.Lamda_d_2 = _Lamda_d_2
        self.X_2_shtrih = _X_2_shtrih
        self.h_c = _h_c
        self.x_1_2_p = _x_1_2_p
        self.c_1_p = _c_1_p
        self.X_1 = _X_1

    def setS(self, s):
        self.s_shtrih = s

    def f1_2(self):
        return 63.61 * self.h_c * 10 ** -3 * math.sqrt(self.s_shtrih)

    def f2_2(self):
        return phi_func(self.f1_2())

    def f3_2(self):
        return self.h_c / (1 + self.f2_2())

    def f4_2(self):
        b_r = self.b_1_r - ((self.b_1_r - self.b_2_r) / self.h_1) * self.f3_2()
        q_r = (math.pi * self.b_1_r ** 2) / 8 + ((self.b_1_r + b_r) / 2) * (self.f3_2() - (self.b_1_r / 2))
        return self.q_c / q_r

    def f5_2(self):
        return 1 + (self.r_c / self.r_2) * (self.f4_2() - 1)

    def f6_2(self):
        return self.f5_2() * self.r_2_shtrih

    def f7_2(self):
        return phi_shtrih_func(self.f1_2())

    def f8_2(self):
        delta_Lambda_p_2_Ksi = (self.h_0 / (3 * self.b_1_r) * (1 - (math.pi * self.b_1_r ** 2) / (8 * self.q_c)) ** 2 + 0.66 - self.b_sh_2 / (2 * self.b_1_r)) * (1 - self.f7_2())
        return self.Lamda_p_2 - delta_Lambda_p_2_Ksi

    def f9_2(self):
        return (self.f8_2() + self.Lamda_l_2 + self.Lamda_d_2) / (self.Lamda_p_2 + self.Lamda_l_2 + self.Lamda_d_2)

    def f10_2(self):
        return self.f9_2() * self.X_2_shtrih

    def f11_2(self):
        return self.r_1 + self.c_1_p * (self.f6_2() / self.s_shtrih)

    def f12_2(self):
        return self.X_1 + self.c_1_p * self.f10_2()

    def f13_2(self):
        I_2_p_shtrih = self.U / math.sqrt(self.f11_2() ** 2 + self.f12_2() ** 2)
        return I_2_p_shtrih

    def f14_2(self):
        I_1_p = self.f13_2() * (math.sqrt(self.f11_2() ** 2 + (self.f12_2() + self.x_1_2_p) ** 2) / (self.c_1_p * self.x_1_2_p))
        return I_1_p



    def calculateTable(self, numeration, s):
        self.setS(s)
        if numeration == 1:
            return self.f1_2()
        else:
            pass
        if numeration == 2:
            return self.f2_2()

        else:
            pass
        if numeration == 3:
            return self.f3_2()
        else:
            pass
        if numeration == 4:
            return self.f4_2()
        else:
            pass
        if numeration == 5:
            return self.f5_2()
        else:
            pass
        if numeration == 6:
            return self.f6_2()
        else:
            pass
        if numeration == 7:
            return self.f7_2()
        else:
            pass
        if numeration == 8:
            return self.f8_2()
        else:
            pass
        if numeration == 9:
            return self.f9_2()
        else:
            pass
        if numeration == 10:
            return self.f10_2()
        else:
            pass
        if numeration == 11:
            return self.f11_2()
        else:
            pass
        if numeration == 12:
            return self.f12_2()
        else:
            pass
        if numeration == 13:
            return self.f13_2()
        else:
            pass
        if numeration == 14:
            return self.f14_2()
        else:
            pass
        return -1


class table3:
    C_N = k_y_1 = u_p = k_ob = X_1 = Z_1 = Z_2 = delta = t_z_1 = b_sh = h_sh = Lamda_p_1 = Lamda_d_1 = Lamda_l_1 = x_1_2_p = t_z_2 = b_sh_2 = Lamda_p_2 = Lamda_l_2 = Lamda_d_2 = h_sh_shtrih = X_2_shtrih = r_1 = r_2_Ksi_shtrih = U = I_1_p = I_1_nom = I2_shtrih = s_nom = h_k = Lamda_p_2_Ksi = K_R = 0
    s_kr = count = 0
    table_2 = 0
    s_shtrih = 0

    def __init__(self, _C_N, _k_y_1, _u_p, _k_ob, _X_1, _Z_1, _Z_2, _delta, _t_z_1, _b_sh, _h_sh, _Lamda_p_1, _Lamda_d_1, _Lamda_l_1, _x_1_2_p, _t_z_2, _b_sh_2, _Lamda_p_2, _Lamda_l_2, _Lamda_d_2, _h_sh_shtrih, _X_2_shtrih, _r_1, _r_2_Ksi_shtrih, _U, _I_1_p, _I_1_nom, _I2_shtrih, _s_nom, _h_k, _Lamda_p_2_Ksi, _K_R, table_2_student):
        self.C_N = _C_N
        self.k_y_1 = _k_y_1
        self.u_p = _u_p
        self.k_ob = _k_ob
        self.X_1 = _X_1
        self.Z_1 = _Z_1
        self.Z_2 = _Z_2
        self.delta = _delta
        self.t_z_1 = _t_z_1
        self.b_sh = _b_sh
        self.h_sh = _h_sh
        self.Lamda_p_1 = _Lamda_p_1
        self.Lamda_l_1 = _Lamda_l_1
        self.Lamda_d_1 = _Lamda_d_1
        self.x_1_2_p = _x_1_2_p
        self.t_z_2 = _t_z_2
        self.b_sh_2 = _b_sh_2
        self.Lamda_p_2 = _Lamda_p_2
        self.Lamda_l_2 = _Lamda_l_2
        self.Lamda_d_2 = _Lamda_d_2
        self.h_sh_shtrih = _h_sh_shtrih
        self.X_2_shtrih = _X_2_shtrih
        self.r_1 = _r_1
        self.r_2_Ksi_shtrih = _r_2_Ksi_shtrih
        self.U = _U
        self.I_1_p = _I_1_p
        self.I_1_nom = _I_1_nom
        self.I2_shtrih = _I2_shtrih
        self.s_nom = _s_nom
        self.h_k = _h_k
        self.Lamda_p_2_Ksi = _Lamda_p_2_Ksi
        self.K_R = _K_R
        #s_kr = self.s_kr_calc()
        #print(s_kr)
        #print(self.calculateTable(20, s_kr))
        self.count_ = 0
        self.table_2 = table_2_student

    def setS(self, s):
        self.s_shtrih = s

    def f1_3(self):
        x_meow = [0.1, 0.2, 0.5, 0.8, 1]
        y_meow = [1.05, 1.1, 1.2, 1.3, 1.4]
        return LinearInterpolation(self.s_shtrih, x_meow, y_meow)

    def f2_3(self):
        return 0.7 * (((self.I_1_p * self.f1_3() * self.u_p) / a_harmonic) * (k_beta_shtrih + self.k_y_1 * self.k_ob * (self.Z_1 / self.Z_2)))

    def f3_3(self):
        return (self.f2_3() * 10 ** -6) / (1.6 * self.delta * 10 ** -3 * self.C_N)

    def f4_3(self):
        return k_del_func(self.f3_3())

    def f5_3(self):
        return (self.t_z_1 * 10 ** 3 - self.b_sh) * (1 - self.f4_3())

    def f6_3(self):
        return self.Lamda_p_1 - (((self.h_sh + 0.58 * self.h_k) / self.b_sh) * (self.f5_3() / (self.f5_3() + 1.5 * self.b_sh)))

    def f7_3(self):
        return self.f4_3() * self.Lamda_d_1

    def f8_3(self):
        return self.X_1 * (self.f6_3() + self.f7_3() + self.Lamda_l_1) / (self.Lamda_p_1 + self.Lamda_d_1 + self.Lamda_l_1)

    def f9_3(self):
        return 1 + (self.f8_3() / self.x_1_2_p)

    def f10_3(self):
        return ((self.t_z_2 * 10 ** 3) - self.b_sh_2) * (1 - self.f4_3())

    def f11_3(self):
        return self.Lamda_p_2_Ksi - (self.h_sh_shtrih / self.b_sh_2) * (self.f10_3() / (self.f10_3() + self.b_sh_2))

    def f12_3(self):
        return self.f4_3() * self.Lamda_d_2

    def f13_3(self):
        return self.X_2_shtrih * (self.f11_3() + self.f12_3() + self.Lamda_l_2) / (self.Lamda_p_2 + self.Lamda_d_2 + self.Lamda_l_2)

    def f14_3(self):
        return self.r_1 + (1 + (self.f8_3() / self.x_1_2_p)) * (self.table_2.calculateTable(6,self.s_shtrih) / self.s_shtrih)

    def f15_3(self):
        return self.f8_3() + (1 + (self.f8_3() / self.x_1_2_p)) * self.f13_3()

    def f16_3(self):
        return self.U / math.sqrt(self.f14_3() ** 2 + self.f15_3() ** 2 )

    def f17_3(self):
        return self.f16_3() * (math.sqrt(self.f14_3() ** 2 + (self.f15_3() + self.x_1_2_p) ** 2)) / (
                (1 + (self.f8_3() / self.x_1_2_p)) * self.x_1_2_p)

    def f18_3(self):
        return self.f17_3() / self.table_2.calculateTable(14,self.s_shtrih)

    def f19_3(self):
        return self.f17_3() / self.I_1_nom

    def f20_3(self):
        return (self.f16_3() / self.I2_shtrih) ** 2 * self.K_R * (self.s_nom / self.s_shtrih)

    def s_kr_calc(self):
        self.s_shtrih = 1
        s_kr = self.table_2.calculateTable(6,self.s_shtrih) / ((self.f8_3() / self.f9_3()) + self.f13_3())
        return s_kr

    def calculateTable(self, numeration, s):
        self.setS(s)
        if numeration == 1:
            return self.f1_3()
        else:
            pass
        if numeration == 2:
            return self.f2_3()

        else:
            pass
        if numeration == 3:
            return self.f3_3()
        else:
            pass
        if numeration == 4:
            return self.f4_3()
        else:
            pass
        if numeration == 5:
            return self.f5_3()
        else:
            pass
        if numeration == 6:
            return self.f6_3()
        else:
            pass
        if numeration == 7:
            return self.f7_3()
        else:
            pass
        if numeration == 8:
            return self.f8_3()
        else:
            pass
        if numeration == 9:
            return self.f9_3()
        else:
            pass
        if numeration == 10:
            return self.f10_3()
        else:
            pass
        if numeration == 11:
            return self.f11_3()
        else:
            pass
        if numeration == 12:
            return self.f12_3()
        else:
            pass
        if numeration == 13:
            return self.f13_3()
        else:
            pass
        if numeration == 14:
            return self.f14_3()
        else:
            pass
        if numeration == 15:
            return self.f15_3()
        else:
            pass
        if numeration == 16:
            return self.f16_3()
        else:
            pass
        if numeration == 17:
            return self.f17_3()
        else:
            pass
        if numeration == 18:
            return self.f18_3()
        else:
            pass
        if numeration == 19:
            return self.f19_3()
        else:
            pass
        if numeration == 20:
            return self.f20_3()
        else:
            pass

        return -1
