from equations import *


def test_substitution():
    method = Substitution('easy')
    print(method.get_roots())
    print(method.get_equation())

def test_matching_bases():
    method = Matching_bases('easy')
    print(method.get_roots())
    print(method.get_equation())

def test_logarithm():
    method = Logarithm('easy')
    print(method.get_roots())
    print(method.get_equation())

for i in range(50):
    test_substitution()
    print('---')

print('*********************************************************************')
for i in range(50):
    test_matching_bases()
    print('---')

print('*********************************************************************')
for i in range(50):
    test_logarithm()
    print('---')


# for i in range(400):
#     if 16**(i/100) == int(16**(i/100)):
#         print('exp',(i/100))
#         print('power',16**(i/100))