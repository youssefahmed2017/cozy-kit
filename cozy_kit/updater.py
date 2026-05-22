import requests

from importlib.metadata import version
from cozy_kit import TextCustomizations

colors = TextCustomizations()

PACKAGE_NAME = "cozy-kit"


def check_for_updates() -> str:
    try:
        current_version = version(PACKAGE_NAME)

        response = requests.get(f"https://pypi.org/pypi/{PACKAGE_NAME}/json")

        latest_version = response.json()["info"]["version"]

        if current_version != latest_version:
            print(
                f'{colors.customize("[ Notice ]", "yellow_bright", "bold")} '
                f"A new update of cozy-kit is here. "
                f'{colors.customize(current_version, "red_bright")} → '
                f'{colors.customize(latest_version, "blue_bright")}'
                f'To update, type in the terminal {colors.customize("pip install --upgrade cozy-kit", "green_bright", "bold")}'
            )

    except Exception:
        # Silent fail so imports never crash
        pass
