# Nesse arquivo vão ficar as funções que realizarão os cálculos


# def base_peso_formula(mmbase:float, mmsal:float, qtcapsulas:int, pesocapsulas:float):
#     "Essa função realiza o cálculo de..."
#     fatordeequivalencia = mmsal/mmbase
#     quantidadepesar =  (qtcapsulas * pesocapsulas) * fatordeequivalencia
#     return quantidadepesar

def dose_medicamento_func(dosequequero: float, concentracaonofrasco: float):
    resp = dosequequero / concentracaonofrasco
    return resp

def dose_diluicao_func(dosequequero: float, concentracaonofrasco: float, mlnofrasco: float):
    resp = (dosequequero*mlnofrasco) / concentracaonofrasco
    return resp

def dose_insulina_func(doseinsulina:float, qtsdias:float, uiampola:float):
    quantovaidurar = uiampola / (doseinsulina * qtsdias)
    return quantovaidurar
