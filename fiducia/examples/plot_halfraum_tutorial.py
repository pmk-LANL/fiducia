"""
Hohlraum unfold tutorial
===================================


"""


#%%
#Importing modules

import numpy as np
import matplotlib.pyplot as plt

from fiducia.data import shot89336
from fiducia.error import detectorUncertainty
from fiducia.main import feelingLucky
# import fiducia.pltDefaults


#%%
#Setting up paths we need to raw data and calibration data

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



#%%
# Next we select which channels to include in the analysis. These
# are Omega-60 Dante channels.
channels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13]



#%%
# Selecting which boundary condition to use in the unfold. The `y0` condition 
# sets the low-energy portion of the spectrum as photon energy approaches
# zero.

# boundary = "y0"

#%%
# Uncertainty propagation using Monte Carlo to obtain covariance
# terms across the various Dante channels.

# detectorUncertainty(channels,
#                     responseFile,
#                     responseUncertaintyFile,
#                     boundary=boundary,
#                     csplineDatasetFile=csplineDatasetFile)

#%%
# For the purposes of this tutorial, we are skipping over this Monte Carlo
# uncertainties propagation and just giving you the resultant file.
# Getting path of MC uncertainties file

csplineDatasetFile = shot89336Dict['MC Uncertainties']


#%%
# input parameters

peaksNum = 1
peakAlignIdx = 0
prominence = 0.01
peakWidth = 10
avgMult = 3
timeStart = -1
timeStop = 4
timeStep = 0.1

# example signal uncertainty.
signalsUncertainty = np.zeros(len(channels))

#%%
# Calculate emitting area of plasma. In this case the emission is
# coming out of the hohlraum laser entrance hole (LEH).

leh_diameter = 1.200 # mm
area = np.pi * (leh_diameter / 2) ** 2

#%%
# Dante viewing angle relative to normal of emitting surface, in degrees.
# This is used to get the projected emitting area.

angle = 37.4

#%%
# Now we bring everything together and run the unfold using Fiducia's
# `feelingLucky()` function

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

#%%
# The results come in a tuple of timesteps, photon energies, spectral
# intensities, total radiated power, and radiation temperature.

times, energies, spectra, power, tRad = results


#%%
# First let's plot the streaked spectrum. For this we have a useful
# function built into Fiducia's visualization library

from fiducia.visualization import plotStreak
plotStreak(times, energies, spectra)
plt.show()


#%% Fiducia automatically integrates the time-resolved unfolded spectra
# at each time step to produce a single value of radiated power at each
# time step. In other words, we have integrated the spectra across
# photon energy to get total radiated power in the soft x-ray spectrum
# covered by all the channels included in our analysis.

plt.scatter(times, power)
plt.xlabel("Time (ns)")
plt.ylabel("Radiated Power (GW/sr)")
plt.show()
    
#%%
# Next we plot the radiation temperature. The radiation temperature is
# obtained by using the Stefan-Boltzmann equation
#
# .. math::
#   P(t) = \sigma_{SB} A \cos(\theta) T_{rad}^4(t)
#
# where :math:`P(t)` is the total radiated power as a function of time,
# :math:`\sigma_{SB}` is the Stefan-Boltzmann constant, :math:`A` is the
# area of the hohlraum LEH, :math:`\theta` is the viewing angle of Dante
# relative to the normal vector of the emitting surface (in this case relative
# to the hohlraum cylindrical axis), and :math:`T_{rad}` is the radiation
# temperature. Note that :math:`A \cos(\theta)` is the projected emitting
# area as viewed by Dante. At :math:`\theta = 0^{\circ}` Dante is viewing
# directly down the hohlraum axis, and so sees the full area of the LEH,
# whereas at :math:`\theta = 90^{\circ}` Dante is looking at the hohlraum
# from the side and does not see the LEH whatsoever.
# Using the radiated power, area, and viewing angle, fiducia has already
# solved for the radiation temperature, which we plot here.

plt.scatter(times, tRad)
plt.xlabel("Time (ns)")
plt.ylabel("Radiation Temperature (eV)")
plt.show()
