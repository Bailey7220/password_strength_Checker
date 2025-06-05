import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check for lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check for digit
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Check for special character
    if re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Final feedback
    if score == 5:
        return "Strong password! Good job!"
    else:
        return "Weak password:\n" + "\n".join(feedback)

if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    result = check_password_strength(user_password)
    print(result)
