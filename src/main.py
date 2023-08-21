## Задача
#Реализуйте функцию, которая выводит на экран список из 5 последних выполненных клиентом операций в формате:
#<дата перевода> <описание перевода>
#<откуда> -> <куда>
#<сумма перевода> <валюта>

# Пример вывода для одной операции:
#14.10.2018 Перевод организации
#Visa Platinum 7000 79** **** 6361 -> Счет **9638
#82771.72 руб.

### Требования

#- Последние 5 выполненных (EXECUTED) операций выведены на экран.
#- Операции разделены пустой строкой.
#- Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018).
#- Сверху списка находятся самые последние операции (по дате).
#- Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX (видны первые 6 цифр и
# последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
#- Номер счета замаскирован и не отображается целиком в формате  **XXXX
#(видны только последние 4 цифры номера счета).

#По каждой операции есть следующие данные:

#- `id` — id транзакциии
#- `date` — информация о дате совершения операции
#- `state` — статус перевода:
#    - `EXECUTED`  — выполнена,
#    - `CANCELED`  — отменена.
#- `operationAmount` — сумма операции и валюта
#- `description` — описание типа перевода
#- `from` — откуда (может отсутстовать)
#- `to` — куда

#0. Импорт всех необходимых функций и классов
from config import JSON_PATH

from utils import load_operations, take_only_executed, get_last_operations, transformation_date, printout


def main():
    operations = load_operations(JSON_PATH)
#    print(operations)                #для отладки, проверяю что загружено

    operations_executed = take_only_executed(operations)
#    print(operations_executed)        #для отладки
    last_operations = get_last_operations(operations_executed)
#    print(last_operations)            #для отладки
    last_operations_date = transformation_date(last_operations)
    #    print(last_operations_date)   #для отладки
    print(printout(last_operations_date))

if __name__ == '__main__':
    main()
