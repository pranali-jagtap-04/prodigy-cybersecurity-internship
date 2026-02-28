import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase letter check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase letter check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Strength evaluation
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback


# 
password = input("Enter your password: ")
strength, feedback = check_password_strength(password)

print("\nPassword Strength:", strength)

if feedback:
    print("Suggestions to improve your password:")
    for tip in feedback:
        print("-", tip)
else:
    print("Your password is strong and secure! ")