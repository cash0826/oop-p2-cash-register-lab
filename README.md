# Object Oriented Programming (OOP) Part 2 - Cash Register Lab

### Set Up
  * Run npm install to install all necessary dependencies.
  * Run pipenv install and pipenv shell
  * Test by running pytest

### Design

Cash Register
* Attributes
  * discount
  * total
  * items
  * previous_transactions
* Methods
  * add_item(item, price, quantity)
  * apply_discount()
  * void_last_transaction()

#### CashRegister class

* ```__init__```:
  * discount
  * Allow for user to input
  * If no input initialize as 0
  * Note that discount is a percentage off of the total cash register price (e.g. a discount of 20 means the customer receives 20% off of their total price)
* ```total```
  * Initialize as 0
* ```items```
  * Initialize as empty array
* ```previous_transactions```
  * Initialize as empty array

#### Properties

* Discount:
  * Ensures discount is an integer
  * Ensures that discount is between 0-100 inclusive
  * If not print “Not valid discount”

#### Methods

* add_item(item, price, quantity)
  * Add price to total
  * Add item to the items array
  * Add an object to the previous transactions with the item, price and quantity.
* apply_discount()
  * Apply discount as percentage off from total
  * Remove the last item of previous_transaction from array
    * Ensure price reflects correctly
    * Ensure items reflects correctly
  * If no transactions in array print “There is no discount to apply.”
* void_last_transaction()
  * Remove the last item of previous_transaction from the array.
    * Ensure the price reflects correctly.
    * Ensure items reflect correctly.
  * If no transactions are in the array, print “There is no transaction to void.”
