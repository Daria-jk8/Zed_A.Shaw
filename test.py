import sys
from timeit import timeit
a = [i for i in range(100)]
b = (i for i in range(100))

print(a)
print(b)
print('-------')
print(type(a))
print(type(b))
print('-------')
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print('-------')
print(timeit("[i for i in range(100)]"))
print(timeit("(i for i in range(100))"))
print('-------')
a.append(666)
print(a)
# b.append(666)
print(list(b))