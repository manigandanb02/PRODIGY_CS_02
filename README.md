# PassProbe - Password Strength Analyzer

## Overview

PassProbe is a Python-based Password Strength Analyzer featuring password strength evaluation, entropy calculation, secure password generation, password comparison, common password detection, activity logging, and security report generation.

This project was developed as part of the Prodigy InfoTech Cyber Security Internship Program.

---

## Password Security Concept

Passwords are the primary line of defense against unauthorized access to systems and accounts. Weak passwords can be easily compromised through brute-force attacks, dictionary attacks, and credential stuffing techniques.

A strong password should:

* Have sufficient length
* Contain uppercase and lowercase letters
* Include numbers
* Include special characters
* Avoid common passwords
* Avoid predictable patterns and sequences

PassProbe analyzes passwords using these principles and provides feedback to help users create stronger and more secure passwords.

---

## Features

### Password Analysis

* Evaluates password strength
* Calculates password entropy
* Provides security ratings and suggestions

### Secure Password Generation

* Generates strong random passwords
* Supports customizable password lengths

### Password Comparison

* Compares two passwords
* Identifies the stronger password

### Activity Logging

* Records operations with timestamps
* Maintains an audit trail

### Security Report Generation

* Generates security reports
* Provides operation and rating statistics

---

## Technologies Used

* Python
* Regular Expressions (RegEx)
* Secrets Module
* File Handling
* Logging and Reporting

---

## Project Structure

```text
PassProbe/
│
├── password_analyzer.py
│
├── modules/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── comparator.py
│   ├── entropy_calculator.py
│   ├── generator.py
│   ├── history_manager.py
│   └── report_manager.py
│
├── data/
│   └── common_passwords.txt
│
└── reports/
    ├── password_security.log
    └── security_report.txt
 
```

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/manigandanb02/PRODIGY_CS_02.git PassProbe
```

### 2. Navigate to the Project Folder

```bash
cd PassProbe
```

### 3. Run the Program

#### Windows

```bash
python password_analyzer.py
```

#### Linux (Ubuntu)

```bash
python3 password_analyzer.py
```

---

## Demo Video

Watch the project demonstration on LinkedIn:

[LinkedIn Demo Video](https://www.linkedin.com/posts/manigandanb02_prodigyinfotech-cybersecurity-python-ugcPost-7473412828838780928-zf_p/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFJ8ul4BQ42d707c6KxMYCd3agIPNUqbyhA)

---

## Learning Outcomes

Through this project, I learned:

* Password security fundamentals
* Password entropy calculation
* Secure password generation techniques
* Common password detection
* File handling in Python
* Logging and auditing
* Report generation
* Menu-driven application development
* Modular programming practices

---

## Disclaimer

This project is developed for educational purposes and cybersecurity awareness. Password strength ratings are calculated using predefined security criteria and are intended to help users create stronger passwords.
