import re

patterns= [r'\d{3}\.\d{3}\.\d{3}\.\d{2}\b', r'\w{1,4}\:\w{1,4}\:\w{1,4}\:\w{1,4}\:\w{1,4}\:\w{1,4}\:\w{1,4}\:']

n= int(input())
s= [input() for _ in range(n)]

for i in s:
  if bool(re.match(patterns[0], i)):
    print('IPv4')
  elif bool(re.match(patterns[1], i)):
    print('IPv6')
  else:
    print('Bukan IP Address')