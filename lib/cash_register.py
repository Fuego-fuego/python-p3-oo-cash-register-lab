#!/usr/bin/env python3
class CashRegister:
  def __init__ (self,discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    
  def add_item (self,title,price,quantity = 1):
    self.total+= price * quantity
    while(quantity>0):
      self.items.append(title)
      quantity-=1    
  
  def apply_discount(self):
    if self.discount > 0:
      self.total -= int(self.total * self.discount / 100)
      print (f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")
    
  def items_list_without_multiples(self):
    return self.items
  
  def void_last_transaction(self):
    pass
  
  def void_last_transaction_with_multiples(self):
    pass