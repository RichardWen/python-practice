import numpy as np
import tensorflow as tf
# Define both the x and y variables
# Since we use the linear regression model, we're trying to find a 
# y = mx + b equation so we must train our tensorflow to look for
# W and b 
x = tf.placeholder(tf.float32, [None, 1])
W = tf.Variable(tf.zeros([1,1]))
b = tf.Variable(tf.zeros([1]))
y = tf.matmul(x,W) + b
y_ = tf.placeholder(tf.float32, [None, 1])
cost = tf.reduce_sum(tf.pow((y_-y),2))

# Generate Fake Data
# W = 2, b = 0
xs = []
ys = []
# We need to train our data.
# GradientDescentOptimizer is what we use as it guides our data
# Look up for more details
train_step = tf.train.GradientDescentOptimizer(0.00001).minimize(cost)

# Create session and run what we generated
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
steps = 500
for i in range (steps):
	xs = np.array([[i]])
	ys = np.array([[2*i]])
	feed = {x: xs, y_: ys}
	sess.run(train_step, feed_dict=feed)

	# Print our output
	print("After %d iteration:" %i)
	print("W: %f" % sess.run(W))
	print("b %f" % sess.run(b))