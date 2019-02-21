def fire(size):
    ls = []

    n = 10

    for i in range(0, n):
        ls2 = []
        for j in range(0, n):
            ls2.append(j)
        ls.append(ls2)

    print(ls)