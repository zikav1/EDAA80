import random

# Laboration 1: apporximera en matematisk konstant (pi)

n = 0

for k in range(1000000):
    x = random.random()
    y = random.random()
    
    if x**2 + y**2 < 1:
        n = n + 1


ratio = n / 1000000
print(4*ratio)
    