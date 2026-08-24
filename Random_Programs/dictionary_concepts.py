"""
PYTHON DICTIONARIES — A COMPLETE, INCREMENTAL TOUR
====================================================
Run this file top to bottom: `python python_dict_concepts.py`

Each SECTION below:
  1. Explains a concept in a comment
  2. Shows a small working example
  3. Ends with `assert` statements that act as tests — if the file
     runs without an AssertionError, you understood the concept correctly.

Sections are ordered from basic -> advanced.
"""

# ======================================================================
# SECTION 1 — Creating dictionaries
# ======================================================================
# A dict maps hashable keys -> values. Several ways to build one:

d1 = {"a": 1, "b": 2}                     # literal
d2 = dict(a=1, b=2)                       # keyword constructor (keys must be valid identifiers)
d3 = dict([("a", 1), ("b", 2)])
#The general rule:
#dict(iterable) works if iterable yields items that are themselves 2-element iterables (regardless of what container type wraps them):           # from a list of (key, value) pairs
#Search with this prompt "i need to understand all the concepts associated with dictionaries in python with coding example and tests in incremental complexity.  i mean concepts like enumeration, zip and all others which will help me understand and learn"
d4 = dict.fromkeys(["a", "b"], 0)         # same value for every key

assert d1 == d2 == d3 == {"a": 1, "b": 2}
assert d4 == {"a": 0, "b": 0}
print("Section 1 OK:", d1, d4)


# ======================================================================
# SECTION 2 — Accessing and updating values
# ======================================================================
person = {"name": "Asha", "age": 30}

# Direct indexing raises KeyError if missing
assert person["name"] == "Asha"

# .get() is the safe version — returns None (or a default) instead of raising
assert person.get("city") is None
assert person.get("city", "Unknown") == "Unknown"

# Adding / updating is just assignment
person["city"] = "Bengaluru"
person["age"] = 31
assert person == {"name": "Asha", "age": 31, "city": "Bengaluru"}

# setdefault(): get a value, and insert it if the key is absent — in one step
count = person.setdefault("visits", 0)
assert count == 0
assert person["visits"] == 0
# calling it again does NOT overwrite an existing value
person["visits"] = 5
assert person.setdefault("visits", 999) == 5

print("Section 2 OK:", person)


# ======================================================================
# SECTION 3 — Removing items
# ======================================================================
d = {"a": 1, "b": 2, "c": 3}

del d["a"]                       # remove by key, raises KeyError if missing
assert d == {"b": 2, "c": 3}

popped = d.pop("b")              # remove AND return the value
assert popped == 2
assert d == {"c": 3}

assert d.pop("missing", "default") == "default"   # pop with a fallback, no error

last_pair = d.popitem()          # removes and returns the LAST inserted (key, value)
assert last_pair == ("c", 3)
assert d == {}

d = {"a": 1}
d.clear()                        # empty the dict in place
assert d == {}
print("Section 3 OK")


# ======================================================================
# SECTION 4 — Iterating: keys(), values(), items()
# ======================================================================
scores = {"math": 90, "physics": 85, "chemistry": 88}

keys_seen = []
for subject in scores:                 # iterating a dict directly gives keys
    keys_seen.append(subject)
assert keys_seen == ["math", "physics", "chemistry"]  # order = insertion order (Python 3.7+)

values_seen = list(scores.values())
assert values_seen == [90, 85, 88]

pairs_seen = list(scores.items())
assert pairs_seen == [("math", 90), ("physics", 85), ("chemistry", 88)]

# The idiomatic way to get both key and value together:
summary = []
for subject, mark in scores.items():
    summary.append(f"{subject}={mark}")
assert summary == ["math=90", "physics=85", "chemistry=88"]

print("Section 4 OK:", summary)


# ======================================================================
# SECTION 5 — enumerate() with dictionaries
# ======================================================================
# enumerate() adds a running INDEX to any iterable. Dicts aren't naturally
# indexed, but you often want "the Nth key" while looping — enumerate gives
# you that without a manual counter variable.

fruits = {"apple": 3, "banana": 5, "cherry": 7}

indexed = []
for i, (fruit, qty) in enumerate(fruits.items()):
    indexed.append((i, fruit, qty))

assert indexed == [
    (0, "apple", 3),
    (1, "banana", 5),
    (2, "cherry", 7),
]

# Start counting from 1 instead of 0 using enumerate's `start` argument
numbered_report = [f"{i}. {fruit}" for i, fruit in enumerate(fruits, start=1)]
assert numbered_report == ["1. apple", "2. banana", "3. cherry"]

print("Section 5 OK:", numbered_report)


# ======================================================================
# SECTION 6 — zip() with dictionaries
# ======================================================================
# zip() pairs up multiple iterables element-by-element. Extremely common
# pattern: build a dict from two parallel lists (keys list + values list).

names = ["Rahul", "Meera", "Karan"]
ages = [25, 31, 28]

people = dict(zip(names, ages))
assert people == {"Rahul": 25, "Meera": 31, "Karan": 28}

# zip() also works on an EXISTING dict's keys/values to pair them back up,
# and to iterate two dicts together (e.g. comparing scores across two tests)
test1 = {"Rahul": 70, "Meera": 88, "Karan": 91}
test2 = {"Rahul": 75, "Meera": 80, "Karan": 95}

improvement = {}
for name, (m1, m2) in zip(test1, zip(test1.values(), test2.values())):
    improvement[name] = m2 - m1
assert improvement == {"Rahul": 5, "Meera": -8, "Karan": 4}

# zip() stops at the SHORTEST iterable — a common gotcha
short = dict(zip(["x", "y", "z"], [1, 2]))   # only 2 pairs, 'z' is dropped
assert short == {"x": 1, "y": 2}

print("Section 6 OK:", people, improvement)


# ======================================================================
# SECTION 7 — Dictionary comprehensions
# ======================================================================
# {key_expr: value_expr for item in iterable [if condition]}

squares = {n: n * n for n in range(6)}
assert squares == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With a filter condition
even_squares = {n: n * n for n in range(10) if n % 2 == 0}
assert even_squares == {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Built from zip() — combining Section 6 and 7
subjects = ["math", "physics", "chemistry"]
marks = [90, 85, 88]
scorecard = {s: m for s, m in zip(subjects, marks)}
assert scorecard == {"math": 90, "physics": 85, "chemistry": 88}

# Inverting a dict (swap keys and values) — only safe if values are unique & hashable
inverted = {v: k for k, v in scorecard.items()}
assert inverted == {90: "math", 85: "physics", 88: "chemistry"}

print("Section 7 OK:", squares, inverted)


# ======================================================================
# SECTION 8 — Merging dictionaries
# ======================================================================
defaults = {"theme": "light", "font_size": 12}
overrides = {"font_size": 16, "language": "en"}

# Method 1: .update() — mutates the dict in place, later values win
merged1 = defaults.copy()
merged1.update(overrides)
assert merged1 == {"theme": "light", "font_size": 16, "language": "en"}

# Method 2: unpacking with ** (Python 3.5+) — creates a NEW dict
merged2 = {**defaults, **overrides}
assert merged2 == merged1

# Method 3: the | and |= merge operators (Python 3.9+)
merged3 = defaults | overrides
assert merged3 == merged1
combo = defaults.copy()
combo |= overrides           # in-place merge
assert combo == merged1

print("Section 8 OK:", merged2)


# ======================================================================
# SECTION 9 — Nested dictionaries
# ======================================================================
company = {
    "engineering": {"headcount": 40, "manager": "Priya"},
    "sales": {"headcount": 15, "manager": "Aman"},
}

assert company["engineering"]["manager"] == "Priya"

# Safely reach into nested structures with chained .get()
missing_manager = company.get("marketing", {}).get("manager", "N/A")
assert missing_manager == "N/A"

# Update a nested value
company["sales"]["headcount"] += 1
assert company["sales"]["headcount"] == 16

# Flatten a nested dict into "dept.field": value pairs
flat = {
    f"{dept}.{field}": value
    for dept, info in company.items()
    for field, value in info.items()
}
assert flat["engineering.headcount"] == 40
assert flat["sales.manager"] == "Aman"

print("Section 9 OK:", flat)


# ======================================================================
# SECTION 10 — Sorting dictionaries
# ======================================================================
# Dicts themselves aren't "sorted" — but you can produce a sorted VIEW
# using sorted() with a key function, most often on .items().

prices = {"pen": 10, "notebook": 45, "eraser": 5, "sharpener": 15}

by_key = dict(sorted(prices.items()))                       # alphabetical by key
assert list(by_key.keys()) == ["eraser", "notebook", "pen", "sharpener"]

by_value_asc = dict(sorted(prices.items(), key=lambda kv: kv[1]))
assert list(by_value_asc.keys()) == ["eraser", "pen", "sharpener", "notebook"]

by_value_desc = dict(sorted(prices.items(), key=lambda kv: kv[1], reverse=True))
assert list(by_value_desc.keys()) == ["notebook", "sharpener", "pen", "eraser"]

# Top-N pattern: cheapest 2 items
cheapest_two = dict(sorted(prices.items(), key=lambda kv: kv[1])[:2])
assert cheapest_two == {"eraser": 5, "pen": 10}

print("Section 10 OK:", by_value_desc)


# ======================================================================
# SECTION 11 — collections.defaultdict
# ======================================================================
# A dict subclass that auto-creates a default value for a missing key
# instead of raising KeyError. Great for grouping/counting.
from collections import defaultdict

words = ["apple", "banana", "avocado", "blueberry", "cherry"]

by_first_letter = defaultdict(list)
for w in words:
    by_first_letter[w[0]].append(w)      # no need to check "if key exists" first

assert by_first_letter == {
    "a": ["apple", "avocado"],
    "b": ["banana", "blueberry"],
    "c": ["cherry"],
}
assert isinstance(by_first_letter["z"], list)   # accessing a missing key auto-creates []
assert by_first_letter["z"] == []

print("Section 11 OK:", dict(by_first_letter))


# ======================================================================
# SECTION 12 — collections.Counter
# ======================================================================
# A dict subclass specialised for counting hashable items.
from collections import Counter

letters = list("mississippi")
letter_counts = Counter(letters)

assert letter_counts["i"] == 4
assert letter_counts["s"] == 4
assert letter_counts["m"] == 1
assert letter_counts["z"] == 0                   # missing keys give 0, not KeyError

assert letter_counts.most_common(2) == [("i", 4), ("s", 4)]

# Counters support arithmetic
more_letters = Counter("mango")
combined = letter_counts + more_letters
assert combined["m"] == 2

print("Section 12 OK:", letter_counts.most_common(3))


# ======================================================================
# SECTION 13 — collections.OrderedDict
# ======================================================================
# Since Python 3.7, plain dicts already preserve insertion order, so
# OrderedDict is mostly legacy — but it adds two extra abilities:
# equality that cares about order, and move_to_end().
from collections import OrderedDict

od = OrderedDict()
od["first"] = 1
od["second"] = 2
od["third"] = 3

od.move_to_end("first")                 # move a key to the end
assert list(od.keys()) == ["second", "third", "first"]

od.move_to_end("third", last=False)     # move a key to the front
assert list(od.keys()) == ["third", "second", "first"]

# Regular dicts compare equal regardless of order; OrderedDicts don't
assert {"a": 1, "b": 2} == {"b": 2, "a": 1}
assert OrderedDict(a=1, b=2) != OrderedDict(b=2, a=1)

print("Section 13 OK:", list(od.items()))


# ======================================================================
# SECTION 14 — collections.ChainMap
# ======================================================================
# Groups multiple dicts into one logical view WITHOUT copying/merging them.
# Lookups check the dicts in order; writes go to the first dict only.
from collections import ChainMap

env_defaults = {"debug": False, "timeout": 30}
user_settings = {"timeout": 60}

settings = ChainMap(user_settings, env_defaults)
assert settings["timeout"] == 60      # found in user_settings (checked first)
assert settings["debug"] is False     # falls through to env_defaults

settings["debug"] = True              # writes go to the FIRST dict (user_settings)
assert user_settings == {"timeout": 60, "debug": True}
assert env_defaults == {"debug": False, "timeout": 30}   # untouched

print("Section 14 OK:", dict(settings))


# ======================================================================
# SECTION 15 — Dictionary views act like sets
# ======================================================================
# .keys() and .items() (if values are hashable) behave like sets and
# support &, |, -, ^ — useful for comparing two dicts.

inventory_mon = {"apple": 10, "banana": 5, "mango": 8}
inventory_tue = {"apple": 10, "banana": 3, "cherry": 6}

common_keys = inventory_mon.keys() & inventory_tue.keys()
assert common_keys == {"apple", "banana"}

only_monday = inventory_mon.keys() - inventory_tue.keys()
assert only_monday == {"mango"}

all_keys = inventory_mon.keys() | inventory_tue.keys()
assert all_keys == {"apple", "banana", "mango", "cherry"}

# .items() set-math finds keys whose (key, value) pair is IDENTICAL in both
unchanged_items = inventory_mon.items() & inventory_tue.items()
assert unchanged_items == {("apple", 10)}    # banana's value differs, so it's excluded

print("Section 15 OK:", common_keys, unchanged_items)


# ======================================================================
# SECTION 16 — Copying: shallow vs deep
# ======================================================================
import copy

original = {"name": "Team A", "members": ["Ravi", "Sana"]}

shallow = original.copy()               # same as dict(original)
shallow["name"] = "Team B"              # top-level change: independent
shallow["members"].append("Zoe")        # nested list is SHARED, not copied!

assert original["name"] == "Team A"                       # unaffected
assert original["members"] == ["Ravi", "Sana", "Zoe"]      # mutated! (shared reference)

deep = copy.deepcopy(original)
deep["members"].append("Leo")
assert original["members"] == ["Ravi", "Sana", "Zoe"]       # deep copy didn't touch original
assert deep["members"] == ["Ravi", "Sana", "Zoe", "Leo"]

print("Section 16 OK: shallow shares nested objects, deepcopy does not")


# ======================================================================
# SECTION 17 — What can be a dictionary key? (hashability)
# ======================================================================
# Keys must be hashable (implement __hash__), which roughly means immutable:
# str, int, float, bool, tuple-of-hashables, frozenset all work.
# list, dict, set are UNHASHABLE and cannot be keys.

valid = {
    "text": 1,
    42: "int key",
    3.14: "float key",
    (1, 2): "tuple key",
    frozenset({1, 2}): "frozenset key",
}
assert valid[(1, 2)] == "tuple key"

try:
    bad = {["a", "b"]: 1}     # list is mutable -> unhashable -> TypeError
    raised = False
except TypeError:
    raised = True
assert raised is True

print("Section 17 OK: unhashable keys correctly rejected")


# ======================================================================
# SECTION 18 — **kwargs and dict unpacking with functions
# ======================================================================
def describe_person(name, age, city="Unknown"):
    return f"{name} ({age}) from {city}"

details = {"name": "Nisha", "age": 27, "city": "Pune"}
assert describe_person(**details) == "Nisha (27) from Pune"

# A function that COLLECTS extra keyword args into a dict
def build_profile(name, **extra_fields):
    profile = {"name": name}
    profile.update(extra_fields)
    return profile

profile = build_profile("Vikram", role="Engineer", level=3)
assert profile == {"name": "Vikram", "role": "Engineer", "level": 3}

print("Section 18 OK:", profile)


# ======================================================================
# SECTION 19 — JSON <-> dict
# ======================================================================
# Python dicts map directly onto JSON objects — this is why dicts are
# the standard way to represent API payloads / config files.
import json

record = {"id": 1, "active": True, "tags": ["new", "urgent"]}
as_json = json.dumps(record)
back_to_dict = json.loads(as_json)

assert isinstance(as_json, str)
assert back_to_dict == record

print("Section 19 OK:", as_json)


# ======================================================================
# ALL SECTIONS PASSED
# ======================================================================
print("\nAll 19 sections executed and all assertions passed.")