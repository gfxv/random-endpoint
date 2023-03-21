import random
import string


def generate_path(length) -> str:
    source = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(source) for i in range(length))
    
    return result_str
