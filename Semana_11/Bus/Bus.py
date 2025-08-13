import os
import Person

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
            print(f"Passenger [{passenger}] boarded the Bus.")
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


class Main:
    def __init__(self):
        pass

    def show_passengers(self, bus):
        """Muestra la lista de pasajeros."""
        if bus.get_list_len() == 0:
            print("\nNo passengers on board.")
            return False
        print("\nPassengers on board:")
        for p in bus.passengers:
            print(f"   - {p}")
        return True

    def drop_passenger(self, bus):
        """Gestiona la baja de un pasajero."""
        if bus.get_list_len() == 0:
            print("\nNo passengers to drop off.")
            return
        name = bus.drop_off_name()
        if name in bus.passengers:
            bus.passengers.remove(name)
            print(f"\nPassenger [{name}] dropped off the Bus.")
            print(f"New passenger list on board: {bus.passengers}")
        else:
            print(f"Passenger [{name}] not found on board.")

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
                        self.show_passengers(bus)
                        drop = bus.ask_drop_off_passenger()
                        if drop == 'yes':
                            self.drop_passenger(bus)
                        else:
                            break  
                    else:
                        drop = bus.ask_drop_off_passenger()
                        if drop == 'yes':
                            self.drop_passenger(bus)
                        else:
                            break 

                else:
                    if bus.ask_for_passenger() == 'yes':
                        name = bus.ask_passenger_name()
                        bus.add_passenger(name)
                    else:
                        see_list = bus.passengers_list_name()
                        if see_list == 'yes':
                            self.show_passengers(bus)
                            drop = bus.ask_drop_off_passenger()
                            if drop == 'yes':
                                self.drop_passenger(bus)
                        else:
                            drop = bus.ask_drop_off_passenger()
                            if drop == 'yes':
                                self.drop_passenger(bus)
                        break

            except Exception as e:
                print(f'An unexpected error occurred: {e}')



ux = Main()
ux.actions(2)
