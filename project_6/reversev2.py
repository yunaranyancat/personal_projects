def Reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


def main():

    rev = Reverse("yunara")
    for char in rev:
        print(char)

    data = 'Yunara'
    print(list(data[i] for i in range(len(data) - 1, -1, -1))) #for data in .....

if __name__ == '__main__':
    main()
