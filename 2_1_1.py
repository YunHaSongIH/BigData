import re

p = re.compile("[akl]")
m = p.findall("abcd name variable")
print(m) # abcd의 a, name 의 a, variable의 a,a,l 이 차례로 매치 되어 총 5개가 반환된다.

