# 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

def desafio1( num: int ) -> int :
    indice: int = num
    soma: int = 0
    k: int = 0

    while ( k < indice ):
        k += 1
        soma += k
    return soma


result:int = desafio1( 13 )
print(result)