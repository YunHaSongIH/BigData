import re

p = re.compile("[^a-z]")
m = p.findall("AB ab a1 b1")
print(m) # 소문자 제외 모두 포함으로 
           # A,B,공백,공백,1,공백,1이 반환된다.
