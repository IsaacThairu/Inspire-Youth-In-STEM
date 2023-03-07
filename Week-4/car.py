#week-4/car.py
class car:
 
    def __init__(self, make, model, year_of_man, engine_capacity,) :
         self.model= model
         self.make = make
         self.year=year_of_man
         self.engine_capacity=engine_capacity
#getters : get the attributes        
def _get_model(self) :
     return self.model

def _get_make(self) :
     return self.make

def _get_year(self) :
     return self.year_of_man

def _get_make(self) :
     return self.make

 #setters:set the attributes
def set_model(self,model):
       self.model=model

def set_model(self,make):
     self.make=make

     def set_model(self,year_of_manufacture):
          self.year_of_manufacture=year_of_manufacture

#objects :insance of the class
car1=car("GTR","nissan",2004,2500)
car2=car("supra","toyota",2007,3200)
car3=car("rx-7","mazda",2009,2800)

print(car1.get_model())
print(car1.get_year())

print(car2.get_model())
print(car2.get_year())

print(car3.get_model())
print(car3.get_year())

print(car1.get_year())
print(car3.get_year())

