# Password Complexity Checker
# Compares password to breached databases using zxcvbn

import zxcvbn

def main(password):
    # Looks at password
    # compares it against serveral factors
    results = zxcvbn(password)
    return results.score


if __name__ == '__main__':
    user_pass = input("What is your password: ")
    print("\n")
    main(user_pass)

