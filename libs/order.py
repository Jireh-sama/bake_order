import random
import string
import time

class Order:
    def __init__(self):
      self.item_list = []
      self.total = 0

    def __str__(self):
      return f"Item(name={self.name}, price={self.price})"

    def add_item(self, name, price, quantity, total):
      self.total += total
      self.item_list.append({
        'name': name,
        'price': price,
        'quantity': quantity,
        'total': total
       })

    def get_total(self):
      return self.total

    def get_items(self):
      return self.item_list

    def clear_order(self):
      self.item_list=[]
      self.total = 0
  
























# import datetime

# class CustomerOrder:
#     next_order_id = 1  # Class variable to track the next available order ID

#     def __init__(self, items=None, status='unpaid'):
#       self.order_id = CustomerOrder.next_order_id
#       CustomerOrder.next_order_id += 1  # Increment the order ID for the next order
#       self.items = items if items else []
#       self.status = status
#       self.date_ordered = datetime.date.today().strftime('%Y-%m-%d')

#     def add_item(self, name, quantity, total):
#       self.items.append({
#         'name': name,
#         'quantity': quantity,
#         'total': total
#       })

#     def remove_item(self, name):
#       for item in self.items:
#         if item['name'] == name:
#           self.items.remove(item)
#           break

#     def total_cost(self):
#       return sum(item['total'] for item in self.items)

#     def display_items(self):
#       print(self.items)