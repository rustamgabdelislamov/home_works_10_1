def filter_by_state(list_dict: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция которая возвращает список словарей с парметром 'state'"""

    filter_by_state_ = [el for el in list_dict if el.get('state') == state]
    return sort_by_date(filter_by_state_)


def sort_by_date(filter_by_state_: list[dict], sorting=None) -> list[dict]:
    """Функция сортировки по дате"""

    if sorting == None:
        sorted_list = sorted(filter_by_state_, key=lambda x: x['date'], reverse=True)
        return sorted_list

    else:
        sorted_list = sorted(filter_by_state_, key=lambda x: x['date'])
        return sorted_list
