def case_1():
    print("Case 1")

def case_2():
    print("Case 2")

def case_3():
    print("Case 3")

case_dict = {
    1: case_1,
    2: case_2,
    3: case_3,
}

case_dict[1]()
case_dict[2]()
case_dict[3]()
