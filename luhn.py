def luhn_algorithm(card_number: str) -> bool:
    """
    Function uses the Luhn algorithm to validate a credit card number
    :arg card_number - card number to validate
    :return: True - if the card number is valid, False - otherwise
    """
    digits = list(map(int, str(card_number)))[::-1]
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] = digits[i] // 10 + digits[i] % 10
    return sum(digits) % 10 == 0
