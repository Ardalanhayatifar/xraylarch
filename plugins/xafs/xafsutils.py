"""
Utility functions used for xafs analysis
"""
import numpy as np
from larch import Group
import scipy.constants as consts
KTOE = 1.e20*consts.hbar**2 / (2*consts.m_e * consts.e) # 3.8099819442818976
ETOK = 1.0/KTOE

def etok(energy):
    """convert photo-electron energy to wavenumber"""
    return np.sqrt(energy/KTOE)

def ktoe(k):
    """convert photo-electron wavenumber to energy"""
    return k*k*KTOE


def set_xafsGroup(group, _larch=None):
    """set _sys.xafsGroup to the supplied group (if not None)

    return _sys.xafsGroup.

    if needed, a new, empty _sys.xafsGroup may be created.
    """
    if group is None:
        if not hasattr(_larch.symtable._sys, 'xafsGroup'):
            _larch.symtable._sys.xafsGroup = Group()
    else:
        _larch.symtable._sys.xafsGroup = group
    return _larch.symtable._sys.xafsGroup


def registerLarchPlugin():
    return ('_xafs', {'etok': etok, 'ktoe': ktoe})
