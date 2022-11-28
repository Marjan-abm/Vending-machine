class Inventory:
    def __init__(self):
        self.inventory = {}

    def get_quantity(self, item):
        return self.inventory[item]

    def add(self, item):
        self.inventory[item] += 1

    def deduct(self, item):
        self.inventory[item] -= 1

    def has_item(self, item):
        return self.inventory[item] > 0

    def clear(self):
        for item in self.inventory.keys():
            self.inventory[item] = 0
            # or self.inventory = {}

    def put(self, item, quantity):
        self.inventory[item] = quantity


from enum import Enum
class ITEMS(Enum):
    CHIPS = 1
    CANDY_BAR = 2
    SODA = 3

from abc import ABC, abstractmethod
class Item(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

class Chips(Item):
    def __init__(self):
        super(Chips, self).__init__(ITEMS.CHIPS, 25)

class Candy_Bar(Item):
    def __init__(self):
        super(Candy_Bar, self).__init__(ITEMS.CANDY_BAR, 35)

class Soda(Item):
    def __init__(self):
        super(Soda, self).__init__(ITEMS.SODA, 45)

# Factory class to create instance of Vending Machine, this can be extended to create instance of
# different types of vending machines.
class VendingMachineFactory:
    def createVendingMachine(self):
        return VendingMachine()

class VendingMachine:
    def __init__(self):
        self.item_inventory = Inventory()
        self.cash_inventory = Inventory()
        self.total_sales = 0
        self.current_balance = 0
        self.current_item = None
        self.initialize_inventories()

    def initialize_inventories(self):
        all_items = [Chips(), Candy_Bar(), Soda()]
        for item in all_items:
            self.item_inventory.put(item, 5)


    def selectItemAndGetPrice(self, item):
        if self.item_inventory.has_item(item):
            self.current_item = item
            return self.current_item.get_price()
        return "Sold Out, Please buy another item"

    def collectItemAndChange(self):
        item = self.collectItem()
        self.total_sales += self.current_item.get_price()
        change = self.collectChange()

        return (item, change)

    def collectItem(self):
        if self.isFullPaid():
            if self.hasSufficientChange():
                self.item_inventory.deduct(self.current_item)
                return self.current_item
            return "Not Sufficient change in Inventory"
        return "Price not full paid"

    def hasSufficientChange(self):
        change_amt = self.current_balance - self.current_item.get_price()
        if self.getChange(change_amt):
            return True
        return False

    def isFullPaid(self):
        return self.current_balance >= self.current_item.get_price()

    def collectChange(self):
        change_amt = self.current_balance - self.current_item.get_price()
        change = self.getChange(change_amt)
        self.updateCashInventory(change)
        self.current_balance = 0
        self.current_item = None
        return change


    def updateCashInventory(self, change):
        for c in change:
            self.cash_inventory.deduct(c)