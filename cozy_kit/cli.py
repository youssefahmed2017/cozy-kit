from importlib.metadata import version
from cozy_kit import *
from cozy_kit import updater

import argparse

details = Details()


def main():
    parser = argparse.ArgumentParser(prog="cozy-kit")

    parser.add_argument("--version", action="store_true", help="Show cozy-kit version")
    parser.add_argument("--info", action="store_true", help="Show cozy-kit info")

    args = parser.parse_args()

    if args.version:
        print(f'cozy-kit v{version("cozy-kit")}')

    elif args.info:
        print(details.about())
        print(
            f"This package is a package made by Youssef Ahmed. \nThe package's latest version was v{version('cozy-kit')}. \nThe package has started to reach a great point where it is starting to become stable"
        )


if __name__ == "__main__":
    main()
