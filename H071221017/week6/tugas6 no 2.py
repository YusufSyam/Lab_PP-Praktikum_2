a = str(input()); a = a + ".txt"
b = str(input()); b = b + ".txt"

try:
    with open(a, "r") as origin:
        x = origin.read()
except:
    print("\nGagal")
else:
  h = x.split("\n") 
  f = 0   
  for i in h:
    if len(i) > f:
      f = len(i)
  for i in range(len(h)):
    h[i] = " "*(f - len(h[i])) + h[i] +'\n'
    with open(b , "w") as copy :
      for i in h:
        copy.write(i)
  print("\nBerhasil")