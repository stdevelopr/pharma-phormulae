formulas = {
    # nome que aparece no index
    "dose de diluição 2": {
        # nome que aparece no topo da tela
        "name": "Quantidade de medicamento",
        # descrição da formula
        "description": "Calcula a quantidade de medicamento em mililitros a ser pego",
        # uma lista com as variaveis e a descrição
        "variables": [{
            "dosequequero":{
                "description":"Digite a dose que gostaria de pegar: "
            }}, 
            {"concentracaonofrasco":{
                "description":"Digite a concentração no frasco em gramas por ml: "
            }}
        ],
        # nome da função que vai fazer o calculo no python
        "function_name": "dose_medicamento",
        # mensagem para exibir no resultado
        "resp_result": "A quantidade de medicamento que você deve pegar em mililitros é: "
    },
    "dose de diluição": {
        "name": "Dose diluição",
        "description": "Calcula a quantidade de medicamento a ser pego",
        "variables": [{
            "dosequequero":{
                "description":"Digite a dose que foi prescrita, em gramas: "
            }},
            {
            "concentracaonofrasco":{
                "description":"Digite a concentração da substância que você tem, em gramas: "
            }},
            {
            "mlnofrasco":{
                "description":"Digite quantos militros de diluente vai usar: "
            }}
        ],
        "function_name": "dose_diluicao",
        "resp_result": "A quantidade de medicamento que você deve pegar em mililitros é: "
    },
     "dias insulina": {
        "name": "Dias insulina",
        "description": "Calcula a quantidade de que vai durar a ampola de insulna",
        "variables": [{
            "doseinsulina":{
                "description":"Digite a quantidade diária de insulina: "
            }},
            {
            "qstdias":{
                "description":"Digite quantos dias o paciente vai tomar este medicamento: "
            }},
            {
            "uiampola":{
                "description":"Digite quantas U.I tem na ampola: "
            }}
        ],
        "function_name": "dose_insulina",
        "resp_result": "A ampola de insulina vai durar (em dias): "
    }
}