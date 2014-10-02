from toolbox import io
import toolbox
import numpy as np
import matplotlib.pyplot as pylab
from exersize1 import initialise
from exersize5 import build_combined, add_noise, convolve_wavelet

if __name__ == "__main__":
	#initialise workspace, parameter file
	
	#define output file
	output = np.zeros(0, dtype=param['sutype'])
	
	#iterate over shot points
	for sx in param['sx_coords']:
		print sx
		#update workspace and parameter file
		#clear workspace
		#build the shot record
		#convolve the wavelet
		#add the noise
		#add to output
	
#write to output		
	toolbox.cp(output, 'survey.su', **param)
		
		