# cozy-kit TextStudio Class

## Import

```python
from cozy_kit import TextStudio
```

## Create an object

```python
text_editor = TextStudio()
```

---

## Available Functions

| Function                                 | Description                     |
|------------------------------------------|---------------------------------|
| `to_morse(text)`                         | Converts text to Morse code     |
| `to_upper(text)`                         | Converts text to uppercase      |
| `to_title(text)`                         | Converts text to title case     |
| `to_lower(text)`                         | Converts text to lowercase      |
| `space_out_letters(text)`                | Adds spaces between letters     |
| `replace_with_spaces(text, replacement)` | Replaces characters with spaces |
| `caesar(text, shift)`                    | Caesar cipher encryption        |
| `reverse(text)`                          | Reverses text                   |
| `word_count(text)`                       | Counts words                    |
| `char_count(text)`                       | Counts characters               |
| `remove_spaces(text)`                    | Removes spaces                  |
| `snake(text)`                            | Converts text to snake_case     |
| `remove_punctuation(text)`               | Removes punctuation             |
| `cozy_box(text)`                         | Put a cool box around the text  |

---

# TextStudio Example

## Usage

```python
from cozy_kit import TextStudio

studio = TextStudio()

text = "Hello World"

print(studio.to_upper(text))
print(studio.to_lower(text))
print(studio.to_title(text))
print(studio.reverse(text))
print(studio.snake(text))
print(studio.space_out_letters(text))
print(studio.to_morse(text))
print(studio.caesar(text, 3))
print(studio.word_count(text))
print(studio.char_count(text))
print(studio.remove_spaces(text))
print(studio.remove_punctuation("Hello, World!"))
```

---

## Output

### to_upper()

```text
HELLO WORLD
```

### to_lower()

```text
hello world
```

### reverse()

```text
dlroW olleH
```

### snake()

```text
hello_world
```

### space_out_letters()

```text
H e l l o   W o r l d
```

### to_morse()

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

### caesar()

```text
Khoor Zruog
```

### word_count()

```text
2
```

### char_count()

```text
11
```

### remove_spaces()

```text
HelloWorld
```

### remove_punctuation()

```text
Hello World
```
