class BankAccount:
    def __init__(self):
        self.balance = 0

    def add_money(self):
        print('Add money')
    
    def withdraw_money(self):
        print('Take out money')


class SavingAccount(BankAccount):
    def __init__(self, min_balance):
        super().__init__()
        self.min_balance = min_balance
    
    def add_money(self, money):
        self.balance += money
        return self.balance
    
    def withdraw_money(self, money):
        if self.balance - money >= self.min_balance:
            self.balance -= money
            return self.balance
        else:
            print('Is not possible to take money off from your account,there is not enough money')
            return self.balance


class Menu:
    def ask_for_money(self):
        while True:
            try:
                ask_for_money = int(input('Enter the amount of money: '))
                if ask_for_money > 0:
                    return ask_for_money
                else:
                    print('Your value must be more than 0. Please try again!')
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    
    def ask_add_option(self):
        return input('Do you want to add money [yes] or [no]: ')
    
    def ask_withdraw_option(self):
        return input('Do you want to withdraw money [yes] or [no]: ')


def main():
    menu_handler = Menu()
    account = SavingAccount(100)

    while True:
        user_option = menu_handler.ask_add_option().lower()
        if user_option == 'yes':
            money = menu_handler.ask_for_money()
            print(f"New balance: {account.add_money(money)}")
        elif user_option == 'no':
            while True:
                wd_op = menu_handler.ask_withdraw_option()
                if wd_op == 'yes':
                    money = menu_handler.ask_for_money()
                    print(account.withdraw_money(money))
                else:
                    break
        else:
            break


if __name__ == '__main__':
    main()
