from card_holder import cardHolder


def print_menu():
    print("Please select one of the following")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show balance")
    print("4. Exit")


def deposit(cardHolder):
    try:
        deposit = float(input("How much money would you like to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print("Thank you for the deposit! Your new balance is: $", str(cardHolder.get_balance()))
    except:
        print("Invalid imput")

def withdraw(cardHolder):
    try:
        withdraw = float(input("How much money would you like to withdraw: "))
        if withdraw <= cardHolder.get_balance():
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("Thank you for the Withdraw! Your new balance is: $", str(cardHolder.get_balance()))
        else:
            print("Not enough funds :(")
    except:
        print("Invalid input")

def check_balance(cardHolder):
    print("Your balance is: $", cardHolder.get_balance())


if __name__ == "__main__":
    current_user = cardHolder("","","","","")

    list_of_cardholders = []
    list_of_cardholders.append(cardHolder("84356438678", 1234, "Colin", "Lombardi", 999.89))
    list_of_cardholders.append(cardHolder("93204476574", 5678, "George", "Bushnach", 892.79))
    list_of_cardholders.append(cardHolder("12389876540", 9010, "Jack", "Santo", 1897.01))


    debitcard_num = ""
    while True:
        try:
            debitcard_num = input("Please imput your debit card number :")

            debitmatch = [holder for holder in list_of_cardholders if holder.cardNum == debitcard_num]
            if (len(debitmatch)> 0):
                current_user = debitmatch[0]
                break
            else:
                print("Card number not on file.")
        except:
            print("CardNumber not on file.")


    while True:
        try:
            user_pin = int(input("Intput your pin here: "))
            if (user_pin == current_user.get_pin()):
                break
            else:
                print("That pin is invalid")

        except:
            print("Invalid please try again")


print("Welcome to cd bank", current_user.get_firstname())
option = 0
while True:
    print_menu()
    try:
        option = int(input())
    except:
        print("Invalid atm operation")

    if option == 1:
        deposit(current_user)
    if option == 2:
        withdraw(current_user)
    if option == 3:
        check_balance(current_user)
    elif option == 4:
        break
    else:
        option = 0

print("Thank you for using cd bank!")
    