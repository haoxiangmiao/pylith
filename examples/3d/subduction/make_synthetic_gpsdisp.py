#!/usr/bin/env python
# -*- Python -*- (syntax highlighting)
#
# ----------------------------------------------------------------------
#
# Brad T. Aagaard, U.S. Geological Survey
# Charles A. Williams, GNS Science
# Matthew G. Knepley, University of Chicago
#
# This code was developed as part of the Computational Infrastructure
# for Geodynamics (http://geodynamics.org).
#
# Copyright (c) 2010-2017 University of California, Davis
#
# See COPYING for license information.
#
# ----------------------------------------------------------------------
#
# Python application to create synthetic data from PyLith points output.
# This script is meant to be used with example step07. It reads the
# slow slip displacements at synthetic cGPS stations from example
# step06, adds noise to the displacements, and then generates text and
# VTK files with the synthetic data. The parameters are defined in
# the make_synthetic_gpsdisp.cfg file.
# Run this script as follows:
# ./make_synthetic_gpsdisp.py
#

import math
import numpy
import h5py
import pdb

from pyre.applications.Script import Script as Application

class MakeSyntheticGpsdisp(Application):
  """
  Python application to create synthetic data from PyLith points output.
  """
  
  import pyre.inventory
  ## Python object for managing MakeSyntheticGpsdisp facilities and properties.
  ##
  ## \b Properties
  ## @li \b point_input_file HDF5 input file generated by PyLith.
  ## @li \b time_step Time step to use for data generation.
  ## @li \b sigma_east Sigma value for east displacements.
  ## @li \b sigma_north Sigma value for north displacements.
  ## @li \b sigma_up Sigma value for up displacements.
  ## @li \b output_file Name of ASCII output file.
  ## @li \b vtk_output_file Name of VTK output file.
  ##

  pointInputFile = pyre.inventory.str("point_input_file", default="cascadia-cgps_points.h5")
  pointInputFile.meta['tip'] = "HDF5 point output file from PyLith."

  timeStep = pyre.inventory.int("time_step", default=0)
  timeStep.meta['tip'] = "Time step to use for data generation."

  sigmaEast = pyre.inventory.float("sigma_east", default=0.0005)
  sigmaEast.meta['tip'] = "Sigma value for East displacements."

  sigmaNorth = pyre.inventory.float("sigma_north", default=0.0005)
  sigmaNorth.meta['tip'] = "Sigma value for North displacements."

  sigmaUp = pyre.inventory.float("sigma_up", default=0.001)
  sigmaUp.meta['tip'] = "Sigma value for Up displacements."

  outputFile = pyre.inventory.str("output_file", default="cascadia-cgps_disp.txt")
  outputFile.meta['tip'] = "Name of ASCII output file."

  vtkOutputFile = pyre.inventory.str("vtk_output_file", default="cascadia-cgps_disp.vtk")
  vtkOutputFile.meta['tip'] = "Name of VTK output file."


  # PUBLIC METHODS /////////////////////////////////////////////////////

  def __init__(self, name="make_synthetic_gpsdisp"):
    Application.__init__(self, name)

    self.coords = None
    self.stations = None
    self.dispRaw = None
    self.dispNoise = None

    self.numStations = 0

    return


  def main(self):
    # pdb.set_trace()
    self._readHDF5()
    self._addNoise()
    self._writeOutput()
    self._writeVTKOutput()

    return
  

  # PRIVATE METHODS /////////////////////////////////////////////////////


  def _configure(self):
    """
    Setup members using inventory.
    """
    Application._configure(self)

    return


  def _readHDF5(self):
    """
    Function to read HDF5 file from PyLith.
    """

    h5 = h5py.File(self.pointInputFile, 'r')
    self.coords = h5['geometry/vertices'][:]
    self.stations = h5['stations'][:]
    self.dispRaw = h5['vertex_fields/displacement'][self.timeStep,:,:]
    h5.close()

    self.numStations = self.coords.shape[0]

    return


  def _addNoise(self):
    """
    Function to add noise to computed displacements.
    """
    self.dispNoise = self.dispRaw.copy()
    self.dispNoise[:,0] += self.sigmaEast * numpy.random.randn(self.numStations)
    self.dispNoise[:,1] += self.sigmaNorth * numpy.random.randn(self.numStations)
    self.dispNoise[:,2] += self.sigmaUp * numpy.random.randn(self.numStations)
    return
    

  def _writeOutput(self):
    """
    Function to write output file with noisy data and uncertainties.
    """
    head = "Station\tX\tY\tZ\tUEast\tUNorth\tUUp\tSigEast\tSigNorth\tSigUp\n"
    outFmt = "%s" + 9 * "\t%g" + "\n"

    f = open(self.outputFile, 'w')
    f.write(head)

    for stationNum in range(self.numStations):
      outLine = outFmt % (self.stations[stationNum],
                          self.coords[stationNum,0], self.coords[stationNum,1],
                          self.coords[stationNum,2],
                          self.dispNoise[stationNum,0],
                          self.dispNoise[stationNum,1],
                          self.dispNoise[stationNum,2],
                          self.sigmaEast, self.sigmaNorth, self.sigmaUp)
      f.write(outLine)

    f.close()

    return
    

  def _writeVTKOutput(self):
    """
    Function to write VTK output file with noisy data and uncertainties.
    """

    sigma = numpy.ones((self.numStations, 3), dtype=numpy.float64)
    sigma[:,0] *= self.sigmaEast
    sigma[:,1] *= self.sigmaNorth
    sigma[:,2] *= self.sigmaUp

    vtkHead = "# vtk DataFile Version 2.0\n" + \
              "Synthetic GPS stations\n" + \
              "ASCII\n" + \
              "DATASET POLYDATA\n" + \
              "POINTS " + repr(self.numStations) + " double\n"

    v = open(self.vtkOutputFile, 'w')
    v.write(vtkHead)
    numpy.savetxt(v, self.coords)

    numConnect = 2 * self.numStations
    connectHead = "VERTICES %d %d\n" % (self.numStations, numConnect)
    v.write(connectHead)
    verts = numpy.arange(self.numStations, dtype=numpy.int)
    sizes = numpy.ones_like(verts)
    outConnect = numpy.column_stack((sizes, verts))
    numpy.savetxt(v, outConnect, fmt="%d")
    
    dispHead = "POINT_DATA " + repr(self.numStations) + "\n" + \
               "VECTORS displacement double\n"
    v.write(dispHead)
    numpy.savetxt(v, self.dispNoise)

    sigHead = "VECTORS uncertainty double\n"
    v.write(sigHead)
    numpy.savetxt(v, sigma)
    v.close()
    
    return


# ----------------------------------------------------------------------
if __name__ == '__main__':
  app = MakeSyntheticGpsdisp()
  app.run()

# End of file
