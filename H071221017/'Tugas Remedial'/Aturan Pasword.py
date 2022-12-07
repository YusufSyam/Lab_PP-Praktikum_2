import re

def validasi(n):
    p = r'^NPX[a-z5]{1,6}NPX$'
    if re.search(p,n):
        print("Valid")
    else:
        print("Tidak Valid")
              
validasi(input())