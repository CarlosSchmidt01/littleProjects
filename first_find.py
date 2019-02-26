s = '..12345678910111213141516171820212223'


import re

l = [a.group() for a in re.finditer(r'(.)\1*', s)]

for i in l:
    if i.isalnum():
        if len(i)>1:
            print(i)
            break
