
# Python List Built-in Methods - All in One File

print("=== append() ===")
lst = [1, 2, 3]
lst.append(4)
print(lst)   # [1, 2, 3, 4]


print("\n=== clear() ===")
lst = [1, 2, 3]
lst.clear()
print(lst)   # []


print("\n=== copy() ===")
lst = [1, 2, 3]
new_list = lst.copy()
print(new_list)   # [1, 2, 3]


print("\n=== count() ===")
lst = [1, 2, 2, 3]
print(lst.count(2))   # 2


print("\n=== extend() ===")
lst1 = [1, 2]
lst2 = [3, 4]
lst1.extend(lst2)
print(lst1)   # [1, 2, 3, 4]


print("\n=== index() ===")
lst = [10, 20, 30]
print(lst.index(20))   # 1


print("\n=== insert() ===")
lst = [1, 2, 3]
lst.insert(1, 100)
print(lst)   # [1, 100, 2, 3]


print("\n=== pop() ===")
lst = [1, 2, 3]
lst.pop(1)
print(lst)   # [1, 3]


print("\n=== remove() ===")
lst = [1, 2, 3]
lst.remove(2)
print(lst)   # [1, 3]


print("\n=== reverse() ===")
lst = [1, 2, 3]
lst.reverse()
print(lst)   # [3, 2, 1]


print("\n=== sort() ===")
lst = [5, 2, 9, 1]
lst.sort()
print(lst)   # [1, 2, 5, 9]


print("\n=== sort(reverse=True) ===")
lst = [5, 2, 9, 1]
lst.sort(reverse=True)
print(lst)   # [9, 5, 2, 1]
