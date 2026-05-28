# cozy-kit

> A cozy Python package with greetings, quotes, bedtime stories, timers, and text utilities.

Created by **Youssef Ahmed**

---

# Requirements

- Python 3.8+

---

# Installation

## Install

```bash
pip install cozy-kit
```

## Upgrade

```bash
pip install --upgrade cozy-kit
```

---

# Quick Example

## Usage

```python
from cozy_kit import Greeting

user = Greeting(
    name="Youssef",
    nickname="Yoyo"
)

print(user.welcome())
```

## Output

```text
Welcome Youssef!
Or welcome Yoyo!
```

---

# Classes

| Class                | Description                                                |
|----------------------|------------------------------------------------------------|
| `Greeting`           | Greetings, quotes, bedtime stories, motivations, fun facts |
| `Timer`              | Countdown, Pomodoro, stopwatch, wait                       |
| `TextEditor`         | Text conversion, ciphers, formatting                       |
| `TextCustomizations` | Text coloring, changing to italic or bold                  |
| `CozyUI`             | Make some cool terminal UI using ascii and unicode symbols |
| `settings (Object)`  | Package settings like [notice if on older update](https://cozy-docs.vercel.app/#settings)
| `Details`            | Package metadata                                           |

---

<h2><a href="https://cozy-docs.vercel.app" target="_blank">See the entire docs</a></h2>

---

# License

MIT
