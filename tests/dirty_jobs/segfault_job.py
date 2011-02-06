#!/usr/bin/env python
# (C) Copyright 2010 Brandyn A. White
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Cause a segfault to exercise our debugging ability"""

__author__ =  'Andrew Miller <amiller@dappervision.com'
__license__ = 'GPL V3'

import hadoopy
import cv

def mapper(key, value):
    """Cause a segfault the best way I know how
    """
    cv.Load("ravage me, opencv")
    

def reducer(key, values):
    pass

if __name__ == "__main__":
    hadoopy.run(mapper, reducer, doc=__doc__)
