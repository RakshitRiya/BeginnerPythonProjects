class CoffeeMachine:
    
    def __init__(self, water, milk, beans, cups, deposit):
        self.water=water
        self.milk=milk
        self.beans=beans
        self.cups=cups
        self.deposit=deposit
    
    def currentState(self):
        print()
        print("The Coffee Machine has:")
        print(self.water, " of water")
        print(self.milk, " of milk")
        print(self.beans, " of beans")
        print(self.cups, " of disposable cups")
        if self.deposit>0:
            print("₹{} of money".format(self.deposit))
        else:
            print("{} of money".format(self.deposit))
        print()
        
    def take(self):
        print("I gave you ₹{}".format(self.deposit))
        self.deposit=0
    
    def refillMachine(self):
        self.water += int(input("Write how many ml of water do you want to add: "))
        self.milk += int(input("Write how many ml of milk do you want to add: "))
        self.beans += int(input("Write how many grams of coffee beans do you want to add: "))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add: "))
        
    def makeCoffee(self, water_amount, milk_amount, bean_amount, price):
        not_enough = []
        if water_amount > self.water:
            not_enough.append("water")
        if milk_amount > self.milk:
            not_enough.append("milk")
        if bean_amount > self.beans:
            not_enough.append("coffee beans")
        if self.cups == 0:
            not_enough.append("cups")
        if len(not_enough) == 0:
            self.cups -= 1
            self.water -= water_amount
            self.milk -= milk_amount
            self.beans -= bean_amount
            self.deposit += price
            print("I have enough resources, making you a coffee!")
            print()
        else:
            print("Sorry, not enough", *not_enough)
            print()

            
    def buyCoffee(self, choice):
        if choice == "1" or choice == "espresso":
            self.makeCoffee(250, 0, 16, 4)
        elif choice == "2" or choice == "latte":
            self.makeCoffee(350, 75, 20, 7)
        elif choice == "3" or choice == "cappuccino":
            self.makeCoffee(200, 100, 12, 6)
            

if __name__ == "__main__":
    coffee_machine = CoffeeMachine(400, 250, 120, 9, 550)
    userInput = input("Write action (buy, fill, take, remaining, exit): ")
    while userInput != "exit":
        if userInput == "take":
            coffee_machine.take()
        if userInput == "fill":
            coffee_machine.refillMachine()
        if userInput == "remaining":
            coffee_machine.currentState()
        if userInput == "buy":
            user_selection = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main "
                                   "menu: ")
            if user_selection == "back":
                userInput = input("Write action (buy, fill, take, remaining, exit): ")
            else:
                coffee_machine.buyCoffee(user_selection)
        else:
            print("Enter a valid choice!")

        userInput = input("Write action (buy, fill, take, remaining, exit): ")
