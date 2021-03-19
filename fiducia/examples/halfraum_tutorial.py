"""
Hohlraum unfold tutorial
===================================


"""

import numpy as np

from fiducia.data import shot89336
from fiducia.error import detectorUncertainty
from fiducia.main import feelingLucky


# load absolute paths to example data
shot89336Dict = shot89336()

# raw Dante data file 
danteFileFull = shot89336Dict['Raw Dante']

# corresponding response functions file
responseFile = shot89336Dict['Response Funcs']

# file of input uncertainties for each channel
responseUncertaintyFile = shot89336Dict['Response Uncertainty']

# oscilloscope offsets file for calibrating channel signals
offsetsFile = shot89336Dict['Oscilloscope Offsets']

# oscilloscope attenuators file to correct for addition attenuation
# on individual channels. Note: that the identification numbers of the
# attenuators used for an Omega-60 shot should be recorded in the header
# of the raw Dante data file.
attenuatorsFile = shot89336Dict['Attenuators']

# # filename for saving spline matrices. This should end with extension .nc
# csplineDatasetFile = 'csplineDataset.nc'



# selecting which channels to include in the analysis
channels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13]

# input params
peaksNum = 1
peakAlignIdx = 0
prominence = 0.01
peakWidth = 10
avgMult = 3
timeStart = -1
timeStop = 4
timeStep = 0.1

# Selecting which boundary condition to use in the unfold. The y0 condition 
# sets the low-energy portion of the spectrum as photon energy approaches
# zero.
boundary = "y0"

# uncertainty propagation using Monte Carlo to obtain covariance
# terms across the various Dante channels.
# detectorUncertainty(channels,
#                     responseFile,
#                     responseUncertaintyFile,
#                     boundary=boundary,
#                     csplineDatasetFile=csplineDatasetFile)
# For the purposes of this tutorial, we are skipping over this Monte Carlo
# uncertainties propagation and just giving you the resultant file.
# Getting path of MC uncertainties file
csplineDatasetFile = shot89336Dict['MC Uncertainties']


# example signal uncertainty.
signalsUncertainty = np.zeros(len(channels))

# Calculate emitting area of plasma. In this case the emission is
# coming out of the hohlraum laser entrance hole (LEH).
leh_diameter = 1.200 # mm
area = np.pi * (leh_diameter / 2) ** 2

# dante viewing angle relative to normal of emitting surface, in degrees.
# This is used to get the projected emitting area.
angle = 37.4

# unfolding spectra
results = feelingLucky(dataFile=danteFileFull,
                       attenuatorsFile=attenuatorsFile,
                       offsetsFile=offsetsFile,
                       responseFile=responseFile,
                       csplineDatasetFile=csplineDatasetFile, 
                       channels=channels,
                       area=area,
                       angle=angle,
                       signalsUncertainty=signalsUncertainty,
                       peaksNum=peaksNum,
                       peakAlignIdx=peakAlignIdx,
                       prominence=prominence,
                       peakWidth=peakWidth,
                       avgMult=avgMult,
                       timeStart=timeStart,
                       timeStop=timeStop,
                       timeStep=timeStep)

# unpacking reuslts
times, energies, spectra, power, tRad = results

