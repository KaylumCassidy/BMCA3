from Stock_class import *

 

userID = 0

stock = []

shopper = []

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

 

        while selection1 != 3:

            print('1. Add Items')

            print('2. View Items')

            print('3. Exit')


            selection1 = int(input('Enter the number of the option (1-3): '))

 

            if selection1 == 1:

                userID += 1

                my_item = Stock()

                my_item.set_name(input('Enter the item name: '))

                #item_type = input('Enter the item type in lowercase (luxury, essential or gift): ')

                my_item.set_type(input('Enter the item type in lowercase (luxury, essential or gift): '))

                #if item_type == 'luxury':

                #    type_l.append(item_type)

                #elif item_type == 'essential':

                #    type_e.append(item_type)

                #elif item_type == 'gift':

                #    type_g.append(item_type)

                my_item.set_expiration(input('Enter the expiration date (dd/mm/yyyy). if there is no expiration the enter none: '))

                my_item.set_userID(userID)

                stock.append(my_item)

 

            if selection1 == 2:

                for i in stock:

                    i.display()

