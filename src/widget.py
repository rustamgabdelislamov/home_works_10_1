from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name_and_number_card: str) -> str:
    """Функция которая скрывает полный номер карты или счета"""
    name_and_number_card_list = name_and_number_card.split()
    name_card = ""
    number_card = ""

    for el in name_and_number_card_list:
        if el.isalpha():
            name_card += el + " "
        else:
            number_card += el

    if len(number_card) == 16:
        return f"{name_card}{get_mask_card_number(number_card)}"

    return f"{name_card}{get_mask_account(number_card)}"


def get_date(date: str) -> str:
    """Функция которая изменяет формат даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
