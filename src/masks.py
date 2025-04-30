def get_mask_card_number(card_number: str) -> str:
    """Функция скрывающая полный номер карты"""

    if len(card_number) == 16:
        return f'{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}'
    return 'Неправильный номер карты'


def get_mask_account(account: str) -> str:
    """Функция скрывающая полный номер счета"""

    if len(account) == 20:
        return f'**{account[-4:]}'
    return 'Неправильный номер счета'
