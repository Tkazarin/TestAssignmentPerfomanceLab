import sys


'''Так как идет речь об одновременной обработке обоих массивов, то
я воспринимаю это как обработку обоих массивов в рамках одного цикла.'''
def main():
    if len(sys.argv) != 5:
        print("Неверное количество аргументов")
        return

    try:
        n1, m1, n2, m2 = map(int, sys.argv[1:5])
    except ValueError:
        print("Все аргументы должны быть целыми числами")
        return

    if n1 <= 0 or n2 <= 0 or m1 <= 0 or m2 <= 0:
        print("Все аргументы должны быть больше 0")
        return

    path1 = ["1"]
    path2 = ["1"]

    i = 0
    j = 0
    done1 = False
    done2 = False

    while not (done1 and done2):
        if not done1:
            i = (i + m1 - 1) % n1
            if i == 0:
                done1 = True
            else:
                path1.append(str(i + 1))
        if not done2:
            j = (j + m2 - 1) % n2
            if j == 0:
                done2 = True
            else:
                path2.append(str(j + 1))

    print("".join(path1) + "".join(path2))


if __name__ == "__main__":
    main()
