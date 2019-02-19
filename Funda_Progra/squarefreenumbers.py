from math import sqrt


def square(n):
    if n % 2 == 0:
        n = n / 2

    # If 2 again divides n,
    # then n is not a square
    # free number.
    if n % 2 == 0:
        return False

    # n must be odd at this
    # point. So we can skip
    # one element
    # (Note i = i + 2)
    for i in range(3, int((n**.5) + 1)):

        # Check if i is a prime
        # factor
        if n % i == 0:
            n = n / i

        # If i again divides, then
        # n is not square free
        if n % i == 0:
            return False
    return True



n=float(input("please give a number"))
if square(n):
    print("Yes")
else:
    print("No")
