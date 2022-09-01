class User:
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawal(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.amount}")

    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()

josh_g = User("Mr. G")
jacob = User("Jake")
paul = User("Pockets")

josh_g.make_deposit(1000)
josh_g.make_deposit(750)
josh_g.make_deposit(7000)
josh_g.make_withdrawal(3500)
josh_g.display_user_balance()

jacob.make_deposit(3250)
jacob.make_deposit(1000)
jacob.make_withdrawal(500)
jacob.make_withdrawal(625)
jacob.display_user_balance()

paul.make_deposit(9750)
paul.make_withdrawal(500)
paul.make_withdrawal(75)
paul.make_withdrawal(200)
paul.display_user_balance()

josh_g.transfer_money(200, paul)