import re

def check_password_strength(password):
    strength = "Weak"
    is_accepted = False

    length_valid = 8 <= len(password) <= 14
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[@#$%*]', password))

    restricted_words = ["password", "12345", "qwerty", "admin", "username"]
    contains_restricted = False
    for word in restricted_words:
        if word.lower() in password.lower():
            contains_restricted = True
            break

    policy_5_met = not contains_restricted

    all_policy_criteria_met = (
        length_valid and
        has_upper and
        has_lower and
        has_digit and
        has_special and
        policy_5_met
    )

    upper_count = len(re.findall(r'[A-Z]', password))
    lower_count = len(re.findall(r'[a-z]', password))
    digit_count = len(re.findall(r'\d', password))
    special_count = len(re.findall(r'[@#$%*]', password))

    if upper_count >= 2 and lower_count >= 2 and digit_count >= 2 and special_count >= 2:
        if all_policy_criteria_met:
            strength = "Strong"
            is_accepted = True

    if strength != "Strong": 
        if has_upper and has_lower and has_digit and has_special:
            if all_policy_criteria_met:
                strength = "High"
                is_accepted = True
            elif (not length_valid or not policy_5_met): 
                strength = "Moderate"
                is_accepted = False 

    return strength, is_accepted

password_input = input("Enter your password: ")
strength, accepted = check_password_strength(password_input)
print(f"Password Strength: {strength}")
print(f"Password Accepted: {accepted}")