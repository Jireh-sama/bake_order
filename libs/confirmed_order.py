
class ConfirmedOrder:
  def __init__(self):
    self.confirmed_order_list = []

  def confirm_order(self, order_list):
    for item in order_list:
      self.confirmed_order_list.append(item)

    print(self.confirmed_order_list)
    
  def get_confirmed_order_list(self):
    return self.confirmed_order_list
  
