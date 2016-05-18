# This program made for some list comprehensions
#
# Created by Eric


def f(x, l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

def main():
    f(2)
    f(3, [3, 2, 1])
    f(3)

if __name__ == "__main__":
    main()
