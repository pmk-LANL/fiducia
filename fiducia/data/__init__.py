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

