import sys
import os

sys.path.insert(0, os.path.abspath("src"))
from pysole.pysole import _standalone, probe, InteractiveConsole

probe(primaryPrompt="[Dev] ", defaultSize="1200x600", runRemainingCode=True, printStartupCode=False, font="Arial", fontSize=16, removeWaterMark=True)

print("Dev Branch")
x = 2
print(x)
