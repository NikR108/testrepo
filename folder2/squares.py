

# simple square class 


class Sqre:
    
    def __init__(self, side):
        
        self.side = side
        
        
    def area(self):
        
        return self.side * self.side
    
    def perim(self):
        
        return self.side * 4
    
    
s1 = Sqre(side=2)

print(s1.area())
print(s1.perim())