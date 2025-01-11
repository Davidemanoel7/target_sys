# 4. Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# SP - R$67.836,43
# RJ - R$36.678,66
# MG - R$29.229,88
# ES - R$27.165,48
# Outros - R$19.849,53
# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

import json

def read_json( filepath: str ):
    try:
        with open( filepath, 'r', encoding='utf-8' ) as j:
            data = json.load( j )
            for d in data:
                d["valor"] = float( d["valor"].replace('.', '').replace(',', '.') )
            
            # if "valor" in data:
            #     valor_str = data["valor"]
            #     valor_float = float( valor_str.replace('.', '').replace(',', '.') )
            #     data["valor"] = valor_float

            return data

    except FileNotFoundError:
        print(f"Erro ao tentar abrir o arquivo. {filepath} Arquivo não encontrado")
        return []
    except json.JSONDecodeError as err:
        print(f"Erro ao decodificar o arquivo JSON: {err}")
        return []

def percentual_participacao( dados: json ) -> dict:
    dict_participacao = {  }

    total = 0.0

    for d in dados:
        dict_participacao.update({ d.get("estado") : 0 })    
        total += d.get("valor")
    
    for d in dados:
        percent_part = float(( d.get("valor")/total ) * 100)
        dict_participacao.update({ d.get("estado") : round( percent_part,2 ) })
    
    
    return dict_participacao

dados = read_json( "q4.json" )

if dados:
    participacao = percentual_participacao( dados )

    print("Percentual de Participação:\n")
    for p in participacao:
        print(f"{p} - { participacao[p] }")