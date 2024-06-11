import random
import string


class Helpers:

    @staticmethod
    def random_email(length):
        letters = string.ascii_lowercase + '1234567890'
        random_string = ''.join(random.choice(letters) for i in range(length))

        return f'{random_string}@stellarburgers.com'
