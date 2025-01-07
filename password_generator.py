import random
import string

import requests
from requests.models import Response

from password import Password


class PasswordGenerator:
    def __init__(self) -> None:
        pass

    def generate_classic_password(
        self, length: int, lowercase: bool, uppercase: bool, digits: bool, special: bool,
    ) -> Password:
        characters: str = ""
        if lowercase:
            characters += string.ascii_lowercase
        if uppercase:
            characters += string.ascii_uppercase
        if digits:
            characters += string.digits
        if special:
            characters += string.punctuation

        if not characters:
            msg: str = "Aucun caractère sélectionné"
            raise ValueError(msg)

        password: str = "".join(random.choice(characters) for _ in range(length))
        return Password(password=password)

    def generate_eff_password(self) -> Password:
        password: str = ""
        url: str = "https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt"
        response: Response = requests.get(url, timeout=5)
        if response.status_code != 200:
            msg: str = "Error fetching data from API"
            raise Exception(msg)
        words: list = response.text.splitlines()
        word_dict: dict = {line.split("\t")[0]: line.split("\t")[1] for line in words}

        for _ in range(6):
            picked_numbers: str = "".join(str(random.randint(1, 6)) for _ in range(5))
            if picked_numbers in word_dict:
                password += word_dict[picked_numbers]

        return Password(password=password)
