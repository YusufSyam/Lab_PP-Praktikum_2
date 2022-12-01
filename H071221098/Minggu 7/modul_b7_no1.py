import re
ini_= input()
x = re.search("[\w^13579_]{40}[13579\s]{5}$",ini_)
print(True) if x else print (False)