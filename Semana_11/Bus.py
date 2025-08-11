import os

class Person:
    def __init__(self, name):
        self.name = name
    

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = [] 

    def ask_for_passenger(self):
        while True:
            try:
                op = input('Do you want to add a new passenger [yes] or [no]: ').strip().lower()
                if op in ('yes', 'no'):
                    return op
                else:
                    raise ValueError('Input must be [yes] or [no]')
            except ValueError as e:
                print(f'{e}')
    
    def ask_passenger_name(self):
        while True:
            try:
                name = input('Add your Full Name: ')
                if not name.replace(" ", "").isalpha():
                    raise ValueError('Name must contain letters only. Please, try again!')
                break
            except ValueError as e:
                print(f"Invalid input: {e}")
        return name
          
    def add_passenger(self, passenger):       
        if self.get_list_len() < self.max_passengers:
            self.passengers.append(passenger)
            print(f"This passenger [{passenger}] boarded the Bus.")
        else:
            print("The bus is full!")

    def get_list_len(self):
        return len(self.passengers)
    
    def ask_drop_off_passenger(self):
        while True:
            try: 
                op = input('Would you like to drop off any passenger: [Yes] or [No] ').strip().lower()

                if op in ('yes', 'no'):
                    return op
                else:
                    raise ValueError ('Input must be [yes] or [no]')
            except ValueError as e:
                print(f'{e}')
    
    def drop_off_name(self):
        while True:
            try:
                name = input('Add the name that you would like to drop off: ')
                if not name.replace(" ", "").isalpha():
                    raise ValueError('Name must contain letters only. Please, try again!')
                break
            except ValueError as e:
                print(f"Invalid input: {e}")
        return name
    
    def passengers_list_name(self):
        while True:
            try: 
                op = input('Would you like to see the passengers list: [Yes] or [No] ').strip().lower()

                if op in ('yes', 'no'):
                    return op
                else:
                    raise ValueError ('Input must be [yes] or [no]')
            except ValueError as e:
                print(f'{e}')

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')


class main():
    def __init__(self):
        pass
     
    def actions(self, sits):
        marcopolo = Bus(sits)
        while True:
            try:
                if marcopolo.get_list_len() >= marcopolo.max_passengers:
                    print("********No more passengers can be added. Bus is full!****")
                    opt = marcopolo.passengers_list_name()
                    if opt == 'yes':
                        print(marcopolo.passengers)
                        drop_off_p = marcopolo.ask_drop_off_passenger()
                        if drop_off_p == 'yes':
                            name = marcopolo.drop_off_name()
                            index = marcopolo.passengers.index(name)
                            deleted_item = marcopolo.passengers.pop(index)
                            print(f'This passenger {deleted_item} drop off the Bus')
                            print(marcopolo.passengers)
                            break
                    else:
                        break
                opt = marcopolo.ask_for_passenger()
                if opt == 'yes':
                    name = marcopolo.ask_passenger_name()
                    marcopolo.add_passenger(name)
                else:
                    break
            except:
                print('Error')


ux = main()
ux.actions(2)
