def multiple_assignment_expressions():
    # expressions added in Python 3.8
    # differs from assignment in the sense they return the right hand side
    # this is the way it is in most other programming languages
    (a := (b := (c := (d := 0))))
    print(a, b, c, d)


def multiple_assignments():
    a = b = c = d = []
    print(a, b, c, d)
    print(a is b)

    # same as
    tmp = []
    a = tmp
    b = tmp
    c = tmp
    d = tmp
    print(a, b, c, d)
    print(a is b)


def tuple_assignments():
    a, b = 1, 2
    print(a, b)


def tricky_assignments():
    a, b = a[:] = [[]], []
    print(a, b)

    # same as
    tmp = [[]], []
    a, b = tmp
    a[:] = tmp
    print(a, b)
    print(a is a[0])


def tricky_assignments2():
    a, b = a[b] = a = [1, 2, 3], 2
    print(a, b)

    # same as
    tmp = [1, 2, 3], 2
    a, b = tmp
    a[b] = tmp
    print(a, b)


tricky_assignments2()
