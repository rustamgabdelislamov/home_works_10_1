def get_mask_card_number(card_number: str) -> str:
    """Функция скрывающая полный номер карты"""

    return f'{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}'


def get_mask_account(account: str) -> str:
    """Функция скрывающая полный номер счета"""

    return f'**{account[-4:]}'


