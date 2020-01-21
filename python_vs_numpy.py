import numpy
import timeit
import matplotlib.pyplot as plt
import random
def python_mat_mult(matrix1,matrix2):
    [[[sum(a*b for a,b in zip(x_row,y_col))] for y_col in zip(*matrix2)] for x_row in matrix1]
def create_python_matrix(rows,columns):
    return [[random.random() for x in range(rows)] for i in range(columns)]
python_times = []
numpy_times = []
j=range(1,4)
# create two lists of the elapsed time for matrix multiplications with python built-in '@' vs numpy.matmul()
# tested with n*n size matrices where n = 10,100,1000...10**5
for n in [10,100,1000]:
    #create two matrices for numpy to multiply
    numpymatrix1 = numpy.random.rand(n,n)
    numpymatrix2 = numpy.random.rand(n,n)

    #create two matrices for python to multiply (without numpy, since we are testing them separateley)
    pythonmatrix1 = create_python_matrix(n,n)
    pythonmatrix2 = create_python_matrix(n,n)

    python_mult = """python_mat_mult(pythonmatrix1,pythonmatrix2)"""

    numpy_mult = """numpy.matmul(numpymatrix1,numpymatrix2)"""

    python_elapsed = timeit.timeit(python_mult,number=1,globals=globals())

    numpy_elapsed = timeit.timeit(numpy_mult,number=1,globals=globals())

    python_times.append(python_elapsed)
    numpy_times.append(numpy_elapsed)
    print("finished: ",n)
print(python_times)
print(numpy_times)


plt.figure(1)
plt.plot([x for x in j],python_times,marker='o')
plt.title("Elapsed time in seconds vs. n value for pure python",y=1.08)
plt.ylabel("Elapsed time (s)")
plt.xlabel("n value")
plt.xticks([x for x in j])
plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0))
plt.savefig('pythonMatMult_elapsed_times.png')
plt.show()

plt.figure(2)
plt.plot([x for x in j],numpy_times,marker='o')
plt.title("Elapsed time in seconds vs. n value for numpy",y=1.08)
plt.ylabel("Elapsed time (s)")
plt.xlabel("n value")
plt.xticks([x for x in j])
plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0))
plt.savefig('numpyMatMult_elapsed_times.png')
plt.show()

plt.figure(3)
plt.plot([x for x in j],python_times,marker='o',label='python')
plt.plot([x for x in j],numpy_times,marker='o',label='numpy')
plt.title("Elapsed time in seconds vs. n value for python vs numpy",y=1.08)
plt.ylabel("Elapsed time (s)")
plt.xlabel("n value")
plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0))
plt.xticks([x for x in j])
plt.legend()
plt.savefig('MatMult_elapsed_times_combined.png')
plt.show()


