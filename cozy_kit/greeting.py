# ============= cozy_kit/greeting.py =============

# ============= IMPORTS =============

import datetime
import random

from pathlib import Path
from cozy_kit._internal import errors
from cozy_kit._internal.json_manager import JSONManager
from cozy_kit._internal.helpers.greeting_helpers import GHelpers

# # ============= PATH VARIABLES =============

BASE_DIR = Path(__file__).resolve().parent
RESOURCES_DIR = BASE_DIR / "resources"

# ============= Greeting CLASS =============


class Greeting(JSONManager, GHelpers):
    """
    A greetings class with fun facts, greetings, and time-aware greetings.
    Methods:
        welcome()
        bye(destination)
        good_morning(), good_afternoon(), good_evening(), and good_night()
        auto_greet()
        holiday_greet()
        random_quote()
        motivation()
        fun_fact()
        add_bedtime_story()
        add_motivation()
        add_fun_fact()

    Details:
        name: str
        age: int
        gender: str
        nickname: str
    """

    def __init__(self, **details):
        # ============= User DETAILS =============

        self.name = details.get("name", "User").title()
        self.age = details.get("age")
        self.gender = details.get("gender", "").title()
        self.nickname = details.get("nickname", "").title()
        super().__init__(name=self.name, nickname=self.nickname)

    def welcome(self) -> str:
        """Welcomes the user.
        Returns:
            str
        """

        return self._say(action="welcome")

    def bye(
        self,
        destination: str = "where ever you are gonna go",
    ) -> str:
        """
        Tells the user goodbye.

        Parameters:
            destination:
                Destination name.
        """

        message = self._say(action="Bye")
        message += f" Have a nice day at {destination}!"

        return message

    # ============= GREETINGS (BASED ON TIME) =============

    def good_morning(self) -> str:
        """Returns a morning quote.
        Raises:
            DatabaseNotFoundError
        """

        message = self._say(action="good morning")
        message += "\nAnyways, here's a quick morning quote."

        mornings_path = RESOURCES_DIR / "mornings.json"
        quotes = self._load_json(mornings_path)

        morning = random.choice(quotes["mornings"])

        morning_quote = f"{morning['name']}\n\n" f"{morning['content']}"

        return f"{message}\n\n{morning_quote}"

    def good_afternoon(self) -> str:
        """Returns an afternoon quote.
        Raises:
            DatabaseNotFoundError
        """

        message = self._say(action="good afternoon")
        message += "\nAnyways, here's  a quick afternoon quote.\n"

        afternoons_path = RESOURCES_DIR / "afternoons.json"
        quotes = self._load_json(afternoons_path)

        quote = random.choice(quotes["afternoons"])

        return f"{message}\n" f"{quote['name']}\n\n" f"{quote['content']}"

    def good_evening(self) -> str:
        """Returns an evening quote.
        Raises:
            DatabaseNotFoundError
        """

        message = self._say(action="good evening")
        message += "\nAnyways, here's a quick evening quote.\n"

        evenings_path = RESOURCES_DIR / "evenings.json"
        quotes = self._load_json(evenings_path)

        quote = random.choice(quotes["evenings"])

        return f"{message}\n" f"{quote['name']}\n\n" f"{quote['content']}"

    def good_night(self) -> str:
        """Returns a bedtime story.
        Raises:
            DatabaseNotFoundError
        """

        message = self._say(action="good night")
        message += "\nAnyways, here's a quick bedtime story.\n"

        bedtime_path = RESOURCES_DIR / "bedtime_stories.json"
        stories = self._load_json(bedtime_path)

        random_title = random.choice(list(stories["bedtime_stories"].keys()))

        random_story = stories["bedtime_stories"][random_title]

        bedtime = f"{random_title}\n\n" f"{random_story}"

        return f"{message}\n\n{bedtime}"

    def holiday_greet(self) -> str:
        """
        Returns a random holiday quote, depending on today's date.
        Raises:
            DatabaseNotFoundError
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
            return ""

        holidays_path = RESOURCES_DIR / "holidays.json"
        data = self._load_json(holidays_path)

        quotes = data["holidays"][holiday_name]

        random_quote = random.choice(quotes)

        return f"🎉 Happy {holiday_name}, " f"{self.name}!\n\n" f"{random_quote}"

    def auto_greet(self) -> str:
        """
        Greets depending on:
            - season
            - current time

        Raises:
            DatabaseNotFoundError
        """

        season = self._get_season()
        hour = datetime.datetime.now().hour
        holiday = self.holiday_greet()

        if holiday:
            return holiday

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

    # ============= RANDOM GREETING =============
    def random_quote(self) -> str:
        """Returns a random time-of-day quote.
        Raises:
            DatabaseNotFoundError
        """

        which = random.randint(0, 3)

        if which == 0:
            return self.good_morning()

        elif which == 1:
            return self.good_afternoon()

        elif which == 2:
            return self.good_evening()

        else:
            return self.good_night()

    # ============= MOTIVATIONS AND FUN FACTS =============

    def motivate(self) -> str:
        """Returns a motivational quote.
        Raises:
            DatabaseNotFoundError
        """

        motivations_path = RESOURCES_DIR / "motivations.json"
        motivations = self._load_json(motivations_path)

        motivation = random.choice(motivations["motivations"])

        return f'{motivation["name"]} \n\n {motivation["content"]}'

    def fun_fact(self) -> str:
        """Returns a fun fact.
        Raises:
            DatabaseNotFoundError
        """

        facts_path = RESOURCES_DIR / "fun_facts.json"
        fun_facts = self._load_json(facts_path)

        fun_fact = random.choice(fun_facts["facts"])

        return f"{fun_fact['name']}\n\n" f"{fun_fact['content']}"

    # ============= EXTEND THE DATABASES =============

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

        Raises:
            InvalidStoryError
            DatabaseNotFoundError
        """

        if not title.strip():
            raise errors.InvalidStoryError("Story title cannot be empty.")

        if not content.strip():
            raise errors.InvalidStoryError("Story content cannot be empty.")

        bedtime_stories_path = RESOURCES_DIR / "bedtime_stories.json"
        data = self._load_json(bedtime_stories_path)

        data["bedtime_stories"][title] = content

        self._save_json(bedtime_stories_path, data)

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

        Raises:
            InvalidMotivationError
            DatabaseNotFoundError
        """

        if not name.strip():
            raise errors.InvalidMotivationError("Motivation name cannot be empty.")

        if not content.strip():
            raise errors.InvalidMotivationError("Motivation content cannot be empty.")

        motivations_path = RESOURCES_DIR / "motivations.json"
        data = self._load_json(motivations_path)

        data["motivations"].append({"name": name, "content": content})

        self._save_json(motivations_path, data)

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

        Raises:
            InvalidFunFactError
            DatabaseNotFoundError
        """

        if not name.strip():
            raise errors.InvalidFunFactError("Fun fact name cannot be empty.")

        if not content.strip():
            raise errors.InvalidFunFactError("Fun fact content cannot be empty.")

        fun_facts_path = RESOURCES_DIR / "fun_facts.json"
        data = self._load_json(fun_facts_path)

        data["facts"].append({"name": name, "content": content})

        self._save_json(fun_facts_path, data)
