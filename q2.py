# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# n é o número que iremos calcular e verificar se faz parte ou não da sequencia...
def is_fibonacci_number(n):
    """
    Verifica se um número pertence à sequência de Fibonacci.
    :param n: Número a ser verificado.
    :return: Booleano indicando se o número pertence a sequência.
    """
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

# Entrada do usuário
n = int(input("Informe um número inteiro não negativo: "))

# Verificação e saída
if is_fibonacci_number(n):
    print(f"O número {n} pertence à sequência de Fibonacci.")
else:
    print(f"O número {n} NÃO pertence à sequência de Fibonacci.")

