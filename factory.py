class Product:
  pass

class FordCar(Product):
  pass

class ToyotaCar(Product):
  pass

class Factory:
  def factorymethod(self):
    raise NotImplementedError()

class FordFactory(Factory):
  def factorymethod(self):
    return FordCar()

class ToyotaFactory(Factory):
  def factorymethod(self):
    return ToyotaCar()

factories = [FordFactory(), ToyotaFactory()]
for f in factories:
  product = f.factorymethod()
  print product