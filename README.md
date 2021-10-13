# match-compare
Rust style match compares in python

## Description

Let's say we have the following code:

```python
my_bet = 5
if my_bet > 4:
    print(f'{my_bet} is greater than 4!')
elif my_bet < 4:
    print(f'{my_bet} is less than 4!')
elif my_bet == 4:
    print(f'{my_bet} equals 4!')
```

Now we can refactor this into this:

```python
from match_compare import compare, Greater, Less, Equal


my_bet = 5
match compare(my_bet, 4):  # output: 5 is greater than 4!
    case Greater(value):
        print(f'{my_bet} is greater than {value}!')
    case Less(value):
        print(f'{my_bet} is less than {value}!')
    case Equal(value):
        print(f'{my_bet} is equal than {value}!')


my_bet = 4
match compare(my_bet, 4):  # output: # 4 equals 4!
    case Greater(value):
        print(f'{my_bet} is greater than {value}!')
    case Less(value):
        print(f'{my_bet} is less than {value}!')
    case Equal(value):
        print(f'{my_bet} equals {value}!')


my_bet = 3
match compare(my_bet, 4):  # output: 3 is less than 4!
    case Greater(value):
        print(f'{my_bet} is greater than {value}!')
    case Less(value):
        print(f'{my_bet} is less than {value}!')
    case Equal(value):
        print(f'{my_bet} equals {value}!')

```
