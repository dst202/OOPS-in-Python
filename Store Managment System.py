class Item:
    pay_rate = 0.8   # The pay rate after 20 percent discount
    all = []

    def __init__(self, name: str, price: int, quantity: int):
        # Run validations for received arguments
        assert price >= 0, f"Price {price } is not greater than zero"
        assert quantity >= 0

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        # Actions to execute
        Item.all.append(self)

    def cal_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
for instance in Item.all:
    print(instance.name)




