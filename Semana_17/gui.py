import FreeSimpleGUI as sg
from datetime import date


class InterfaceHandler:

    def __init__(self):
        pass


    def ask_for_category(self):
        layout = [[sg.Text("Add your Category Name"),sg.InputText(key="-CATEGORY-")],
                  [sg.Text('Do you want to continue with the process?')],
                  [sg.Button("Aceptar"), sg.Button("Cancel")]
                  ]
        window = sg.Window("Category", layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                window.close()
                return None
            
            if event == "Aceptar":
                window.close()
                return {        
                    "category_name": values["-CATEGORY-"]
                }
    
    def ask_for_financial_movement(self):
        today_date = date.today()

        layout = [
            [sg.Input(today_date.strftime("%Y-%m-%d"), disabled=True)],
            [sg.Text('Cost: '), sg.InputText(key="-COST-")],
            [sg.Text('Movement Type:'), sg.InputText(key="-MV_TYPE-")],
            [sg.Button("Aceptar"), sg.Button("Cancel")]
        ]

        window = sg.Window("Financial Movement", layout)
        
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                window.close()
                return None
            
            if event == "Aceptar":
                window.close()
                return {        
                    "today_time": today_date,
                    "cost": values["-COST-"],
                    "movement_type": values["-MV_TYPE-"]
                }
    def display_information(self,data):
        headings = ["Date", "Category", "Cost", "Type"]
        layout = [
            [sg.Table(
                values=data,
                headings=headings,
                key="-TABLE-",
                auto_size_columns=True,
                justification="center",
                num_rows=5
            )],
            [sg.Button("Salir")]
        ]

        sg.Window("Tabla básica", layout).read(close=True)