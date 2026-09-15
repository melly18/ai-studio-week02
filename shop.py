class Customer:
    def __init__(self, name, grade="basic"):
        self.name = name
        self.grade = grade
        self.points = 0

    def add_points(self, amount):
        self.points += int(amount * 0.05)

    def get_discount_rate(self):
        if self.grade == "vip":
            return 0.1
        return 0.03

    def summary(self):
        return f"[{self.grade}] {self.name} (포인트: {self.points:,})"


class Order:
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer
        self.items = items

    def total_price(self):
        total = sum(price for _, price in self.items)
        return int(total * (1 - self.customer.get_discount_rate()))

    def add_item(self, name, price):
        self.items.append((name, price))

    def pay(self):
        price = self.total_price()
        self.customer.add_points(price)