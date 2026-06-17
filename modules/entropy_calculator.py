import math
import re


def calculate_entropy(password: str) -> float:
    if not password:
        return 0.0

    charset_size = 0

    if re.search(r"[a-z]", password):
        charset_size += 26
    if re.search(r"[A-Z]", password):
        charset_size += 26
    if re.search(r"[0-9]", password):
        charset_size += 10
    if re.search(r"[^A-Za-z0-9]", password):
        charset_size += 33

    if charset_size == 0:
        return 0.0

    entropy = len(password) * math.log2(charset_size)
    return round(entropy, 2)
