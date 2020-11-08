from src.domain import *


def test_createExpense():
    """
    Test function for creating expenses.
    """
    e1 = createExpense(1, 100, 'gas')
    assert e1['apartmentNumber'] == 1
    assert e1['amount'] == 100
    assert e1['expenseType'] == 'gas'

    e2 = createExpense(4, 120, 'water')
    assert e2['apartmentNumber'] == 4
    assert e2['amount'] == 120
    assert e2['expenseType'] == 'water'


def test_toStr():
    """
    Test function for printing an expense.
    """
    e1 = createExpense(1, 100, 'electricity')
    assert toStr(e1) == "Ap. nr: 1, Amount: 100, Type: electricity"
    e2 = createExpense(2, 120, 'gas')
    assert toStr(e2) == "Ap. nr: 2, Amount: 120, Type: gas"


def runTests():
    test_createExpense()
    test_toStr()
