#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      PC105
#
# Created:     12-01-2016
# Copyright:   (c) PC105 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("v.pyx")
)