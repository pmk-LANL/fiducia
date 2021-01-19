#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:11:09 2019

Fiducia setup script.

@author: Pawel M. Kozlowski
"""

from setuptools import setup

setup(name='fiducia',
      version='0.2',
      description='DANTE data unfolder using cubic-spline algorithm',
      url='https://github.com/lanl/fiducia',
      author='Pawel M. Kozlowski, et al.',
      author_email='pkozlowski@lanl.gov',
      license='BSD',
      packages=['fiducia'],
      zip_safe=True)