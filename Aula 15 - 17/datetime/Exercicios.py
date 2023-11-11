from datetime import datetime,timedelta


# 2 - Calcule e exiba a data e hora exatas daqui a 7 dias a partir de agora.
x = datetime.now()
y = x + timedelta(days=7)
print(y)


# 3 - Peça ao usuário para inserir um ano e, em seguida, exiba o ano atual.
x = input( "Insira aqui um ano : ")

y = datetime.now().year

print ( y )


# 4 - Calcule e exiba a data e hora atuais em um formato personalizado(utilize diretivas).

x = datetime.now()

y = datetime.strftime(x, "%y-%b-%a")

print ( y )