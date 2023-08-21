#0. Импорт функций подлежащих тестированию

from src.utils import load_operations, take_only_executed, get_last_operations, transformation_date, printout
import pytest

# Создаем фикстуру, которая запускается перед каждым тестом
#@pytest.fixture
#def operations():
#    return [
#  {
#    "id": 441945886,
#    "state": "EXECUTED",
#    "date": "2019-08-26T10:50:58.294041",
#    "operationAmount": {
#      "amount": "31957.58",
#      "currency": {
#        "name": "руб.",
#        "code": "RUB"
#      }
#    },
#    "description": "Перевод организации",
#    "from": "Maestro 1596837868705199",
#    "to": "Счет 64686473678894779589"
#  },
#  {
#    "id": 596171168,
#    "state": "EXECUTED",
#    "date": "2018-07-11T02:26:18.671407",
#    "operationAmount": {
#      "amount": "79931.03",
#      "currency": {
#        "name": "руб.",
#        "code": "RUB"
#      }
#    },
#    "description": "Открытие вклада",
#    "to": "Счет 72082042523231456215"
#  },
#  {
#    "id": 594226727,
#    "state": "CANCELED",
#    "date": "2018-09-12T21:27:25.241689",
#    "operationAmount": {
#      "amount": "67314.70",
#      "currency": {
#        "name": "руб.",
#        "code": "RUB"
#      }
#    },
#    "description": "Перевод организации",
#    "from": "Visa Platinum 1246377376343588",
#    "to": "Счет 14211924144426031657"
#  },
#  {}
#]

operations = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 596171168,
    "state": "EXECUTED",
    "date": "2018-07-11T02:26:18.671407",
    "operationAmount": {
      "amount": "79931.03",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 72082042523231456215"
  },
  {
    "id": 594226727,
    "state": "CANCELED",
    "date": "2018-09-12T21:27:25.241689",
    "operationAmount": {
      "amount": "67314.70",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 1246377376343588",
    "to": "Счет 14211924144426031657"
  },
  {
    "id": 558167602,
    "state": "EXECUTED",
    "date": "2019-04-12T17:27:27.896421",
    "operationAmount": {
      "amount": "43861.89",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 73654108430135874305",
    "to": "Счет 89685546118890842412"
  },
  {},
  {
    "id": 667307132,
    "state": "EXECUTED",
    "date": "2019-07-13T18:51:29.313309",
    "operationAmount": {
      "amount": "97853.86",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 1308795367077170",
    "to": "Счет 96527012349577388612"
  }
]


def test_take_only_executed():
    '''на вход подается набор тестовых операций, присвоенный переменной operations'''
    assert take_only_executed(operations) == [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 596171168,
    "state": "EXECUTED",
    "date": "2018-07-11T02:26:18.671407",
    "operationAmount": {
      "amount": "79931.03",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "from": None,
    "to": "Счет 72082042523231456215"
  },
  {
    "id": 558167602,
    "state": "EXECUTED",
    "date": "2019-04-12T17:27:27.896421",
    "operationAmount": {
      "amount": "43861.89",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 73654108430135874305",
    "to": "Счет 89685546118890842412"
  },
  {
    "id": 667307132,
    "state": "EXECUTED",
    "date": "2019-07-13T18:51:29.313309",
    "operationAmount": {
      "amount": "97853.86",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 1308795367077170",
    "to": "Счет 96527012349577388612"
  }
]


operations_executed = [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 596171168,
    "state": "EXECUTED",
    "date": "2018-07-11T02:26:18.671407",
    "operationAmount": {
      "amount": "79931.03",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "from": None,
    "to": "Счет 72082042523231456215"
  },
  {
    "id": 594226727,
    "state": "CANCELED",
    "date": "2018-09-12T21:27:25.241689",
    "operationAmount": {
      "amount": "67314.70",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 1246377376343588",
    "to": "Счет 14211924144426031657"
  },
  {
    "id": 558167602,
    "state": "EXECUTED",
    "date": "2019-04-12T17:27:27.896421",
    "operationAmount": {
      "amount": "43861.89",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 73654108430135874305",
    "to": "Счет 89685546118890842412"
  },
  {
    "id": 667307132,
    "state": "EXECUTED",
    "date": "2019-07-13T18:51:29.313309",
    "operationAmount": {
      "amount": "97853.86",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 1308795367077170",
    "to": "Счет 96527012349577388612"
  }
]

def test_get_last_operations():
    '''на вход подается набор тестовых операций, присвоенный переменной operations_executed'''
    assert get_last_operations(operations_executed) == [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
        {
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {
            "amount": "97853.86",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612"
    },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
    {
    "id": 558167602,
    "state": "EXECUTED",
    "date": "2019-04-12T17:27:27.896421",
    "operationAmount": {
      "amount": "43861.89",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 73654108430135874305",
    "to": "Счет 89685546118890842412"
  },
 {'date': '2018-09-12T21:27:25.241689',
  'description': 'Перевод организации',
  'from': 'Visa Platinum 1246377376343588',
  'id': 594226727,
  'operationAmount': {'amount': '67314.70',
                      'currency': {'code': 'RUB', 'name': 'руб.'}},
  'state': 'CANCELED',
  'to': 'Счет 14211924144426031657'}
]

last_operations = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
        {
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {
            "amount": "97853.86",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612"
    },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
    {
    "id": 558167602,
    "state": "EXECUTED",
    "date": "2019-04-12T17:27:27.896421",
    "operationAmount": {
      "amount": "43861.89",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 73654108430135874305",
    "to": "Счет 89685546118890842412"
  },
 {'date': '2018-09-12T21:27:25.241689',
  'description': 'Перевод организации',
  'from': 'Visa Platinum 1246377376343588',
  'id': 594226727,
  'operationAmount': {'amount': '67314.70',
                      'currency': {'code': 'RUB', 'name': 'руб.'}},
  'state': 'CANCELED',
  'to': 'Счет 14211924144426031657'}
]


def test_transformation_date():
    '''на вход подается набор тестовых операций, присвоенный переменной last_operations'''
    assert transformation_date(last_operations) == [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "26.08.2019",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
        {
        "id": 667307132,
        "state": "EXECUTED",
        "date": "13.07.2019",
        "operationAmount": {
            "amount": "97853.86",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612"
    },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "03.07.2019",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
    {
    "id": 558167602,
    "state": "EXECUTED",
    "date": "12.04.2019",
    "operationAmount": {
      "amount": "43861.89",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 73654108430135874305",
    "to": "Счет 89685546118890842412"
  },
 {'date': '12.09.2018',
  'description': 'Перевод организации',
  'from': 'Visa Platinum 1246377376343588',
  'id': 594226727,
  'operationAmount': {'amount': '67314.70',
                      'currency': {'code': 'RUB', 'name': 'руб.'}},
  'state': 'CANCELED',
  'to': 'Счет 14211924144426031657'}
]

last_operations_date = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "26.08.2019",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
        {
        "id": 667307132,
        "state": "EXECUTED",
        "date": "13.07.2019",
        "operationAmount": {
            "amount": "97853.86",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612"
    },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "03.07.2019",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
    {
    "id": 558167602,
    "state": "EXECUTED",
    "date": "12.04.2019",
    "operationAmount": {
      "amount": "43861.89",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 73654108430135874305",
    "to": "Счет 89685546118890842412"
  },
 {'date': '12.09.2018',
  'description': 'Перевод организации',
  'from': 'Visa Platinum 1246377376343588',
  'id': 594226727,
  'operationAmount': {'amount': '67314.70',
                      'currency': {'code': 'RUB', 'name': 'руб.'}},
  'state': 'CANCELED',
  'to': 'Счет 14211924144426031657'}
]


def test_printout():
    '''на вход подается набор тестовых операций, присвоенный переменной last_operations'''
    assert printout(last_operations_date) == None
