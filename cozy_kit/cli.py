from importlib.metadata import version
from cozy_kit import *

import argparse
import webbrowser

details = Details()


def main():
    parser = argparse.ArgumentParser(prog="cozy-kit")

    parser.add_argument(
        "--version", "-V", action="store_true", help="Show cozy-kit version"
    )
    parser.add_argument("--info", "-I", action="store_true", help="Show cozy-kit info")
    parser.add_argument(
        "--license", action="store_true", help="Show cozy-kit's license"
    )
    parser.add_argument(
        "--pypi",
        action="store_true",
        help="Open cozy-kit's PyPI page in the browser",
    )
    parser.add_argument(
        "--github",
        action="store_true",
        help="Open cozy-kit's GitHub repo in the browser",
    )
    parser.add_argument(
        "--homepage",
        action="store_true",
        help="Open cozy-kit's Homepage in the browser",
    )
    parser.add_argument(
        "--docs",
        action="store_true",
        help="Open cozy-kit's Documentation website in the browser",
    )

    args = parser.parse_args()

    if args.version:
        print(f'cozy-kit v{version("cozy-kit")}')

    elif args.info:
        print(details.about())
        print(
            f"This package is a package made by Youssef Ahmed. \nThe package's latest version was v{version('cozy-kit')}. \nThe package has started to reach a great point where it is starting to become stable"
        )

    elif args.license:
        print("MIT License")

    elif args.pypi:
        webbrowser.open_new_tab("https://pypi.org/project/cozy-kit/")
        print("Successfully opened cozy-kit's PyPI page ✔️")

    elif args.github:
        webbrowser.open_new_tab("https://github.com/youssefahmed2017/cozy-kit/")
        print("Successfully opened cozy-kit's GitHub repo ✔️")

    elif args.homepage:
        webbrowser.open_new_tab("https://cozykit-home.vercel.app/")
        print("Successfully opened cozy-kit's Homepage ✔️")

    elif args.docs:
        webbrowser.open_new_tab("https://cozy-docs.vercel.app/")
        print("Successfully opened cozy-kit's Documentation ✔️")


if __name__ == "__main__":
    main()
