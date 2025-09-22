import random
import sympy as sp
from equations import Equation

class Function:
    def __init__(self, 
        name:str,
        type:str, 
        domain:tuple, 
        range:tuple, 
        equation:Equation, 
        inverse:'Function', 
        increasing:bool, 
        boundedness:tuple) -> None:
