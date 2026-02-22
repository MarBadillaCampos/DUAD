from gui import InterfaceHandler
from actions import actionHandler
from data import DataHandler


def main():
    gui_handler = InterfaceHandler()
    actions_handler = actionHandler()
    data_handler = DataHandler()
    gui_handler.display_information(actions_handler,data_handler)
    



if __name__ == '__main__':
    main()