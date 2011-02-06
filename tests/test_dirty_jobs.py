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

__author__ = 'Brandyn A. White <bwhite@cs.umd.edu>'
__license__ = 'GPL V3'

import unittest
import hadoopy
import subprocess
import time

class Test(unittest.TestCase):

    def __init__(self, *args, **kw):
        super(Test, self).__init__(*args, **kw)
        self.data_path = 'hadoopy-test-data/%f/' % (time.time())
        filename = 'wc-input-alice.tb'
        self.input_path = self.data_path + filename
        cmd = 'hadoop fs -put %s %s' % (filename, self.input_path)
        subprocess.check_call(cmd.split())

    def _output_path(self):
        return self.data_path + 'output-%f' % (time.time())
        
    def test_segfault(self):
        out_path = self._output_path()
        hadoopy.launch_frozen(self.input_path, out_path, 'dirty_jobs/segfault_job.py')
        
if __name__ == '__main__':
    unittest.main()
