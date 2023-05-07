import math


class ThermalCalculation:
    delta_nu_pov_1 = delta_nu_iz_p_1 = delta_nu_iz_l_1 = delta_nu_pov_l_1 =delta_nu_1_shtrih\
        = delta_gamma_v = delta_nu_1 = teta_v_shtrih = Q_v = 0

    def __init__(self, K, k_ro, P_e_1, P_st_osn, D, l_1, a_1, Z_1, P_p_1, b_iz_p_1, lambda_ekv, b_1, b_2,
                 lambda_ekv_shtrih, l_l_1, b_iz_l_1, h_p_1, l_vbl, l_avg_1, sum_P, P_e_2, P_meh, s_kor, a_v,
                 m_shtrih, n, D_a):
        # пункт 64
        P_e_p_1_shtrih = k_ro * P_e_1 * ((2 * l_1) / l_avg_1)
        self.delta_nu_pov_1 = K * ((P_e_p_1_shtrih + P_st_osn) / math.pi * D * l_1 * a_1)
        # пункт 65
        self.delta_nu_iz_p_1 = (P_e_p_1_shtrih / (Z_1 * P_p_1 * l_1)) * (
                (b_iz_p_1 / lambda_ekv) + ((b_1 + b_2) / 16 * lambda_ekv_shtrih))
        # пункт 66
        P_l_1 = P_p_1
        P_e_l_1_shtrih = k_ro * P_e_1 * ((2 * l_l_1) / l_avg_1)
        self.delta_nu_iz_l_1 = (P_e_l_1_shtrih / (2 * Z_1 * P_l_1 * l_l_1)) * (
                (b_iz_l_1 / lambda_ekv) + (h_p_1 / 12 * lambda_ekv_shtrih))
        # пункт 67
        self.delta_nu_pov_l_1 = (K * P_e_l_1_shtrih) / (2 * math.pi * D * l_vbl * a_1)
        # пункт 68
        self.delta_nu_1_shtrih = ((self.delta_nu_pov_1 + self.delta_nu_iz_p_1) * 2 * l_1 + (
                    self.delta_nu_iz_l_1 + self.delta_nu_pov_l_1) * 2 * l_l_1) / l_avg_1
        # пункт 69
        summ_P_shtrih = sum_P + (k_ro - 1) * (P_e_1 + P_e_2)
        summ_P_v_shtrih = summ_P_shtrih - (1 - K) * (P_e_p_1_shtrih + P_st_osn) - 0.9 * P_meh
        self.delta_gamma_v = summ_P_v_shtrih / (s_kor * a_v)
        # пункт 70
        self.delta_nu_1 = self.delta_nu_1_shtrih + self.delta_gamma_v
        # пункт 71
        k_m = m_shtrih * math.sqrt((n / 100) * D_a)
        self.teta_v_shtrih = 0.6 * D_a ** 3 * (n / 100)
        self.Q_v = k_m * summ_P_shtrih / (1100 * self.delta_gamma_v)
