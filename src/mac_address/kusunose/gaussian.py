import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import subprocess

def mk_gaussian(size, s=1, scale=1):
    m = 2  #dimension
    mean = np.zeros(m)
    sigma = np.eye(m) * s
    x1 = np.linspace(-scale, scale, size[0])
    x2 = np.linspace(-scale, scale, size[1])
    X1, X2 = np.meshgrid(x1, x2)
    X = np.c_[np.ravel(X1), np.ravel(X2)]
    y = stats.multivariate_normal.pdf(x=X, mean=mean, cov=sigma)
    y = y.reshape(X1.shape)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X1, X2, y, cmap='bwr', linewidth=0)
    fig.colorbar(surf)
    #plt.savefig('gaussian_preview.jpg')
    return y
