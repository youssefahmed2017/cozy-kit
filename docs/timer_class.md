# cozy-kit Timer Class

## Import

```python
from cozy_kit import Timer
```

## Create an object

```python
timer = Timer()
```

---

## Available Functions

| Function                                                 | Description                    |
|----------------------------------------------------------|--------------------------------|
| `countdown(count, time_type, show)`                      | Starts a countdown             |
| `pomodoro(work_time, break_time, long_break_time, show)` | Starts a Pomodoro timer        |
| `wait(count, time_type)`                                 | Sleeps for a specific duration |
| `get_time()`                                             | Returns the current time       |
| `start_stopwatch()`                                      | Starts the stopwatch           |
| `end_stopwatch()`                                        | Stops the stopwatch            |

---

## Supported Time Types

| Type   | Meaning |
|--------|---------|
| `sec`  | Seconds |
| `min`  | Minutes |
| `hour` | Hours   |

---

# Countdown Example

## Usage

```python
from cozy_kit import Timer

timer = Timer()

timer.countdown(
    count=5,
    time_type='sec',
    show=print
)
```

## Output

```text
00:05
00:04
00:03
00:02
00:01
⏰ Time's up!
```

---

# Stopwatch Example

## Usage

```python
from cozy_kit import Timer
import time

timer = Timer()

timer.start_stopwatch()

time.sleep(3)

elapsed = timer.end_stopwatch()

print(elapsed)
```

## Output

```text
0:00:03.002194
```

---

# Wait Example

## Usage

```python
from cozy_kit import Timer

timer = Timer()

print("Waiting...")

timer.wait(3, "sec")

print("Done!")
```

## Output

```text
Waiting...
Done!
```

---

# Pomodoro Example

## Usage

```python
from cozy_kit import Timer

timer = Timer()

timer.pomodoro(
    work_time=1,
    break_time=1,
    long_break_time=2,
    show=print
)
```

## Output

```text
💻 Work Time
01:00
...

☕ Short Break Time
01:00
...

💻 Work Time
01:00
...

⏰ Long Break Time
02:00
...
```
