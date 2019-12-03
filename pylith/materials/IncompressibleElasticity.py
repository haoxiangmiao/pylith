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
# @file pylith/materials/IncompressibleElasticity.py
#
# @brief Python object for solving the elasticity equation with an incompressible material.
#
# Factory: material

from .Material import Material
from .materials import IncompressibleElasticity as ModuleIncompressibleElasticity

from .IsotropicLinearIncompElasticity import IsotropicLinearIncompElasticity


class IncompressibleElasticity(Material, ModuleIncompressibleElasticity):
    """
    Python material property manager.

    INVENTORY

    Properties
      - *use_body_force* Include body force term in elasticity equation.

    Facilities
      - *bulk_rheology* Bulk rheology for incompessible elastic material.

    FACTORY: material
    """

    import pyre.inventory

    from pylith.topology.Subfield import subfieldFactory
    from .AuxSubfieldsElasticity import AuxSubfieldsElasticity
    auxiliarySubfields = pyre.inventory.facilityArray(
        "auxiliary_subfields", itemFactory=subfieldFactory, factory=AuxSubfieldsElasticity)
    auxiliarySubfields.meta['tip'] = "Discretization of incompressible elasticity properties."

    from .DerivedSubfieldsElasticity import DerivedSubfieldsElasticity
    derivedSubfields = pyre.inventory.facilityArray(
        "derived_subfields", itemFactory=subfieldFactory, factory=DerivedSubfieldsElasticity)
    derivedSubfields.meta['tip'] = "Discretization of derived subfields (e.g., stress and strain)."

    useBodyForce = pyre.inventory.bool("use_body_force", default=False)
    useBodyForce.meta['tip'] = "Include body force term in elasticity equation."

    rheology = pyre.inventory.facility(
        "bulk_rheology", family="incompressible_elasticity_rheology", factory=IsotropicLinearIncompElasticity)
    rheology.meta['tip'] = "Bulk rheology for elastic material."

    # PUBLIC METHODS /////////////////////////////////////////////////////

    def __init__(self, name="incompressibleelasticity"):
        """
        Constructor.
        """
        Material.__init__(self, name)
        return

    def preinitialize(self, problem):
        """
        Setup material.
        """
        self.rheology.preinitialize(problem)
        Material.preinitialize(self, problem)

        self.rheology.addAuxiliarySubfields(self, problem)

        ModuleIncompressibleElasticity.useBodyForce(self, self.useBodyForce)
        return

    def _createModuleObj(self):
        """
        Create handle to C++ IncompressibleElasticity.
        """
        ModuleIncompressibleElasticity.__init__(self)
        ModuleIncompressibleElasticity.setBulkRheology(self, self.rheology)  # Material sets auxiliary db in rheology.
        return


# Factories

def material():
    """
    Factory associated with IncompressibleElasticity.
    """
    return IncompressibleElasticity()


# End of file
