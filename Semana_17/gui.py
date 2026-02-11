import FreeSimpleGUI as sg
from datetime import date
from movement import Movement
import re
 


class InterfaceHandler:

    def __init__(self):
        pass
             
    def ask_for_financial_movement(self):
        today_date = date.today()

        layout = [
            [sg.Text("Add your Category Name"),sg.InputText(key="-CATEGORY-")],
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
                 category = values["-CATEGORY-"].strip()

                 if category == "":
                    sg.popup("Category name cannot be empty value")
                    continue
                 
                 if not category.isalpha():
                     sg.popup("Invalid input: numbers or special values are not allowed")
                     continue                  
                
                 window.close()
                 return {       
                    "today_time": today_date,
                    "category_name": category,
                    "cost": values["-COST-"],
                    "movement_type": values["-MV_TYPE-"]
                }
            
    def display_information(self, actions_handler):               
        headings = ["Date", "Category", "Cost", "Type"]

        layout = [
            [sg.Table(
                values=actions_handler.create_list_table(),
                headings=headings,
                key="-TABLE-",
                auto_size_columns=False,
                col_widths=[15, 20, 10, 10],
                justification="center",
                num_rows=10
            )],
            [sg.Button("Add Movement"), sg.Button("Cancel")],
        ]

        window = sg.Window("Movements Table", layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == "Cancel":
                break

            if event == "Add Movement":

                mv_data = self.ask_for_financial_movement()
                if mv_data is None:
                    continue

                new_movement = Movement(
                    mv_data["today_time"],
                    mv_data["category_name"],
                    mv_data["cost"],
                    mv_data["movement_type"]
                )

                actions_handler.add_movement(new_movement)

                window["-TABLE-"].update(values=actions_handler.create_list_table())

        window.close()
