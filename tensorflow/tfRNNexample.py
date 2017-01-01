import tensorflow as tf 
from tensorflow.examples.tutorials.mnist import input_data

# Set random seed for comparing the two result calculations
tf.set_random_seed(1)

# Data
mnist = input_data.read_data_sets('MNIST_data',one_hot=True)

# Parameters
lr = 0.001
training_iters = 1000000
batch_size = 128
display_step = 10

n_inputs = 28
n_steps = 28
n_hidden_units = 128
n_classes = 10