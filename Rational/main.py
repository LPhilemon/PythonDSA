from numbers import Rational
from rational import rational

rational_one = rational(1, 4)
rational_two = rational(1, 3)
rational_three = rational(1, 6)


def main():
    rational_one.display()
    rational_two.display()
    rational_three.display()
    print(rational_one.get_numerator())
    print(rational_one.get_denominator())
    print(rational_one + rational_two)
    print(rational_one - rational_two)
    print(rational_one * rational_two)
    print(rational_one / rational_two)
    print(rational_one == rational_two)
    print(rational_one == rational_three)

if __name__ == '__main__':
    main()
