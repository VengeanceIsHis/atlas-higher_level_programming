#!/usr/bin/python3
import hidden_4 as hidden


def main():
    mo_names = dir(hidden)
    for name in mo_names:
        if not name.startswith('_'):
            print(name)


if __name__ == "__main__":
    main()
