class ComplexNumber:
    def __init__(self, real, imag) -> None:
        self.real = real
        self.imag = imag

    def __add__(self, number):
        return ComplexNumber(self.real + number.real, self.imag + number.imag)

    def __sub__(self, number):
        return ComplexNumber(self.real - number.real, self.imag - number.imag)
    
    def __str__(self) -> str:
        if(self.imag < 0):
            return f"{self.real} {self.imag}j"
        return f"{self.real} +{self.imag}j"

x = ComplexNumber(2, 2)
y = ComplexNumber(-1, -11)

print(x+y)
print(x-y)