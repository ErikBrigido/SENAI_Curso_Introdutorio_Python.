#1 -  Crie uma tupla chamada frutas com pelo menos 5 frutas diferentes. Em seguida, acesse e imprima o terceiro elemento da tupla.

frutas = ('banana','maça','uva','pêra','limão')
print(frutas[2])

#2 - Crie uma tupla chamada `numeros` com alguns números inteiros. Em seguida, converta essa tupla em uma lista e imprima a lista resultante.

numeros = (2,4,6,8,10)
lista = list(numeros)

print(lista)

#3 - Crie uma tupla chamada `meses` com os nomes dos meses do ano até Setembro. Use um loop `for` para imprimir cada mês em uma linha separada.

meses = ("janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro")

for i in meses:
    print(i)

#4 - Crie uma lista chamada notas com algumas notas de alunos. Em seguida, converta essa lista em uma tupla e imprima a tupla resultante.

notas = [5,6,7,8,10]
tupla = tuple(notas)

print(tupla)

#5 - Crie uma lista chamada ponto que represente as coordenadas (x, y) de um ponto. 
#Em seguida, desempacote os elementos da lista em duas variáveis separadas (x e y) e imprima os valores.

ponto = [2, 5]

x, y = ponto

print ("A cordenada X é :", x)
print ("A coordenada y é :", y)