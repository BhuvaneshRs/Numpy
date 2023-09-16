x=np.arange(0,10,dtype='int8') #Start Stop Dtype
x
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int8)

y=np.arange(0,20,2,dtype='int8')  #Start Stop Step Dtype
y
array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18], dtype=int8)

z=np.arange(0,100,10,dtype='int8')
array([ 0, 10, 20, 30, 40, 50, 60, 70, 80, 90], dtype=int8)

z.nbytes
10

z.ndim
1

z.size
10
