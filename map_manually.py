from zip_manualy import zip_manualy


def map_manually(func, *args):
    for a in zip_manualy(*args):
        yield func(*a)


if __name__ == '__main__':
    x = [1, 2, 3, 4]
    y = [6, 7, 8, 2]

    for i in map_manually(pow, x, y):
        print(i)
