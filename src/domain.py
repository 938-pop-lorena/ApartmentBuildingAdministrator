def createExpense(apartmentNumber: int, amount: int, expenseType: str):
    """
    Creates a new Expense dictionary.

    :param apartmentNumber: Positive integer
    :param amount: Positive integer
    :param expenseType: from one of the predefined categories water, heating, electricity, gas and other
    :return:
    """
    expense = {'apartmentNumber': apartmentNumber,
               'amount': amount,
               'expenseType': expenseType}
    return expense


def getApartmentNumber(expense: dict):
    return expense['apartmentNumber']


def getAmount(expense: dict):
    return expense['amount']


def getExpenseType(expense: dict):
    return expense['expenseType']


def setApartmentNumber(expense: dict, value: int):
    expense['apartmentNumber'] = value


def setAmount(expense: dict, value: int):
    expense['amount'] = value


def setExpenseType(expense: dict, value: str):
    expense['expenseType'] = value


def toStr(expense: dict):
    return "Ap. nr: {}, Amount: {}, Type: {}".format(expense['apartmentNumber'],
                                                     expense['amount'],
                                                     expense['expenseType'])


def isEqual(expense: dict, other: dict):
    if expense['apartmentNumber'] == other['apartmentNumber'] and \
            expense['expenseType'] == other['expenseType']:
        return True
    return False
