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


# Health check endpoint simulation
if __name__ == '__main__':
    print('Python Service is running')
    print('Version: 1.0.0')
    print('Health: OK')

