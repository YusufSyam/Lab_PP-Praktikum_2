import re

string = input("Masukkan String S : ")
match = re.search("[02468a-zA-Z]{40}[13579 ]{5}", string)

if match:
    print("True")
else:
    print("False")