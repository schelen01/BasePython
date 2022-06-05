#Laço de repetição com While
import math


contador =1
while contador <=5:
    print("Olá mundo")
    contador =contador +1

#Laço com for
for item in [1,3,6,2,5]:
    print(item)

#Posso pedir para o for executar a funão 5x e mostrar os números ao quadrado
for item in range(5):
     print(item**2)

# def é para função em Python
def calculo_imc(peso, altura):
    print(peso /altura ** 2)

calculo_imc(peso =69, altura= 1.60)

#Um exemplo simples de uma seleção binária usando a instrução ifelse é a seguinte:
n = 10
if n<0:
       print("Desculpe, o valor é negativo")
else:
   print(math.sqrt(n))

#elif
pontuacao =55
if pontuacao>= 90:
       print('A')
elif pontuacao>= 80:
   print('B')
elif pontuacao>= 70:
   print('C')
elif pontuacao>= 60:
   print('D')
else:
   print('F')

#Se quiséssemos criar uma lista dos primeiros 10 quadrados perfeitos, poderíamos usar uma instrução for:
listaQuadrados=[]
for x in range(1,11):
    listaQuadrados.append(x*x)
   
listaQuadrados
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#podemos fazer a mesma coisa em uma única etapa:
listaQuadrados=[x*x for x in range(1,11)]
listaQuadrados

#Para que apenas determinados itens sejam adicionados:
listaQuadrados=[x*x for x in range(1,11) if x%2 != 0]
listaQuadrados
#[1, 9, 25, 49, 81]

#função UpperCase
[letra.upper() for letra in 'estruturas' if letra not in 'aeiou']
#['S', 'T', 'R', 'C', 'T', 'R', 'S']
