import hashlib
import multiprocessing as mp
from typing import Union, Optional

from tqdm import tqdm


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


def enumerate_card_num(
        original_hash: str,
        last_numbers: str,
        bins: tuple,
        pools: int
) -> Optional[str]:
    """
    The function enumerates the true card number by known hash
    :arg original_hash - hash value of desired card number
    :arg bins - tuple of possible card BINs
    :arg last_numbers - four last digits of desired card number
    :arg pools - number of generated processes
    :return: enumerated card number if it was found and None instead
    """
    arguments = []
    for i in range(1000000):
        arguments.append((i, original_hash, bins, last_numbers))
    with mp.Pool(processes=pools) as p:
        for result in p.starmap(
                check_card_number,
                tqdm(
                    arguments,
                    desc="The process of enumerating the true card number: ",
                    ncols=120)):
            if result:
                p.terminate()
                return result
    return None
