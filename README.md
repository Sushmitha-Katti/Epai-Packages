# Session12 - Packages

Packages are modules, but modules are not necessarily be a package.
Packages can contain modules, sub packages as well
If a module is a package it much have __path__.

**Advantantages of using Packages**
1. Can Organise the code in better way. We can have sub packages. Heirarchy of the code will be good.
2. Easy to read/understand.
3. Easier debug/test
4. Hides the inner implemention from users and makes it easier to understand and use for users.

## **Assignment**
Build a calculator package that has separate module for:
1. sin, cos, tan, tanh, SoftMax, Sigmoid, ReLU, log and e
2. The modules shall include their derivatives as well
3. If we do import calculator, we should be able to access all the above function (except deviratives)
4. For derivates we must do: from package import derivatives. 
5. Outputs are returned as well as printed using only f-string
6. Write simple test cases to check the outputs of each operator and their derivative

## **Implementation**

1. ### Code Structure


calculator
├── init         
├── Cos                        
├── E   
├── Log         
├── Relu 
├── Sigmoid    
├── Sin 
├── SoftMax          
├── Tan          
├── Tanh
├── derivaties                 
│   ├──init
│   ├── DCos          
│   ├── DE   
│   ├── DLog         
│   ├── DRelu 
│   ├── DSigmoid       
│   ├── DSin  
│   ├── DSoftMax          
│   ├── DTan           
│   └── DTanh     
            
   
 
2. ### Usage
    ```python
    import calculator # This works
    from calculator import derivatives # This works
    # import calculator.derivative  ------This doesn't work--------

    # To use functions

    calculator.sin(x)
    calculator.cos(x)
    ....

    #To use derivatives

    derivates.dcos(x)
    derivatives.dsine(x)
    ```

    #### **List of available functions**

    **From calculator**

    1. sin(x)
    2. cos(x)
    3. log(x)
    4. e(x)
    5. relu(x)
    6. sigmoid(x)
    7. softmax(x) -- > This takes array as input
    8. tan(x)
    9. tanh(x)

    **From derivaties**
    1. dsin(x)
    2. dcos(x)
    3. dlog(x)
    4. de(x)
    5. drelu(x)
    6. dsigmoid(x)
    7. dsoftmax(x) -- > This takes array as input
    8. dtan(x)
    9. dtanh(x)

3. ### **Test Cases**
    Some simple test cases to test the functionalities
    1. Readme exists or not, have proper content and formating
    2. For all the funtions documentation and annotation are provided or not, all functions name should be small letters.
    3. Whether all the functions can be directly accessed through calculator package without using their respective modules 
    4. Whether all the derviative functions can be directly accessed through derivative sub package package without using their respective modules
    5. Correctness of each functions
    


 
