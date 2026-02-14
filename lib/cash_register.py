#!/usr/bin/env python3

# build a cash register object
# add items
# apply discounts
# void previous transactions

class CashRegister:
  def __init__(self, discount=0, total=0):
    self.discount = discount
    self.total = total
    self.items = []
    self.previous_transactions = []
    
  @property
  def discount(self):
    return self._discount
  @discount.setter
  def discount(self, value):
    if type(value) is int and 0 <= value <= 100:
      self._discount = value
    else:
      raise ValueError("Not valid discount")
  
  def add_item(self, item, price, quantity=1):
    self.total += price * quantity

    # record each individual item in the items list
    for _ in range(quantity):
      self.items.append(item)

    new_transaction = {
      "item": item,
      "price": price,
      "quantity": quantity
    }
    self.previous_transactions.append(new_transaction)
    
  def apply_discount(self):
    if self.items == [] or self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total = self.total - (self.total * (self.discount / 100))
      print(f"After the discount, the total comes to ${self.total:.0f}.") # format with 2 decimal places
    
  def void_last_transaction(self):
    if self.previous_transactions == []:
      print("There is no transaction to void.")
    else:
      last_transaction = self.previous_transactions.pop()
      for _ in range(last_transaction["quantity"]):
        self.items.remove(last_transaction["item"])
      self.total -= (last_transaction["price"] * last_transaction["quantity"])
