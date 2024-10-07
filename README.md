# Password Complexity Checker

## Overview

The **Password Complexity Checker** is a Python tool that evaluates the complexity of passwords entered by users. It provides feedback on various password requirements, helping users create secure passwords.

## Features

- Checks the length of the password (minimum 10 characters)
- Validates the presence of:
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Special characters (punctuation)

## Requirements

- Python 3.x
- `os` and `string` modules (included with Python standard library)

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/jesudeyi/PRODIGY_CS_03.git
   ```

2. Run the tool:
   ```bash
   python passwordChecker.py
   ```

3. Follow the prompts to enter a password and receive feedback on its complexity.

## Code Explanation

- **clear_screen()**: Clears the terminal screen based on the operating system.
- **get_password()**: Prompts the user to enter a password.
- **check_len(password)**: Checks if the password meets the minimum length requirement.
- **check_upper(password)**: Validates the presence of at least one uppercase letter.
- **check_lower(password)**: Validates the presence of at least one lowercase letter.
- **check_digit(password)**: Validates the presence of at least one digit.
- **check_special_character(password)**: Validates the presence of at least one special character.

## Example Output

```
Welcome to Password Complexity Checker
Enter your password: examplePassword123!
Your password is long enough.
Your password has enough digits.
Your password should contain a special character!
Do you want to check another password? 
y/n: y
```

## Contribution

Feel free to fork this repository and make contributions. Open issues for any feature requests or bugs.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---
