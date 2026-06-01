from importlib.metadata import version
from cozy_kit import *
from cozy_kit import updater

import argparse

details = Details()


def main():
    parser = argparse.ArgumentParser(prog="cozy-kit")

    parser.add_argument("--version", action="store_true", help="Show CozyKit version")
    parser.add_argument("--info", action="store_true", help="Show CozyKit info")

    if settings.notice_if_on_older_update:
        updater.check_for_updates()

    args = parser.parse_args()

    if args.version:
        print(f'CozyKit v{version("cozy-kit")}')

    elif args.info:
        print(details.about())


if __name__ == "__main__":
    main()
