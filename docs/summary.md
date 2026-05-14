# Features

<details>
<summary>Open Section</summary>

## Greeting
- Welcome messages
- Goodbye messages
- Morning greetings
- Afternoon greetings
- Evening greetings
- Bedtime stories
- Motivational quotes
- Fun facts
- Automatic greetings based on time & season

## Timer
- Countdown timers
- Pomodoro timers
- Stopwatch support
- Time waiting utilities
- Current time utilities

## TextStudio
- Morse code conversion
- Caesar cipher
- Text formatting utilities
- Word & character counting
- Punctuation removal
- Snake case conversion
- Letter spacing utilities

</details>

---

# Full Package Example

<details>
<summary>Open Full Example</summary>

# Usage

```python
from cozy_kit import Greeting, Timer, TextStudio
import time

# Greeting
user = Greeting(
    name="Youssef",
    age=16,
    gender="male",
    nickname="Yoyo"
)

print(user.welcome())
print(user.good_morning())
print(user.fun_facts())

# TextStudio
studio = TextStudio()

text = "Hello World"

print(studio.to_upper(text))
print(studio.reverse(text))
print(studio.to_morse(text))
print(studio.caesar(text, 3))

# Timer
timer = Timer()

timer.countdown(
    count=5,
    time_type='sec',
    show=print
)

timer.start_stopwatch()

time.sleep(2)

print(timer.end_stopwatch())
```

---

# Example Output

```text
Welcome Youssef!
Or welcome Yoyo!

Good Morning Youssef!
Or good morning Yoyo!

Anyways, here's a quick morning quote.

Albert Einstein

Life is like riding a bicycle.
To keep your balance, you must keep moving.

Space Facts

A day on Venus is longer than a year on Venus.

HELLO WORLD

dlroW olleH

.... . .-.. .-.. --- / .-- --- .-. .-.. -..

Khoor Zruog

00:05
00:04
00:03
00:02
00:01

⏰ Time's up!

0:00:02.001392
```

</details> 