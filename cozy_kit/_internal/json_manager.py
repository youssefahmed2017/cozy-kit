# ============= cozy_kit/_internal/json_manager.py =============

# ============= IMPORTS =============

from pathlib import Path
from cozy_kit._internal import errors

import json

# ============= JSONManage CLASS =============


class JSONManager:
    @staticmethod
    def _load_json(path: Path) -> dict:
        try:
            with open(path, "r", encoding="utf-8") as file:  # Open file
                return json.load(file)

        except FileNotFoundError:  # Raise exception if file doesn't exist
            raise errors.DatabaseNotFoundError(
                "Database not found. "
                "Check if there is a typo "
                "in the database name."
            )

    @staticmethod
    def _save_json(path: Path, data: dict) -> None:

        try:
            with open(path, "w", encoding="utf-8") as file:  # Open file
                json.dump(data, file, indent=4)

        except FileNotFoundError:  # Raise exception if file doesn't exist
            raise errors.DatabaseNotFoundError(
                "Database not found. "
                "Check if there is a typo "
                f"in the database name ({path})."
                "Note: this is a developer error. If you are a user, please report this to use on GitHub: https://github.com/youssefahmed2017/cozy-kit/issues"
            )
