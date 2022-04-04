#!/usr/bin/env python
import random
import time
import numpy as np
n=512

#populate the matrices with random values between 0.0 and 1.0
A = np.random.rand(512, 512).astype("float")
B = np.random.rand(512, 512).astype("float")
C = np.zeros((512, 512), dtype="float")

start = time.time()
#matrix multiplication
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i, j] += A[i,k] * B[k,j]

end = time.time()
# Elapsed time 
print("Elapsed time in seconds %0.6f" % (end-start))
