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

| Class        | Description                                                |
|--------------|------------------------------------------------------------|
| `Greeting`   | Greetings, quotes, bedtime stories, motivations, fun facts |
| `Timer`      | Countdown, Pomodoro, stopwatch, wait                       |
| `TextStudio` | Text conversion, ciphers, formatting                       |
| `Details`    | Package metadata                                           |

---

# Accessing Package Details

To access metadata like the author name, use the `Details` class:

```python
from cozy_kit import Details

info = Details()
print(info.details["author"])
# Youssef Ahmed
```

You can also access individual attributes directly:

```python
from cozy_kit import Details

info = Details()
print(info.author)
print(info.github)
```

---

# [See the entire docs](https://cozy-docs-27xdiooln-youssefahmed2017s-projects.vercel.app/)

---

# License

MIT
