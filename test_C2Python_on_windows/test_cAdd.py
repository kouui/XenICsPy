import ctypes
from numpy.ctypeslib import ndpointer
import matplotlib.pyplot as plt
import numpy as np




if __name__=="__main__":

    cLib = ctypes.CDLL('./cAdd.dll')
    cos_ = cLib.cos_

    cos_.restype = None
    cos_.argtypes = [ctypes.c_int,
                    ndpointer(ctypes.c_double),
                    ndpointer(ctypes.c_double),]

    size = 101
    x = np.linspace(0, 2*np.pi, size, dtype=np.double) # np.double与C里头的double对应

    result = np.zeros(size, dtype=np.double)
    cos_(size,x,result)

    fig, ax = plt.subplots(1,1, figsize=(7,3), dpi=200)
    ax.plot(x, result, label='wrapped cos_')
    ax.plot(x, np.cos(x),'--', label='numpy.cos', alpha=0.6)
    ax.legend(loc="best")
    plt.show()
