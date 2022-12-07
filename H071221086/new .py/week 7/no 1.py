import re

#untuk menginput string yang kita ingin masukkan
string_s = input(' ')
print(len(string_s))

#kondisi awal dan akhir
awal = r'[0?2?4?6?8?a-z?A-Z?]'
akhir = r'[1?3?5?7?9? ?]'

#program mencari 45 string atau mengecek 45 string
result1 = re.findall(akhir, string_s[0:40])
result2 = re.findall(awal, string_s[40:45])
print(result1, result2)
if result1:
    print('false')
    exit()
elif result2:
    print('false')
    exit()
if len (string_s) == 45:
    print('true')
else:
    print('false')
    exit()