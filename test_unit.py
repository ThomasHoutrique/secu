import unittest
from password import Password


class TestPassword(unittest.TestCase):
    def test_password_length(self):
        password: str = Password(password="password")
        self.assertEqual(password.check_length(), True)

if __name__ == "__main__":
    unittest.main()
