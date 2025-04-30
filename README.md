# Home_works_10_1
# Этот проект предназначен для сортировки списка словарей по ключевому слову 'state' и дате по убыванию.
## Установка
1. Клонируйте репозиторий ```git@github.com:rustamgabdelislamov/home_works_10_1.git```
2. Установите зависимости ```poetry instal```
3. Для запуска используйте ```python main.py```
### Описание функций
1. Функция filter_by_state
    ```def filter_by_state(list_dict: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция которая возвращает список словарей с парметром 'state'"""

    filter_by_state_ = [el for el in list_dict if el.get('state') == state]
    return sort_by_date(filter_by_state_)
Принимает список словарей и смотрит соответсвует ли аргумент state заданному, если аргумент находится то он добавляется в список filter_by_state_ и далее через функцию sort_by_date сортируется по дате, по убыванию

2. Функция sort_by_date
   ```def sort_by_date(filter_by_state_: list[dict], sorting=None) -> list[dict]:
    """Функция сортировки по дате"""

    if sorting == None:
        sorted_list = sorted(filter_by_state_, key=lambda x: x['date'], reverse=True)
        return sorted_list

    else:
        sorted_list = sorted(filter_by_state_, key=lambda x: x['date'])
        return sorted_list
Принимает аргумент filter_by_state_из предыдущей функции и сортирует список по аргументу date по умолчанию

### Пример работы функции
на входе ```[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-05-29T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
        
на выходе ```[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

### Тестирования
функция get_mask_account тестируется через фиксутры 
функция get_mask_card_number и sort_by_date через accept 
оcтальные функции через параметризацию

