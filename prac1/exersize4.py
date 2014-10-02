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

def reflection_coefficient(z0, z1):
	#calculate reflection coefficient
	
	#return coefficient
	pass

def transmission_coefficient(z0, z1):
	#calculate transmission coefficient
	
	#return coefficient
	pass
	
#-----------------------------------------------------------------------
#              main functions
#-----------------------------------------------------------------------

@io
def build_reflector(workspace, **params):
	'''
	builds reflector
	'''
	
	#some shortcuts
	vp = params['model']['model']['vp']
	rho = params['model']['model']['rho']
	R = params['model']['model']['R']
	sz = params['sz']
	gz = params['gz']
	sx = params['sx']
	
	numpoints = 100 #used for interpolating through the model
	for gx in workspace['gx']:
		#calculate nearest midpoint
		#calculate h, the half-offset
		#the next line extracts the non-zero reflection points at this midpoint
		#and iterates over them
		for cmpz in (np.nonzero(R[cmpx,:])[0]):
			ds = np.sqrt(cmpz**2 + (h)**2)/float(numpoints) # line step distance
			#predefine outputs
			amp = 1.0
			time = 0.0

			#traveltime from source to cdp
			vp_down = toolbox.find_points(sx, sz, cmpx, cmpz, numpoints, vp)
			#update time

			#traveltime from cdp to geophone
			vp_up = toolbox.find_points(cmpx, cmpz, gx-1, gz, numpoints, vp)
			#update time

			#loss due to spherical divergence
			#calculate divergence
			#update amplitude

			#~ #transmission losses from source to cdp
			rho_down = toolbox.find_points(sx, sz, cmpx, cmpz, numpoints, rho)
			z0s = rho_down * vp_down
			z1s = toolbox.roll(z0s, 1)
			correction = np.cumprod(transmission_coefficient(z0s, z1s) )[-1] 
			#update amps

			#amplitude loss at reflection point
			correction = R[cmpx,cmpz]
			#update amps
			#transmission loss from cdp to source
			rho_up = toolbox.find_points(cmpx, cmpz, gx-1, gz, numpoints, rho)
			z0s = rho_up * vp_up
			z1s = toolbox.roll(z0s, 1)
			correction = np.cumprod(transmission_coefficient(z0s, z1s))[-1]
			#update amps

			#convert to coordinates

			#update workspace
	return workspace


	
if __name__ == '__main__':
	#initialise workspace
	
	#define a temporary shot location
	
	#update the workspace and parameter file with 
	#shot location, offset and absolute offset

	#build the reflected wave
	
	#add an agc
	
	#view it with agc
	
	pass

		

		
		
	
	
	

	
	
	