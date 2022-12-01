# Program mengecek apakah sebuah inputan merupakan
# IPv4, IPv6 atau bukan keduanya

import re

regex_ipv4 = r'^(([0-1]?[\d][\d]?|[0-2]?[0-4][\d]|25[0-5]).){3}([0-1]?[\d][\d]?|2[0-4][\d]|25[0-5])$'
regex_ipv6 = r'(([\d,A-F,a-f]{1,4}?:){7})([\d,A-F,a-f]{1,4})$'

n = int(input(''))
list_address = []

for i in range(n):
    address = input('')
    list_address.append(address)

print() 

for x in list_address:
    ipv4 = re.search(regex_ipv4, x)
    if ipv4:
        print('IPv4')
    else:
        ipv6 = re.search(regex_ipv6, x)
        if ipv6:
            print('IPv6')
        else:
            print('Bukan IP Address')