from datetime import datetime
from pathlib import Path


LOG_FILE = Path("reports/password_security.log")


def ensure_log_file():
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not LOG_FILE.exists():
        LOG_FILE.write_text("", encoding="utf-8")


def save_history(result, action="ANALYZE"):
    ensure_log_file()

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            f"{action} | "
            f"Length={result['length']} | "
            f"Entropy={result['entropy']:.2f} bits | "
            f"Score={result['score']}/100 | "
            f"Rating={result['rating']}\n"
        )


def save_comparison_history(result1, result2, stronger):
    ensure_log_file()

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            f"COMPARE | "
            f"Password 1={result1['rating']} ({result1['score']}/100) | "
            f"Password 2={result2['rating']} ({result2['score']}/100) | "
            f"Stronger={stronger}\n"
        )


def export_log_file():
    ensure_log_file()

    print("\nLog file is ready.")
    print(f"File location: {LOG_FILE}")
    print("Go to reports folder to view the log file.")
