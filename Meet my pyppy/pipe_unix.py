import sys


def main():
    for line in sys.stdin:          # pipe can be used now
        print(line.rstrip())


if __name__ == "__main__":
    main()
