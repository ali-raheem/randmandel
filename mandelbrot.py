#!/usr/bin/python

import cmath
import random
import numpy as np
import scipy.misc as smp
from mandel import isMandelbrot

def gen_rand_colours():
	colours = []
	i = 0
	while (256 > i):
		colours.append([
			random.randint(0,256),
			random.randint(0,256),
			random.randint(0,256)
		])
		i += 1
	return colours

def mandelbrot (width, height, colours):
	thresh = 1000
	data = np.zeros((height, width, 3), dtype=np.uint8)
	x = 0
	y = 0
	while (x < width):
		while (y < height):
			ij = isMandelbrot(x, y, width, height, thresh)
	   		data[y, x] = colours[ij]
			#print ("mandelbrot(%i, %i) = %i."%(x, y, ij))
			y += 1
		x += 1
		y = 0
	return data
	
if __name__ == '__main__':
	colours = gen_rand_colours()
	data = mandelbrot(640, 480, colours)
	img = smp.toimage(data)
	smp.imshow(img)
	smp.imsave('output.png', img)
