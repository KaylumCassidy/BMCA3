class Stock(object):

    def _init_(self):
        self.name = ''
        self.type = ''
        self.amount = 0

    def set_name(self, n):
        self.name = n

    def get_name(self):
        return self.name

    def set_balance(self, b):
        self.balance = b

    def get_balance(self):
        return self.balance

    def set_type(self, t):
        self.type = t

    def get_type(self):
        return self.type


    def display(self):
        print(f'Name: {self.name}')
        print(f'Balance: {self.balance}')
        print(f'type: {self.type}') 


class Customer(object):

    def _init_(self):
        self.bastket = []
        self.amount = 0

    def set_bastket(self, b):
        self.bastket = b

    def get_bastket(self):
        return self.bastket

    def set_amount(self, a):
        self.amount = a

    def get_amount(self):
        return self.amount

    def display(self):
        print(f'bastket: {self.bastket}')
        print(f'Balance: {self.amount}')


stock = []
shopper = []
selection = 0

while selection != 5:
    print('1. Stock screen')
    print('2. Shopper screen')
    print('3. Calculations screen')
    print('4. Item package screen')
    print('5. Exit')

    selection = int(input('Enter option (1-5): '))

    if selection == 1:
        selection1 = 0

        while selection1 != 3:
            print('1. Add Items')
            print('2. View Items')
            print('5. Exit')

