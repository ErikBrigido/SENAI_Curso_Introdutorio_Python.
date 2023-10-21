#Crie um dicionário que represente um 
#dicionário de sinônimos. Em seguida, 
#peça ao usuário para digitar uma palavra e, 
#se a palavra estiver no dicionário, 
#mostre o seu sinônimo.


dicionario = {1: 'porta', 2: 'janela', 3: 'telhado', 4: 'portão'}

a = int(input('Digite aqui o número correspondente ao objeto que deseja: '))

if a in dicionario:
    acesso = dicionario[a]
    print(f'O item que deseja é o(a) {acesso} !')
else:
    print('Número do objeto não correspondente !')

    #crie um dicionário com 5 letras, e acesse 
#o 3º indice

estrelas = {1:'*',2:'**',3:'***',4:'****',5:'*****'}

acesso1 = estrelas [3]

print(acesso1)