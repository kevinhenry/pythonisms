class Counting:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


if __name__ == "__main__":
    myclass = Counting()
    myiter = iter(myclass)

    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
