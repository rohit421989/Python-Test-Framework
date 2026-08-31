#How To Find the Length of a List in Python
# a=[1, 2, 3, 4, 5]
# print(len(a))

# #To check if an element exists in a list

# try:
#     x=a.index(33)
#     print(x)
# except ValueError:
#     print("Element does not exist in the list")

# # we can use count
# if a.count(3)>0:
#     print("Element exists in the list")

# cleared = {"x": 10, "y": 20}
# result = cleared.clear()
# print(result)  # Output: {}
# assert result is None
# assert cleared == {}

# summary_dict={'a': 1, 'b': 2, 'c': 33}
# val=summary_dict.setdefault("d", 3)
# print("setdefault('d', 3) ->", val, type(val))

# # copy_dict = summary_dict.copy()
# # print( copy_dict == summary_dict)
# # print(copy_dict is not summary_dict)
# keys_view = summary_dict.keys()
# values_view = summary_dict.values()
# items_view = summary_dict.items()
# print("keys() ->", keys_view, type(keys_view))
# print("values() ->", values_view, type(values_view))
# print("items() ->", items_view, type(items_view))
# print("list(keys()) ->", list(keys_view))
# print("list(values()) ->", list(values_view))
# print("list(items()) ->", list(items_view))



# fruit_prices = {"apple": 5, "banana": 7}
# print("pop('apple') ->", fruit_prices.pop("apple"))
# print("after pop ->", fruit_prices)
# print("pop('missing', 0) ->", fruit_prices.pop("missing",0), type(fruit_prices.pop("missing", 0)))


# pair_dict = {"first": 1, "second": 2}
# last_pair = pair_dict.popitem()
# print("popitem() ->", last_pair, type(last_pair))
# print("after popitem ->", pair_dict)




# print("setdefault('c', 3) ->", summary_dict.setdefault("c", 3), type(summary_dict.setdefault("c", 3)))
# print("after setdefault, dict ->", summary_dict)
# print("setdefault('a', 99) ->", summary_dict.setdefault("a", 99), type(summary_dict.setdefault("a", 99)))


update_target = {"name": "Asha"}
#x=update_target.update({"name":"Rk","age": 30, "city": "New York"})
#x=update_target.update(name='Rk',age= 30, city= 'New York')
# x=update_target.update((('name','Rk'),('age', 30), ('city', 'New York')))
# print("update() ->", x, type(x))
# print("after update, dict ->", update_target)

x=update_target.values()
y=update_target.keys()
print("values() ->", x, type(x))
print("list(values()) ->", list(x))
print("list(keys()) ->", list(y))