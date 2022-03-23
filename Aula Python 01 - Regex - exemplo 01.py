import re

txt = "Os melhores engenheiros são do Brasil"
x = re.search("^Os.*Brasil$", txt)

if x:
    print("Padrão detectado!")
else:
    print("Padrão nao detectado!")