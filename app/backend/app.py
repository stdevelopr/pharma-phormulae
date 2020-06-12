from flask import Flask, render_template, jsonify, request
from formulas_functions import *
from formulas_description import formulas
import os

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/formulas_ref")
def formulas_ref():

    return jsonify(formulas)


# @app.route("/base_peso")
# def base_peso():
#     mmbase = float(request.args.get('mmbase'))
#     mmsal = float(request.args.get('mmsal'))
#     qtcapsulas = int(request.args.get('qtcapsulas'))
#     pesocapsulas = float(request.args.get('pesocapsulas'))
#     msg = formulas['base_peso']['resp_result']
#     resp = base_peso_formula(mmbase,mmsal,qtcapsulas,pesocapsulas)
#     return jsonify(msg+str(resp))

@app.route("/dose_medicamento")
def dose_medicamento():
    dosequequero = float(request.args.get('dosequequero'))
    concentracaonofrasco = float(request.args.get('concentracaonofrasco'))
    msg = formulas['dose de diluição 2']['resp_result']
    resp = dose_medicamento_func(dosequequero, concentracaonofrasco)
    return jsonify(msg+str(resp))

@app.route("/dose_diluicao")
def dose_diluicao():
    dosequequero = float(request.args.get('dosequequero'))
    concentracaonofrasco = float(request.args.get('concentracaonofrasco'))
    mlnofrasco = float(request.args.get('mlnofrasco'))
    msg = formulas['dose de diluição']['resp_result']
    resp = dose_diluicao_func(dosequequero, concentracaonofrasco, mlnofrasco)
    return jsonify(msg+str(resp))

@app.route("/dose_insulina")
def dose_insulina():
    doseinsulina = float(request.args.get('doseinsulina'))
    qtsdias = float(request.args.get('qstdias'))
    uiampola = float(request.args.get('uiampola'))
    msg = formulas['dias insulina']['resp_result']
    resp = dose_insulina_func(doseinsulina, qtsdias, uiampola)
    return jsonify(msg+str(resp))



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', '5000'))