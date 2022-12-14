class Stock(object):

    def _init_(self):

        self.name = ''

        self.price = 0

        self.type = ''

        self.expiration = ''

        self.userID = 0

 

    def set_name(self, n):

        self.name = n

 

    def get_name(self):

        return self.name

   
   
    def set_price(self, p):
   
        self.price = p

   
   
    def get_price(self):
   
        return self.price

 

    def set_type(self, t):

        self.type = t

 

    def get_type(self):

        return self.type

 

    def set_expiration(self, e):

        self.expiration = e

 

    def get_expiration(self):

        return self.expiration

 

    def set_userID(self, u):

        self.userID = u

 

    def get_userID(self):

        return self.userID

 

    def display(self):

        print(f'Name: {self.name}')

        print(f'Price: {self.price}')

        print(f'type: {self.type}')

        print(f'expiration: {self.expiration}')

        print(f'userID: {self.userID}')

class Customer(object):

    def _init_(self):

        self.name = ''

        self.amount = 0


    def set_name(self, n):

        self.name = n

 

    def get_name(self):

        return self.name

 

    def set_balance(self, b):

        self.balance = b

 

    def get_balance(self):

        return self.balance

 

    def display(self):

        print(f'basket: {self.name}')

        print(f'Balance: {self.balance}')


userID = 0

stock = []

basket = []

tax_lux = 1.2
tax_ess = 1.1
tax_gif = 1.05

selection = 0


while selection != 5:

    print('1. Stock screen')

    print('2. Shopper screen')

    print('3. Calculations screen')

    print('4. Item package screen')

    print('5. Exit')

 

    selection = int(input('Enter the number of the option (1-5): '))

 

    if selection == 1:

        selection1 = 0

        while selection1 != 4:

            print('<>')

            print('1. Add Items')

            print('2. View Items')

            print('3. remove items')

            print('4. exit')

            print('<>')

 

            selection1 = int(input('Enter the number of the option (1-3): '))

 

            if selection1 == 1:

                userID += 1

                my_item = Stock()

                my_item.set_name(input('Enter the item name: '))

                my_item.set_price(int(input('Enter the price of the item: ')))
               
                my_item.set_type(input('Enter the item type in lowercase (luxury, essential or gift): '))

                my_item.set_expiration(input('Enter the expiration date (dd/mm/yyyy). if there is no expiration the enter none: '))

                my_item.set_userID(userID)

                stock.append(my_item)

 

            if selection1 == 2:

                for i in stock:

                    i.display()

           

            if selection1 == 3:

                itm = int(input('Enter the userID of the item you want to remove: '))

                for x in stock:

                    if x.get_userID() == itm:

                        stock.remove(x)

           
   
    if selection == 2:

        selection2 = 0

        while selection2 != '3':

            print('1. Add products to the basket')
            print('2. Total Price of purchase')
            print('3. Exit')


            selection2 = input('Please choose an option 1-3:')

 

            if selection2 == '1':
                    total= 0
                    print('Choose the quantity of each item that you would like to buy?')

                    print(' ')
                    for i in stock:
                        i.display()
                        

                    quantity = int(input(f'How many of these would you like to buy?'))
                    name = (input(f'whick porduct would you like to buy?'))
                    for Stock in stock:
                        if Stock.get_name() == name:
                            if Stock.get_type() == 'gift':

                                total1 = Stock.get_price() * quantity * tax_gif
                                total = total + total1
                                print(f'Successfully added {quantity} of {name} which is taxed Total current price is €{total}.')

                                shopper = Customer()
                                shopper.set_name(name)
                                shopper.set_balance(total)
                                basket.append(shopper)

                            if Stock.get_type() == 'luxury':

                                total1 = Stock.get_price() * quantity * tax_lux
                                total = total + total
                                print(f'Successfully added {quantity} of {name} which is taxed Total current price is €{total}.')

                                shopper = Customer()
                                shopper.set_name(name)
                                shopper.set_balance(total)
                                basket.append(shopper)
                            

                            if Stock.get_type() == 'essential':

                                total1 = Stock.get_price() * quantity * tax_ess
                                total = total + total1
                                print(f'Successfully added {quantity} of {name} which is taxed Total current price is €{total}.')

                                shopper = Customer()
                                shopper.set_name(name)
                                shopper.set_balance(total)
                                basket.append(shopper)

                
 
            elif selection2 == '2':

                print(f'The total price total of your basket is: €{total1} including tax')

 

            elif selection2 == '3':

                break