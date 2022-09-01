class User:
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount
        return self

    def make_withdrawal(self, amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.amount}")
        return self

    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

josh_g = User("Mr. G")
jacob = User("Jake")
paul = User("Pockets")

josh_g.make_deposit(1000).make_deposit(750).make_deposit(7000).make_withdrawal(3500).display_user_balance()

jacob.make_deposit(3250).make_deposit(1000).make_withdrawal(500).make_withdrawal(625).display_user_balance()

paul.make_deposit(9750).make_withdrawal(500).make_withdrawal(75).make_withdrawal(200).display_user_balance()

josh_g.transfer_money(200, paul)