import re

s = input ()

if len (s) == 45:
    if re.match (r"[A-za-z02468]+", s[:40]):
        if re.match(r"[13579]", s[-5]):
            print ("True")
        else:
            print ("False")
    else:
        print ("False")
else:
    print ("False")