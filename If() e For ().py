#Senha

senha_digitada = input('Digite uma senha : ')
nome = input ("Digite seu nome : ")
senha = '1234'

if senha == senha_digitada and nome =='Camila':
    print("Acesse, você digitou corretamente")
else:
    print((f'Não pode acessar, porque voce digitou {senha_digitada} ou {nome} incorretamente.'))


# Crie uma condição para comparar idades: 45 e 18 -  QUAL É MENOR E QUAL É MAIOR?

idade1 = int(input("Digite aqui a sua idade :"))
idade2 = int(input("Digite aqui a sua idade :"))

if idade1 > idade2:
    print(f'{idade1} é maior que {idade2}')      
else:
    print(f'{idade1} é menor que {idade2}')

#Crie um sistema para permitir a verificação de menores em um show

pessoa = int(input("Digite aqui a sua idade:"))

 if pessoa >= 18:
    print ("Pode entrar maior de idade")
else:
    print("Proibida a entrada")

#Crie um sistema para permitir a verificação de menores em um show - Com FOR

capacidade_show = int(input("Digite aqui aqui a capacidade do Show ( 1 a 10) : "))

for i in range(capacidade_show):
    pessoa = int(input("Digite aqui a sua idade:"))
    if pessoa >= 18:
        print ("Pode entrar maior de idade")
    else:
        print("Proibida a entrada")

# Crie um algoritmo que permita a entrada de 3 notas de alunos, utilize o bloco de código if() para verificar se o aluno passou. Com FOR

quantidade_de_alunos = 3

for i in range(quantidade_de_alunos):
    nota = int(input("Digite aqui a nota doa aluno:"))
    if nota >= 6:
        print ("Aprovado !")
    else:
        print("Reprovado !")