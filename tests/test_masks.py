from src.masks import get_mask_account, get_mask_card_number

def test_get_mask_account():
    assert get_mask_account('11111111111111111234') == '**1234'


def test_get_mask_account_len_figure():
    assert get_mask_account('111111111111111124') == 'Неправильный номер счета'