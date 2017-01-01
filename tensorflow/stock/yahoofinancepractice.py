import numpy as np
from TFMLP import MLPR
import matplotlib.pyplot as mpl
from sklearn.preprocessing import scale
 
pth ="..\python\yahoo.csv"
A = np.loadtxt(pth, delimiter=",", skiprows=1, usecols=(0	,4))
A = scale(A)
#y is the dependent variable
y = A[:, 1].reshape(-1, 1)
#A contains the independent variable
A = A[:, 0].reshape(-1, 1)
#Plot the high value of the stock price

#Number of neurons in the input layer
i = 1
#Number of neurons in the output layer
o = 1
#Number of neurons in the hidden layers
h = 128
#The list of layer sizes
layers = [i, h, h, h, h, h, h, h, h, h, o]
mlpr = MLPR(layers, maxItr = 1000, tol = 0.40, reg = 0.001, verbose = True)

#Length of the hold-out period
nHours = 20+
n = len(A)
#Learn the data
mlpr.fit(A[0:(n-nHours)], y[0:(n-nHours)])

#Begin prediction
yHat = mlpr.predict(A)

#Mark Turning Points
largeBefore = True;
for i in range(len(yHat) - 1):
	if (yHat[i + 1] < yHat[i] and largeBefore == True):
		mpl.plot(A[i], yHat[i], marker='x', color='#000000')
		print(A[i], i)
		largeBefore = False;
	elif (yHat[i + 1] > yHat[i] and largeBefore == False):
		mpl.plot(A[i], yHat[i], marker='x', color='#000000')
		print(A[i], i)
		largeBefore = True;		
#Plot the results
mpl.plot(A, y, c='#b0403f')
mpl.plot(A, yHat, c='#5aa9ab')

mpl.show()