class Customer:
    def __init__(self, name, grade="basic"):
        self.name = name
        self.grade = grade
        self.points = 0

    def add_points(self, amount):
        self.points += int(amount * 0.03)

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


c1 = Customer("이서강")
c2 = Customer("김강서", "vip")

o1 = Order("PA-405", c1, [("아메리카노", 3800)])
o2 = Order("AS-414", c2, [("딸기 홀케이크", 45000), ("망고 스무디", 8700)])
o3 = Order("MA-315", c1, [("카페 모카", 4700), ("아메리카노", 3800), ("샌드위치", 7100)])

o2.add_item("초코 마시멜로 쿠키", 5600)

print(f"{o1.order_id}: {o1.total_price():,}원 결제 필요")
o1.pay()
print(o1.customer.summary())

print(f"{o2.order_id}: {o2.total_price():,}원 결제 필요")
o2.pay()
print(o2.customer.summary())

print(f"{o3.order_id}: {o3.total_price():,}원 결제 필요")
o3.pay()
print(o3.customer.summary())