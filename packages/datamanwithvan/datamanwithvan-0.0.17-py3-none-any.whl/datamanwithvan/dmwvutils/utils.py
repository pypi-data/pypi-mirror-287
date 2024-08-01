import random
import string


class Utils:

    dummy_attribute = None

    def __init__(self):
        pass

    def generate_random_string(self, length):
        """
        Generate a random string of specified length containing
        numbers and Latin characters.

        Parameters:
        - length (int): The length of the string to be generated.

        Returns:
        - str: A random string of specified length.
        """
        # Define the set of characters to choose from
        characters = string.ascii_letters + string.digits
        # Use random.choices to generate a list of characters
        # of the specified length
        random_string = ''.join(random.choices(characters, k=length))
        return random_string
