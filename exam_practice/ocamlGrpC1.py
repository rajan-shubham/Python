class Expression:
    pass

class MyInt(Expression):
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

    def __add__(self, other):
        if isinstance(other, MyInt):
            return MyInt(self.i + other.i)
        elif isinstance(other, MyString):
            return MyString(str(self.i) + other.s)
        else:
            raise TypeError("Invalid input for addition")

class MyString(Expression):
    def __init__(self, s):
        self.s = s

    def __repr__(self):
        return self.s

    def __add__(self, other):
        if isinstance(other, MyString):
            return MyString(self.s + other.s)
        elif isinstance(other, MyInt):
            return MyString(self.s + str(other.i))
        else:
            raise TypeError("Invalid input for addition")

if __name__ == "__main__":
    x, y = MyInt(345), MyString("well")
    print(x)
    print(y)
    print(x + y)
