class Bank:
    def __init__(self, acount_number, name, money):
        self.account_number = acount_number
        self.name = name
        self.money = money

    def deposit(self, percent):
        self.money = self.money + percent


    def withdraw(self, amount):

        if self.money < amount:
            print("No money no honey")
        else:
            self.money = self.money - amount - self.bank_fee()

    def bank_fee(self):
        bank_fee = 0.1 * self.money
        return bank_fee


    def show(self):
        print("Account number: ", self.account_number)
        print("Account name: ", self.name)
        print("Account Balance: ", self.money, " UAH")


alisa_client = Bank(12345678, "Alisa", 200_000)

alisa_client.withdraw(5000)  # Account number:  12345678
alisa_client.deposit(10_000)  # Account name:  Alisa
alisa_client.show()  #Account Balance:  185000.0  UAH
print(alisa_client.bank_fee()) # 18500.0
