import random
import string

"""

"""
def generate_key_class():
    """Generates a class key consisting of characters from A-Z and 0-9.

    Returns:
        str: A string representing the generated class key with a length of 6 characters.
    """
    while True:
        
        key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return key
