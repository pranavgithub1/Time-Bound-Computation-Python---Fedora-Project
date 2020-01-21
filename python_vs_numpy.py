import numpy
import timeit
import matplotlib.pyplot as plt
def python_mat_mult(matrix1,matrix2):
    [[[sum(a*b for a,b in zip(x_row,y_col))] for y_col in zip(*matrix2)] for x_row in matrix1]
python_times = []
numpy_times = []
n_list = [10^x for x in range(1,11)]
# create two lists of the elapsed time for matrix multiplications with python built-in '@' vs numpy.matmul()
# tested with n*n size matrices where n = 10,100,1000...10^10
for n in n_list:
    matrix1 = numpy.random.rand(n,n)
    matrix2 = numpy.random.rand(n,n)

    python_mult = """python_mat_mult(matrix1,matrix2)"""

    numpy_mult = """numpy.matmul(matrix1,matrix2)"""

    python_elapsed = timeit.timeit(python_mult,number=500,globals=globals())/500

    numpy_elapsed = timeit.timeit(numpy_mult,number=500,globals=globals())/500

    python_times.append(python_elapsed)
    numpy_times.append(numpy_elapsed)
print(python_times)
print(numpy_times)


plt.figure(1)
plt.plot([x for x in range(1,11)],python_times,marker='o',linestyle='None')
plt.title("Elapsed time in seconds vs. n value for pure python",y=1.08)
plt.ylabel("Elapsed time (s)")
plt.xlabel("n value")
plt.xticks([x for x in range(1,11)])
plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0))
plt.savefig('pythonMatMult_elapsed_times.png')
plt.show()

plt.figure(2)
plt.plot([x for x in range(1,11)],numpy_times,marker='o',linestyle='None')
plt.title("Elapsed time in seconds vs. n value for numpy",y=1.08)
plt.ylabel("Elapsed time (s)")
plt.xlabel("n value")
plt.xticks([x for x in range(1,11)])
plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0))
plt.savefig('numpyMatMult_elapsed_times.png')
plt.show()

plt.figure(3)
plt.plot([x for x in range(1,11)],python_times,marker='o',linestyle='None',label='python')
plt.plot([x for x in range(1,11)],numpy_times,marker='o',linestyle='None',label='numpy')
plt.title("Elapsed time in seconds vs. n value for python vs numpy",y=1.08)
plt.ylabel("Elapsed time (s)")
plt.xlabel("n value")
plt.ylim(0,0.01)
plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0))
plt.xticks([x for x in range(1,11)])
plt.legend()
plt.savefig('MatMult_elapsed_times_combined.png')
plt.show()
