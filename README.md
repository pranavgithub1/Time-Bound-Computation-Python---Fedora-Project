# Time-Bound-Computation-Python---Fedora-Project
Matrix multiplication efficiency using pure python vs python with numpy was tested.

A simple python matrix multiplication function was created:
```
def python_mat_mult(matrix1,matrix2):
    [[[sum(a*b for a,b in zip(x_row,y_col))] for y_col in zip(*matrix2)] for x_row in matrix1]
```
This was tested against the following numpy code:
```
numpy.matmul(matrix1,matrix2)
```
Random matrices of size (n,n) were used to test for n values 10, 100 and 1000. These were the most values I could test due to the limitations of my system.
The matrices were created sepereatley for testing python and numpy multiplication. For python a function was written to create random matrices:
```
def create_python_matrix(rows,columns):
    return [[random.random() for x in range(rows)] for i in range(columns)]
```
For numpy the matrices were created as follows:
```
numpy.random.rand(n,n)
```
The timeit module was used to get the execution time in seconds for the matrix operation for a specific n value in a for loop. This was then appended to a list, to create two lists. One for the python execution times (called python_times) and one for the numpy execution times (called numpy_times). 
```
python_mult = """python_mat_mult(pythonmatrix1,pythonmatrix2)"""
numpy_mult = """numpy.matmul(numpymatrix1,numpymatrix2)"""

python_elapsed = timeit.timeit(python_mult,number=1,globals=globals())
numpy_elapsed = timeit.timeit(numpy_mult,number=1,globals=globals())

python_times.append(python_elapsed)
numpy_times.append(numpy_elapsed)
```
I was only able to use 1 reding from the timit module due to the limitations of my computer.

Matplotlib graphs were created using this as data.
"numpyMatMult_elapsed_times.png" is a graph of the numpy performance alone
"pythonMatMult_elapsed_times.png" is a graph of the python performance alone
"MatMult_elapsed_times_combined.png" is a graph of the performance together. This graph allows you to see the clear winner, numpy.

The reason numpy is faster is due to the way it's arrays are stored in memory. A numpy array is more densely packed in memory and it frees memory faster than python lists.

Here were the results in seconds from the test:
```
Python Times(s): [0.00014179999999996973, 0.094526, 170.15191320000002]
Numpy Times(s): [5.430000000000712e-05, 0.0002750000000000252, 0.03332709999997974]
```
