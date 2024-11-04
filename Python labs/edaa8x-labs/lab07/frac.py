def gcd(a: int, b: int) -> int:
        
    while b != 0:
        t = b
        b = a % b
        a = t
            
    return abs(a)



class Frac:
    
    def __init__(self, numer: int, denom: int) -> None:
        n = gcd(numer, denom)
        self.numer = numer // n
        self.denom = denom // n

    def add(self, other: 'Frac') -> 'Frac':
        
        numer_one = self.numer * other.denom
        numer_two = self.denom * other.numer
        
        denom = self.denom * other.denom
        numer = numer_one + numer_two
        
        return Frac(numer, denom)
    
    
    def sub(self, other: 'Frac') -> 'Frac':
        
                
        numer_one = self.numer * other.denom
        numer_two = self.denom * other.numer
        
        denom = self.denom * other.denom
        numer = numer_one - numer_two
        
        return Frac(numer, denom)
    
    def mul(self, other: 'Frac') -> 'Frac':
        return Frac(self.numer * other.numer, self.denom * other.denom)
    
    
    def div(self, other: 'Frac') -> 'Frac':
        return Frac(self.numer * other.denom, self.denom * other.numer)
    
    
    
    def __add__(self, other: 'Frac') -> 'Frac':
        return self.add(other)
    
    def __sub__(self, other: 'Frac') -> 'Frac':
        return self.sub(other)
    
    def __mul__(self, other: 'Frac') -> 'Frac':
        return self.mul(other)
    
    def __div__(self, other: 'Frac') -> 'Frac':
        return self.div(other)
      
    def __str__(self):
        return f'{self.numer}/{self.denom}'


x = Frac(1, 6)
y = Frac(1, 6)
z = x.add(y)
print(f"{x} + {y} = {z}")

print()

x = Frac(2, 3)
y = Frac(1, 6)
z = x.sub(y)
print(f"{x} - {y} = {z}") 

print()

x = Frac(2, 5)
y = Frac(3, 4)
z = x.mul(y)
print(f"{x} * {y} = {z}") 

print()

x = Frac(3, 7)
y = Frac(5, 2)
z = x.div(y)
print(f"{x} / {y} = {z}")


print()


x = Frac(1, 3)
y = Frac(1, 6)
z = x.add(x).add(y).add(y)
print(f'{x} + {x} + {y} + {y} = {z}')

print()


x = Frac(1, 3)
y = Frac(1, 6)
mul_result = y.mul(y)  
z = x.add(x).add(mul_result)
print(f'{x} + {x} + {y} * {y} = {z}')

print()

x = Frac(1, 3)
y = Frac(1, 3)
result = x + y
print(result)















