def fa(n: int) -> int:
    if n == 0:
        return 3
    return -2 * fa(n-1)


def fb(n: int) -> int:
    if n == 0:
        return 3
    return 3 * fb(n-1) + 7


def fc(n: int) -> int:
    if n == 0:
        return 3
    return (fc(n-1)) ** 2 - 2 * fc(n-1) - 2


def fd(n: int) -> int:
    if n == 0:
        return 3
    return 3 ** (fd(n-1)//3)


funcs = [fa, fb, fc, fd]

for func, letter in zip(funcs, ("a", "b", "c", "d")):
    for i in range(6):
        print(f"{letter}({i}) = {func(i)}")

"""
a(0) = 3
a(1) = -6
a(2) = 12
a(3) = -24
a(4) = 48
a(5) = -96
b(0) = 3
b(1) = 16
b(2) = 55
b(3) = 172
b(4) = 523
b(5) = 1576
c(0) = 3
c(1) = 1
c(2) = -3
c(3) = 13
c(4) = 141
c(5) = 19597
d(0) = 3
d(1) = 3
d(2) = 3
d(3) = 3
d(4) = 3
d(5) = 3
"""
