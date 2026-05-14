# cozy-kit Greeting Class

## Import

```python
from cozy_kit import Greeting
```

## Create an object

```python
person = Greeting(
    name='Example',
    age=12,
    gender='male',
    nickname='Example.Nickname'
)
```

---

## Available Functions

| Function           | Description                      |
|--------------------|----------------------------------|
| `welcome()`        | Welcomes the user                |
| `bye(destination)` | Says goodbye                     |
| `good_morning()`   | Returns a morning quote          |
| `good_afternoon()` | Returns an afternoon quote       |
| `good_evening()`   | Returns an evening quote         |
| `good_night()`     | Returns a bedtime story          |
| `auto_greet()`     | Automatically selects a greeting |
| `motivate()`       | Returns a motivational quote     |
| `fun_facts()`      | Returns a random fun fact        |

---

# Greeting Examples

## Usage

```python
from cozy_kit import Greeting

user = Greeting(
    name="youssef",
    age=16,
    gender="male",
    nickname="joe"
)

print(user.welcome())

print(user.bye("school"))

print(user.good_morning())

print(user.fun_facts())

print(user.auto_greet())
```

---

## Example Output

### welcome()

```text
Welcome Youssef!
Or welcome Joe!
```

### bye()

```text
Bye Youssef! Have a nice day at school!
Or bye Joe!
```

### good_morning()

```text
Good Morning Youssef!
Or good morning Joe!

Anyways, here's a quick morning quote.

Albert Einstein

Life is like riding a bicycle.
To keep your balance, you must keep moving.
```

### fun_facts()

```text
Space Facts

A day on Venus is longer than a year on Venus.
```

### auto_greet()

```text
Good Afternoon Youssef!
Or good afternoon Joe!

Steve Jobs

The only way to do great work is to love what you do.
```
