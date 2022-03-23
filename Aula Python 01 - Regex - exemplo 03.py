#EXEMPLO FINDALL
import re

txt = "oi! teu pai tem boi? Foi o que pensei"

x = re.findall("oi",txt)

print(x)
print(len(x))