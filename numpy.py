import numpy as np
a=np.array([1,2,3])
print(a.size)
print(a.itemsize)
print(a.dtype)
print(a.shape)
print(a.reshape(3,1))
print(a.sum())
print(a.max())
print(a.min())
print(np.sqrt(3))
print(a.std())
k=np.arange(0,10,2)
print(k)
print(a)
j=np.array([1,2,3,4,5])
print(k+j)
ab=np.zeros((3,2),dtype="float64")
print(ab)
print(a[0])
print(a[1:3])
c=np.arange(10).reshape(2,5)
print(c)
d=np.arange(10,20).reshape((2,5))
print(d)
print(np.vstack([c,d]))
print(np.hstack([c,d]))
e=np.arange(0,100).reshape((1,100))
print(np.hsplit(e,4))

e=np.arange(0,100).reshape((100,1))
print(np.vsplit(e,4))

k=np.arange(1,100)
j=k>90
print(j)
print(k[j])
k[j]=-1
print(k)


a=np.arange(0,10).reshape(2,5)
b= np.arange(10,20).reshape(2,5)
for row in a:
    print(row)

for row in a:
    for cell in row:
        print(cell)

for x in np.nditer(a,order='C'):
    print(x)
for x in np.nditer(a,order='F'):
    print(x)
for x in np.nditer(a,order='F',op_flags=['readwrite']):
    x[...]=x*x
print(a)
for x in np.nditer(a,order='F',flags=['external_loop']):
    print(x)
for x,y in np.nditer([a,b]):
    print(x,y)
