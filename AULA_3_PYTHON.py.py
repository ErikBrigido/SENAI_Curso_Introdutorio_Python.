# 1 - Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.

a = int(input("Digite aqui um numero inteiro:"))
b = a**2

print("O quadrado do numero",a,"é ",b)

#2 -Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.

c = input("Digite aqui o seu primeiro nome:")
d = input("Digite aqui o seu segundo nome:")

print(a + ' ' + b)

#3 - Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.

a = input("Digite aqui um numero:")
b = input ("Digite aqui um numero:")

print (a + ' '+ b)

#4 -Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.

a = int(input("Digite um numero inteiro para concatenção"))
b = 'Python'

print (b, a)

#5 - Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.

a = " Até 2050 o vasco será o maior do Brasil"

b = input("Digite aqui uma palavra :")

print(a,b)

#6 - Crie três variáveis para armazenar a quantidade de horas, minutos e segundos. Concatene esses valores para formar uma mensagem de tempo no formato "hh:mm:ss".

h = input("Digite aqui a hora:")
m = input("Digite aqui o minuto:")
s = input("Digite aqui o segundo :")

print(F'{h}:{m}:{s}')

#7 - Declare duas variáveis com números de telefone, incluindo um código de área e o número principal. Concatene esses valores para formar um número de telefone completo.

a = int(input("Digite aqui o seu DDD :"))
a1 = int(input("Digite aqui o numero de celular ( sem o 9 na frente ) :"))

print(f'({a})9{a1}')

#8 - Crie uma lista de ingredientes para uma receita. Use concatenação para formar uma única string que liste os ingredientes separados por vírgulas.

lista = [ "farinha", "ovo", "manteira"]

print(lista[0],",", lista[1],",", lista[2])

#9 - Peça ao usuário para digitar três adjetivos e armazene-os em variáveis. Em seguida, use essas palavras para criar uma frase concatenada que descreve algo interessante.

a = input("Digite um Adjetivo :")
b = input("Digite um Adjetivo :")
c = input("Digite um Adjetivo :")

print(f'Nossa que bolo {a}. Achei muito {b} a forma que fez ele. O Sabor esta {c}.')
