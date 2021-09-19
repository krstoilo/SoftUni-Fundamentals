class Vehicle:
    def __init__(self, type, model, price, owner=""):
        self.type = type
        self.model = model
        self.price = float(price)
        self.owner = ""

    def buy(self, money, owner):
        if self.owner != "":
            print("Car already sold")
        if float(money) >= self.price and self.owner is None:
            print(f"Successfully bought a {self.type}. Change: {float(money)-self.price:.2f}")
        else:
            print("Sorry, not enough money")

    def sell(self):
        if self.owner is None:
            return print("Vehicle has no owner")
        else:
            self.owner = None

    def __repr__(self):
        if self.owner is None:
            return f"{self.model} {self.type} is on sale: {self.price:.0f}"
        else:
            return f"{self.model} {self.type} is owned by: {self.owner}"


car = Vehicle("car", "Nissan", 14000, "Kremena")
car.buy(10000, "Pesho")


