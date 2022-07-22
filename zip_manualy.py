def zip_manualy(*args):
    min_len = min([len(a) for a in args])
    for i in range(min_len):
        yield tuple([a[i] for a in args])


if __name__ == '__main__':
    lst1 = [1,2,3]
    lst2 = [4,5,6]

    assert list(zip(lst1,lst2)) == list(zip_manualy(lst1,lst2))
