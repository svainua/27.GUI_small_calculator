# def add(*args):
#     print(args[4])
#
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# print(add(10, 5, 5, 2, 11))


def calculate(**kwargs):
    print(kwargs)

calculate(add=3, multiply=5)