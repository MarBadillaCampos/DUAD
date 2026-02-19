import FreeSimpleGUI as sg
from datetime import date
from movement import Movement
import re
 


class InterfaceHandler:

    def __init__(self):
        pass
             
    def ask_for_financial_movement(self):
        today_date = date.today().strftime("%d-%m-%Y")

        layout = [
            [sg.Text("Add your Category Name"),sg.InputText(key="-CATEGORY-")],
            [sg.Input(today_date, disabled=True)],
            [sg.Text('Cost: '), sg.InputText(key="-COST-")],
            [sg.Text('Movement Type:'), 
            sg.Radio("Income", "MOVEMENT", key="-INCOME-", default=True),
            sg.Radio("Expense", "MOVEMENT", key="-EXPENSE-")],
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
                 cost = values["-COST-"]
                 today_date = str(today_date)


                 if values["-INCOME-"]:
                    movement_type = 'ingreso'

                 if values["-EXPENSE-"]:
                     movement_type = 'gasto'

                 if category == "":
                    sg.popup("Category name cannot be empty value")
                    continue
                 
                 if not all(word.isalpha() for word in category.split(" ")):
                     sg.popup("Invalid input: numbers or special values are not allowed")
                     continue
                 try:
                     new_cost = float(cost)

                     if  new_cost <= 0:
                         sg.popup("Cost must be greater than 0")
                         continue
                  
                 except ValueError:
                     sg.popup("Invalid input")
                     continue
                 
                 window.close()
                 return {       
                    "today_time": today_date,
                    "category_name": category,
                    "cost": new_cost,
                    "movement_type": movement_type
                }

            
    def display_information(self, actions_handler):               
        headings = ["Date", "Category", "Cost", "Type"]

        layout = [
            [sg.Table(
                values=actions_handler.create_list(),
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
                

                window["-TABLE-"].update(values=actions_handler.create_list())

        window.close()
