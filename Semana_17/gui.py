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
                  [sg.Button("Accept"), sg.Button("Cancel")]
                  ]

        window = sg.Window("Category", layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                window.close()
                return None
            
            if event == "Accept":
                category = values["-CATEGORY-"].strip()
                if category == "":
                    sg.popup("Category name cannot be empty value")
                    continue

                if not all(word.isalpha() for word in category.split(" ")):
                     sg.popup("Invalid input: numbers or special values are not allowed")
                     continue

                window.close()
                return category
            
    def ask_for_dates(self):
        layout = [[sg.Text("Start Date"),sg.InputText(key="-STARTDATE-")],
                  [sg.Text("End Date"),sg.InputText(key="-ENDDATE-")],
                  [sg.Button("Accept"), sg.Button("Cancel")]
                  ]

        window = sg.Window("DATES", layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                window.close()
                return None
            
            if event == "Accept":
                start_date = values["-STARTDATE-"].strip()
                end_date = values["-ENDDATE-"].strip()

                if start_date == "":
                    sg.popup("Start Date cannot be empty value")
                    continue

                if end_date == "":
                    sg.popup("End Date cannot be empty value")
                    continue

                window.close()
                return  {    
                    "start_date": start_date,
                    "end_date": end_date}

             
    def ask_for_financial_movement(self ):
        today_date = date.today()
        aux_date = today_date.strftime("%d-%m-%Y")

        layout = [
            [sg.Text('Date: '),sg.InputText(key="-DATE-",default_text=aux_date)],
            [sg.Text('Cost: '), sg.InputText(key="-COST-")],
            [sg.Text('Movement Type:'), 
            sg.Radio("Income", "MOVEMENT", key="-INCOME-", default=True),
            sg.Radio("Expense", "MOVEMENT", key="-EXPENSE-")],
            [sg.Button("Accept"), sg.Button("Cancel")]
        ]

        window = sg.Window("Financial Movement", layout)
        
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                window.close()
                return None
            
            if event == "Accept":
                 editable_date = values["-DATE-"]

                 if editable_date == "":
                     sg.popup("Date field is empty, Actual Date will be use instead of")
                     editable_date = today_date

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
                    "today_date": editable_date,
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
            [sg.Text("", key="-FILTERINFO-")],
            [sg.Table(
                values=actions_handler.create_list(),
                headings=headings,
                key="-TABLE-",
                auto_size_columns=False,
                col_widths=[15, 20, 10, 10],
                justification="center",
                num_rows=10
            )],
            [sg.Button("Add Movement"),sg.Button("Filter"), sg.Button("Cancel")],
        ]

        window = sg.Window("Movements Table", layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == "Cancel":
                data_handler.validate_data(file)
                data_handler.save_movements(file, actions_handler.movement_list)
                break
            
            if event == "Filter":
                filter_data = self.ask_for_dates()
                if filter_data is None:
                    break

                start_date = filter_data["start_date"]
                end_date = filter_data["end_date"]

                filtered_movements = actions_handler.filter_by_date(start_date, end_date)

                window["-TABLE-"].update(values=[
                    [m.today_date.strftime("%d-%m-%Y"), m.category, m.cost, m.mv_type]
                    for m in filtered_movements])
                
                window["-FILTERINFO-"].update(f"Filtered from {start_date} to {end_date}")

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
