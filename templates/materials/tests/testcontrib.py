#!/usr/bin/env python
#
# ======================================================================
#
#                           Brad T. Aagaard
#                        U.S. Geological Survey
#
# {LicenseText}
#
# ======================================================================
#

import unittest

def suite():

  suite = unittest.TestSuite()

  from TestPlaneStrainState import TestPlaneStrainState
  suite.addTest(unittest.makeSuite(TestPlaneStrainState))

  return suite

def main():
  unittest.TextTestRunner(verbosity=2).run(suite())
  return

if __name__ == '__main__':
  main()
  

# End of file 
