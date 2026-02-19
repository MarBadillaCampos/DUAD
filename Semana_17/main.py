from gui import InterfaceHandler
from actions import actionHandler
from data import DataHandler


def main():
    gui_handler = InterfaceHandler()
    actions_handler = actionHandler()
    data_handler = DataHandler()

    gui_handler.display_information(actions_handler)

    #Json
    file = "./Semana_17/json/financial_movements.json"
    data_handler.import_data(file)
    data_handler.validate_path(file)
    new_list = actions_handler.create_list()
    data_handler.save_data(file, new_list)

    #CSV



if __name__ == '__main__':
    main()