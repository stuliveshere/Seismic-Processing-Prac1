# in prac 1 we will build a synthetic shot record. 
# it will compose of 3 separate components
#	direct wave
#	refracted wave
#	reflected wave
# based up on a predefined model.

from toolbox import io
import toolbox
import numpy as np
import matplotlib.pyplot as pylab
from exersize1 import initialise
from exersize2 import diverge


#-----------------------------------------------------------------------
#              useful functions
#-----------------------------------------------------------------------

def refract(x, v0, v1, z0):
	#refraction time calculation
	
	#return time
	pass
	
#-----------------------------------------------------------------------
#              main functions
#-----------------------------------------------------------------------

@io
def build_refractor(workspace, **params):
	'''
	builds refractor
	'''
	
	#some shortcuts
	v0 = params['model']['vp'][0]
	v1 = params['model']['vp'][1]
	z0 = params['model']['dz'][0]
	
	#calculate refraction times

	#create amplitude array
	
	#calculate the spherical divergence correction
	
	#apply correction and remove nans

	#it probably wont exceed 1s, but to make it look right we 
	#need to limit it so that it doesnt cross over the direct
	#recalculate direct times
	#filter 

	#convert to array coordinates

	#add to workspace
	
	#return workspace


	
if __name__ == '__main__':
	#initialise workspace
	
	#define a temporary shot location
	
	#update the workspace and parameter file with 
	#shot location, offset and absolute offset

	#build the refracted wave
	
	#add an agc
	
	#view it with agc
	
	pass

		

		
		
	
	
	

	
	
	