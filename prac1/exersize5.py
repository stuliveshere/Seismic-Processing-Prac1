from toolbox import io
import toolbox
import numpy as np
import matplotlib.pyplot as pylab
from exersize1 import initialise
from exersize2 import  build_direct
from exersize3 import build_refractor
from exersize4 import build_reflector

#-----------------------------------------------------------------------
#              useful functions
#-----------------------------------------------------------------------

@io
def build_combined(workspace, **params):
	workspace = build_direct(workspace, None, **params)
	workspace = build_refractor(workspace, None, **params)
	workspace = build_reflector(workspace, None, **params)
	return workspace
	
@io
def add_noise(workspace, **params):
	noise = np.random.normal(0.0, 1e-8, size=(workspace['trace'].shape))
	#add noise to the workspace
	return workspace
	
@io
def convolve_wavelet(workspace, **params):
	wavelet = toolbox.ricker(60)	
	workspace =  toolbox.conv(workspace, wavelet)
	return workspace

if __name__ == '__main__':
	#initialise workspace
	
	#define a temporary shot location
	
	#update the workspace and parameter file with 
	#shot location, offset and absolute offset

	#build the shot record
	
	#convolve in the wavelet
	
	#add noise
	
	#add an agc
	
	#view it with agc
	
	pass
