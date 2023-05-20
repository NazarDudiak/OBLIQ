import random
import string


def generate(length=32, symbols_type=None):
    """
    :param length: length of token which will generate
    :param symbols_type: [0] = lower, [1] = upper, [2] = num, [3] = symbols
    :return: generated token
    """
    if symbols_type is None:
        symbols_type = [1, 1, 1, 0]
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all_symbols = ""

    if symbols_type[0] == 1:
        all_symbols += lower
    if symbols_type[1] == 1:
        all_symbols += upper
    if symbols_type[2] == 1:
        all_symbols += num
    if symbols_type[3] == 1:
        all_symbols += symbols

    temp = random.sample(all_symbols*5, length)
    token = "".join(temp)
    return token
