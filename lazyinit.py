class LazyCalc:
  
  def __init__(self):
    self.dict = {}  

  def calc(self, n):
    if n not in self.dict:
      def recursion(n):
        if n <= 1:
          return 1
        else:
          return n * recursion(n - 1) 
      res = recursion(n)
      self.dict[n] = res 
    return self.dict[n]
    

class Main():
  def __init__(self):
    self.lazy_calc = None
  def get_lazy_calc(self):
    if not self.lazy_calc:
      self.lazy_fact = LazyCalc()
    return self.lazy_fact


main = Main()
lazy_calc = main.get_lazy_calc()
print lazy_calc.calc(5)
print lazy_calc.calc(5)