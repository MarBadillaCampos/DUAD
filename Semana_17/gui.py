import FreeSimpleGUI as sg
from datetime import date
from movement import Movement
from data import DataHandler
 


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
                category = values["-CATEGORY-"].strip()
                if category == "":
                    sg.popup("Category name cannot be empty value")
                    continue

                if not all(word.isalpha() for word in category.split(" ")):
                     sg.popup("Invalid input: numbers or special values are not allowed")
                     continue

                window.close()
                return category

             
    def ask_for_financial_movement(self ):
        today_date = date.today().strftime("%d-%m-%Y")

        layout = [
            [sg.Text('Fecha: '),sg.Input(today_date, disabled=True)],
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
                 cost = values["-COST-"]


                 if values["-INCOME-"]:
                    mv_type = 'ingreso'

                 if values["-EXPENSE-"]:
                     mv_type = 'gasto'

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
                    "today_date": today_date,
                    "cost": new_cost,
                    "mv_type": mv_type
                }

            
    def display_information(self, actions_handler,data_handler):               
        headings = ["today_date", "category", "cost", "mv_type"]
        file = "./Semana_17/csv/financial_movements.csv"

        movements = data_handler.load_movements(file)
        for movement in movements:
            actions_handler.add_movement(movement)

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
                data_handler.validate_data(file)
                data_handler.write_csv_file(file, actions_handler.movement_list)
                break

            if event == "Add Movement":
                category_data = self.ask_for_category()
                if category_data is None:
                    continue

                mv_data = self.ask_for_financial_movement()
                if mv_data is None:
                    continue

                new_movement = Movement(
                    mv_data["today_date"],
                    category_data,
                    mv_data["cost"],
                    mv_data["mv_type"]
                )

                actions_handler.add_movement(new_movement)
                
                window["-TABLE-"].update(values=actions_handler.create_list())

        window.close()
