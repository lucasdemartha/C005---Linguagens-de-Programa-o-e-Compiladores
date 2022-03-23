#Linguagens de Programação e Compiladores
#Aula Python 01
'''
nome = "Lucas"
peso = 94.1
print("Meu nome é:",nome, "\nMeu peso é:", peso,"Kg")

print("\nTipo da variável nome:", type(nome))
print("Tipo da variável peso:", type(peso))
'''
'''
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))

print("---------------------------------")
print("Meu nome é:",nome, "\nMeu peso é:", peso,"Kg")

print("\nTipo da variável nome:", type(nome))
print("Tipo da variável peso:", type(peso))
'''

nome = "Lucas"
peso = 94.1
print("Meu nome é {} e meu peso é {}Kg".format(nome,peso))

#if
'''
if peso > 150:
    print("Peso pesado!")
elif peso > 90:
    print("Peso medio!")
else:
    print("Peso pena!")
'''

#FOR
#1. For tradicional (envolve indices)
#No Python o primeiro argumento é sempre Inclusive
#e o segundo Exclusive
'''
for i in range(1,11):
    print(i)
'''
#FOR EACH
#Criando uma lista no Python

lista = [1,2,3,4,5] #Coleção mutavel/posso add futuramente
print(lista)
tupla = (6,7,8,9,10) #Coleção imutavel/fixo n pode add mais
print(tupla)

for aux in lista:
    print(aux)
    