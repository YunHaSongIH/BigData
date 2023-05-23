import re

p = re.compile("(the)+")
m = p.findall("Lorem Ipsum has been the industry's standard dummy text ever since the 1500s")
print(m) 
