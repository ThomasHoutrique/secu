import argparse

from exceptions import (
    PasswordComplexityException,
    PasswordLengthException,
)
from password import Password
from password_generator import PasswordGenerator


def generate_password(length: int, lowercase: bool, uppercase: bool, digits: bool, special: bool) -> Password:
    generator: PasswordGenerator = PasswordGenerator()
    return generator.generate_classic_password(
        length=length,
        lowercase=lowercase,
        uppercase=uppercase,
        digits=digits,
        special=special,
    )

def check_password(user_password: str) -> float:
    checker: Password = Password(password=user_password)
    if checker.check_length():
        raise PasswordLengthException
    if checker.check_pwned():
        raise PasswordPwnedException
    if checker.check_complexity():
        raise PasswordComplexityException
    return checker.check_entropy()


def main() -> None:
    parser = argparse.ArgumentParser(description="Password utility")
    subparsers = parser.add_subparsers(dest="command")

    check_parser = subparsers.add_parser("check", help="Check password security")
    check_parser.add_argument("password", help="Password to check")

    generate_parser = subparsers.add_parser(
        "generate", help="Generate a secure password",
    )
    generate_parser.add_argument("length", type=int, help="Length of the password")
    generate_parser.add_argument(
        "--lowercase", action="store_true", help="Include lowercase letters",
    )
    generate_parser.add_argument(
        "--uppercase", action="store_true", help="Include uppercase letters",
    )
    generate_parser.add_argument("--digits", action="store_true", help="Include digits")
    generate_parser.add_argument(
        "--special", action="store_true", help="Include special characters",
    )

    subparsers.add_parser(
        "generate_eff", help="Generate a secure EFF password",
    )

    args = parser.parse_args()

    if args.command == "check":
        entropy = check_password(user_password=args.password)
        print(f"Le mot de passe est sécurisé avec une entropie de {round(entropy,2)}")
    elif args.command == "generate":
        classic_password: float = generate_password(
            length=args.length,
            lowercase=args.lowercase,
            uppercase=args.uppercase,
            digits=args.digits,
            special=args.special,
        )
        print(f"Mot de passe généré: {classic_password.password} avec une entropie de {round(classic_password.check_entropy(),2)}")
    elif args.command == "generate_eff":
        eff_password = PasswordGenerator().generate_eff_password()
        print(f"Mot de passe EFF généré: {eff_password.password} avec une entropie de {round(eff_password.check_entropy(),2)}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
