"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""

def fibonacci(num):
    #inicializo com os valores que sao padrão no inicio da sequencia
    a, b = 0, 1
    
    # verifica enquanto o numero atual da sequencia for menor q o que foi digitado
    while a <= num:
        # verifica se o numero digitado for igual ao numero atual, ele pertence a sequencia de fibonacci
        if a == num:
            return True
        # faz a atualização dos valores atuais paara o proximo valor da sequencia
        a, b = b, a + b
    
    # caso o numero digitado nao tenha sido encontrado na sequencia ele retorna false
    return False

# o usuario ira digitar um numero qualquer de sua preferencia
numero = int(input("Digite um numero para verificar se o mesmo pertence à sequencia de Fibonacci: "))

# verificar se o numero digitado pertence ou não a sequencia, para indicar qual saida é correta
if fibonacci(numero):
    print(f"O numero {numero} pertence à sequencia de Fibonacci.")
else:
    print(f"O numero {numero} não pertence à sequencia de Fibonacci.")
