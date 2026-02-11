from gui import InterfaceHandler
from movement import Movement
from actions import actionHandler
from movement import Movement


def main():
    gui_handler = InterfaceHandler()
    actions_handler = actionHandler()

    gui_handler.display_information(actions_handler)


if __name__ == '__main__':
    main()