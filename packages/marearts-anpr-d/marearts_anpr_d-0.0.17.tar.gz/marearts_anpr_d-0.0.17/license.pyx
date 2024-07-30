# File: license.pyx
# cython: language_level=3
# distutils: language = c

def decrypt(x):
    return decrypt_c(x)

cpdef int decrypt_c(int x):
    return x * 2