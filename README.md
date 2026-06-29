# Task 3: Secure Coding Review & Remediation

## 1. Vulnerability Identified: SQL Injection (SQLi)
In the file `vulnerable_code.py`, user input (`username`) was directly concatenated into the SQL query string using Python's f-strings:
```python
query = f"SELECT * FROM users WHERE username = '{username}'"
