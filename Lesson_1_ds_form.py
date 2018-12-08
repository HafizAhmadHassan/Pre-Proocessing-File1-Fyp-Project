from __future__ import print_function
import csv
import os, csv
# mannulay create file first
import cv2
import numpy as np
import scipy.misc
from scipy import misc
from scipy.misc.pilutil import Image

import numpy as np
import argparse
import cv2

import itertools
c1 = itertools.count()
def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
 
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)




for path, dirs, files in os.walk("dat"):
    for filename in files:
	try:
    		a=str(c1.next())
    		if filename[0] == 'b' :
        		im = cv2.imread(path + "/" + filename)
        		im = cv2.resize(im, (256, 256)) 
        		img = adjust_gamma(im,1.5)
		#im = im/255.0
		#im_power_law_transformation = cv2.pow(im,1.5)
		#im_result = scipy.misc.toimage(im_power_law_transformation)
			cv2.imwrite(filename,img)    	
       		else :
       		#os.rename(path + "/" +filename ,path + "/" + 'train_'+ a + '.jpg')
       			im = cv2.imread(path + "/" + filename)
       			im = cv2.resize(im, (256, 256))
			img=adjust_gamma(im,0.67)
			cv2.imwrite(filename,img)   
		#im_power_law_transformation = cv2.pow(im,0.5)
		#im_result = scipy.misc.toimage(im_power_law_transformation)
		#misc.imsave(path + "/" +'train_'+ a +'.jpg',im_result) 
	except:
		pass
	
		

