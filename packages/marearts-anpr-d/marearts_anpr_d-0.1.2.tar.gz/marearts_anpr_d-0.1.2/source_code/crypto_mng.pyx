# cython: embedsignature=False
# cython: binding=False
# cython: language_level=3

# crypto_mng.pyx

cdef int secure_encryption(int x) nogil:
    return x * 2

cdef int secure_decryption(int x) nogil:
    return x * 2

cpdef int encryption(int x):
    if x < 0:
        raise ValueError("Input must be non-negative")
    return secure_encryption(x)

cpdef int decryption(int x):
    if x < 0:
        raise ValueError("Input must be non-negative")
    return secure_decryption(x)