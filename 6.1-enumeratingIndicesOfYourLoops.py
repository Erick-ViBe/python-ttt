x = ["angela", "john", "mary", "sam"]
person_no = 1

for name in x:
    print(f"{person_no}. {name}")
    person_no += 1

print(list(enumerate(x)))

for idx, name in enumerate(x):
    print(f"{idx+1}. {name}")
