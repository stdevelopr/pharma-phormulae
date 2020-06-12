from flask import Flask, render_template, jsonify, request
from formulas_functions import base_peso_formula, calc_nada_formula
from formulas_description import formulas
import os

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/formulas_ref")
def formulas_ref():

    return jsonify(formulas)


@app.route("/base_peso")
def base_peso():
    mmbase = float(request.args.get('mmbase'))
    mmsal = float(request.args.get('mmsal'))
    qtcapsulas = int(request.args.get('qtcapsulas'))
    pesocapsulas = float(request.args.get('pesocapsulas'))
    msg = formulas['base_peso']['resp_result']
    resp = base_peso_formula(mmbase,mmsal,qtcapsulas,pesocapsulas)
    return jsonify(msg+str(resp))

@app.route("/calc_nada")
def formula_nada():
    msg = formulas['calc_nada']['resp_result']
    resp = calc_nada_formula()
    return jsonify(msg+resp)




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', '5000'))