import re

a = str(input())
b = "^([a-zA-Z02468]{40}[13579\s]{5})"
c = re.match(b, a)

if c :
    print(True)
else :
    print(False)