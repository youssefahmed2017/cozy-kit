import json, random
from pathlib import Path
import datetime

"""This module is the module you might use everyday:
        welcome() welcomes you,
        bye() says goodbye to you,
        good_night() tells you a bedtime story
        good_morning() gives you a paragraph for the morning"""

BASE_DIR = Path(__file__).resolve().parent

class Greeting:
    def __init__(self, **details):
        """Here is what you can enter:
                name,
                age,
                height,
                weight,
                eye_color,
                hair_color,
                gender,
                and nickname"""
        self.details = details
        self.name = details.get("name").title()
        self.age = details.get('age')
        self.gender = details.get('gender').title()
        self.nickname = details.get('nickname').title()

    def __say(self, something):
        message = f'{something.title()} {self.name}!'


        if self.nickname:
            message += f'\nOr {something} {self.nickname}!'

        return message

    def welcome(self):
        return self.__say(something='welcome')

    def bye(self, destination="Where ever you're gonna go"):
        message = f'Bye {self.name}! Have a nice day at {destination}!'
        if self.nickname:
            message += f'\nOr bye {self.nickname}!'
        return message

    def good_night(self):
        message = self.__say('good night')

        message += "\nAnyways, here's a quick bedtime story.\n"

        bedtime_path = BASE_DIR / "jsons" / "bedtime_stories.json"

        with open(bedtime_path, 'r', encoding='utf-8') as bedtime_stories:
            stories = json.load(bedtime_stories)

        random_title = random.choice(
            list(stories['bedtime_stories'].keys())
        )

        random_story = stories['bedtime_stories'][random_title]

        bedtime = f'{random_title}\n\n{random_story}'

        return f"{message}\n\n{bedtime}"

    def good_morning(self):
        message = self.__say('good morning')

        message += "\nAnyways, here's a quick morning quote."

        mornings_path = BASE_DIR / "jsons" / "mornings.json"

        with open(mornings_path, 'r', encoding='utf-8') as morning_quotes:
            quotes = json.load(morning_quotes)
        morning = random.choice(
            quotes['mornings']
        )

        morning_quote = (
            f"{morning['name']}\n\n"
            f"{morning['content']}"
        )

        return f"{message}\n\n{morning_quote}"

    def motivate(self):

        mots_path = BASE_DIR / "jsons" / "motivations.json"

        with open(mots_path, 'r', encoding='utf-8') as file:
            motivates = json.load(file)

        motivation = random.choice(
            motivates['motivations']
        )

        return motivation['name'], motivation['content']

    def fun_facts(self):
        facts_path = BASE_DIR / "jsons" / "fun_facts.json"

        with open(facts_path, 'r') as file:
            fun_facts = json.load(file)

        fun_fact = random.choice(fun_facts['facts'])

        return f"{fun_fact['name']}\n\n{fun_fact['content']}"

    def good_afternoon(self):
        message = self.__say('good afternoon')

        message += "\nAnyways, here's a quick afternoon quote.\n"

        afternoons_path = BASE_DIR / "jsons" / "afternoons.json"

        with open(afternoons_path, 'r', encoding='utf-8') as afternoon_quotes:
            quotes = json.load(afternoon_quotes)

        quote = random.choice(quotes['afternoons'])

        return f"{message}\n{quote['name']}\n\n{quote['content']}"

    def good_evening(self):
        message = self.__say('good evening')

        message += "\nAnyways, here's a quick evening quote.\n"

        afternoons_path = BASE_DIR / "jsons" / "afternoons.json"

        with open(afternoons_path, 'r', encoding='utf-8') as afternoon_quotes:
            quotes = json.load(afternoon_quotes)

        quote = random.choice(quotes['afternoons'])

        return f"{message}\n{quote['name']}\n\n{quote['content']}"

    def auto_greet(self):
        hour = datetime.datetime.now().hour
        month = datetime.datetime.now().month

        # Detect season
        if month in [12, 1, 2]:
            season = "winter"

        elif month in [3, 4, 5]:
            season = "spring"

        elif month in [6, 7, 8]:
            season = "summer"

        else:
            season = "autumn"

        # Winter times
        if season == "winter":
            if 6 <= hour < 11:
                return self.good_morning()

            elif 11 <= hour < 16:
                return self.good_afternoon()

            elif 16 <= hour < 20:
                return self.good_evening()

            else:
                return self.good_night()

        # Summer times
        elif season == "summer":
            if 5 <= hour < 12:
                return self.good_morning()

            elif 12 <= hour < 18:
                return self.good_afternoon()

            elif 18 <= hour < 22:
                return self.good_evening()

            else:
                return self.good_night()

        # Spring & autumn
        else:
            if 6 <= hour < 12:
                return self.good_morning()

            elif 12 <= hour < 17:
                return self.good_afternoon()

            elif 17 <= hour < 21:
                return self.good_evening()

            else:
                return self.good_night()
