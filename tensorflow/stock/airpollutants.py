import time
import math
import os
from datetime import date
from datetime import timedelta
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
import pandas_datareader as pdr
from pandas_datareader import data, wb
from six.moves import cPickle as pickle

NHistData = 30
TrainDataSetSize = 500

trainData = None
loadNew = False

filename = 'Bejing_2016_AirQuality'
if os.path.exists(filename):
	try:
		with open(filename, 'rb') as f:
			save = pickle.load(f)
			trainDataPollutants = save['trainDataPollutants']
			trainDataVolume = save['trainDataVolume']
			del save
	except Exception as e:
		print('Unable to process data from', filename, ':', e)
		raise
	print('%s already present - Skipping requestion/pickling.' % filename)
else:
	f = pdr.data.DataReader()