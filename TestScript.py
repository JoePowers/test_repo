#!/usr/bin/env python
# encoding: utf-8
"""
TestCode.py - generate some random data and then plot a hist of it.
Created by JDP for python training class on 2014.11.06
"""

import numpy as np
import matplotlib.pyplot as plt


def show_histgumbel(data_length=50000, bins=100):
	"""Takes:
		data_length: how many data points to plot (defult 50000)
		bins: how many bins in hist (defult 100)
	   Gives:
		None
	"""
	data = np.random.gumbel(0,1,50000)
	plt.hist(data,50)
	plt.show()

def main():
	show_histgumbel(10000, 50)

if __name__ == '__main__':
	main()
