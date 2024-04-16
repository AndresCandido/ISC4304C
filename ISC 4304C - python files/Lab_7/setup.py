from distutils.core import setup
from Cython.Build import cythonize
import numpy
#cimport numpy

setup(
    ext_modules=cythonize("juliapart.pyx",
                          annotate=True,
                          language_level = "3"),
    include_dirs=[numpy.get_include()],    
)
