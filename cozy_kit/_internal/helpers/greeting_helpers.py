# ============= cozy_kit/_internal/helpers/greeting_helpers.py =============

from datetime import datetime


class GHelpers:
    def __init__(self, nickname, name):
        self.nickname = nickname
        self.name = name

    def _say(self, action: str) -> str:
        message = f"{action.title()} {self.name}!"

        if self.nickname:
            message += f"\nOr {action.title()} {self.nickname}!"

        return message

    @staticmethod
    def _get_season() -> str:
        month = datetime.now().month

        # find season
        if month in (12, 1, 2):
            season = "winter"

        elif month in (3, 4, 5):
            season = "spring"

        elif month in (6, 7, 8):
            season = "summer"

        else:
            season = "autumn"

        return season
