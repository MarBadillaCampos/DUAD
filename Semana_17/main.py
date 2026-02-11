from gui import InterfaceHandler
from actions import actionHandler


def main():
    gui_handler = InterfaceHandler()
    actions_handler = actionHandler()

    gui_handler.display_information(actions_handler)


if __name__ == '__main__':
    main()