

# simple class for shapes 


class rect:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perim(self):
        return 2*(self.length + self.width)
    
    

r1 = rect(4, 2)

print(r1.area())
print(r1.perim())
