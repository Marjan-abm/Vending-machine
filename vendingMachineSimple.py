items = [
    {
        'code':0,
        'name':'Soda',
        'price':0.95
    },
    {
        'code':1,
        'name':'Candy Bar',
        'price':0.60
    },
    {
        'code':2,
        'name':'Chips',
        'price':0.99
    },
]

is_quit = False
item = ''

while is_quit == False:
    print("Welcome to the vending machine")
    for i in items:
        print(f"Item Name: {i['name']} - Price: {i['price']} - code: {i['code']}")

    query = int(input("Enter the code number of the item you want to get: "))
    for i in items:
        if query == i['code']:
            item = i
    if item == '':
        print('INVALID CODE')
    else:
        print(f"Great, {item['name']} will cost you {item['price']} dollars")

        price = float(input(f"Enter {item['price']} dollars to purchase: "))
        if price == item['price']:
            print(f"Thank you for buying here is your {item['name']}")
        elif price > item['price']:
            change = price - item['price']
            print(f"Here is your {item['name']} and your change is {change}")
        else:
            print(f"Your money is not enough, please try again")

    query = input("Do you want to continue buying or quit? to continue click c and to quit click q ")
    if query == 'c':
        is_quit = False
    else:
        is_quit = True
    print('')