class Rational:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator + self.denominator * other.numerator, self.denominator * other.denominator)
        else:
            return Rational(self.numerator + other * self.denominator, self.denominator)

    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator - self.denominator * other.numerator, self.denominator * other.denominator)
        else:
            return Rational(self.numerator - other * self.denominator, self.denominator)

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.numerator, self.denominator * other.denominator)
        else:
            return Rational(self.numerator * other, self.denominator)

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator, self.denominator * other.numerator)
        else:
            return Rational(self.numerator / other, self.denominator)

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator == self.denominator * other.numerator
        else:
            return self.numerator == other * self.denominator

    def display(self):
        print(f"{self.numerator}/{self.denominator}")