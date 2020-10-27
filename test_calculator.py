import pytest
import os
import inspect
import re
import random
import calculator
import math
import numpy as np
from calculator import derivatives


all_modules = [calculator, derivatives]
README_CONTENT_CHECK_FOR = [
                'e',
                'tan',
                'sigmoid',
                'softmax',
                'relu',
                'sin',
                'cos',
                'derivative',
                'calculator',
                'tanh',
                'e',
                'relu'
            ]
derivatives_functions = ['dcos', 'de', 'dlog', 'drelu', 'dsigmoid', 'dsin', 'dsoftmax', 'dtan', 'dtanh']
calculator_functions = ['cos', 'e', 'log', 'relu', 'sigmoid', 'sin', 'softmax', 'tan', 'tanh', ]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
   
    assert len(readme_words) >= 350, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 5

def test_function_name_had_cap_letter():
    for each_module in all_modules:
        functions = inspect.getmembers(each_module, inspect.isfunction)
        for function in functions:
            assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_doc_string():
    '''
    Test case to check whether the functions have docstrings or not.
    '''
    for each_module in all_modules:
        functions = inspect.getmembers(each_module, inspect.isfunction)
        for function in functions:
            print(function[1].__doc__)
            assert function[1].__doc__

def test_function_annotation_string():
    '''
    Test case to check whether the functions have annotations or not.
    '''
    for each_module in all_modules:
        functions = inspect.getmembers(each_module, inspect.isfunction)
        for function in functions:
            print(function[1])
            assert function[1].__annotations__

def test_function_derivative_function_in_calculator() : 
    '''
    Test whether the derivate functions are directly accessible from calculator or not
    '''
    calculator_dir_functions = dir(calculator)
    for each_function in derivatives_functions:
        assert (each_function in calculator_dir_functions) == False , "Derivative functions should not directly accessible by calcuator functions"
    
def test_function_in_calculator():
    '''
    Test whether the functions other than derivative functions are directly accessible or not
    '''
    calculator_dir_functions =  dir(calculator)
    for each_function in calculator_functions:
        assert (each_function in calculator_dir_functions) == True, "These functions should be accessible directly"

def test_function_in_derivatives():

    '''
    Test whether the functions inside the dervative directory are directly accessible or not without calling their modules"
    '''
    derivatives_dir_functions = dir(derivatives)

    for each_function in derivatives_functions:
        assert (each_function in derivatives_dir_functions) == True, "These functions should be accessible directly"


num = random.randint(1, 10)
def test_functions_e():
    
    assert math.exp(num) == calculator.e(num), 'E implementation failed'

def test_function_cos():
    assert math.cos(num) == calculator.cos(num), 'cos implementation failed'

def test_function_log():
    assert math.log(num)  == calculator.log(num), ' Log implementaion failed'

def test_function_relu():
    assert calculator.relu(num) == 0 if num < 0 else num , 'Relu implementaion failed'
    

def test_function_sigmoid():
    assert calculator.sigmoid(0) == 0.5, 'Sigmoid implementaion failed'

def test_function_sin():
    assert math.sin(num)  == calculator.sin(num), 'Sin implementaion failed'

def test_function_softmax():
    assert calculator.softmax([num,num]) == [0.5, 0.5], 'Softmax implemenation failed'

def test_functions_tan():
    assert math.tan(num)  == calculator.tan(num), 'Tan implementaion failed'

def test_function_tanh():
    assert math.tanh(num)  == calculator.tanh(num), 'Tanh implementaion failed'

def test_function_de():
    
    assert math.exp(num) == derivatives.de(num), 'dE implementation failed'

def test_function_dcos():
    assert -math.sin(calculator.cos(num)) == derivatives.dcos(calculator.cos(num)), 'dcos implementation failed'

def test_function_dlog():
    assert 1/calculator.log(num)  == derivatives.dlog(calculator.log(num)), 'dLog implementaion failed'

def test_function_drelu():
    assert derivatives.drelu(calculator.relu(num)) == 0 if num <= 0 else 1 , 'dRelu implementaion failed'
    

def test_function_dsigmoid():
    assert derivatives.dsigmoid(calculator.sigmoid(num)) == calculator.sigmoid(num)*(1-calculator.sigmoid(num)), 'dSigmoid implementaion failed'

def test_function_dsin():
    assert math.cos(calculator.sin(num))  == derivatives.dsin(calculator.sin(num)), 'dSin implementaion failed'

def test_function_dsoftmax():
    assert derivatives.dsoftmax(calculator.softmax([num,num])).all() == np.array([[ 0.25, -0.25], [-0.25,  0.25]]).all(), 'dSoftmax implemenation failed'

def test_function_dtan():
    assert (1/(math.cos(calculator.tan(num))**2))  == derivatives.dtan(calculator.tan(num)), 'dTan implementaion failed'

def test_function_dtanh():
    assert (1  - calculator.tanh(num)**2)  == derivatives.dtanh(calculator.tanh(num)), 'dTanh implementaion failed'


