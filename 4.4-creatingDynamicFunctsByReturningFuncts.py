def custom_operator(x):
    return (x + 2) ** 2
x = custom_operator(10)
print(x)

def custom_operator_2(x):
    return (x + 3) ** 2
x = custom_operator_2(10)
print(x)


def custom_operator_maker(increment=2, power=2):
    def return_this_funct(x):
        return (x + increment) ** power
    return return_this_funct

f1 = custom_operator_maker(2, 2)
f2 = custom_operator_maker(3, 2)

print(f1(10))
print(f2(10))
