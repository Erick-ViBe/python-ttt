original = [[1, 2], [3, 4]]


copy = original
copy.append([5, 6])
print(original)
# [[1, 2], [3, 4], [5, 6]]
print(copy)
# [[1, 2], [3, 4], [5, 6]]


shallow_copy = list(original)
shallow_copy.append([7])
print(original)
# [[1, 2], [3, 4], [5, 6]]
print(shallow_copy)
# [[1, 2], [3, 4], [5, 6], [7]]

shallow_copy[0][0] = "XYZ"
print(original)
# [[1, 2], [3, 4], [5, 6]]
print(shallow_copy)
# [[1, 2], [3, 4], [5, 6], [7]]


import copy
deepcopied_list = copy.deepcopy(original)
deepcopied_list.append([7, 8])
print(original)
# [['XYZ', 2], [3, 4], [5, 6]]
print(deepcopied_list)
# [['XYZ', 2], [3, 4], [5, 6], [7, 8]]

deepcopied_list[0][0] = "ABC"
print(original)
# [['XYZ', 2], [3, 4], [5, 6]]
print(deepcopied_list)
# [['ABC', 2], [3, 4], [5, 6], [7, 8]]
