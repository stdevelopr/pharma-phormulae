formulas = {
    # nome que aparece no index
    "base_peso": {
        # nome que aparece no topo da tela
        "name": "Fórmula base peso",
        # descrição da formula
        "description": "Fórmula para calcular...",
        # uma lista com as variaveis e a descrição
        "variables": [{
            "mmbase":{
                "description":"Digite a massa molecular da base:"
            }}, 
            {"mmsal":{
                "description":"Digite a massa molecular do sal:"
            }},
            {"qtcapsulas":{
                "description": "Quantidade de capsulas"
            }},
            {"pesocapsulas":{
                "description": "Peso das capsulas (mg)"
            }}
        ],
        # nome da função que vai fazer o calculo no python
        "function_name": "base_peso",
        # mensagem para exibir no resultado
        "resp_result": "A quantidade que voce deve pesar deste sal em mg: "
    },
    "calc_nada": {
        "name": "Faz nada",
        "description": "Fórmula que nao calcula nada...",
        "variables": [{
            "nada":{
                "description":"faz coisa nenhuma:"
            }
        }],
        "function_name": "calc_nada",
        "resp_result": "testando...."
    }
}