import datetime
import json
import random

from pathlib import Path
from . import errors

BASE_DIR = Path(__file__).resolve().parent
RESOURCES_DIR = BASE_DIR / "resources"


class Greeting:
    def __init__(self, **details):
        """
        Available details:
            - name
            - age
            - gender
            - nickname
        """

        self.name = details.get("name", "User").title()
        self.age = details.get("age")
        self.gender = details.get("gender", "").title()
        self.nickname = details.get("nickname", "").title()

    def __say(self, something: str) -> str:
        message = f"{something.title()} {self.name}!"

        if self.nickname:
            message += f"\nOr {something} {self.nickname}!"

        return message

    def __get_season(self) -> str:
        holiday_message = self.holiday_greet()

        if holiday_message:
            return holiday_message

        month = datetime.datetime.now().month

        if month in [12, 1, 2]:
            season = "winter"

        elif month in [3, 4, 5]:
            season = "spring"

        elif month in [6, 7, 8]:
            season = "summer"

        else:
            season = "autumn"

        return season

    def __load_json(self, path: Path) -> dict:
        """Helper to load a JSON file, raising DatabaseNotFoundError if missing."""

        try:
            with open(path, "r", encoding="utf-8") as file:
                return json.load(file)

        except FileNotFoundError:
            raise errors.DatabaseNotFoundError(
                "Database not found. "
                "Check if there is a typo "
                "in the database name."
            )

    def __save_json(self, path: Path, data: dict) -> None:
        """Helper to save a JSON file, raising DatabaseNotFoundError if missing."""

        try:
            with open(path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

        except FileNotFoundError:
            raise errors.DatabaseNotFoundError(
                "Database not found. "
                "Check if there is a typo "
                "in the database name."
            )

    def welcome(self) -> str:
        """Welcomes the user."""

        return self.__say(something="welcome")

    def bye(
        self,
        destination="Where ever you are gonna go",
    ) -> str:
        """
        Tells the user goodbye.

        Parameters:
            destination:
                Destination name.
        """

        message = f"Bye {self.name}! " f"Have a nice day at {destination}!"

        if self.nickname:
            message += f"\nOr bye {self.nickname}!"

        return message

    def good_morning(self) -> str:
        """Returns a morning quote."""

        message = self.__say("good morning")
        message += "\nAnyways, here's a quick morning quote."

        mornings_path = RESOURCES_DIR / "mornings.json"
        quotes = self.__load_json(mornings_path)

        morning = random.choice(quotes["mornings"])

        morning_quote = f"{morning['name']}\n\n" f"{morning['content']}"

        return f"{message}\n\n{morning_quote}"

    def good_afternoon(self) -> str:
        """Returns an afternoon quote."""

        message = self.__say("good afternoon")
        message += "\nAnyways, here's  a quick afternoon quote.\n"

        afternoons_path = RESOURCES_DIR / "afternoons.json"
        quotes = self.__load_json(afternoons_path)

        quote = random.choice(quotes["afternoons"])

        return f"{message}\n" f"{quote['name']}\n\n" f"{quote['content']}"

    def good_evening(self) -> str:
        """Returns an evening quote."""

        message = self.__say("good evening")
        message += "\nAnyways, here's a quick evening quote.\n"

        evenings_path = RESOURCES_DIR / "evenings.json"
        quotes = self.__load_json(evenings_path)

        quote = random.choice(quotes["evenings"])

        return f"{message}\n" f"{quote['name']}\n\n" f"{quote['content']}"

    def good_night(self) -> str:
        """Returns a bedtime story."""

        message = self.__say("good night")
        message += "\nAnyways, here's a quick bedtime story.\n"

        bedtime_path = RESOURCES_DIR / "bedtime_stories.json"
        stories = self.__load_json(bedtime_path)

        random_title = random.choice(list(stories["bedtime_stories"].keys()))

        random_story = stories["bedtime_stories"][random_title]

        bedtime = f"{random_title}\n\n" f"{random_story}"

        return f"{message}\n\n{bedtime}"

    def auto_greet(self) -> str:
        """
        Greets depending on:
            - season
            - current time
        """

        season = self.__get_season()
        hour = datetime.datetime.now().hour

        if season == "winter":
            if 6 <= hour < 11:
                return self.good_morning()

            elif 11 <= hour < 16:
                return self.good_afternoon()

            elif 16 <= hour < 20:
                return self.good_evening()

            return self.good_night()

        elif season == "summer":
            if 5 <= hour < 12:
                return self.good_morning()

            elif 12 <= hour < 18:
                return self.good_afternoon()

            elif 18 <= hour < 22:
                return self.good_evening()

            return self.good_night()

        else:
            if 6 <= hour < 12:
                return self.good_morning()

            elif 12 <= hour < 17:
                return self.good_afternoon()

            elif 17 <= hour < 21:
                return self.good_evening()

            return self.good_night()

    def motivate(self) -> str:
        """Returns a motivational quote."""

        motivations_path = RESOURCES_DIR / "motivations.json"
        motivations = self.__load_json(motivations_path)

        motivation = random.choice(motivations["motivations"])

        return f'{motivation["name"]} \n\n {motivation["content"]}'

    def fun_fact(self) -> str:
        """Returns a fun fact."""

        facts_path = RESOURCES_DIR / "fun_facts.json"
        fun_facts = self.__load_json(facts_path)

        fun_fact = random.choice(fun_facts["facts"])

        return f"{fun_fact['name']}\n\n" f"{fun_fact['content']}"

    def add_bedtime_story(
        self,
        title: str,
        content: str,
    ) -> None:
        """
        Adds a bedtime story.

        Parameters:
            title:
                Story title.

            content:
                Story content.
        """

        if not title.strip():
            raise errors.InvalidStoryError("Story title cannot be empty.")

        if not content.strip():
            raise errors.InvalidStoryError("Story content cannot be empty.")

        bedtime_stories_path = RESOURCES_DIR / "bedtime_stories.json"
        data = self.__load_json(bedtime_stories_path)

        data["bedtime_stories"][title] = content

        self.__save_json(bedtime_stories_path, data)

    def random_quote(self) -> str:
        """Returns a random time-of-day quote."""

        which = random.randint(0, 3)

        if which == 0:
            return self.good_morning()

        elif which == 1:
            return self.good_afternoon()

        elif which == 2:
            return self.good_evening()

        else:
            return self.good_night()

    def add_motivation(
        self,
        name: str,
        content: str,
    ) -> None:
        """
        Adds a motivational quote.

        Parameters:
            name:
                Quote name/title.

            content:
                Quote content.
        """

        if not name.strip():
            raise errors.InvalidMotivationNameError("Motivation name cannot be empty.")

        if not content.strip():
            raise errors.InvalidMotivationContentError(
                "Motivation content cannot be empty."
            )

        motivations_path = RESOURCES_DIR / "motivations.json"
        data = self.__load_json(motivations_path)

        data["motivations"].append({"name": name, "content": content})

        self.__save_json(motivations_path, data)

    def add_fun_fact(
        self,
        name: str,
        content: str,
    ) -> None:
        """
        Adds a fun fact.

        Parameters:
            name:
                Fact name/title.

            content:
                Fact content.
        """

        if not name.strip():
            raise errors.InvalidFunFactError("Fun fact name cannot be empty.")

        if not content.strip():
            raise errors.InvalidMotivationContentError(
                "Fun fact content cannot be empty."
            )

        fun_facts_path = RESOURCES_DIR / "fun_facts.json"
        data = self.__load_json(fun_facts_path)

        data["facts"].append({"name": name, "content": content})

        self.__save_json(fun_facts_path, data)

    def holiday_greet(self) -> str:
        """
        Returns a random holiday quote
        depending on today's date.
        """

        today = datetime.datetime.now()

        current_date = (
            today.month,
            today.day,
        )

        holidays = {
            (1, 1): "New Year's Day",
            (2, 14): "Valentine's Day",
            (4, 22): "Earth Day",
            (7, 30): "International Friendship Day",
            (10, 4): "World Smile Day",
            (11, 20): "Children's Day",
        }

        holiday_name = holidays.get(current_date)

        if holiday_name is None:
            return None

        holidays_path = RESOURCES_DIR / "holidays.json"
        data = self.__load_json(holidays_path)

        quotes = data["holidays"][holiday_name]

        random_quote = random.choice(quotes)

        return f"🎉 Happy {holiday_name}, " f"{self.name}!\n\n" f"{random_quote}"
