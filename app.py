"""
Simple Python Service

This is a minimal Python service example for CI/CD demonstration
"""


def greet(name='World'):
    """Greet someone by name."""
    return f'Hello, {name}!'


def add(a, b):
    """Add two numbers."""
    return a + b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


# # ============================================================================
# # VULNERABLE CODE FOR SECURITY TESTING (CodeQL)
# # Uncomment the code below to enable vulnerabilities for testing
# # ============================================================================

# import os
# import subprocess
# import sqlite3
# import hashlib


# def vulnerable_sql_query(user_id):
#     """
#     VULNERABLE: SQL Injection vulnerability
#     CodeQL should detect this as user input is directly concatenated into SQL query
#     """
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     # VULNERABLE: Direct string concatenation with user input
#     query = f"SELECT * FROM users WHERE id = {user_id}"
#     cursor.execute(query)
#     return cursor.fetchall()


# def vulnerable_command_execution(filename):
#     """
#     VULNERABLE: Command Injection vulnerability
#     CodeQL should detect this as user input is used in os.system without sanitization
#     """
#     # VULNERABLE: User input directly used in system command
#     os.system(f"cat {filename}")


# def vulnerable_subprocess_call(user_input):
#     """
#     VULNERABLE: Command Injection via subprocess
#     CodeQL should detect this as user input is used in subprocess without proper escaping
#     """
#     # VULNERABLE: User input directly used in subprocess call
#     subprocess.call(['echo', user_input], shell=True)


# def vulnerable_path_traversal(filename):
#     """
#     VULNERABLE: Path Traversal vulnerability
#     CodeQL should detect this as user input is used directly in file operations
#     """
#     # VULNERABLE: User input used directly without path validation
#     with open(filename, 'r') as f:
#         return f.read()


# def vulnerable_weak_cryptography(password):
#     """
#     VULNERABLE: Weak cryptography
#     CodeQL should detect this as MD5 is cryptographically broken
#     """
#     # VULNERABLE: Using weak hash algorithm
#     return hashlib.md5(password.encode()).hexdigest()


# def vulnerable_xss(user_input):
#     """
#     VULNERABLE: XSS (Cross-Site Scripting) vulnerability
#     CodeQL should detect this as user input is returned without sanitization
#     """
#     # VULNERABLE: User input returned without escaping
#     return f"<div>{user_input}</div>"


# Health check endpoint simulation
if __name__ == '__main__':
    print('Python Service is running')
    print('Version: 1.0.0')
    print('Health: OK')

