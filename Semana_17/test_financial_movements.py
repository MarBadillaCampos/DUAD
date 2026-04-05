from actions import actionHandler
from unittest.mock import mock_open, patch
from data import DataHandler
from categoryhandler import categoryHandler
from movement import Movement
from datetime import datetime
from category import Category


class MockMovement:
    def __init__(self,today_date,category,cost,mv_type):
        self.today_date = today_date
        self.category = category
        self.cost = cost
        self.mv_type = mv_type


class MockCategory:
    def __init__(self,category_name, color):
        self.category_name = category_name
        self.color = color 


def test_get_total_income():

    income_list = [
        MockMovement("01-04-2026", MockCategory("Comida", "grey"),5000, 'ingreso'),
        MockMovement("01-04-2026", MockCategory("Transporte", "green"),2000, 'ingreso'),
        MockMovement("01-04-2026", MockCategory("Gasolina", "blue"),100, 'ingreso'),
    ]

    ac_handler = actionHandler()
    result = ac_handler.get_total_income(income_list)

    assert result == 7100

def test_get_total_expense():

    expense_list = [
        MockMovement("15-02-2026", MockCategory("Comida", "grey"),2500, 'gasto'),
        MockMovement("25-01-2026", MockCategory("Transporte", "green"),1000, 'gasto'),
        MockMovement("08-03-2026", MockCategory("Gasolina", "blue"),6000, 'gasto'),
    ]
    ac_handler = actionHandler()
    result = ac_handler.get_total_expense(expense_list)

    assert result == 9500

def test_get_profit():
    expense = 4000
    income = 5000

    ac_handler = actionHandler()
    result = ac_handler.get_profit_value(income,expense)
    assert result == 1000

def test_save_movements():

    class MockMovement:
        def to_dict(self):
            return {
                "today_date": "01-01-2024",
                "category_name": "food",
                "color": "red",
                "cost": 1000,
                "mv_type": "ingreso"
            }

    movement_list = [MockMovement(), MockMovement()]

    m = mock_open()

    with patch("builtins.open", m):
        handler = DataHandler()
        handler.save_movements("fake.csv", movement_list, "2000", "500", "1500")
    handle = m()
    written_content = "".join(call.args[0] for call in handle.write.call_args_list)

    assert "Totals" in written_content
    assert "Income: 2000" in written_content
    assert "Expense: 500" in written_content
    assert "Net prof: 1500" in written_content


csv_content = """today_date,category_name,color,cost,mv_type
2024-01-01,food,red,1000,ingreso
2024-01-02,food,blue,abc,ingreso
2024-01-03,food,green,500,
"""


def test_validate_content(tmp_path):
    path = tmp_path / "test.csv"

    with open(path, "w") as f:
        f.write(csv_content)    
    data_handler = DataHandler()
    result = data_handler.read_movements(path)
    assert len(result) == 1
    assert  result[0]["cost"] == 1000.0
    assert isinstance(result[0]["cost"],float)

csv_content_sec= """today_date,category_name,color,cost,mv_type
20-03-2026,food,red,1000,ingreso
20-03-2026,transporte,blue,500,ingreso
20-03-2026,Bonus,green,5000,
"""

def test_load_movements(tmp_path):
     path = tmp_path / "test.csv"

     with open(path, "w") as f:
        f.write(csv_content_sec)    
     data_handler = DataHandler()
     category_handler = categoryHandler()
     result = data_handler.load_movements(path, category_handler)

     assert len(result) == 2
     assert isinstance(result[0], Movement)
     assert result[0].cost == 1000.0
     assert result[0].mv_type == 'ingreso'

def test_filter_by_date():

    expense_list = [
        MockMovement(datetime.strptime("15-01-2026", "%d-%m-%Y").date(), MockCategory("Comida", "grey"),2500, 'gasto'),
        MockMovement(datetime.strptime("25-02-2026", "%d-%m-%Y").date(), MockCategory("Transporte", "green"),1000, 'gasto'),
        MockMovement(datetime.strptime("15-02-2026", "%d-%m-%Y").date(), MockCategory("Gasolina", "blue"),10000, 'gasto'),
        MockMovement(datetime.strptime("08-03-2026", "%d-%m-%Y").date(), MockCategory("Helados", "green"),6000, 'ingreso'),
        MockMovement(datetime.strptime("15-04-2026", "%d-%m-%Y").date(), MockCategory("Libro", "purple"),1500, 'gasto'),

    ]
    start_date = datetime.strptime("15-02-2026", "%d-%m-%Y").date()
    end_date = datetime.strptime("08-03-2026", "%d-%m-%Y").date() 


    ac_handler = actionHandler()
    ac_handler.movement_list = expense_list
    result = ac_handler.filter_by_date(start_date,end_date)

    assert len(result) == 3

def test_filter_by_date_no_results():
    expense_list = [
        MockMovement(datetime.strptime("01-01-2026", "%d-%m-%Y").date(), MockCategory("Computadora", "green"), 100, 'gasto'),
    ]
    start_date = datetime.strptime("01-02-2026", "%d-%m-%Y").date()
    end_date = datetime.strptime("10-02-2026", "%d-%m-%Y").date() 

    ac_handler = actionHandler()
    ac_handler.movement_list = expense_list

    

    result = ac_handler.filter_by_date(start_date, end_date)

    assert result == []

def test_filter_by_date_all_outside_range():
    expense_list = [
        MockMovement(datetime.strptime("01-01-2026", "%d-%m-%Y").date(), MockCategory("Libro", "blue"), 100, 'gasto'),
        MockMovement(datetime.strptime("02-01-2026", "%d-%m-%Y").date(), MockCategory("Zapatos", "red"), 200, 'gasto'),
    ]

    start_date = datetime.strptime("01-02-2026", "%d-%m-%Y").date()
    end_date = datetime.strptime("10-02-2026", "%d-%m-%Y").date() 

    ac_handler = actionHandler()
    ac_handler.movement_list = expense_list

    result = ac_handler.filter_by_date(start_date, end_date)

    assert len(result) == 0


def test_check_category():
        color = "green"
        category_name = "COMIDA"

        category_aux = categoryHandler()
        assert not category_aux.category_color
        result = category_aux.check_category(category_name,color)

        assert isinstance(result, Category)
        assert result.category_name == "comida"
        assert "comida" in category_aux.category_color
        assert category_aux.category_color["comida"] is result


 





     







    


        
