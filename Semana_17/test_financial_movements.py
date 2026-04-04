from actions import actionHandler
import unittest
from unittest.mock import mock_open, patch
from data import DataHandler
import pytest

class MockMovement:
    def __init__(self, cost):
        self.cost = cost


def test_get_total_income():
    income_list = [
        MockMovement(1500),
        MockMovement(2000),
        MockMovement(500)
    ]

    ac_handler = actionHandler()
    result = ac_handler.get_total_income(income_list)

    assert result == 4000

def test_get_total_expense():
    expense_list = [
        MockMovement(100),
        MockMovement(200),
        MockMovement(3000)
    ]
    ac_handler = actionHandler()
    result = ac_handler.get_total_expense(expense_list)

    assert result == 3300

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


def test_financial_movements_file_not_found():
    data_handler = DataHandler()

    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            data_handler.validate_data("no_fake_file.csv")