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
    '''calculate zero-offset reflection coefficient'''

    return

def transmission_coefficient(z0, z1):
    '''calculate zero-offset transmission coefficient'''

    return 

#-----------------------------------------------------------------------
#              main functions
#-----------------------------------------------------------------------

@io
def build_reflector(dataset, **kwargs):
        '''
        builds reflector
        '''
        
        #some shortcuts
        vp = kwargs['model']['vp']
        rho = kwargs['model']['rho']
        R = kwargs['model']['R']
        sz = kwargs['sz']
        gz = kwargs['gz']
        sx = kwargs['sx']
        gx = kwargs['gx']
        
        numpoints = 100 #used for interpolating through the model
        for g in  gx:
                cmpx = np.floor((g + sx)/2.).astype(np.int) # nearest midpoint
                h = cmpx - sx #half offset
                #the next line extracts the non-zero reflection points at this midpoint
                rp = np.nonzero(R[cmpx,:])[0]
                #and iterates over them
                for cmpz in (rp):
                        #~ print cmpx, cmpz
                        ds = np.sqrt(cmpz**2 + (h)**2)/float(numpoints) # line step distance
                        #predefine outputs
                        amp = 1.0
                        time = 0.0

                        #traveltime from source to cdp
                        vp_down = toolbox.find_points(sx, sz, cmpx, cmpz, numpoints, vp)
                        time += 0

                        #traveltime from cdp to geophone
                        vp_up = toolbox.find_points(cmpx, cmpz, g, gz, numpoints, vp)
                        time += 0

                        #loss due to spherical divergence
                        amp *= 0

                        #transmission losses from source to cdp
                        rho_down = toolbox.find_points(sx, sz, cmpx, cmpz, numpoints, rho)
                        z0s = rho_down * vp_down
                        z1s = toolbox.roll(z0s, 1)
                        correction = np.cumprod(transmission_coefficient(z0s, z1s) )[-1] 
                        amp *= 0
                        #amplitude loss at reflection point
                        correction = R[cmpx,cmpz]
                        amp *= 0
                        #transmission loss from cdp to source
                        rho_up = toolbox.find_points(cmpx, cmpz, g, gz, numpoints, rho)
                        z0s = rho_up * vp_up
                        z1s = toolbox.roll(z0s, 1)
                        correction = np.cumprod(transmission_coefficient(z0s, z1s))[-1]
                        amp *= 0

                        #calculate coordinates
                        
                        #write out data
                        
        return 


        
if __name__ == '__main__':
        #initialise

        
        #build reflector

        #display
        pass


                

                
                
        
        
        

        
        
        