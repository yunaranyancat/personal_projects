class Vector2D:
    x = 0.0
    y = 0.0

    def Set(self, x, y):
        self.x = x
        self.y = y

def main():
    vec = Vector2D()
    vec.Set(5, 6)
    print("X : "+str(vec.x)+" Y : "+str(vec.y))

if __name__ == '__main__':
    main()
