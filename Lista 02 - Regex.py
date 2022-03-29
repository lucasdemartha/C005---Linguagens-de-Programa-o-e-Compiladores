import re

txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz"
lista = []

#Exercicio 1 

'''
x= re.search("sonhos",txt)

print(x)
'''

#Exercicio 2

'''
for match in re.finditer("[a-zA-ZçãÉé]*as",txt):
    lista.append(match.group())


print("Palavras:",lista)
'''

#Exercicio 3

'''
x = re.sub(r"(grande|maior)", "surreal", txt)
print(x)
'''

#Exercicio 4

'''
x= re.search("inspiração",txt)

print(x.span())
'''

#Exercicio 5
'''
for match in re.finditer(r"[a-zA-ZçãéÉ]{9,}",txt):
    lista.append(match.group())

print("Palavras:",lista)
'''

#Exercicio 6

'''
x = re.split(r"(\.|,)", txt)
print(x)
'''

#Exercicio 7

'''
for match in re.finditer(r"([a-zA-Zçã]*é|É[a-zAZçã]*)",txt):
    lista.append(match.group())

print("Palavras:",lista)
'''

#Exercicio 8

'''
for match in re.finditer(r"([a-zA-ZçãéÉ]+)",txt):
    lista.append(match.group())

print(lista)
print(len(lista))
'''