x = [1, 2, 3, 4, 1, 2]
x = set(x)
print(x)

x.add(4)
x.add(5)
print(x)


y = [1, 2, 3, 4, 1, 2]
y = frozenset(y)
print(y)
# frozenset is inmutable
#y.add(4)  #Error! AttributeError
#y.clear() #Error! AttributeError
