import numpy as np
a=np.array([[2,3,1],[1,4,3]])
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))

b=np.array([[2,4,3],[2,4,1]])
print(np.dot(a,b.transpose()))

print(np.cross(a,b))

print(np.sort(a))
print(np.sort(a, axis=0))
print(np.sort(a, axis=0, kind="mergesort"))