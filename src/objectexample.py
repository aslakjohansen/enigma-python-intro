class Person:
    def __init__ (self, name):
        self.name = name
    
    def get_name (self): return self.name
    def set_name (self, name):
        self.name = name

def printname (self):
    print(self.name)

p = Person('Aslak')
print(p.get_name())

setattr(Person, 'printname', printname)
p.printname()
