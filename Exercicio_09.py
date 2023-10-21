# Exercício 1: Escreva uma função que calcule 
# a soma dos números de 1 a N, 
# onde N é um número inteiro dado. 

n = int(input('Digite um numero até onde o calculo deve se estender :'))
tupla = tuple(range(1, n + 1))

soma = sum(tupla)
print (soma)

# Exercício 2: Escreva uma função que 
# conte quantas vezes uma letra 
# específica aparece em uma palavra.

n = input('Digite aqui UMA palavra :')

a = input ('Qual letra quer contar?')

b = n.count(a)

print(b)

###################################

palavra = input('digite ')

letra = input('letra ')

print(len([i for i in palavra 
                    if i == letra]))

# Exercício 3: Escreva uma função que calcule 
# o fatorial de um número 
# inteiro não negativo N.

intervalo_de_fatoração = int(input('Digite aqui um numero'))

tupla = tuple(range(1, intervalo_de_fatoração+1))
fatorial = 1
for i in tupla :
     fatorial *= i
print (fatorial)

# Exercício 4: Crie um Dicionário, 
# adicione elementos ao dicionário e os 
# mostre na tela.

dicionario = {}

dicionario = {1:'lanterna',2:'pilha',3:'abajur'}

dicionario['4']='tênis'

print(dicionario)


# Exerc´cio 5: Utilizando Dicionários, 
# que peça para o usuário 
# inserir o nome de três produtos 
# # de mercado e seus respectivos preços 
# e os mostre na tela.

# # Criar um dicionário para armazenar 
# produtos e preços
# produtos = {}

produtos = {}

for i in range(3):
    produto = input(f"Digite o nome do produto {i + 1}: ")
    preco = float(input(f"Digite o preço do produto {i + 1}: "))
    produtos[produto] = preco

print("Produtos e Preços:")
for produto, preco in produtos.items():
    print(f"{produto}: R$ {preco:.2f}")

