from modules.analyzer import analyze_password
from modules.generator import generate_password
from modules.comparator import compare_passwords
from modules.history_manager import save_history, save_comparison_history, export_log_file
from modules.report_manager import export_report


def display_analysis(result):
    print("\nPASSWORD ANALYSIS")
    print("-" * 40)
    print(f"Entropy            : {result['entropy']:.2f} bits")
    print(f"Security Score     : {result['score']}/100")
    print(f"Rating             : {result['rating']}")

    print("\nSuggestions")
    print("-" * 40)
    for suggestion in result["suggestions"]:
        print(f"- {suggestion}")


def analyze_password_menu():
    password = input("\nEnter password to analyze: ")
    result = analyze_password(password)
    display_analysis(result)
    save_history(result, "ANALYZE")


def generate_password_menu():
    try:
        length = int(input("\nEnter password length (min=8, max=64): "))
    except ValueError:
        print("\nInvalid input. Default length 16 used.")
        length = 16

    if length < 8:
        print("\nMinimum length is 8. Using 8.")
        length = 8

    if length > 64:
        print("\nMaximum length is 64. Using 64.")
        length = 64

    password = generate_password(length)
    result = analyze_password(password)

    print("\nGenerated Password")
    print("-" * 40)
    print(password)

    display_analysis(result)
    save_history(result, "GENERATE")


def compare_passwords_menu():
    password1 = input("\nEnter first password: ")
    password2 = input("Enter second password: ")

    result1, result2, stronger = compare_passwords(password1, password2)

    print("\nPASSWORD COMPARISON")
    print("=" * 40)

    print("\nPassword 1")
    print("-" * 20)
    print(f"Score  : {result1['score']}/100")
    print(f"Rating : {result1['rating']}")

    print("\nPassword 2")
    print("-" * 20)
    print(f"Score  : {result2['score']}/100")
    print(f"Rating : {result2['rating']}")

    print("\nResult")
    print("-" * 20)
    print(f"Stronger Password : {stronger}")

    save_comparison_history(result1, result2, stronger)


def main():
    while True:
        print("\n" + "=" * 40)
        print("PASSWORD SECURITY ANALYZER")
        print("=" * 40)
        print("1. Analyze Password")
        print("2. Generate Password")
        print("3. Compare Passwords")
        print("4. Export Log File")
        print("5. Export Security Report")
        print("6. Exit")

        choice = input("\nSelect option: ")

        if choice == "1":
            analyze_password_menu()
        elif choice == "2":
            generate_password_menu()
        elif choice == "3":
            compare_passwords_menu()
        elif choice == "4":
            export_log_file()
        elif choice == "5":
            export_report()
        elif choice == "6":
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()
