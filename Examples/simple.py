import pysole

foo = "bar"

def greet(name):
    print(f"Hello, {name}! Welcome to pysole.")

def add(a, b):
    """Add two numbers"""
    return a + b

def average(numbers):
    """Find average of a list of numbers"""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    # Launch the live console for interactive testing
    pysole.probe(runRemainingCode=True,
                 printStartupCode=True
                 )
    # Demo code to show off startup ability
    add(1,2)
    greet("Alice")
    avg = average([1, 2, 3, 4, 5])