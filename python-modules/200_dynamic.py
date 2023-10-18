#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    len = len(sys.argv)
    print(f"{len-1} {'arguments.' if len-1 == 0 else 'agruments:'}")
    arguments = sys.argv[1:]
    num = 1
    for arg in arguments:
        print(f"{num}: {arg}")
        num += 1
