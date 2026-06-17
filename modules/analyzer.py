import re
from pathlib import Path
from modules.entropy_calculator import calculate_entropy


COMMON_PASSWORD_FILE = Path("data/common_passwords.txt")


def load_common_passwords():
    COMMON_PASSWORD_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not COMMON_PASSWORD_FILE.exists():
        COMMON_PASSWORD_FILE.write_text("", encoding="utf-8")

    with open(COMMON_PASSWORD_FILE, "r", encoding="utf-8") as file:
        return {line.strip().lower() for line in file if line.strip()}


def get_rating(score):
    if score >= 80:
        return "Very Strong"
    elif score >= 60:
        return "Strong"
    elif score >= 40:
        return "Moderate"
    return "Weak"


def analyze_password(password: str):
    suggestions = []
    common_passwords = load_common_passwords()

    if not password:
        return {
            "length": 0,
            "score": 0,
            "rating": "Weak",
            "entropy": 0.0,
            "has_lower": False,
            "has_upper": False,
            "has_digit": False,
            "has_symbol": False,
            "suggestions": ["Enter a password to analyze."]
        }

    length = len(password)
    score = 0

    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_symbol = bool(re.search(r"[^A-Za-z0-9]", password))

    password_lower = password.lower()

    if password_lower in common_passwords:
        return {
            "length": length,
            "score": 0,
            "rating": "Weak",
            "entropy": calculate_entropy(password),
            "has_lower": has_lower,
            "has_upper": has_upper,
            "has_digit": has_digit,
            "has_symbol": has_symbol,
            "suggestions": ["Avoid common passwords."]
        }

    if re.search(r"(.)\1{2,}", password):
        score -= 10
        suggestions.append("Avoid repeated characters.")

    if re.search(r"(1234|abcd|qwerty|asdf|password)", password, re.IGNORECASE):
        score -= 10
        suggestions.append("Avoid predictable sequences.")

    if re.search(r"(19|20)\d{2}", password):
        score -= 10
        suggestions.append("Avoid using years.")

    if length >= 8:
        score += 25
    else:
        suggestions.append("Use at least 8 characters.")

    if length >= 12:
        score += 25
    else:
        suggestions.append("Use 12 or more characters for better security.")

    if has_lower:
        score += 10
    else:
        suggestions.append("Add lowercase letters.")

    if has_upper:
        score += 10
    else:
        suggestions.append("Add uppercase letters.")

    if has_digit:
        score += 10
    else:
        suggestions.append("Include numbers.")

    if has_symbol:
        score += 20
    else:
        suggestions.append("Include symbols like !@#$.")

    score = max(0, min(100, score))

    return {
        "length": length,
        "score": score,
        "rating": get_rating(score),
        "entropy": calculate_entropy(password),
        "has_lower": has_lower,
        "has_upper": has_upper,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
        "suggestions": suggestions if suggestions else ["Password passed all checks."]
    }
