import re

txt = "O rato roeu a roupa do rei de roma. Que rato danado!"
lista = []

x = re.search("rato",txt)
'''
if x:
    print("Padrao detectado", x.span())
else:
    print("Padrao nao detectado")
'''

for match in re.finditer("r[a-z]+o",txt):

    if x:
        print("Padrao detectado", match.span())
        lista.append(match.span())
    else:
        print("Padrao nao detectado")

print("Numero de deteccoes:",len(lista))

