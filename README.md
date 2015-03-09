# Perceptron algorithm

Tested with Python 2.7.6, Ubuntu 14.04. 

Source code is available in the **src** directory.
Program can be run with default parameters by:
<code>python main.py</code>

**Default parameters are**

- tests: 1 (number of tests; iterations parameter is increased after each test, so if we want to run a program 50 times - with different number of iterations, then tests=50 and iterations=1)
- test_training: False (if true, run test function against the training data)
- iterations: 1 (number of iterations to run)

**Parameters are given as in any other program**

<code>-h        Prints help</code>

<code>-i int  Number of iterations</code>

<code>-t int  Number of tests</code>

<code>-T        Run test function against the training data</code>

**Examples**

<code>python main.py -h</code>

Prints help information.

<code>python main.py -i 10</code>

Runs the program once with 10 iterations. Runs the test function against the test data.

<code>python main.py -t 10</code>

Runs the program 10 times. As the default iterations number is 1, it runs it 10 times with iterations: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
Results are saved into a tsv file (training.txt or test.txt) with columns: accuracy, error, iterations.
Runs the test function against the test data.

<code>python main.py -t 10 -i 5</code>

Runs the program 10 times. As the iterations parameter is set to 5, it runs it 10 times with iterations: 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
Results are saved into a tsv file (training.txt or test.txt) with columns: accuracy, error, iterations.
Runs the test function against the test data.

<code>python main.py -T</code>

Parameter -T makes the program run the test function against the training data. Obviously, high accuracy should be expected. The **-T** parameter could be obviously added in the previous examples.
