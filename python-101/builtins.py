"""idiomatic module structure"""

# imports
from os import sys

# constants
# exception classes
# interface functions
# classes
# internal functions & classes


def lists_construct():
    # example construction
    print "\nList constructors:"
    fred = ["a", "b"]
    suzy = list()
    suzy.append("c")
    suzy += "d"

    print fred
    print suzy


def lists_range():
    print "\nList ranges:"
    fred = range(10) #0..9
    print fred
    fred = range(1,10) #1..9
    print fred
    fred = range(1,10,2)
    print fred

    suzy = list(xrange(1,20,3)) #1..18
    print suzy
    crazy = suzy*2  # the same list, repeated
    print crazy
    # slicing and indexing seem straightforward; can have negatives


def lists_operations():
    print "\nList operations:"
    mylist = ["fred"]
    print mylist
    mylist.append("suzy")
    print mylist
    mylist.insert(1, "ma")
    print mylist
    mylist.extend(["foo","bar"])
    print mylist
    mylist.remove("foo")
    print mylist
    print mylist.pop()
    print mylist
    del mylist[2]
    print mylist


def dictionaries():
    print {}
    print {"a": 1, 2: "b" }



def main():
    print("\nHello Python World\n")
    lists_construct()
    lists_range()
    lists_operations()
    dictionaries()


if __name__ == '__main__':
    status = main()
    print("\nGoodbye!\n")
    sys.exit(status)
