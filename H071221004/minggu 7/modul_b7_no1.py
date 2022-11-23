import re

string_s= input('masukkan string S :')
if len(string_s)==45:
    if re.match(r'[A-Za-z02468]', string_s[:40]):
        if re.match(r'[13579\s]', string_s[-5:]):
            print(True)
        else:
            print(False)
    else:
        print(False)
else:
    (False)

