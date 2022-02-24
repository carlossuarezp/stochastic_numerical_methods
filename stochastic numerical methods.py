import numpy as np

# generate n u[0,1] random variables
# using the numpy module we create a vector X: let each random variable X_n be the nth entry 
# that is, X_n = X[n]

def ln_2(size):
	X=[]
	Y=[]
	y_sum = 0
	# numpy.random.uniform() method
	X = np.random.uniform(size=size)
	for i in range(0,size):
		# Y_i = 1/(1+X_i) = 1/(1+X[i]) = Y[i]
		value = 1/(1+X[i])
		Y.append(value)
	for j in range(0,size):
		y_sum = y_sum+Y[j]
	y = y_sum/size
	print('Result with n=', size, '; y=',y)
	print('----------------------------')


# area of one quadrant (1/4) of the unit circle = pi/4
# are of the unit square = 1
# ratio of circle area over square area = ratio of points in the arc over points inside the square = pi/4
# pi = 4*(number of points in the arc/total number of points)  [approximately]
# Let k = number of points in the arc = number of points (a,b) for which a^2+b^2 <= 1
# Now we are ready to solve the problem with code by using the numpy library and a simple loop

def pi(size):
	k = 0
	# numpy.random.uniform() method
	X = np.random.uniform(size=size)     # X_n = X[n]
	Y = np.random.uniform(size=size)     # Y_n = Y[n]
	for i in range(0,size):
		value = (X[i])**2 + (Y[i])**2
		if (value<1):
			k = k+1
	pi = 4*k/size
	print('Result with n=', size, '; pi=', pi)
	print('----------------------------')


pi(100)
pi(1000)
ln_2(100)
ln_2(1000)