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
from exersize2 import diverge, build_direct


#-----------------------------------------------------------------------
#              useful functions
#-----------------------------------------------------------------------

def refract(x, v0, v1, z0):
        '''calculates refracted wave traveltime'''

        return 
        
#-----------------------------------------------------------------------
#              main functions
#-----------------------------------------------------------------------

@io
def build_refractor(dataset, **kwargs):
        '''
        builds refractor
        '''
        
        #extract the base of weathering from the model

        
        #extract v0 and v1

        #calculate refraction travel times


        #create amplitude array

        #calculate the spherical divergence correction

        #apply correction


        #it probably wont exceed 1s, but to make it look right we 
        #need to limit it so that it doesnt cross over the direct


        #convert coordinates to integers

        #write values to array

        return 


        
if __name__ == '__main__':
        #initialise
        
        
        #build refractor
        
        #display
        
        pass

                

                
                
        
        
        

        
        
        