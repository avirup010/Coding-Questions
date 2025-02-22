#Incorrect Regex 

import re
T = int(input())
for _ in range(T):  
    try:
        print(bool(re.compile(input())))
    except:
        print('False')
