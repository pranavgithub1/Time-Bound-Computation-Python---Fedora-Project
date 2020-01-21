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
Random matrices of size (n,n) were used to test for n values 10,100,1000...10^10.

The timeit module was used to get the execution time in seconds for the matrix operation for a specific n value in a for loop. This was then appended to a list, to create two lists. One for the python execution times (called python_times) and one for the numpy execution times (called numpy_times). 
```
python_mult = """python_mat_mult(matrix1,matrix2)"""
numpy_mult = """numpy.matmul(matrix1,matrix2)"""

python_elapsed = timeit.timeit(python_mult,globals=globals())
numpy_elapsed = timeit.timeit(numpy_mult,globals=globals())

python_times.append(python_elapsed)
numpy_times.append(numpy_elapsed)
```


Matplotlib graphs were created using this as data.
