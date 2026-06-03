# cozy-kit

![Logo](https://raw.githubusercontent.com/youssefahmed2017/cozy-kit/main/cozy-logo.png)

![Version](https://img.shields.io/pypi/v/cozy_kit)
![Python Version](https://img.shields.io/pypi/pyversions/cozy-kit)
![License](https://img.shields.io/pypi/l/cozy-kit)

![Issues](https://img.shields.io/github/issues/youssefahmed2017/cozy-kit)
![GitHub stars](https://shields.io/github/stars/youssefahmed2017/cozy-kit)
![Last Commit](https://img.shields.io/github/last-commit/youssefahmed2017/cozy-kit)

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

# Quick Examples

## Greeting Usage

```python
from cozy_kit import Greeting

user = Greeting(
    name="Youssef",
    nickname="Yoyo"
)

print(user.welcome())
```

---

## Output

```text
Welcome Youssef!
Or welcome Yoyo!
```

## Timer Usage
```python
from cozy_kit import Timer

timer = Timer()

timer.countdown(
    count=5,
    time_type="sec",
    show=print
)
```

## Output
```text
5
4
...
⏰ Time's up!
```

## TextEditor Usage
```python
from cozy_kit import TextEditor

editor = TextEditor()

print(editor.reverse("Hello"))
```

## Output
```text
olleH
```

## TextCustomizations Usage
```python
from cozy_kit import TextCustomizations

customizer = TextCustomizations()

print(customizer.customize("WARNING", "yellow", "bold"))
```

## Output
```text
WARNING (bold yellow)
```

## CozyUI Usage
```python
from cozy_kit import CozyUI

ui = CozyUI()

print(ui.progress_bar(70))
```

## Output

```text

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
| `settings (object)`  | The package settings like `notice_if_on_older_update`      |
| `Details`            | Package metadata                                           |

---

# Why cozy-kit?

cozy-kit is a collection of utilities for Python developers.

Features include:

- Greetings and quotes
- Countdowns and Pomodoro timers
- Stopwatches
- Text formatting
- Terminal UI helpers
- Fun facts and bedtime stories

---

## [See The Homepage](https://cozykit-home.vercel.app)

## or

## [See the entire Documentation](https://cozy-docs.vercel.app)

---

# License

MIT
