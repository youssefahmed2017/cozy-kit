# cozy-kit

> A cozy Python package with greetings, quotes, bedtime stories, timers, and text utilities.

Created by **Youssef**

---
# Requirements

- Python +3.8

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

# Other Docs

- [Greeting Class](https://github.com/youssefahmed2017/cozy-kit/blob/main/docs/greeting_class.md)

- [Timer Class](https://github.com/youssefahmed2017/cozy-kit/blob/main/docs/timer_class.md)

- [TextStudio Class](https://github.com/youssefahmed2017/cozy-kit/blob/main/docs/textstudio_class.md)

- [Quick Summary Of Everything](https://github.com/youssefahmed2017/cozy-kit/blob/main/docs/summary.md)

---

# Quick Note
### If you want to access something outside that is not __versio (like author), You can't type:
```python
from cozy_kit import *

print(__author__)
```
### You need to type:
```python
from cozy_kit import *

# Create Object
__details__ = Details.__details__

print(__details__['author'])

# or

from cozy_kit import Details

# Create Object
__details__ = Details.__details__

print(__details__['author'])
```
