class MyClass:
    number = 0
    name = "noname"

def main():
    me = MyClass()
    me.number = 1234
    me.name = "Yunara"

    friend = MyClass()
    friend.number = 1
    friend.name = "John"

    empty = MyClass()

    print("Name : " + me.name + ", Favorite Number : " + str(me.number))
    print("Name : " + friend.name + ", Favorite Number : " + str(friend.number))
    print("Name : " + empty.name + ", Favorite Number : " + str(empty.number))

if __name__ == '__main__':
    main()
