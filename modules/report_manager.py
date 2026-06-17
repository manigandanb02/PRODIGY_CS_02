from datetime import datetime
from pathlib import Path


LOG_FILE = Path("reports/password_security.log")
REPORT_FILE = Path("reports/security_report.txt")


def ensure_report_files():
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not LOG_FILE.exists():
        LOG_FILE.write_text("", encoding="utf-8")

    if not REPORT_FILE.exists():
        REPORT_FILE.write_text("", encoding="utf-8")


def export_report():
    ensure_report_files()

    log_data = LOG_FILE.read_text(encoding="utf-8")

    analyze_count = log_data.count("ANALYZE |")
    generate_count = log_data.count("GENERATE |")
    compare_count = log_data.count("COMPARE |")

    total_operations = analyze_count + generate_count + compare_count

    weak = log_data.count("Rating=Weak")
    moderate = log_data.count("Rating=Moderate")
    strong = log_data.count("Rating=Strong")
    very_strong = log_data.count("Rating=Very Strong")

    # Count ratings from comparison records also
    weak += log_data.count("Password 1=Weak") + log_data.count("Password 2=Weak")
    moderate += log_data.count("Password 1=Moderate") + log_data.count("Password 2=Moderate")
    strong += log_data.count("Password 1=Strong") + log_data.count("Password 2=Strong")
    very_strong += log_data.count("Password 1=Very Strong") + log_data.count("Password 2=Very Strong")

    total_evaluations = weak + moderate + strong + very_strong

    report = f"""
PASSWORD SECURITY REPORT
========================================

Generated On: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Total Operations: {total_operations}
Total Password Evaluations: {total_evaluations}

Operation Summary:
------------------------------
ANALYZE   : {analyze_count}
GENERATE  : {generate_count}
COMPARE   : {compare_count}

Password Rating Summary:
------------------------------
Weak        : {weak}
Moderate    : {moderate}
Strong      : {strong}
Very Strong : {very_strong}
"""

    REPORT_FILE.write_text(report.strip(), encoding="utf-8")

    print("\nSecurity report exported successfully.")
    print(f"File location: {REPORT_FILE}")
    print("Go to reports folder to view the report.")
