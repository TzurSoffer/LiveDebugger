from liveConsole import InteractiveConsole

def greet(name):
    print(f"Hello, {name}! Welcome to liveConsole.")

def add(a, b):
    return a + b

if __name__ == "__main__":
    # Launch the live console for interactive testing
    console = InteractiveConsole()
    console.probe()
