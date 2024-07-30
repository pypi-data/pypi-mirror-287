# crypto_mng.pyx
# cython: language_level=3
# distutils: language = c

def encryption(x):
    x = c_encryption(x)
    return x

def description(x):
    x = c_description(x)
    return x

cpdef int c_encryption(int x):
    x = x * 2
    return x

cpdef int c_description(int x):
    x = x * 2
    return x