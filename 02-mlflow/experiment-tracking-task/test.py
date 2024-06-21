import radon
from radon.raw import analyze
import radon.raw

def calculate_complexity(code):
    cc = radon.raw.raw_metrics(code)
    for func in cc:
        print(f"Function: {func[0]}")
        print(f"Cyclomatic complexity: {func[1]}")
        print()

# Example usage:
code = """
def my_function(a, b):
    if a > b:
        return a
    else:
        return b

def my_function2(a, b):
    if a > b:
        return a
    else:
        return b
"""

calculate_complexity(code)