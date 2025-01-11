# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

def read_json( filepath: str ):
    try:
        with open( filepath, 'r', encoding='utf-8' ) as j:
            data = json.load( j )
            return data
    except FileNotFoundError:
        print(f"Erro ao tentar abrir o arquivo. {filepath} Arquivo não encontrado")
        return []
    except json.JSONDecodeError as err:
        print(f"Erro ao decodificar o arquivo JSON: {err}")
        return []


def get_menor_valor_mensal( data: json ):
    values = []
    for d in data:
        values.append( d.get("valor") )

    return min(values)

def get_maior_valor_mensal( data: json ):
    values = []
    for d in data:
        values.append( d.get("valor") )

    return max(values)

def get_media_valor_mensal( data: json ) -> float:
    count = 0
    total_sum = 0
    for d in data:
        total_sum += d.get("valor")
        count += 1

    return total_sum/count

def get_count_sup_media_mensal( data: json, media: float ):
    qnt_dias = 0
    for d in data:
        if ( d.get("valor") > media):
            qnt_dias += 1
    return qnt_dias


dados = read_json( "q3.json" )

media_mensal = get_media_valor_mensal( dados )
qnt_dias = get_count_sup_media_mensal( dados, media_mensal )

if dados:
    print(f"Menor valor mensal: {get_menor_valor_mensal( dados )}")
    print(f"Maior valor mensal: {get_maior_valor_mensal( dados )}")
    print(f"Tivemos {qnt_dias} dias em que o valor de faturamento diário foi superior à média mensal {media_mensal}")