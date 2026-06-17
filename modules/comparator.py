from modules.analyzer import analyze_password


def compare_passwords(password1: str, password2: str):
    result1 = analyze_password(password1)
    result2 = analyze_password(password2)

    if result1["score"] > result2["score"]:
        stronger = "Password 1"
    elif result2["score"] > result1["score"]:
        stronger = "Password 2"
    else:
        stronger = "Both passwords have equal strength"

    return result1, result2, stronger
