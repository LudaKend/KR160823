def load_operations(JSON_PATH):
    '''Загружает список операций из файла json'''
    with open(JSON_PATH, encoding='utf-8') as file:
        import json
        operations_json = json.loads(file.read())
    return operations_json

#print(load_operations(JSON_PATH))       # для отладки
#operations = load_operations() # для отладки

def take_only_executed(operations):
    '''Выбирает из списка операций только выполненые (со статусом EXECUTED)
    для операции "Открытие вклада" параметр "from" заполняет по-умолчанию None
    некорректные пустые словари - не рассматривает'''
    operations_executed = []
    for line in operations:
#        print(line)
        temp_dict = line
#        print(temp_dict) # для отладки
        if temp_dict == {}:
            continue
        if temp_dict["state"] == "EXECUTED":
            operations_executed.append(temp_dict)    #['date']
#            print(operations_executed) # для отладки - здесь всё отлично работает
            if temp_dict["description"] == "Открытие вклада":
                temp_dict["from"] = None
#    print(operations_executed)  # для отладки
    return operations_executed
#temp_dict['pk'] == pk:
#print(take_only_executed(operations)) # для отладки


def get_last_operations(operations_executed):
    '''выбирает пять последних по дате операций'''
#    def get_date(x):               # это конструкция от наставника, не смогла разобраться!
#        return x['date']
#    print(x)
#    print(operations_executed)       # для отладки
    from operator import itemgetter
#    print(operations_executed)
    last_operations = sorted(operations_executed, key=itemgetter('date'), reverse=True) # key=itemgetter('date'),

    return last_operations[:5]


def transformation_date(last_operations):
    '''преобразует дату в формат ДД.ММ.ГГГГ'''
    last_operations_date = []
    for temp_dict in last_operations:
#        print(temp_dict)   # для отладки
        new_date = temp_dict['date']
#        print(new_date)                    # для отладки
        new_date = new_date[:10]
#        print(new_date)                    # для отладки
        new_list = new_date.split('-')
#        print(new_list)                    # для отладки
#        new_list = new_list.reverse()    не сработал метод
#        print(new_list[::-1])              # для отладки
        new_list = new_list[::-1]
#        print(new_list)                    # для отладки
        temp_dict['date'] = '.'.join(new_list)
#        print(temp_dict['date'])           # для отладки
        last_operations_date.append(temp_dict)
#    print(last_operations_date)
    return last_operations_date

def printout(last_operations_date):
    '''выводит на печать полученные данные в требуемом для виджета формате'''
    for temp_dict in last_operations_date:
        print(temp_dict['date'], temp_dict['description'])
        if temp_dict['from'] == None:
            print(f" -> **{temp_dict['to'][-4:]}")
        elif 'Счет' in temp_dict['from']:
            print(f"**{temp_dict['from'][-4:]} -> **{temp_dict['to'][-4:]}")
        else:
            print(f"{temp_dict['from'][:-12]} {temp_dict['from'][-12:-10]}** **** {temp_dict['from'][-4:]} -> **{temp_dict['to'][-4:]}")
        print(temp_dict['operationAmount']['amount'], temp_dict['operationAmount']['currency']['name'])
        print()
