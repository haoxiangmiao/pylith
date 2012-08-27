// -*- C++ -*-
//
// ======================================================================
//
// Brad T. Aagaard, U.S. Geological Survey
// Charles A. Williams, GNS Science
// Matthew G. Knepley, University of Chicago
//
// This code was developed as part of the Computational Infrastructure
// for Geodynamics (http://geodynamics.org).
//
// Copyright (c) 2010-2012 University of California, Davis
//
// See COPYING for license information.
//
// ======================================================================
//

// DO NOT EDIT THIS FILE
// This file was generated from python application elasticityexplicitapp.

#include "ElasticityExplicitGravData2DLinear.hh"

const int pylith::feassemble::ElasticityExplicitGravData2DLinear::_spaceDim = 2;

const int pylith::feassemble::ElasticityExplicitGravData2DLinear::_cellDim = 2;

const int pylith::feassemble::ElasticityExplicitGravData2DLinear::_numVertices = 3;

const int pylith::feassemble::ElasticityExplicitGravData2DLinear::_numCells = 1;

const int pylith::feassemble::ElasticityExplicitGravData2DLinear::_numBasis = 3;

const int pylith::feassemble::ElasticityExplicitGravData2DLinear::_numQuadPts = 1;

const char* pylith::feassemble::ElasticityExplicitGravData2DLinear::_matType = "ElasticPlaneStrain";

const char* pylith::feassemble::ElasticityExplicitGravData2DLinear::_matDBFilename = "data/elasticplanestrain.spatialdb";

const int pylith::feassemble::ElasticityExplicitGravData2DLinear::_matId = 0;

const char* pylith::feassemble::ElasticityExplicitGravData2DLinear::_matLabel = "elastic strain 2-D";

const PylithScalar pylith::feassemble::ElasticityExplicitGravData2DLinear::_dt =   1.00000000e-02;

const PylithScalar pylith::feassemble::ElasticityExplicitGravData2DLinear::_dtStableExplicit =   1.50923086e-04;

const PylithScalar pylith::feassemble::ElasticityExplicitGravData2DLinear::_gravityVec[] = {
  0.00000000e+00, -1.00000000e+08,
};

const PylithScalar pylith::feassemble::ElasticityExplicitGravData2DLinear::_vertices[] = {
  2.00000000e-01, -4.00000000e-01,
  3.00000000e-01,  5.00000000e-01,
 -1.00000000e+00, -2.00000000e-01,
};

const int pylith::feassemble::ElasticityExplicitGravData2DLinear::_cells[] = {
0,1,2,
};

const PylithScalar pylith::feassemble::ElasticityExplicitGravData2DLinear::_verticesRef[] = {
 -1.00000000e+00, -1.00000000e+00,
  1.00000000e+00, -1.00000000e+00,
 -1.00000000e+00,  1.00000000e+00,
};

const PylithScalar pylith::feassemble::ElasticityExplicitGravData2DLinear::_quadPts[] = {
 -3.33333333e-01, -3.33333333e-01,
};

const PylithScalar pylith::feassemble::ElasticityExplicitGravData2DLinear::_quadWts[] = {
  2.00000000e+00,
};

const PylithScalar pylith::feassemble::ElasticityExplicitGravData2DLinear::_basis[] = {
  3.33333333e-01,  3.33333333e-01,
  3.33333333e-01,};

const PylithScalar pylith::feassemble::ElasticityExplicitGravData2DLinear::_basisDerivRef[] = {
 -5.00000000e-01, -5.00000000e-01,
  5.00000000e-01,  0.00000000e+00,
  0.00000000e+00,  5.00000000e-01,
};

const PylithScalar pylith::feassemble::ElasticityExplicitGravData2DLinear::_fieldTIncr[] = {
  1.30000000e+00, -9.00000000e-01,
  1.40000000e+00,  1.50000000e+00,
  5.00000000e-01, -9.00000000e-01,
};

const PylithScalar pylith::feassemble::ElasticityExplicitGravData2DLinear::_fieldT[] = {
  1.60000000e+00, -8.00000000e-01,
  9.00000000e-01,  7.00000000e-01,
 -2.00000000e-01, -1.10000000e+00,
};

const PylithScalar pylith::feassemble::ElasticityExplicitGravData2DLinear::_fieldTmdt[] = {
  8.00000000e-01,  1.00000000e-01,
  5.00000000e-01,  3.00000000e-01,
 -1.00000000e-01, -6.00000000e-01,
};

const PylithScalar pylith::feassemble::ElasticityExplicitGravData2DLinear::_valsResidual[] = {
 -7.10095578e+10,  9.10600148e+10,
 -1.02829242e+10, -1.66809658e+11,
  8.12828570e+10, -6.17535647e+10,
};

const PylithScalar pylith::feassemble::ElasticityExplicitGravData2DLinear::_valsJacobian[] = {
  1.52777778e+06,  0.00000000e+00,
  1.52777778e+06,  0.00000000e+00,
  1.52777778e+06,  0.00000000e+00,
  0.00000000e+00,  1.52777778e+06,
  0.00000000e+00,  1.52777778e+06,
  0.00000000e+00,  1.52777778e+06,
  1.52777778e+06,  0.00000000e+00,
  1.52777778e+06,  0.00000000e+00,
  1.52777778e+06,  0.00000000e+00,
  0.00000000e+00,  1.52777778e+06,
  0.00000000e+00,  1.52777778e+06,
  0.00000000e+00,  1.52777778e+06,
  1.52777778e+06,  0.00000000e+00,
  1.52777778e+06,  0.00000000e+00,
  1.52777778e+06,  0.00000000e+00,
  0.00000000e+00,  1.52777778e+06,
  0.00000000e+00,  1.52777778e+06,
  0.00000000e+00,  1.52777778e+06,
};

const PylithScalar pylith::feassemble::ElasticityExplicitGravData2DLinear::_valsResidualLumped[] = {
 -7.10086411e+10,  9.10610843e+10,
 -1.02842992e+10, -1.66813631e+11,
  8.12833153e+10, -6.17506619e+10,
};

const PylithScalar pylith::feassemble::ElasticityExplicitGravData2DLinear::_valsJacobianLumped[] = {
  4.58333333e+06,  4.58333333e+06,
  4.58333333e+06,  4.58333333e+06,
  4.58333333e+06,  4.58333333e+06,
};

pylith::feassemble::ElasticityExplicitGravData2DLinear::ElasticityExplicitGravData2DLinear(void)
{ // constructor
  spaceDim = _spaceDim;
  cellDim = _cellDim;
  numVertices = _numVertices;
  numCells = _numCells;
  numBasis = _numBasis;
  numQuadPts = _numQuadPts;
  matType = const_cast<char*>(_matType);
  matDBFilename = const_cast<char*>(_matDBFilename);
  matId = _matId;
  matLabel = const_cast<char*>(_matLabel);
  dt = _dt;
  dtStableExplicit = _dtStableExplicit;
  gravityVec = const_cast<PylithScalar*>(_gravityVec);
  vertices = const_cast<PylithScalar*>(_vertices);
  cells = const_cast<int*>(_cells);
  verticesRef = const_cast<PylithScalar*>(_verticesRef);
  quadPts = const_cast<PylithScalar*>(_quadPts);
  quadWts = const_cast<PylithScalar*>(_quadWts);
  basis = const_cast<PylithScalar*>(_basis);
  basisDerivRef = const_cast<PylithScalar*>(_basisDerivRef);
  fieldTIncr = const_cast<PylithScalar*>(_fieldTIncr);
  fieldT = const_cast<PylithScalar*>(_fieldT);
  fieldTmdt = const_cast<PylithScalar*>(_fieldTmdt);
  valsResidual = const_cast<PylithScalar*>(_valsResidual);
  valsJacobian = const_cast<PylithScalar*>(_valsJacobian);
  valsResidualLumped = const_cast<PylithScalar*>(_valsResidualLumped);
  valsJacobianLumped = const_cast<PylithScalar*>(_valsJacobianLumped);
} // constructor

pylith::feassemble::ElasticityExplicitGravData2DLinear::~ElasticityExplicitGravData2DLinear(void)
{}


// End of file
