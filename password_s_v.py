import re

def validate_password(password):
    # Criteria: >8 chars, upper, lower, digit, special
    if len(password) < 8: return False
    if not re.search(r'[A-Z]', password): return False
    if not re.search(r'[a-z]', password): return False
    if not re.search(r'\d', password): return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password): return False
    return True

password_to_check = input("Enter password :")
validity=validate_password(password_to_check )

print(f"The password is {"valid" if validity==True else "invalid"}")
def validate_email_regex(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.fullmatch(pattern, email):
        return True
    else:
        return False

E_mail=input("Enter E-mail :")
message=validate_email_regex(E_mail)
print(f"Email is {"valid" if E_mail==True else "invalid"}")
