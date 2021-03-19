"""
Hohlraum unfold tutorial
===================================


"""



import numpy as np
import os
import xarray as xr
import datetime
import matplotlib.pyplot as plt


from fiducia.error import detectorUncertainty
from fiducia.main import feelingLucky


def danteName(shotNum):
    """
    Construct name of dante data file, given shot number.
    """
    name = 'dante_dante' + str(shotNum) + '.dat'
    return name


def dantePath(directory, shotNum):
    """
    Construct full path name for DANTE file given shot number.
    """
    filePath = os.path.join(directory, danteName(shotNum))
    return filePath


#current ignal data is from 86455
shotNum = 86455
# selecting which channels to analyze
channels = [2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14]

# response functions file
dirResponse = '/home/pkozlowski/LANL_postdoc/codes/python/fiducia/data/calibration/'
responseFile = 'do170801_2018-03-07_response_functions.csv'
#responseUncertaintyFile = 'exampleuncertainty_1dper.csv'
responseUncertaintyFile = 'exampleuncertainty_1d-PMK100.csv'

# DANTE measurement data file(s) (not aligned)
dirCOAX = '/home/pkozlowski/LANL_postdoc/codes/python/fiducia/data/COAX/86455/'

# directory to partially reduced data provided by Dan (just attenuator correction and bkg subtraction)
dirDan = '/home/pkozlowski/LANL_postdoc/codes/python/fiducia/data/Dan/'


# directory with calibration files for attenuators and offsets on DANTE channels
dirCal = '/home/pkozlowski/LANL_postdoc/codes/python/fiducia/data/calibration/'
offsetsFile = 'Offset.xls'
attenuatorsFile = 'TableAttenuators.xls'

#filenames spline matrices
csplineDatasetFile = 'csplineDataset.nc'


danteFileFull = dantePath(dirCOAX, shotNum)


    
  
#%% saving uncertainty propagation matrices
boundary = "y0"

# run error prop and MC
#detectorUncertainty(channels,
#                    dirResponse + responseFile,
#                    dirResponse + responseUncertaintyFile,
#                    boundary=boundary,
#                    csplineDatasetFile=csplineDatasetFile)


# unfolding spectra

#example signal uncertainty.
signalsUncertainty = np.zeros(len(channels))

area = np.pi * 0.6 ** 2
# dante viewing angle relative to normal of emitting surface, in degrees 
#angle = 37.4
#angle = 69.09
angle = 69.18
results = feelingLucky(dataFile=danteFileFull,
                       attenuatorsFile=dirCal + attenuatorsFile,
                       offsetsFile=dirCal + offsetsFile,
                       responseFile=dirResponse + responseFile,
                       csplineDatasetFile=csplineDatasetFile, 
                       channels=channels,
                       area=area,
                       angle=angle,
                       signalsUncertainty=signalsUncertainty)

# unpacking reuslts
times, energies, spectra, power, tRad = results

