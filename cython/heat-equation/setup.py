from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

setup(
    name='heat_optimised',
    ext_modules=cythonize(
        Extension(
            "heat_optimised",
            sources=["heat_optimised.pyx"],
            include_dirs=[numpy.get_include()]
        )
    ),
    install_requires=["numpy"]
)
