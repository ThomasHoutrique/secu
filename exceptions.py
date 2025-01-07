class PasswordException(Exception):
    pass

class PasswordLengthException(PasswordException):
    def __init__(self, message="Le mot de passe doit contenir au moins 12 caractères"):
        self.message = message
        super().__init__(self.message)

class PasswordCompromisedException(PasswordException):
    def __init__(self, message="Le mot de passe a été compromis"):
        self.message = message
        super().__init__(self.message)

class PasswordComplexityException(PasswordException):
    def __init__(self, message="Le mot de passe doit contenir au moins une majuscule, une minuscule, un chiffre et un caractère spécial"):
        self.message = message
        super().__init__(self.message)
