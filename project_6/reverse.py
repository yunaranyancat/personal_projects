class Reverse:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

def main():

    rev = Reverse("yunara")
    for char in rev:
        print(char)


if __name__ == '__main__':
    main()
