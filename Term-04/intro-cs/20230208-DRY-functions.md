# The D.R.Y principle:
Don't Repeat Yourself.

Here is some Python code that I was working with today for a project:
``` python
import random

def random_name():
    names = ['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Harper', 'Evelyn', 'Abigail', 'Emily', 'Elizabeth', 'Avery', 'Sofia', 'Ella', 'Madison', 'Scarlett', 'Victoria', 'Aria', 'Grace', 'Chloe', 'Camila', 'Penelope', 'Riley', 'Nora', 'Lily', 'Eleanor', 'Hazel', 'Aubrey']
    pick = random.choice(names)
    return pick

def random_importance():
    options = ['not_important', 'somewhat_important', 'important', 'very_important']
    pick = random.choice(options)
    return pick

def random_competence():
    options = ["cant_do_it", "need_help", "can_do_it_easily"]
    pick = random.choice(options)
    return pick

def random_comfort():
    options = ["hate_it", "dont_like_it", "neutral", "like_it", "love_it"]
    pick = random.choice(options)
    return pick

random_name       = random_name()
random_importance = random_importance()
random_competence = random_competence()
random_comfort    = random_comfort()
  
  ```

This can be optimized in order to minimize repetition. Try this:

``` python
import random

names             = ['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Harper', 'Evelyn', 'Abigail', 'Emily', 'Elizabeth', 'Avery', 'Sofia', 'Ella', 'Madison', 'Scarlett', 'Victoria', 'Aria', 'Grace', 'Chloe', 'Camila', 'Penelope', 'Riley', 'Nora', 'Lily', 'Eleanor', 'Hazel', 'Aubrey']
importance_levels = ['not_important', 'somewhat_important', 'important', 'very_important']
competence_levels = ["cant_do_it", "need_help", "can_do_it_easily"]
comfort_levels    = ["hate_it", "dont_like_it", "neutral", "like_it", "love_it"]


def random_item(list):
    return random.choice(list)

random_name       = random_item(names)
random_importance = random_item(importance_levels)
random_competence = random_item(competence_levels)
random_comfort    = random_item(comfort_levels)
```
Heck, I could reduce this further, since the function is largely unnecessary:
``` python
import random

names             = ['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Harper', 'Evelyn', 'Abigail', 'Emily', 'Elizabeth', 'Avery', 'Sofia', 'Ella', 'Madison', 'Scarlett', 'Victoria', 'Aria', 'Grace', 'Chloe', 'Camila', 'Penelope', 'Riley', 'Nora', 'Lily', 'Eleanor', 'Hazel', 'Aubrey']
importance_levels = ['not_important', 'somewhat_important', 'important', 'very_important']
competence_levels = ["cant_do_it", "need_help", "can_do_it_easily"]
comfort_levels    = ["hate_it", "dont_like_it", "neutral", "like_it", "love_it"]

random_name       = random.choice(names)
random_importance = random.choice(importance_levels)
random_competence = random.choice(competence_levels)
random_comfort    = random.choice(comfort_levels)
```
