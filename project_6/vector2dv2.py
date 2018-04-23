class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    vec = Vector2D(5, 6)
    print("X : "+str(vec.x)+" Y : "+str(vec.y))

if __name__ == '__main__':
    main()
