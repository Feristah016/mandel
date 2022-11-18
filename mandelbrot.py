import numpy
import numba
import matplotlib.pyplot as plt

@numba.jit
def m(r, i, max):
  c = complex(r,i)
  z = 0.0j

  for l in range(max):
    z = z*z + c
    if (z.real*z.real + z.imag*z.imag) >= 4:
      return l
  return max

col = int(input("col: "))
row = int(input("row: "))

result = numpy.zeros([row, col])

for roo, r in enumerate(numpy.linspace(-2, 1, num=row)):
  for co, i in enumerate(numpy.linspace(-1, 1, num=col)):
    result[roo, co] = m(r, i, 100)


def plotting(result):
  plt.figure(dpi=100)
  plt.imshow(result.T, cmap="afmhot", interpolation="spline36", extent=[-2,1,-1,1])
  #plt.imshow(result.T, interpolation="bilinear", extent=[-2,1,-1,1])
  plt.show()

plotting(result)
