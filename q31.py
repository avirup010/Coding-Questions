#Polar Coordinates in Python
# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

n = input()
print(abs(complex(n)))
print(cmath.phase(complex(n)))
