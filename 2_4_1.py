import re

p = re.compile("\w+t{2}\w+")
m = p.findall("stage total attribute attention")
print(m) 
