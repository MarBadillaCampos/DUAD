class BankAccount:
    def __init__(self):
        self.balance = 0

    def add_money(self, money):
        self.balance += money
        return self.balance
    
    def withdraw_money(self, money):
        self.balance -= money
        return self.balance

class SavingAccount(BankAccount):
    def __init__(self, min_balance):
        super().__init__()
        self.min_balance = min_balance
    
    def withdraw_money(self, money):
        if self.balance - money >= self.min_balance:
            return super().withdraw_money(money)
        else:
            print(f"Cannot withdraw. Minimum balance is {self.min_balance}")
            return None

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
        while True:
            try:
                add_money = input('Do you want to add money [yes] or [no]: ')

                if add_money in ('yes' 'no'):
                    return add_money
                else:
                    raise  ValueError ('Input must be [yes] or [no]')
            except ValueError as e:
                print(f'{e}')
        
    
    def ask_withdraw_option(self):
        while True:
            try:
                withdraw_money = input('Do you want to withdraw money [yes] or [no]: ')
                if withdraw_money in ('yes' 'no'):
                    return withdraw_money
                else:
                    raise  ValueError ('Input must be [yes] or [no]')
            except ValueError as e:
                print(f'{e}')
        
def main():
    menu_handler = Menu()
    account = SavingAccount(100)

    while True:
        user_option = menu_handler.ask_add_option().lower()
        if user_option == 'yes':
            money = menu_handler.ask_for_money()
            print(f"Your Currently Balance: {account.add_money(money)}")
        elif user_option == 'no':
            while True:
                wd_op = menu_handler.ask_withdraw_option()
                if wd_op == 'yes':
                    money = menu_handler.ask_for_money()
                    result = account.withdraw_money(money)
                    if result is not None: 
                        print(f"Your Currently Balance: {account.balance}")
                    else:
                         print(f"You cannot withdraw that mount. your balance is {account.balance}")

                elif wd_op == 'no':
                    break
                else:
                    print('Error')
            break
        else:
            print('Error')
        

if __name__ == '__main__':
    main()
