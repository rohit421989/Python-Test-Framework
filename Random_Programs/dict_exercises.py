"""
PYTHON DICTIONARY EXERCISES — 9 PHASES, INCREMENTAL DIFFICULTY
=================================================================
How to use this file:
  1. Fill in each function below (replace `raise NotImplementedError`
     with your solution). Read the docstring for what's expected.
  2. Run:  python3 test_dict_exercises.py dict_exercises
  3. It will print PASS / FAIL / TODO / ERROR for every exercise.
  4. Work phase by phase — each phase builds on concepts from the last.
     Phases 2-3 lean on enumerate()/zip()/comprehensions from your
     dictionary-concepts lesson; phases 6+ use the `collections` module.
  5. Stuck? dict_exercises_solutions.py has full reference answers —
     but try each exercise yourself first.

Concept map (which phase teaches/uses what):
  Phase 1 -> creation, .get(), .setdefault(), removal
  Phase 2 -> iteration, enumerate(), zip()
  Phase 3 -> dict comprehensions
  Phase 4 -> merging, nested dicts
  Phase 5 -> sorting with sorted()
  Phase 6 -> collections: defaultdict, Counter, ChainMap
  Phase 7 -> views as sets, hashability
  Phase 8 -> **kwargs, JSON
  Phase 9 -> capstone: combine everything
"""
from collections import defaultdict, Counter, ChainMap
import json


# ======================================================================
# PHASE 1 — Creation, access, removal (single concepts)
# ======================================================================

def ex1_1_get_safe(d, key, default):
    """Return d[key] if present, else `default`. Must NOT raise KeyError.
    ex1_1_get_safe({"a": 1}, "a", 0)  -> 1
    ex1_1_get_safe({"a": 1}, "b", 99) -> 99
    """
    return d.get(key, default)



def ex1_2_add_or_update(d, key, value):
    """Return a NEW dict equal to `d` but with d[key] = value.
    The original `d` must be left unmodified.
    """
    raise NotImplementedError


def ex1_3_remove_key(d, key):
    """Return a NEW dict equal to `d` with `key` removed (no error if missing).
    The original `d` must be left unmodified.
    """
    raise NotImplementedError


def ex1_4_toggle_visit(d):
    """Return a NEW dict where d["visits"] is incremented by 1.
    If "visits" doesn't exist yet, treat it as starting at 0.
    Use .setdefault() for this one.
    ex1_4_toggle_visit({})            -> {"visits": 1}
    ex1_4_toggle_visit({"visits": 3}) -> {"visits": 4}
    """
    raise NotImplementedError


# ======================================================================
# PHASE 2 — Iteration, enumerate(), zip()
# ======================================================================

def ex2_1_sum_values(d):
    """Return the sum of all values in d."""
    raise NotImplementedError


def ex2_2_indexed_keys(d):
    """Return a list of "index:key" strings using enumerate().
    ex2_2_indexed_keys({"x": 1, "y": 2}) -> ["0:x", "1:y"]
    """
    raise NotImplementedError


def ex2_3_dict_from_lists(keys, values):
    """Build a dict by pairing `keys` and `values` positionally using zip()."""
    raise NotImplementedError


def ex2_4_diff_by_position(d1, d2):
    """d1 and d2 have the SAME keys in the same order. Return a dict mapping
    each key -> (d2's value - d1's value), using zip() to pair the values up.
    ex2_4_diff_by_position({"a":1,"b":2}, {"a":5,"b":1}) -> {"a":4, "b":-1}
    """
    raise NotImplementedError


def ex2_5_numbered_report(d, start=1):
    """Return a list like ["1. x", "2. y", ...] over d's keys, using
    enumerate(..., start=start).
    """
    raise NotImplementedError


# ======================================================================
# PHASE 3 — Dictionary comprehensions
# ======================================================================

def ex3_1_filter_dict(d, predicate):
    """Return a new dict containing only (k, v) pairs where predicate(k, v)
    is True. Use a dict comprehension.
    """
    raise NotImplementedError


def ex3_2_invert_dict(d):
    """Return a new dict with keys and values swapped (comprehension)."""
    raise NotImplementedError


def ex3_3_squares(n):
    """Return {0: 0, 1: 1, 2: 4, ..., n-1: (n-1)**2} via comprehension."""
    raise NotImplementedError


def ex3_4_scorecard(subjects, marks):
    """Combine zip() + a dict comprehension to build {subject: mark}."""
    raise NotImplementedError


# ======================================================================
# PHASE 4 — Merging & nested dictionaries
# ======================================================================

def ex4_1_merge(d1, d2):
    """Return a new dict merging d1 and d2; d2's values win on conflicts.
    Try doing this with the ** unpacking or | operator.
    """
    raise NotImplementedError


def ex4_2_deep_get(nested, path, default=None):
    """`path` is a list of keys to follow into `nested` dict-of-dicts.
    Return the value at that path, or `default` if any key along the
    way is missing.
    ex4_2_deep_get({"a": {"b": {"c": 5}}}, ["a", "b", "c"]) -> 5
    ex4_2_deep_get({"a": {}}, ["a", "b", "c"], "N/A")       -> "N/A"
    """
    raise NotImplementedError


def ex4_3_flatten(nested, sep="."):
    """`nested` is a dict of dicts, one level deep. Flatten it into a
    single-level dict with keys like "outer.inner".
    ex4_3_flatten({"eng": {"hc": 10}, "sales": {"hc": 5}})
        -> {"eng.hc": 10, "sales.hc": 5}
    """
    raise NotImplementedError


def ex4_4_increment_nested(counters, category, item):
    """`counters` is a dict like {"fruit": {"apple": 1}}. Return a NEW
    counters dict with counters[category][item] incremented by 1
    (creating the category/item if missing). Original must be unmodified.
    """
    raise NotImplementedError


# ======================================================================
# PHASE 5 — Sorting dictionaries
# ======================================================================

def ex5_1_sort_by_key(d):
    """Return a new dict with items sorted alphabetically/numerically by key."""
    raise NotImplementedError


def ex5_2_sort_by_value_desc(d):
    """Return a new dict with items sorted by value, highest first."""
    raise NotImplementedError


def ex5_3_top_n(d, n):
    """Return a new dict with only the n highest-value items."""
    raise NotImplementedError


# ======================================================================
# PHASE 6 — collections module: defaultdict, Counter, ChainMap
# ======================================================================

def ex6_1_group_by_length(words):
    """Group `words` by their length using defaultdict(list).
    ex6_1_group_by_length(["a","bb","cc","ddd"])
        -> {1: ["a"], 2: ["bb","cc"], 3: ["ddd"]}
    """
    raise NotImplementedError


def ex6_2_count_chars(s):
    """Return a Counter of character frequencies in string s."""
    raise NotImplementedError


def ex6_3_most_common_word(words, n=1):
    """Return the n most common words as a list of (word, count) tuples,
    using Counter.most_common().
    """
    raise NotImplementedError


def ex6_4_layered_settings(*dicts):
    """Return a ChainMap over the given dicts (first dict has priority
    on lookups).
    """
    raise NotImplementedError


# ======================================================================
# PHASE 7 — Views as sets, hashability
# ======================================================================

def ex7_1_common_keys(d1, d2):
    """Return the set of keys present in BOTH d1 and d2 (use & on .keys())."""
    raise NotImplementedError


def ex7_2_only_in_first(d1, d2):
    """Return the set of keys present in d1 but NOT in d2 (use - on .keys())."""
    raise NotImplementedError


def ex7_3_is_hashable(x):
    """Return True if x could be used as a dict key, False otherwise.
    Don't hardcode types — actually try hashing it.
    """
    raise NotImplementedError


# ======================================================================
# PHASE 8 — **kwargs and JSON
# ======================================================================

def ex8_1_build_record(name, **fields):
    """Return {"name": name, **fields} — collect extra keyword args into
    the resulting dict.
    """
    raise NotImplementedError


def ex8_2_to_json(d):
    """Return a JSON string for dict d, with keys sorted alphabetically."""
    raise NotImplementedError


def ex8_3_from_json(s):
    """Parse JSON string `s` back into a Python dict."""
    raise NotImplementedError


# ======================================================================
# PHASE 9 — CAPSTONE: combine everything
# ======================================================================

def ex9_1_word_frequency_report(text, top_n=3):
    """Lowercase + split `text` into words, count frequencies (Counter),
    and return the top_n as a numbered list of strings:
    ["1. the (3)", "2. cat (2)", ...]
    Combine: string ops, Counter, most_common(), enumerate().
    """
    raise NotImplementedError


def ex9_2_grade_summary(records):
    """`records` is a list of (student_name, subject, mark) tuples.
    Return {student_name: average_mark} rounded to 2 decimals.
    Combine: defaultdict(list) for grouping, then a dict comprehension
    to compute averages.
    ex9_2_grade_summary([("Sam","math",80), ("Sam","sci",90), ("Ana","math",70)])
        -> {"Sam": 85.0, "Ana": 70.0}
    """
    raise NotImplementedError


def ex9_3_merge_configs(defaults, *overrides):
    """Merge `defaults` with any number of `overrides` dicts, applied in
    order (later overrides win). Return a single plain dict (not a
    ChainMap this time) using the | operator in a loop, or reduce().
    """
    raise NotImplementedError
