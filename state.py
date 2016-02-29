class Context:
  def __init__(self, state):
    try:
      self.state = state
    except WrongStateError:
      pass

  def register(self):
    try:
      self.state.register(self)
    except WrongStateError:
      pass

  def cancel(self):
    try:
      self.state.cancel(self)
    except WrongStateError:
      pass

  def ship(self):
    try:
      self.state.ship(self)    
    except WrongStateError:
      pass

class State(object):
  def __init__(self, order):
      self.order = order

  def register(self, context):
    raise WrongStateError('You can not register in %s phase' % self.order.status)
  
  def cancel(self, context):
    raise WrongStateError('You can not cancel in %s phase' % self.order.status)
  def ship(self, context):
    raise WrongStateError('You can not ship in %s phase' % self.order.status)    
class InitialState(State):
  def __init__(self, order):
    super(InitialState, self).__init__(order)

  def register(self, context):
    self.order.desc = 'Order is in register state'
    self.order.status = 'register'
    context.state = RegisterState(order)
    print self.order.desc

class RegisterState(State):
  def __init__(self, order):
    super(RegisterState, self).__init__(order)

  def cancel(self, context):
    self.order.desc = 'Order is cancelled' 
    self.order.status = 'cancel'
    context.state = CancelState(order)
    print self.order.desc
  
  def ship(self, context):
    self.order.desc = 'Order is shipping'
    self.order.status = 'shipping'
    context.state = ShippingState(order)
    print self.order.desc

class CancelState(State):
  def __init__(self, order):
    super(CancelState, self).__init__(order)

  def register(self, context):
    self.order.desc = 'Order is in register state'
    self.order.status = 'register'
    context.state = RegisterState(order)
    print self.order.desc

class ShippingState(State):
  def __init__(self, order):
    super(ShippingState, self).__init__(order)

class WrongStateError(Exception):
  def __init__(self, msg):
    self.msg = msg
    print self.msg

class Order:
  status = None
  desc = None

order = Order()
state = InitialState(order)
context = Context(state)
context.register()
context.cancel()
context.ship()
context.register()
context.ship()
context.cancel()