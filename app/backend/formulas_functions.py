# Nesse arquivo vão ficar as funções que realizarão os cálculos


def base_peso_formula(mmbase:float, mmsal:float, qtcapsulas:int, pesocapsulas:float):
    "Essa função realiza o cálculo de..."
    fatordeequivalencia = mmsal/mmbase
    quantidadepesar =  (qtcapsulas * pesocapsulas) * fatordeequivalencia
    return quantidadepesar

def calc_nada_formula():
    return "OK"
