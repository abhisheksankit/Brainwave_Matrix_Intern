import re

# Optional: Add a list of common passwords
COMMON_PASSWORDS = ["123456", "password", "admin", "qwerty", "letmein", "abc123"]

def check_password_strength(password):
    score = 0
    suggestions = []

    # Check length
    if len(password) >= 12:
        score += 30
    elif len(password) >= 8:
        score += 20
        suggestions.append("Make your password longer (12+ characters).")
    else:
        score += 5
        suggestions.append("Password too short. Use at least 8 characters.")

    # Check lowercase
    if re.search(r"[a-z]", password):
        score += 10
    else:
        suggestions.append("Add lowercase letters.")

    # Check uppercase
    if re.search(r"[A-Z]", password):
        score += 10
    else:
        suggestions.append("Add uppercase letters.")

    # Check digits
    if re.search(r"[0-9]", password):
        score += 10
    else:
        suggestions.append("Add numbers.")

    # Check special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 15
    else:
        suggestions.append("Add special characters (!@#$ etc).")

    # Check common passwords
    if password.lower() in COMMON_PASSWORDS:
        score -= 20
        suggestions.append("Avoid using common passwords.")

    # Final judgment
    if score >= 75:
        strength = "Strong"
    elif score >= 50:
        strength = "Moderate"
    else:
        strength = "Weak"

    return score, strength, suggestions

if __name__ == "__main__":
    password = input("Enter your password: ")
    score, strength, suggestions = check_password_strength(password)

    print(f"\nScore: {score}/100")
    print(f"Strength: {strength}")
    if suggestions:
        print("Suggestions:")
        for tip in suggestions:
            print(f"- {tip}")
