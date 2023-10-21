
#essa aqui é a função da qualculadora
def calculadora(operacao):
    x = float(input("Insira o primeiro número: "))
    y = float(input("Insira o segundo número: "))

    if operacao == 'soma':
        resultado = x + y
    elif operacao == 'subtracao':
        resultado = x - y
    elif operacao == 'divisao':
        resultado = x / y
    elif operacao == 'multiplicacao':
        resultado = x * y
#Retorno caso o usuario NÃO digite uma operação dentre as possiveis.
    else:
        resultado = None
        print("Operação inválida. Escolha entre soma, subtracao, divisao, multiplicacao ou potencia.")

    return resultado

#aqui o usuario vai inserir a operação que deseja, dentro das opções
operacao_desejada = input("Escolha a operação desejada (soma, subtracao, divisao, multiplicacao.: ")

#a variavel calculo 'chama' a funnçao calculadora e atribuiu ao parametro "operacao" a 'operacao desejada' que será inserida.
calculo = calculadora(operacao_desejada)

#Esse é o retorno do calculo, caso o usuario tenha digitado uma operação dentre as possiveis.
if calculo != None:
    print(f"O resultado da {operacao_desejada} é: {calculo}")