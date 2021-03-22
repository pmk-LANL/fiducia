#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 15:04:49 2021

Submodule/directory with data for examples and testing.

@author: Pawel M. Kozlowski
"""

import os.path as osp


def _fetch(data_filename):
    r"""
    Fetches the absolute path of the file give the relative location
    of the file within the fiducia package.
    
    Parameters
    ----------
    data_filename : str
        Relative path of file within the fiducia.data submodule.
        
    Returns
    -------
    resolved_path : 
        Absolute path to data file within fiducia.data submodule.
    """
    data_dir = osp.abspath(osp.dirname(__file__))
    resolved_path = osp.join(data_dir, '..', data_filename)
    # check that the resolved path corresponds to a files that exists
    if not osp.isfile(resolved_path):
        raise Exception(f"No such file {resolved_path}")
    return resolved_path


def shot89336():
    r"""
    Gets absolute paths to example data for shot 89336 on Omega-60.
    """
    # raw Dante data file 
    danteFileRel = 'data/dante_dante89336.dat'
    # corresponding response functions file
    responseFileRel = 'data/do171127_2018-10-29_response_functions.csv'
    # file of input uncertainties for each channel
    responseUncertaintyFileRel = 'data/exampleuncertainty_1d.csv'
    # oscilloscope offsets file for calibrating channel signals
    offsetsFileRel = 'data/Offset.xls'
    # oscilloscope attenuators file to correct for addition attenuation
    # on individual channels. Note: that the identification numbers of the
    # attenuators used for an Omega-60 shot should be recorded in the header
    # of the raw Dante data file.
    attenuatorsFileRel = 'data/TableAttenuators.xls'
    # MC propagated uncertainties
    csplineDatasetFileRel = 'data/csplineDataset.nc'
    
    # getting absolute paths to data files
    danteFileAbs = _fetch(danteFileRel)
    responseFileAbs = _fetch(responseFileRel)
    responseUncertaintyFileAbs = _fetch(responseUncertaintyFileRel)
    offsetsFileAbs = _fetch(offsetsFileRel)
    attenuatorsFileAbs = _fetch(attenuatorsFileRel)
    csplineDatasetFileAbs = _fetch(csplineDatasetFileRel)
    
    # saving absolute paths into a dict
    dataDict = {'Raw Dante' : danteFileAbs,
                'Response Funcs' : responseFileAbs,
                'Response Uncertainty' : responseUncertaintyFileAbs,
                'Oscilloscope Offsets' : offsetsFileAbs,
                'Attenuators' : attenuatorsFileAbs,
                'MC Uncertainties' : csplineDatasetFileAbs,
                'LA-UR': 'LA-UR-21-22787'}
    return dataDict