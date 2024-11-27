import constants
import cortevigas
import pandas as pd
from flexvigas import flexion

def calculate(fc, fy, E, L, B, H, r, a, e, cm, sc, tipo):
    # Calcular Inercia de la viga
    Inertia = 1/12 * B * H**3 * (0.01**4)  # m4

    # Determinacion de qu:
    PPlosa = 2.5 * e * 0.01 * a
    PPviga = 2.5 * H * B * 0.01 * 0.01
    Qsc = a * sc * 0.001
    Qcm = a * cm * 0.001

    qu1 = 1.2 * (Qcm + PPlosa + PPviga) + 1.6 * Qsc
    qu2 = 1.4 * (Qcm + PPlosa + PPviga)

    qu = max(qu1, qu2)

    quLP = 2 * (Qcm + PPlosa + PPviga) + Qsc

    qINS = 1 * (Qcm + PPlosa + PPviga) + Qsc

    # Llenado de matriz de resultados
    M = ["Mi", "Mc", "Md"]
    V = ["Vi", "Vc", "Vd"]
    D = ["Di", "Dc", "Dd"]

    results = []

    m_results = ["Moment"]
    ro_rob_results = ["ρ /ρb [%]"]
    v_results = ["Shear"]
    du_results = ["Def. Long_term [cm]"]
    di_results = ["Def. Inst. [cm]"]

    ## MOMENTO Y RO ROB
    for col in range(3):
        # CALCULO MOMENTO
        mu = constants.res[tipo][M[col]] * qu * L ** 2
        f = flexion(H, B, r, fc, fy, mu, 0)
        # CALCULO CORTE
        vu = constants.res[tipo][V[col]] * qu * L
        corte = cortevigas.corte(B, H, r, fc, fy, vu, 0, 0.75)
        # Resultados momento:
        m_results.append([f"Mu = {round(mu, 1)} [ton m]", f"As = {f[0]} [cm²]", f"Asc = {f[1]} [cm²]"])
        # Resultados ro_rob
        ro_rob_results.append([f"{f[2]} %"])
        # Resultados de Corte
        if not corte == ["cambiar seccion"]:
            v_results.append([f"Vu = {round(vu, 1)} [ton]; Av = {corte[0]} [cm²/m]; s = {corte[1]} cm"])
        else:
            v_results.append([f"Vu = {round(vu, 1)} [ton]; change section"])
        # Resultados de def. largo plazo
        du = constants.res[tipo][D[col]] * quLP * L**4 / (E * Inertia) * 100
        du_results.append([f"{round(du, 1)}"])
        # Resultados de def. inst.
        di = constants.res[tipo][D[col]] * qINS * L**4 / (E * Inertia) * 100
        di_results.append([f"{round(di, 1)}"])
    results.append(m_results)
    results.append(ro_rob_results)
    results.append(v_results)
    results.append(du_results)
    results.append(di_results)

    columns = ["Value", "Left Side", "Center Side", "Right Side"]

    df = pd.DataFrame(results, columns=columns)

    return df, qu