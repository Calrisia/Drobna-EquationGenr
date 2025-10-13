from equations import *


def test_substitution():
    method = Substitution('hard')
    print(method.get_roots())
    print(method.get_equation())

def test_matching_bases():
    method = Matching_bases('hard')
    print(method.get_roots())
    print(method.get_equation())

def test_logarithm():
    method = Logarithm('hard')
    print(method.get_roots())
    print(method.get_equation())

# for i in range(50):
#     test_substitution()
#     print('---')

# print('*********************************************************************')
# for i in range(50):
#     test_matching_bases()
#     print('---')

print('*********************************************************************')
for i in range(50):
    test_logarithm()
    print('---')


