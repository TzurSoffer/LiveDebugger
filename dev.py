import sys
import os

sys.path.insert(0, os.path.abspath("src"))
from pysole.pysole import _standalone, probe, InteractiveConsole

# probe(primaryPrompt="[Dev] ", defaultSize="1200x600", runRemainingCode=True, printStartupCode=False, font="Arial", fontSize=16, removeWaterMark=True)
# if __name__ == "__main__":
probe(runRemainingCode=True, printStartupCode=True)
print("a")
def main():
    print("Hello, world!")
    x = 2
    if x == 1:
        print("False")
        
        print("Still False")

    elif x == 2:
        if True:
            print("True")
    print(x)
main()