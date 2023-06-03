import hashlib
from typing import Union


def check_card_number(
        main_card_number_part: int,
        original_hash: str,
        bins: tuple,
        last_numbers: str
) -> Union[str, bool]:
    """
    The function assemblies a card number and checks the
    matching the true hash value and a card number hash
    :arg main_card_number_part - unknown part of card_number
    :arg original_hash - hash value of desired card number
    :arg bins - tuple of possible card BINs
    :arg last_numbers - four last digits of desired card number
    :return: card number if a card number hash matches to the
             true hash value and False otherwise
    """
    for card_bin in bins:
        card_number = f"{card_bin}{main_card_number_part:06d}{last_numbers}"
        if hashlib.blake2s(card_number.encode()).hexdigest() == original_hash:
            return card_number
    return False
