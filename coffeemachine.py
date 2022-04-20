import os
import time

# Coffee Machine


def main():
    
        water  = 300
        milk   = 200
        coffee = 100
        money  = 0
        cents    = 0.01
        nickle  = 0.05
        dime    = 0.10
        quarter = 0.25
        os.system('clear')
        selection = (input('\n\nWhat would you like? (espresso/latte/cappuccino): ') )

        # If user wants an espresso
        if selection == 'espresso':
            # setting payment = 0 and removing 50ml of water from machine
            payment = 0
            water -= 50

            # If we don't have enough water then we will send user back to main menu 
            if water < 0:
                water += 50
                os.system('clear')
                print("Sorry, there isn't enough water for that!")
                time.sleep(2)
                return main()
            
            # If we don't have enough coffee then we will send user back to main menu
            coffee -= 18
            if coffee < 0:
                coffee += 18
                os.system('clear')
                print("Sorry, there isn't enough coffee for that!")
                time.sleep(2)
                return main()

            # If we have sufficient water and coffee
            else:
                # We will tell the user how much it is, and then prompt to enter coins 
                if payment < 2.50:
                    os.system('clear')
                    print('An espresso costs: $2.50\n')
                    print('Please enter your coins below\n\n')
                    quarters_paid = quarter * float(input('How many quarters?: '))
                    dimes_paid    = dime    * float(input('How many dimes?: '))
                    nickles_paid  = nickle  * float(input('How many nickles?: '))
                    cents_paid    = cents   * float(input('How many pennies?: '))
                    payment += float(quarters_paid + dimes_paid + nickles_paid + cents_paid)

                    # If user pays the amount needed
                    if payment >= 2.50:
                        change = payment - 2.50
                        money += payment - change
                        os.system('clear')
                        print(f'\nHere is your change: ${round(change, 2)}\n')
                        print('Enjoy your espresso!')
                        time.sleep(2)
                        return main()
                    
                    # If the user doesn't pay the amount needed
                    else:
                        os.system('clear')
                        print("\nSorry, you didn't give enough money.")
                        print(f'Here is your money back: ${round(payment, 2)}')
                        time.sleep(2)
                        return main()

        if selection == 'latte':
            payment = 0
            water - 200

            if water < 0:
                water + 200
                os.system('clear')
                print("Sorry, there isn't enough water for that!")
                time.sleep(2)
                return main()

            coffee - 24
            if coffee < 0:
                coffee + 24
                os.system('clear')
                print("Sorry, there isn't enough coffee for that!")
                time.sleep(2)
                return main()

            milk - 150
            if milk < 0:
                milk + 150
                os.system('clear')
                print("Sorry, there isn't enough milk for that!")
                time.sleep(2)
                return main()

            else:
                if payment < 4.00:
                    os.system('clear')
                    print('An espresso costs: $4.00\n')
                    print('Please enter your coins below\n\n')
                    quarters_paid = quarter * float(input('How many quarters?: '))
                    dimes_paid    = dime    * float(input('How many dimes?: '))
                    nickles_paid  = nickle  * float(input('How many nickles?: '))
                    cents_paid    = cents   * float(input('How many pennies?: '))
                    payment += float(quarters_paid + dimes_paid + nickles_paid + cents_paid)

                    if payment >= 4.00:
                        change = payment - 4.00
                        money += payment - change
                        os.system('clear')
                        print(f'\nHere is your change: ${round(change, 2)}\n')
                        print('Enjoy your latte!')
                        time.sleep(2)
                        return main()
                    else:
                        os.system('clear')
                        print("\nSorry, you didn't give enough money.")
                        print(f'Here is your money back: ${round(payment, 2)}')
                        time.sleep(2)
                        return main()
        

        if selection == 'cappuccino':
            payment = 0
            water - 250

            if water < 0:
                water + 250
                os.system('clear')
                print("Sorry, there isn't enough water for that!")
                time.sleep(2)
                return main()

            coffee - 24
            if coffee < 0:
                coffee + 24
                os.system('clear')
                print("Sorry, there isn't enough coffee for that!")
                time.sleep(2)
                return main()

            milk - 100
            if milk < 0:
                milk + 100
                os.system('clear')
                print("Sorry, there isn't enough milk for that!")
                time.sleep(2)
                return main()

            else:
                if payment < 5:
                    os.system('clear')
                    print('An espresso costs: $5.00\n')
                    print('Please enter your coins below\n\n')
                    quarters_paid = quarter * float(input('How many quarters?: '))
                    dimes_paid    = dime    * float(input('How many dimes?: '))
                    nickles_paid  = nickle  * float(input('How many nickles?: '))
                    cents_paid    = cents   * float(input('How many pennies?: '))
                    payment += float(quarters_paid + dimes_paid + nickles_paid + cents_paid)

                    if payment >= 5.00:
                        change = payment - 5.00
                        money += payment - change
                        os.system('clear')
                        print(f'\nHere is your change: ${round(change, 2)}\n')
                        print('Enjoy your latte!')
                        time.sleep(2)
                        return main()
                    else:
                        os.system('clear')
                        print("\nSorry, you didn't give enough money.")
                        print(f'Here is your money back: ${round(payment, 2)}')
                        time.sleep(2)
                        return main()
        
                    

        if selection == 'off':
            quit()
        
        if selection == 'report':
            report = print(f' \n Water: {water}ml\n', f'Milk: {milk}ml\n', f'Coffee: {coffee}g\n', f'Money: ${money}\n\n' )
            time.sleep(2)
            return main()


main() 