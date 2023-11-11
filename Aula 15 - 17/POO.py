# 1 - Crie uma classe chamada Cachorro com um atributo nome e um método 
# latir que imprima "Woof!" quando chamado. 
# Em seguida, crie um objeto da 
# classe Cachorro e chame o método latir.

# class Cachorro:
#     def __init__(self,name):
#         self.nome = name
    
#     def latir (self):
#             print('Woof!')

# dog = Cachorro("Dudu")

# dog.latir()

# 2Crie uma classe chamada Retangulo com atributos largura e 
# altura. Adicione um método chamado calcular_area que retorna a área do retângulo.

# class retangulo:
#      def __init__(self, largura, altura):
#           self.largura = largura
#           self.altura = altura

#      def calcular (self):
#           calculo = self.largura * self.altura
#           print(calculo)

# retangulo = retangulo(10, 10)

# calculo = retangulo.calcular()

# 3: Crie uma classe chamada Carro com um atributo chamado velocidade 
# (inicialmente 0). Em seguida, adicione um método chamado acelerar que aumenta a
# velocidade em 5 unidades a cada vez que é chamado.

class Carro:
     def __init__(self, velocidade):
        self.velocidade = velocidade

     def acelerar():
        for v in range (self.velocidade, 100,5):
            print(v)

vel = int(input("insira"))

carro = Carro(vel)

Carro.acelerar()


# 4 - Crie uma classe chamada Gato que herda da classe Cachorro do exercício anterior. 
#  O método latir da classe Cachorro deve ser substituído por um método miar na classe 
# Gato que imprime "Miau!".
