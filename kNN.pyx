cdef extern from "math.h":
    extern float sqrt(float)
    extern float pow(float,float)
cpdef float p_sqrt(float x):
    return sqrt(x)
cpdef float p_pow(float x,float n):
    return pow(x,n)
