import sys
import os

# Detect if running as a frozen executable (cx_Freeze sets sys.frozen)
if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)  # cx_Freeze sets sys.executable path
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, os.path.join(base_path, "obfuscated"))

from util_py_files.adder import *
from util_py_files.subtractor import *




def calculator():
    while 1:
        mode = input("Enter a mode: add / sub / exit: ")
        if mode == "add":
            n1 = int(input("Enter first number: "))
            n2 = int(input("Enter second number: "))
            print(f"The sum is {add(n1,n2)}")
        elif mode == "sub":
            n1 = int(input("Enter first number: "))
            n2 = int(input("Enter second number: "))
            print(f"The difference is {sub(n1,n2)}")
        elif mode == "exit":
            break


if __name__ == "__main__":
    calculator()
