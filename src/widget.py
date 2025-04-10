from masks import get_mask_card_number
from masks import get_mask_account

def mask_account_card(name_and_number_card: str) -> str:
    name_and_number_card_list = name_and_number_card.split()
    name_card = ""
    number_card = ""

    for el in name_and_number_card_list:
        if el.isalpha():
            name_card += el + ' '
        else:
            number_card += el

    if len(number_card) == 16:
        return f"{name_card}{get_mask_card_number(number_card)}"

    return f"{name_card}{get_mask_account(number_card)}"

print(mask_account_card("Счет 73654108430135874305"))