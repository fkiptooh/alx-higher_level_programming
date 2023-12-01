#!/usr/bin/python3

from sys import argv
def main():
    num_args = len(argv) - 1
    print(f"{num_args}{'.' if num_args == 0 else ':'} argument{'s' if num_args != 1 else ''}")

    if num_args > 0:
        for i, arg in enumerate(argv[1:], start=1):
            print(f"{i}: {arg}")
if __name__ == "__main__":
    main()
