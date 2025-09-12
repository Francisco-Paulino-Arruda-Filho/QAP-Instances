class enigma:
    def __iter__(self):
        self.x = 128
        return self

    def __next__(self):
        y = self.x 
        def z(a):
            return a - int(a/2)
        self.x = z(self.x)
        return y


coisa = enigma()
x = iter(coisa)

for i in range(5):
    print(next(x))