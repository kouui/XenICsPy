import ctypes
from numpy.ctypeslib import ndpointer
import matplotlib.pyplot as plt
import numpy as np




if __name__=="__main__":

    lib = ctypes.CDLL('./cMandelbrot.dll')
    mandelbrot = lib.mandelbrot

    mandelbrot.restype = None
    mandelbrot.argtypes = [ctypes.c_int,
                           ctypes.c_int,
                           ndpointer(ctypes.c_int),]

    size = 400
    iterations = 100
    col = np.empty((size, size), dtype=np.int32)
    mandelbrot(size, iterations, col)

    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    ax.imshow(np.log(col), cmap=plt.cm.hot)
    ax.set_axis_off()
    plt.show()
