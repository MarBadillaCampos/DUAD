import os
class Person:
    def __init__(self, name):
        self.name = name

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = [] 

    def ask_for_passenger(self):
        return self._ask_yes_no('Do you want to add a new passenger [yes] or [no]: ')
    
    def ask_passenger_name(self):
        while True:
            try:
                name = input('Add your Full Name: ')
                if not name.replace(" ", "").isalpha():
                    raise ValueError('Name must contain letters only. Please, try again!')
                return name
            except ValueError as e:
                print(f"Invalid input: {e}")
          
    def add_passenger(self, passenger):       
        if self.get_list_len() < self.max_passengers:
            self.passengers.append(passenger)
            print(f"Passenger [{passenger.name}] boarded the Bus.")
        else:
            print("The bus is full!")

    def get_list_len(self):
        return len(self.passengers)
    
    def ask_drop_off_passenger(self):
        return self._ask_yes_no('Would you like to drop off any passenger [yes] or [no]: ')
    
    def drop_off_name(self):
        while True:
            try:
                name = input('Add the name that you would like to drop off: ')
                if not name.replace(" ", "").isalpha():
                    raise ValueError('Name must contain letters only. Please, try again!')
                return name
            except ValueError as e:
                print(f"Invalid input: {e}")
    
    def passengers_list_name(self):
        return self._ask_yes_no('Would you like to see the passengers list [yes] or [no]: ')

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _ask_yes_no(self, prompt):
        while True:
            try:
                op = input(prompt).strip().lower()
                if op in ('yes', 'no'):
                    return op
                else:
                    raise ValueError('Input must be [yes] or [no]')
            except ValueError as e:
                print(f'{e}')

    def show_passengers(self):
        if self.get_list_len() == 0:
            print("\nNo passengers on board.")
            return False
        print("\nPassengers on board:")
        for p in self.passengers:
            print(f"   - {p.name}")
        return True

    def drop_passenger(self,drop_name):
        for pass_aux in self.passengers:
            if pass_aux.name == drop_name:
               self.passengers.remove(pass_aux)
               print(f"\nPassenger [{pass_aux.name}] dropped off the Bus.")
               break
        else:
            print(f"Passenger [{pass_aux.name}] not found on board.")


class Main:
    def __init__(self):
        pass
    def actions(self, sits):
        bus = Bus(sits)
        while True:
            try:
                if bus.get_list_len() >= bus.max_passengers:
                    print("\n" + "="*50)
                    print("No more passengers can be added. The bus is FULL!")
                    print("="*50)

                    see_list = bus.passengers_list_name()
                    if see_list == 'yes':
                        bus.show_passengers()
                        drop = bus.ask_drop_off_passenger()
                        if drop == 'yes':
                            name = bus.drop_off_name()
                            bus.drop_passenger(name)
                            bus.show_passengers()
                            break
                        else:
                            break  
                    else:
                        drop = bus.ask_drop_off_passenger()
                        if drop == 'yes':
                            bus.drop_passenger(name)
                        else:
                            break 
                else:
                    op =  bus.ask_for_passenger()
                    if op == 'yes':
                        name = bus.ask_passenger_name()
                        passenger = Person(name) 
                        bus.add_passenger(passenger)
                    elif op == 'no':
                        see_list = bus.passengers_list_name()
                        if see_list == 'yes':
                            bus.show_passengers()
                            drop = bus.ask_drop_off_passenger()
                            if drop == 'yes':
                                name = bus.drop_off_name()
                                bus.drop_passenger(name)
                                bus.show_passengers()
                                break
                            else:
                                break
                    else:
                        print('Error')
            except Exception as e:
                print(f'An unexpected error occurred: {e}')



ux = Main()
ux.actions(3)
