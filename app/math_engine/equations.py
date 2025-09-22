import random
import sympy as sp
from abc import ABC, abstractmethod
from math import sqrt, log10
from operator import sub, add, mul, truediv, pow

class Method(ABC):
    def __init__(self, level):
        self.level = level
        self.equation, self.roots = self.create()
        self.steps = self.solving_steps()

    @abstractmethod
    def create(self):
        '''Creates equation and its roots'''
        return sp.Eq(), list()

    @abstractmethod
    def solving_steps(self):
        '''list of steps to solve equation'''
        return list()
    
    def get_roots(self):
        return self.roots
    
    def get_equation(self):
        return self.equation


class Substitution(Method):

    def create(self):
        self.val_r = random.randint(2, 6)  # root of the exponent x

        self.val_x1 = random.randint(0, 10 - self.val_r) # main x of the equation
        self.val_x2 = random.randint(0, 10 - self.val_r) # main x of the equation

        self.val_t1 = self.val_r ** self.val_x1 # main power 1 of the equation
        self.val_t2 = self.val_r ** self.val_x2 # main power 2 of the equation
        self.val_q = -self.val_t1 # coefficient of the equation
        self.val_p = -self.val_t2 # constant of the equation

        self.val_a = random.choice([i for i in range(-10, 11) if i != 0]) # coefficient of the equation
        self.val_b = self.val_a * (self.val_p + self.val_q)
        self.val_c = self.val_a * (self.val_p * self.val_q)

        # variables
        t = sp.symbols('t')
        x = sp.symbols('x')
        
        # quadratic equation
        quad_eq = sp.Eq(self.val_a * (t ** 2) + self.val_b * t + self.val_c, 0)

        # main equation
        if self.level == 'easy':
            eq = sp.Eq(self.val_a * (self.val_r ** (2*x)) + self.val_b * (self.val_r ** x), -self.val_c)
        else:
            eq = AdvancedEquation([[self.val_a], '*', [self.val_r, 2*x], '+',[self.val_b], '*', [self.val_r, x]], [-self.val_c], [self.val_x1, self.val_x2], 'S')

        return eq, [self.val_x1, self.val_x2]
    
    

    def solving_steps(self):
        return []


class Matching_bases(Method):
    def create(self):
        self.val_r = random.randint(2, 11)  # root of the exponent x
        self.val_x = random.randint(-3, 5) # main x of the equation

    
        if self.val_x < 0:
            self.val_t = sp.symbols(f'1/{self.val_r ** abs(self.val_x)}')
        else:
            self.val_t = self.val_r ** self.val_x # main power of the equation

        x = sp.symbols('x')
        if self.level == 'easy':
            eq = sp.Eq(self.val_r ** x, self.val_t)
        else:
            eq = AdvancedEquation([[self.val_r, x]], [[self.val_t]], [self.val_x], 'MB') # [Number, sign, number, exponent]

        return eq, [self.val_x]
    
    def solving_steps(self):
        return []
        

class Logarithm(Method): # prerobit
    def create(self):
        # val_x = log10(val_number_right)/log10(val_number_left)
        # self.val_x = val_x

        # base = random.choice([9, 16])
        # x_val = random.randint(1, 10) / 2



        # exp_left_side = round(random.uniform(1.0, 2.0), 1)
        # print(exp_left_side)
        # val_x = random.randint(1, 5)
        # exp_right_side = exp_left_side * val_x


        # number_left = 10 ** exp_left_side
        # number_right = 10 ** exp_right_side

        number_right = random.randint(1, 500)
        number_left = random.randint(1, 500)
        val_x = log10(number_right)/log10(number_left)

        x = sp.symbols('x')
        self.val_x = val_x
        if self.level == 'easy':
            eq = sp.Eq(number_left ** x, number_right)
            print('root:', log10(number_right)/log10(number_left))

        else:
            eq = AdvancedEquation([[number_left, x]], [[number_right]], [self.val_x], 'L')

        return eq, [self.val_x]
    
    def solving_steps(self):
        return []


class AdvancedEquation:
    def __init__(self, left_side, right_side, roots, type):
        self.left_side = left_side
        self.right_side = right_side
        self.roots = roots
        self.type = type

        plus_coef = random.randint(1, 3)
        complex_exp = random.randint(1, 3)

        signs_exp = random.choices(['+', '-', '*', '/'], k=complex_exp)
        signs_coef = random.choices(['+', '-', '*', '/'], k=plus_coef)


        for coefs in range(random.randint(1, 3)):
            self.left_side.append(random.choice(['+', '-', '*', '/']))
            self.left_side.append([random.randint(2, 5), random.randint(2, 5) if random.randint(0, 2) == 1 else None])




        



































# cemetery


    #     self.left_side = left_side
    #     self.right_side = right_side
    #     self.roots = roots

    #     self.equation = self.create()
    #     return self.equation

    # def create(self):
    #     changes = [self.complex_exp, self.coef_to_power, self.one_to_exp_zero, self.neg_exponent, self.dec_coef, self.other_side]
    #     for change in changes:
    #         change()
    #     return self.equation
    
    # def complex_exp(self):
    #     for coef in self.left_side:
    #         if coef is str:
    #             continue

    #         num_a = coef[0]
    #         sign = coef[1]
    #         num_b = coef[2]
    #         exp = coef[3]

    #         if sign is not None and num_b is not None and exp is int:
    #             number = sign(num_a, num_b) ** exp
    #         elif exp is int:
    #             number = num_a ** exp
    #         else:
    #             number = num_a



    #     numbers = random.choice(['both_fractions', 'one_fraction', 'both_integers'])
    #     x = sp.symbols('x')
    #     if numbers == 'both_fractions':
    #         numerator_left = random.randint(1, 11)
    #         numerator_right = random.randint(1, 11)
    #         denominator_left = random.randint(1, 11)
    #         denominator_right = random.randint(1, 11)

    #         number_left = sp.symbols(f'{numerator_left}/{denominator_left}')
    #         number_right = sp.symbols(f'{numerator_right}/{denominator_right}')

    #         val_number_left = numerator_left/denominator_left
    #         val_number_right = numerator_right/denominator_right

    #         if self.level == 'advanced':
    #             eq = AdvancedEquation([[numerator_left, '/', denominator_left, x]], [[numerator_right, '/', denominator_right, 1]], [val_x])

    #     elif numbers == 'one_fraction':
    #         numerator_left = random.randint(1, 11)
    #         denominator_left = random.randint(1, 11)
    #         number_right = random.randint(1, 11)

    #         number_left = sp.symbols(f'{numerator_left}/{denominator_left}')
    #         val_number_left = numerator_left/denominator_left
    #         val_number_right = number_right

    #         if self.level == 'advanced':
    #             eq = AdvancedEquation([[numerator_left, '/', denominator_left, x]], [[number_right, '/', 1, 1]], [val_x])
    #     else:
    #         number_right = random.randint(1, 11)
    #         number_left = random.randint(1, 11)
    #         val_number_left = number_left
    #         val_number_right = number_right

    #         if self.level == 'advanced':
    #             eq = AdvancedEquation([[number_left, '/', 1, x]], [[number_right, '/', 1, 1]], [val_x])
            
    #    # define logarythm of both sies first


# def neg_exponent(self, coef):
#         if coef == self.val_a:
#             self.val_a = ((1/self.val_a) ** -1)
#         elif coef == self.val_b:
#             self.val_b = ((1/self.val_b) ** -1)
#         elif coef == self.val_c:
#             self.val_c = ((1/self.val_c) ** -1)
#         else:
#             self.val_r = ((1/self.val_r) ** -1)

#     def dec_coef(self, coef):
#         n = random.randint(1, 10)
        
#         if coef == self.val_a:
#             self.val_a = (self.val_a - n) + n
#         elif coef == self.val_b:
#             self.val_b = (self.val_b - n) + n
#         elif coef == self.val_c:
#             self.val_c = (self.val_c - n) + n
#         else:
#             self.val_r = (self.val_r - n) + n

#     def other_side(self, coef): # ###
#         pass

#     def coef_to_power(self, coef):# only for special cases
#         if int(sqrt(coef)) == sqrt(coef):
#             if coef == self.val_a:
#                 self.val_a = int(sqrt(coef)) ** 2
#             elif coef == self.val_b:
#                 self.val_b = int(sqrt(coef)) ** 2
#             elif coef == self.val_c:
#                 self.val_c = int(sqrt(coef)) ** 2
                
#         elif int(sqrt(coef, 3)) == sqrt(coef, 3):
#             if coef == self.val_a:
#                 self.val_a = int(sqrt(coef)) ** 3
#             elif coef == self.val_b:
#                 self.val_b = int(sqrt(coef)) ** 3
#             elif coef == self.val_c:
#                 self.val_c = int(sqrt(coef)) ** 3
    

#     def complex_exp(self, coef):# only for special cases
         
            

#     def one_to_exp_zero(self, coef):
#         if coef == 1:
#             if coef == self.val_a:
#                 self.val_a = self.val_r ** 0
#             elif coef == self.val_b:
#                 self.val_b = self.val_r ** 0
#             elif coef == self.val_c:
#                 self.val_c = self.val_r ** 0
#         else:
#             pass
            