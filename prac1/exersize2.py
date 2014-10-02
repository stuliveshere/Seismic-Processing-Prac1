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

#-----------------------------------------------------------------------
#              useful functions
#-----------------------------------------------------------------------
def diverge(distance, coefficient=3.0):
	#spherical divergence correction
	
	#return result
	pass

	
#-----------------------------------------------------------------------
#              main functions
#-----------------------------------------------------------------------

@io
def build_direct(workspace, **params):
	'''
	calculates direct wave arrival time and 
	imposes it upon an array. assumes 330 m/s
	surface velocity
	'''
	
	#define velocity and calculate direct times
	
	#set base amplitude (from testing)
	
	#calculate the spherical divergence correction
	
	#apply correction and remove nans
	
	#we are not interested in anything after 1 second

	#convert to coordinates

	#add to workspace
	
	#return workspace
	pass


	
if __name__ == '__main__':
	#initialise workspace
	
	#define a temporary shot location
	
	#update the workspace and parameter file with 
	#shot location, offset and absolute offset

	#build the direct wave
	
	#view the direct wave
	
	#add an agc
	
	#view it with agc
	
	pass


		

		
		
	
	
	

	
	
	