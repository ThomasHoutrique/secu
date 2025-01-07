from hashlib import sha1
from math import log2

from requests import get
from requests.models import Response


class Password:
    def __init__(self, password: str) -> None:
        self.password = password
        self.password_min_length = 12

    def check_length(self) -> bool:
        return len(self.password) < self.password_min_length

    def check_pwned(self) -> bool:
        url: str = "https://api.pwnedpasswords.com/range/"
        sha1_password: str = sha1(self.password.encode()).hexdigest().upper()
        prefix: str = sha1_password[:5]
        response: Response = get(url + prefix, timeout=5)
        if response.status_code != 200:
            msg: str = "Error fetching data from API"
            raise Exception(msg)
        return any(sha1_password[5:] in line for line in response.text.splitlines())

    def check_complexity(self) -> bool:
        return not (
            any(c.isupper() for c in self.password)
            and any(c.islower() for c in self.password)
            and any(c.isdigit() for c in self.password)
            and any(not c.isalnum() for c in self.password)
        )

    def check_entropy(self) -> bool:
        """Checking the entropy using H = log2(S^L)."""
        char_set: set = set(self.password)
        char_set_size: set = len(char_set)
        password_size: int = len(self.password)
        return log2(char_set_size**password_size)
