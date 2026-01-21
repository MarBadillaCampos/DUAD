from gui import InterfaceHandler
from movement import Movement
from actions import actionHandler
from movement import Movement


def main():
    gui_handler = InterfaceHandler()
    actions_handler = actionHandler()

    #Get information from the GUI
    name_category = gui_handler.ask_for_category()
    name_category = name_category['category_name']
    aux_info =  gui_handler.ask_for_financial_movement()
    today_date = aux_info['today_time']
    cost = aux_info['cost']
    movement_type = aux_info['movement_type']

    aux_movement = Movement(today_date,name_category,cost,movement_type)
    actions_handler.add_movement(aux_movement)
    aux_values = actions_handler.read_movement_list()
    print(aux_values)
    #gui_handler.display_information(aux_values)
    #actions_handler.read_movement_list(copy_list)




    


   




if __name__ == '__main__':
    main()