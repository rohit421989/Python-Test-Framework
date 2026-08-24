"""
Test runner for dict_exercises.py

Usage:
    python3 test_dict_exercises.py dict_exercises            # test your work
    python3 test_dict_exercises.py dict_exercises_solutions  # sanity-check the answer key

Prints PASS / FAIL / TODO / ERROR for every exercise across all 9 phases.
"""
import importlib, sys

MODNAME = sys.argv[1] if len(sys.argv) > 1 else "solutions"
m = importlib.import_module(MODNAME)

results = []

def _a(cond):
    if not cond:
        raise AssertionError()

def check(name, fn_name, test_fn):
    fn = getattr(m, fn_name, None)
    if fn is None:
        results.append((name, "MISSING", f"{fn_name} not found"))
        return
    try:
        test_fn(fn)
        results.append((name, "PASS", ""))
    except NotImplementedError:
        results.append((name, "TODO", "not implemented yet"))
    except AssertionError as e:
        results.append((name, "FAIL", str(e) or "assertion failed"))
    except Exception as e:
        results.append((name, "ERROR", f"{type(e).__name__}: {e}"))

# PHASE 1
check("1.1 get_safe", "ex1_1_get_safe", lambda f: (
    _a(f({"a": 1}, "a", 0) == 1),
    _a(f({"a": 1}, "b", 99) == 99),
))
check("1.2 add_or_update", "ex1_2_add_or_update", lambda f: (
    _a(f({"a": 1}, "b", 2) == {"a": 1, "b": 2}),
    _a(f({"a": 1}, "a", 5) == {"a": 5}),
))
check("1.3 remove_key", "ex1_3_remove_key", lambda f: (
    _a(f({"a": 1, "b": 2}, "a") == {"b": 2}),
    _a(f({"a": 1}, "z") == {"a": 1}),
))
check("1.4 toggle_visit", "ex1_4_toggle_visit", lambda f: (
    _a(f({}) == {"visits": 1}),
    _a(f({"visits": 3}) == {"visits": 4}),
))

# PHASE 2
check("2.1 sum_values", "ex2_1_sum_values", lambda f: (
    _a(f({"a": 1, "b": 2, "c": 3}) == 6),
))
check("2.2 indexed_keys", "ex2_2_indexed_keys", lambda f: (
    _a(f({"x": 1, "y": 2}) == ["0:x", "1:y"]),
))
check("2.3 dict_from_lists", "ex2_3_dict_from_lists", lambda f: (
    _a(f(["a", "b"], [1, 2]) == {"a": 1, "b": 2}),
))
check("2.4 diff_by_position", "ex2_4_diff_by_position", lambda f: (
    _a(f({"a": 1, "b": 2}, {"a": 5, "b": 1}) == {"a": 4, "b": -1}),
))
check("2.5 numbered_report", "ex2_5_numbered_report", lambda f: (
    _a(f({"x": 0, "y": 0}) == ["1. x", "2. y"]),
))

# PHASE 3
check("3.1 filter_dict", "ex3_1_filter_dict", lambda f: (
    _a(f({"a": 1, "b": 2, "c": 3}, lambda k, v: v > 1) == {"b": 2, "c": 3}),
))
check("3.2 invert_dict", "ex3_2_invert_dict", lambda f: (
    _a(f({"a": 1, "b": 2}) == {1: "a", 2: "b"}),
))
check("3.3 squares", "ex3_3_squares", lambda f: (
    _a(f(4) == {0: 0, 1: 1, 2: 4, 3: 9}),
))
check("3.4 scorecard", "ex3_4_scorecard", lambda f: (
    _a(f(["math", "sci"], [90, 80]) == {"math": 90, "sci": 80}),
))

# PHASE 4
check("4.1 merge", "ex4_1_merge", lambda f: (
    _a(f({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}),
    _a(f({"a": 1}, {"a": 9}) == {"a": 9}),
))
check("4.2 deep_get", "ex4_2_deep_get", lambda f: (
    _a(f({"a": {"b": {"c": 5}}}, ["a", "b", "c"]) == 5),
    _a(f({"a": {}}, ["a", "b", "c"], "N/A") == "N/A"),
))
check("4.3 flatten", "ex4_3_flatten", lambda f: (
    _a(f({"eng": {"hc": 10}, "sales": {"hc": 5}}) == {"eng.hc": 10, "sales.hc": 5}),
))
check("4.4 increment_nested", "ex4_4_increment_nested", lambda f: (
    _a(f({}, "fruit", "apple") == {"fruit": {"apple": 1}}),
    _a(f({"fruit": {"apple": 1}}, "fruit", "apple") == {"fruit": {"apple": 2}}),
))

# PHASE 5
check("5.1 sort_by_key", "ex5_1_sort_by_key", lambda f: (
    _a(list(f({"b": 1, "a": 2}).keys()) == ["a", "b"]),
))
check("5.2 sort_by_value_desc", "ex5_2_sort_by_value_desc", lambda f: (
    _a(list(f({"a": 1, "b": 3, "c": 2}).keys()) == ["b", "c", "a"]),
))
check("5.3 top_n", "ex5_3_top_n", lambda f: (
    _a(f({"a": 1, "b": 3, "c": 2}, 2) == {"b": 3, "c": 2}),
))

# PHASE 6
check("6.1 group_by_length", "ex6_1_group_by_length", lambda f: (
    _a(f(["a", "bb", "cc", "ddd"]) == {1: ["a"], 2: ["bb", "cc"], 3: ["ddd"]}),
))
check("6.2 count_chars", "ex6_2_count_chars", lambda f: (
    _a(f("aab")["a"] == 2),
    _a(f("aab")["b"] == 1),
))
check("6.3 most_common_word", "ex6_3_most_common_word", lambda f: (
    _a(f(["a", "b", "a"], 1) == [("a", 2)]),
))
check("6.4 layered_settings", "ex6_4_layered_settings", lambda f: (
    _a(f({"x": 1}, {"x": 0, "y": 2})["x"] == 1),
    _a(f({"x": 1}, {"x": 0, "y": 2})["y"] == 2),
))

# PHASE 7
check("7.1 common_keys", "ex7_1_common_keys", lambda f: (
    _a(f({"a": 1, "b": 2}, {"b": 9, "c": 3}) == {"b"}),
))
check("7.2 only_in_first", "ex7_2_only_in_first", lambda f: (
    _a(f({"a": 1, "b": 2}, {"b": 9}) == {"a"}),
))
check("7.3 is_hashable", "ex7_3_is_hashable", lambda f: (
    _a(f((1, 2)) is True),
    _a(f([1, 2]) is False),
))

# PHASE 8
check("8.1 build_record", "ex8_1_build_record", lambda f: (
    _a(f("Sam", role="eng", level=2) == {"name": "Sam", "role": "eng", "level": 2}),
))
check("8.2 to_json", "ex8_2_to_json", lambda f: (
    _a(f({"b": 1, "a": 2}) == '{"a": 2, "b": 1}'),
))
check("8.3 from_json", "ex8_3_from_json", lambda f: (
    _a(f('{"a": 1}') == {"a": 1}),
))

# PHASE 9
check("9.1 word_frequency_report", "ex9_1_word_frequency_report", lambda f: (
    _a(f("the cat sat on the mat the cat ran", 2) == ["1. the (3)", "2. cat (2)"]),
))
check("9.2 grade_summary", "ex9_2_grade_summary", lambda f: (
    _a(f([("Sam", "math", 80), ("Sam", "sci", 90), ("Ana", "math", 70)]) == {"Sam": 85.0, "Ana": 70.0}),
))
check("9.3 merge_configs", "ex9_3_merge_configs", lambda f: (
    _a(f({"a": 1, "b": 2}, {"b": 3}, {"c": 4}) == {"a": 1, "b": 3, "c": 4}),
))

# ---- report ----
width = max(len(r[0]) for r in results)
counts = {"PASS": 0, "FAIL": 0, "TODO": 0, "ERROR": 0, "MISSING": 0}
for name, status, msg in results:
    counts[status] = counts.get(status, 0) + 1
    line = f"{name.ljust(width)}  {status}"
    if msg:
        line += f"  -- {msg}"
    print(line)

print("\nSummary:", ", ".join(f"{k}={v}" for k, v in counts.items() if v))
