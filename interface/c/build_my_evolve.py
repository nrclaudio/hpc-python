import os
from cffi import FFI
ffibuilder = FFI()


with open(os.path.join(os.path.dirname(__file__), "evolve.h")) as f:
    ffibuilder.cdef(f.read())

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source("_my_evolve",
                      """#include "evolve.h" """,
                      sources=['evolve.c'],
                      library_dirs=[os.path.dirname(__file__), ],
                      libraries=["m"]
                      )

ffibuilder.compile(verbose=True)
