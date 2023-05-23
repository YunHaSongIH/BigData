import re

p = re.compile("[^ ]*")
m = p.findall("angle square art port")
print(m) 

p = re.compile("[^ ]+")
m = p.findall("angle square art port")
print(m) 