# Exercício 1: Verificação de Número Positivo

# Escreva um programa em Python que solicite ao 
# usuário um número inteiro e 
# verifique se o número é positivo, negativo ou zero. 
# Em seguida, exiba uma mensagem apropriada de acordo 
# com o resultado da verificação.

a = int(input("Digite um numero inteiro qualquer :"))

if a < 0:
    print(f"O numero {a} é negativo !")
elif a > 0:
    print(f"O numero {a} é positivo !")
else:
    print(f"O numero da variavel é {a}!")

# Exercício 2: Classificação de Triângulos

# Escreva um programa em Python que receba três comprimentos de lados de um triângulo e 
# determine se o triângulo 
# é equilátero, isósceles ou escaleno.

a = float(input("Digite um numero qualquer :"))
b = float(input("Digite um numero qualquer :"))
c = float(input("Digite um numero qualquer :"))

if a == b and b == c:
    print("Este tringulo é EQUILATERO !")
elif a == b and b != c:
    print("Este tringulo é ISOSCELES !")
else:
    print("Este trinagulo é ESCALENO!")

# Exercício 3: Verificação de Ano Bissexto

# Um ano é bissexto se for divisível por 4, exceto para anos que são divisíveis por 100. 
# No entanto, anos divisíveis por 400 
# também são bissextos. Escreva um programa em Python que solicite um ano ao usuário 
# e determine se é um ano bissexto ou não.

a = int(input("Digite aqui o ano :"))

if a % 4 == 0 and not a % 100 == 0:
    print("Esse ano É Bissexto !")
elif a % 400 == 0:
    print("Esse ano É Bissexto !")
else:
    print("Esse ano NÃO é Bissexto !")
    