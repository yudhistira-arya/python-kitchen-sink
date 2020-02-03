a = ('name', 'age', 'address')
b = ('Smith', '10', '300 Street.')

zipped = zip(a, b)

if __name__ == '__main__':
    # destructure the iterator value
    for i, (itema, itemb) in enumerate(zipped):
        print(i, itema, itemb)
