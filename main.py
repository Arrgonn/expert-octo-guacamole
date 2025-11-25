import math

class MATH:
    def __init__(self, x, b): 
        self.x = x
        self.b = b 

    def floor(self): # ⌊x⌋ 
        return math.floor(self.x) 
        
    def mod(self): #xmod(b)
        y = math.floor(self.x/self.b) 
        z = self.b*y
        n = self.x-z
        print(f'Quotient (y): {y}, Produit (z): {z}, Reste (n): {n}')
        return n 

value = MATH(-50, 8)

print(f'Plancher de {value.x}: {value.floor()}') 
print(f'Reste de {value.x} mod {value.b}: {value.mod()}')