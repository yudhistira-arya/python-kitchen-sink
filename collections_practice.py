from collections import namedtuple

def iterator_practice():
    list1 = [1, 2, 3, 4, 5]
    print(f"type of list1: {str(type(list1))}")
    list1_iterator = iter(list1)
    print(f"type of list1_iterator: {str(type(list1_iterator))}")
    print(next(list1_iterator))
    print(next(list1_iterator))
    print(next(list1_iterator))
    print(next(list1_iterator))
    print(next(list1_iterator))
    try:
        print(next(list1_iterator))
    except StopIteration:
        print("End of iterator")

    list2 = [1, 2, 3, 4, 5]
    list2_iterator = iter(list2)
    for it in list2_iterator:
        print(it)

if __name__ == '__main__':

    a = ('name', 'age', 'address')
    b = ('Smith', '10', '300 Street.')

    zipped = zip(a, b)
    print(f"zipped: {zipped.__next__()}")

    # destructure the iterator value
    for i, (itema, itemb) in enumerate(zipped):
        print(i, itema, itemb)

    iterator_practice()

    Book = namedtuple("Book", "author title genre")
    books = [
        Book("Pratchett", "Nightwatch", "fantasy"),
        Book("Pratchett", "Thief Of Time", "fantasy"),
        Book("Le Guin", "The Dispossessed", "scifi")]

    fantasy_authors_set = {b.author for b in books if b.genre == 'fantasy'}
    print(fantasy_authors_set)
    fantasy_authors_dict = {b.author: b for b in books if b.genre == 'fantasy'}
    print(fantasy_authors_dict)

