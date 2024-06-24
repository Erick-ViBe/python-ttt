class Programmer:
    lang = ""
    experience = 0

    def __init__(self, lang, experience):
        self.lang = lang
        self.experience = experience


programmer1 = Programmer("python", 4)
programmer2 = Programmer("python", 4)

print(programmer1 == programmer2)
# False
print(id(programmer1))
# 4308466512
print(id(programmer2))
# 4309907200


programmer3 = programmer2
print(programmer3 == programmer2)
# True



class NewProgrammer:
    lang = ""
    experience = 0

    def __init__(self, lang, experience):
        self.lang = lang
        self.experience = experience

    def __eq__(self, compared):
        return self.lang == compared.lang and self.experience == compared.experience

    def __ne__(self, compared):
        return (self.lang != compared.lang) or (self.experience != compared.experience)


n1 = NewProgrammer("python", 5)
n2 = NewProgrammer("python", 5)
n3 = NewProgrammer("Scala", 5)

print(n1 == n2)
# True

print(n1 == n3)
# False

print(n1 != n3)
# True
