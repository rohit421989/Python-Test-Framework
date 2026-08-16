#How To Find the Length of a List in Python
a=[1, 2, 3, 4, 5]
print(len(a))

#To check if an element exists in a list

try:
    x=a.index(33)
    print(x)
except ValueError:
    print("Element does not exist in the list")

# we can use count
if a.count(3)>0:
    print("Element exists in the list")