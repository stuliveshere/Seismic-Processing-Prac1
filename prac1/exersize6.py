from toolbox import io
import toolbox
import numpy as np
import matplotlib.pyplot as pylab
from multiprocessing import Pool
from exersize1 import initialise
from exersize5 import build_combined, add_noise, convolve_wavelet

def run(sx):
	#initialise 
	print sx
	#update workspace and parameter file
	#clear workspace
	#build the shot record
	#convolve the wavelet
	#add the noise
	#add to output

	#write to output	

if __name__ == "__main__":
	#initialise workspace, parameter file
	
	#allocate worker pool
	pool = Pool(processes=8)
	#run worker pool
	result = pool.map(run, param['sx_coords'])
	#workspace = toolbox.agc('.shot201.su', None, None)
	#toolbox.display(workspace, None, None)	
		