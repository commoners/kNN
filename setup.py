from distutils.core import setup
from Cython.Build import cythonize
setup(name='kNN',
      ext_modules = cythonize('kNN.pyx')
      )
