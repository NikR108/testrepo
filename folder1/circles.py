

# simple circle shape class 

import math as m
class circ:
    
    def __init__(self, radius):
        self.radius = radius
        
        
    def area(self):
        return m.pi * self.radius * self.radius
    
    def perim(self):
        return 2 * m.pi * self.radius
    
    
    
c1 = circ(1)

print(c1.area())
print(c1.perim())