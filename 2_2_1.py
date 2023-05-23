import re

p = re.compile("[a][a-z]*")
m = p.findall("abcd aa a")
print(m) 
