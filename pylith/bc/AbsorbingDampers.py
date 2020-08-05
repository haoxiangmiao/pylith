# ----------------------------------------------------------------------
#
# Brad T. Aagaard, U.S. Geological Survey
# Charles A. Williams, GNS Science
# Matthew G. Knepley, University of Chicago
#
# This code was developed as part of the Computational Infrastructure
# for Geodynamics (http://geodynamics.org).
#
# Copyright (c) 2010-2016 University of California, Davis
#
# See COPYING for license information.
#
# ----------------------------------------------------------------------
#
# @file pylith/bc/AbsorbingDampers.py
#
# @brief Python object for managing absorbing dampers boundary condition.
#
# Factory: boundary_condition

from pylith.bc.BoundaryCondition import BoundaryCondition
from .bc import AbsorbingDampers as ModuleAbsorbingDampers


class AbsorbingDampers(BoundaryCondition, ModuleAbsorbingDampers):
    """
    Python object for managing absorbing dampers condition.

    INVENTORY

    Properties
      - None

    Facilities
      - *auxiliary_subfields* Discretization of time-dependent Neumann parameters.

    FACTORY: boundary_condition
    """

    import pyre.inventory

    from .AuxSubfieldsAbsorbingDampers import AuxSubfieldsAbsorbingDampers
    from pylith.topology.Subfield import subfieldFactory
    auxiliarySubfields = pyre.inventory.facilityArray(
        "auxiliary_subfields", itemFactory=subfieldFactory, factory=AuxSubfieldsAbsorbingDampers)
    auxiliarySubfields.meta['tip'] = "Discretization of absorbing dampers parameters."

    # PUBLIC METHODS /////////////////////////////////////////////////////

    def __init__(self, name="absorbingdampers"):
        """
        Constructor.
        """
        BoundaryCondition.__init__(self, name)
        return

    def preinitialize(self, problem):
        """
        Do pre-initialization setup.
        """
        BoundaryCondition.preinitialize(self, problem)
        return

    # PRIVATE METHODS ////////////////////////////////////////////////////

    def _configure(self):
        """
        Setup members using inventory.
        """
        BoundaryCondition._configure(self)
        return

    def _createModuleObj(self):
        """
        Create handle to corresponding C++ object.
        """
        ModuleAbsorbingDampers.__init__(self)
        return


# Factories

def boundary_condition():
    """
    Factory associated with AbsorbingDampers.
    """
    return AbsorbingDampers()


# End of file
