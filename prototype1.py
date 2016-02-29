from copy import deepcopy

class Prototype:
  def __init__(self, example):
    self.example = example

  def clone(self):
    return deepcopy(self.example)


class ToyotaCar: 
  pass

class FordCar: 
  pass

def clone(prototype):
  return prototype.clone()

p1 = Prototype(ToyotaCar())
p2 = Prototype(FordCar())

obj1 = p1.clone()
print obj1
obj2 = p2.clone()
print obj2