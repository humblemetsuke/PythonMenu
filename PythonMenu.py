

## Burger Bytes
from random import randint
def BurgerBytes():
    # Parent Class
    class FoodItem:
        CurrentOrder = []
        TotPrice = float(0)

        def __init__(self, deals):
            self.CurrentOrder += [deals]

        def price(self, value):
            self.TotPrice += value

    # Child Classes
    class Burger(FoodItem):
        BurgerType = ("").lower()
        BurgerPrice = float(10)

        # Version of item requested in order
        def __init__(self, kind):
            self.BurgerType = kind

        def AddBurger(self):
            # add to order
            add = self.BurgerType + " Burger"
            self.CurrentOrder += [add]


    class Drink(FoodItem):
        DrinkType = ("").lower()
        SoftPrice = float(2)
        BeerPrice = float(5)
        SpiritPrice = float(6)

        # Version of item requested in order
        def __init__(self, kind):
            self.DrinkType = kind

        def AddDrink(self):
            # Add to order
            self.CurrentOrder += [self.DrinkType]


    class Side(FoodItem):
        SideType = ("").lower()
        SidePrice = float(3)

        # Version of item requested in order
        def __init__(self, kind):
            self.SideType = kind

        def AddSide(self):
            # add to order
            self.CurrentOrder += [self.SideType]


    class Combo(FoodItem):
        MealDeal = "".lower()
        disprice = float()
        off = 0.15 # discount amount

        def __init__(self, deal):
            self.MealDeal = deal

        # Apply discount
        def Discount(self):
            self.TotPrice = self.TotPrice - (self.TotPrice * float(self.off))
            self.disprice = float("{:.2f}".format(self.TotPrice))
            print("Price for this combo is: £", round(float(f'{self.disprice:.2f}'), 2))
            self.price(self.disprice)


    class Toppings(Burger):
        ToppingType = "".lower()
        ToppingPrice = float(0.5)

        # Version of item requested in order
        def __init__(self, kind):
            super().__init__(kind)
            self.ToppingType = kind

        def AddToppings(self):
            # add to order
            self.CurrentOrder.append(self.ToppingType)


    class Condiments(Side):
        CondType = "".lower()
        CondPrice = float(0.25)

        # Version of item requested in order
        def __init__(self, kind):
            super().__init__(kind)
            self.CondType = kind

        def AddCond(self):
            # add to order
            self.CurrentOrder.append(self.CondType)


    class Orders:
        Tip = float()
        AllOrders = []

        def TodaysOrders(self, OrdId, OrdPrice):
            self.AllOrders.append(OrdId)
            self.AllOrders.append(OrdPrice)


    # Varieties of food items
    burgers = "Beef\n Chicken\n Mushroom"
    sides = "Chips\n Cheesy Chips\n Onion Rings"
    drinks = "Coke\n Fanta\n Sprite\n Water\n Open Source Lager\n Bitwise Pale Ale\n Bath Tub Gin & Tonic"
    tops = "Jalapeno\nCheese"

    # print menu
    print("\nMENU\n\nBurgers All Served With Tomato & Lettuce - All £10\n", burgers, "\n\nSides - All £3\n", sides,
        "\n\nDrinks - Soft £2, Beer £5, Gin £6\n", drinks, "\n\nAdditional Burger Topping - 50p each\n", tops)

    # Whilst order is ongoing
    OrderOnTheGo = "Yes"

    # Item codes
    Items = {"B": "Beef",
            "C": "Chicken",
            "M": "Mushroom",
            "c": "Chips",
            "cc": "Cheesy Chips",
            "o": "Onion Rings",
            "K": "Coke",
            "F": "Fanta",
            "S": "Sprite",
            "W": "Water",
            "L": "Lager",
            "P": "Ale",
            "G": "Gin & Tonic",
            "CH":"Cheese",
            "J":"Jalapeno"}
    MD = {"Y": "Meal Deal? Yes!",
        "N": "Meal Deal? No :("}
    soft = ["K", "F", "S", "W"]
    beer = ["L", "P"]
    spirits = ["G"]

# Initialise order taking
    print("If you would like to cancel your order at any time, enter Q")
    OrdPrice = 0
    numdeals = 0
    ORDER = []
    # Order is ongoing until loop is broken
    DayDone = "No"     
    while  DayDone != "Yes" or DayDone != "Y":
        OrdID = randint(10000, 99999)
        print(OrdID)
        while OrderOnTheGo == "Yes" or OrderOnTheGo == "Y":
            FoodItem.TotPrice = 0


            # ask if combo
            deal = input("Would you like to have a combo today for 15% off?! (Burger + Drink + Side) (Y/N) ").title()
            MealDeal = deal
            deals = FoodItem(MD[deal])
            if deal == "N" or deal == "No":

                ## Single items
                # Burger
                burger = input("Would you like a burger today? (Y/N) ").lower()
                if burger == "y":
                    kind = input("Beef(B), Chicken(C), Mushroom(M) ").title()
                    food = Burger(Items[kind])
                    OrdB = food.AddBurger()
                    FoodItem.TotPrice += Burger.BurgerPrice
                    top = input("Would you like any additional toppings? (Y/N) ").title()
                    if top == "Y":
                        ja = input("Would you like Jalapeno? (Y/N) ").title()
                        ch = input("Would you like cheese? (Y/N)" ).title()
                        if ja == "Y" and ch == "Y":
                            FoodItem.TotPrice += (Toppings.ToppingPrice * 2)
                            top1 = Toppings(Items["J"])
                            top2 = Toppings(Items["CH"])
                            OrdT1 = top1.AddToppings()
                            OrdT2 = top2.AddToppings()
                        elif ja == "Y" and ch == "N":
                            FoodItem.TotPrice += Toppings.ToppingPrice
                            top1 = Toppings(Items["J"])
                            OrdT1 = top1.AddToppings()
                        elif ja == "N" and ch == "Y":
                            FoodItem.TotPrice += Toppings.ToppingPrice
                            top2 = Toppings(Items["CH"])
                            OrdT2 = top2.AddToppings()
                # option to quit            
                elif burger == "Q" or burger == "q":
                    print("Thank you for your custom, have a nice day!")
                    break

                # Drink
                drink = input("Would you like a drink? (Y/N) ").lower()
                if drink == "y":
                    kind = input(
                        "Coke(K), Fanta(F), Water(W), Open Source Larger(L), Bitwise Pale Ale(P), Bath Tub Gin & Tonic(G) ").title()
                    if kind in soft:
                        FoodItem.TotPrice += Drink.SoftPrice
                    elif kind in beer:
                        FoodItem.TotPrice += Drink.BeerPrice
                    elif kind in spirits:
                        FoodItem.TotPrice += Drink.SpiritPrice
                    # option to quit
                    elif drink == "Q" or drink == "q":
                        print("Thank you for your custom, have a nice day!")
                        break
                    liquid = Drink(Items[kind])
                    OrdD = liquid.AddDrink()

                # Side
                side = input("Would you like a side today? (Y/N) ").title()
                if side == "Y":
                    kind = input("Chips(c), Cheesy Chips(cc), Onion Rings(o) ").lower()
                    extra = Side(Items[kind])
                    OrdS = extra.AddSide()
                    FoodItem.TotPrice += Side.SidePrice
                    condi = input("Would you like any sauce with your side? (Y/N) ").title()
                    if condi == "Y":
                        condiment = input("Ketchup, BBQ, or Mayo: ")
                        FoodItem.TotPrice += float(Condiments.CondPrice)
                        sauce = Condiments(condiment)
                        OrdC = sauce.AddCond()
                        condi = input("Would you like any other sauce with your side? (Y/N) ").title()
                        if condi == "Y":
                            condiment = input("Ketchup, BBQ, or Mayo: ")
                            FoodItem.TotPrice += float(Condiments.CondPrice)
                            sauce = Condiments(condiment)
                            OrdC = sauce.AddCond()
                # option to quit
                elif side == "Q" or side == "q":
                    print("Thank you for your custom, have a nice day!")
                    break
                # Show running total
                print("Price for this section is: £", f'{FoodItem.TotPrice:.2f}')
                OrdPrice += float(FoodItem.TotPrice)

            # option to quit
            elif deal == "Q" or deal == "Quit":
                print("Thank you for your custom")
                break

            # take combo order
            elif deal == "Y":
                numdeals += 1
                burger = input("What kind of burger? (Beef(B), Chicken(C), Mushroom(M)) ").title()
                # option to quit
                if burger == "Q" or burger == "q":
                    print("Thank you for your custom")
                    break
                drink = input("What drink? (Coke(K), Fanta(F), Water(W), Open Source Larger(L), Bitwise Pale Ale(P), Bath Tub Gin & Tonic(G)) ").title()
                # option to quit
                if drink == "Q" or drink == "q":
                    print("Thank you for your custom")
                    break
                side = input("What side would you like? (Chips(c), Cheesy Chips(cc), Onion Rings(o)) ").lower()
                food = Burger(Items[burger])
                OrdB = food.AddBurger()
                FoodItem.TotPrice += Burger.BurgerPrice
                # specify drink
                if drink in soft:
                    FoodItem.TotPrice += Drink.SoftPrice
                elif drink in beer:
                    FoodItem.TotPrice += Drink.BeerPrice
                elif drink in spirits:
                    FoodItem.TotPrice += Drink.SpiritPrice
                liquid = Drink(Items[drink])
                OrdD = liquid.AddDrink()
                extra = Side(Items[side])
                OrdS = extra.AddSide()
                FoodItem.TotPrice += Side.SidePrice
                top = input("Would you like any additional toppings? (Y/N) ").title()
                if top == "Y":
                    ja = input("Would you like Jalapeno? (Y/N) ").title()
                    ch = input("Would you like cheese? (Y/N)").title()
                    if ja == "Y" and ch == "Y":
                        FoodItem.TotPrice += (Toppings.ToppingPrice * 2)
                        top1 = Toppings(Items["J"])
                        top2 = Toppings(Items["CH"])
                        OrdT1 = top1.AddToppings()
                        OrdT2 = top2.AddToppings()
                    elif ja == "Y" and ch == "N":
                        FoodItem.TotPrice += Toppings.ToppingPrice
                        top1 = Toppings(Items["J"])
                        OrdT1 = top1.AddToppings()
                    elif ja == "N" and ch == "Y":
                        FoodItem.TotPrice += Toppings.ToppingPrice
                        top2 = Toppings(Items["CH"])
                        OrdT2 = top2.AddToppings()
                # calculate total after discount        
                md = Combo(MD[deal])
                OFF = md.Discount() 
                OrdPrice += round(FoodItem.TotPrice * 0.85, 2)
                condi = input("Would you like any sauce with your side? (Y/N) ").title()
                if condi == "Y":
                    condiment = input("Ketchup, BBQ, or Mayo: ")
                    sauce = Condiments(condiment)
                    OrdC = sauce.AddCond()
                    OrdPrice += round(Condiments.CondPrice)
                    condi = input("Would you like any other sauce with your side? (Y/N) ").title()
                    if condi == "Y":
                        condiment = input("Ketchup, BBQ, or Mayo: ")
                        OrdPrice += float(Condiments.CondPrice)
                        sauce = Condiments(condiment)
                        OrdC = sauce.AddCond()

            else:
                print("I didn't get that, try again please")
            OrderOnTheGo = input("Would you like anything else? (Y/N) ").title()

        # print out order and subtotal
        print("\nToday you have ordered:")
        for i in range(len(FoodItem.CurrentOrder)):
            print(FoodItem.CurrentOrder[i])
        OrdPrice = float(((f'{float(OrdPrice):.2f}')))
        print("For a total price of: £", f'{float(OrdPrice):.2f}')

        # optional tip
        tip = input("Would you like to add a tip today? Y/N ").title()
        staff = 0
        if tip == "Y":
            amount = float(input("How much would you like to tip? (%) "))
            tipa = 1 + (amount / 100)
            staff = OrdPrice * tipa
            OrdPrice *= tipa
        # option to quit
        elif tip == "Q":
            OrdPrice = f'{OrdPrice:.2f}'
            print("That brings your total today to: £", f'{float(OrdPrice):.2f}')
            print("Thank you for your custom, have a nice day!")
            ORDER = [FoodItem.CurrentOrder, OrdPrice, staff, OrdID]
            attach = OrdID.AllOrders()
            attach = OrdPrice.AllOrders()
        else:
            pass

        # print final price
        OrdPrice = f'{OrdPrice:.2f}'
        print("That brings your total today to: £", f'{float(OrdPrice):.2f}')
        print("Thank you for your custom, have a nice day!")
        ORDER.append(OrdID)
        ORDER.append(FoodItem.CurrentOrder)
        ORDER.append(OrdPrice)
        ORDER.append(staff)
        ORDER.append("End")

        attach = OrdID.AllOrders()
        attach = OrdPrice.AllOrders()

        # check if day is done
        DayDone = input("Is the business day done? ").title()
        if DayDone == 'Y' or DayDone == 'Yes':
             # print all orders for the day
            print(Orders.TodaysOrders())
        else:
            BurgerBytes()
        break

BurgerBytes()