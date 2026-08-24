"""Reference solutions — used only to validate the test harness."""
from collections import defaultdict, Counter, ChainMap
import json

# ---------- PHASE 1 ----------
def ex1_1_get_safe(d, key, default):
    return d.get(key, default)

def ex1_2_add_or_update(d, key, value):
    new_d = dict(d)
    new_d[key] = value
    return new_d

def ex1_3_remove_key(d, key):
    new_d = dict(d)
    new_d.pop(key, None)
    return new_d

def ex1_4_toggle_visit(d):
    d = dict(d)
    d["visits"] = d.setdefault("visits", 0) + 1
    return d

# ---------- PHASE 2 ----------
def ex2_1_sum_values(d):
    return sum(d.values())

def ex2_2_indexed_keys(d):
    return [f"{i}:{k}" for i, k in enumerate(d)]

def ex2_3_dict_from_lists(keys, values):
    return dict(zip(keys, values))

def ex2_4_diff_by_position(d1, d2):
    return {k: v2 - v1 for k, (v1, v2) in zip(d1, zip(d1.values(), d2.values()))}

def ex2_5_numbered_report(d, start=1):
    return [f"{i}. {k}" for i, k in enumerate(d, start=start)]

# ---------- PHASE 3 ----------
def ex3_1_filter_dict(d, predicate):
    return {k: v for k, v in d.items() if predicate(k, v)}

def ex3_2_invert_dict(d):
    return {v: k for k, v in d.items()}

def ex3_3_squares(n):
    return {i: i * i for i in range(n)}

def ex3_4_scorecard(subjects, marks):
    return {s: m for s, m in zip(subjects, marks)}

# ---------- PHASE 4 ----------
def ex4_1_merge(d1, d2):
    return {**d1, **d2}

def ex4_2_deep_get(nested, path, default=None):
    current = nested
    for key in path:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current

def ex4_3_flatten(nested, sep="."):
    flat = {}
    for outer, inner in nested.items():
        for k, v in inner.items():
            flat[f"{outer}{sep}{k}"] = v
    return flat

def ex4_4_increment_nested(counters, category, item):
    counters = {k: dict(v) for k, v in counters.items()}
    counters.setdefault(category, {})
    counters[category][item] = counters[category].get(item, 0) + 1
    return counters

# ---------- PHASE 5 ----------
def ex5_1_sort_by_key(d):
    return dict(sorted(d.items()))

def ex5_2_sort_by_value_desc(d):
    return dict(sorted(d.items(), key=lambda kv: kv[1], reverse=True))

def ex5_3_top_n(d, n):
    return dict(sorted(d.items(), key=lambda kv: kv[1], reverse=True)[:n])

# ---------- PHASE 6 ----------
def ex6_1_group_by_length(words):
    groups = defaultdict(list)
    for w in words:
        groups[len(w)].append(w)
    return dict(groups)

def ex6_2_count_chars(s):
    return Counter(s)

def ex6_3_most_common_word(words, n=1):
    return Counter(words).most_common(n)

def ex6_4_layered_settings(*dicts):
    return ChainMap(*dicts)

# ---------- PHASE 7 ----------
def ex7_1_common_keys(d1, d2):
    return d1.keys() & d2.keys()

def ex7_2_only_in_first(d1, d2):
    return d1.keys() - d2.keys()

def ex7_3_is_hashable(x):
    try:
        hash(x)
        return True
    except TypeError:
        return False

# ---------- PHASE 8 ----------
def ex8_1_build_record(name, **fields):
    record = {"name": name}
    record.update(fields)
    return record

def ex8_2_to_json(d):
    return json.dumps(d, sort_keys=True)

def ex8_3_from_json(s):
    return json.loads(s)

# ---------- PHASE 9 (capstone) ----------
def ex9_1_word_frequency_report(text, top_n=3):
    words = text.lower().split()
    counts = Counter(words)
    ranked = counts.most_common(top_n)
    return [f"{i}. {w} ({c})" for i, (w, c) in enumerate(ranked, start=1)]

def ex9_2_grade_summary(records):
    summary = defaultdict(list)
    for name, subject, mark in records:
        summary[name].append(mark)
    return {name: round(sum(marks) / len(marks), 2) for name, marks in summary.items()}

def ex9_3_merge_configs(defaults, *overrides):
    merged = dict(defaults)
    for o in overrides:
        merged |= o
    return merged
