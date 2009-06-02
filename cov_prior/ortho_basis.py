# Author: Anand Patil
# Date: 2 June 2009
# License: Creative Commons BY-NC-SA
####################################

import pymc as pm
import numpy as np

__all__ = ['OrthogonalBasis','check_orthogonality','covariance']

def check_orthogonality(value, tol=1e-10):
    """
    Returns 0 if the matrix is orthogonal (up to tolerance), 
    -inf if it is not. You can use this in potentials.
    """
    if np.abs(np.dot(value,value.T) - np.eye(value.shape[0])).max() > tol:
        return -np.inf
    else:
        return 0

class OrthogonalBasis(pm.Stochastic):
    "An orthogonal basis, stored in the columns of a matrix."
    def __init__(self, name, n, constrain=True, *args, **kwargs):
        self.n = n
        if constrain:
            lpf = check_orthogonality
        else:
            lpf = lambda value: 0
        pm.Stochastic.__init__(self, lpf, 'An orthonormal basis', name, {}, dtype=np.dtype('float'), value=np.array(np.eye(n),order='F'), *args, **kwargs)

def ev_to_cov(o,v):
    return np.dot(o*v,o.T)

def covariance(name, v, o=None, doc="A covariance matrix", constrain=True, *args, **kwds):
    """
    Deterministic converting a vector of eigenvalues and an 
    orthogonal basis to a covariance matrix. If with_potential,
    also returns a potential enforcing orthogonality.
    """
    
    if o is None:
        o = OrthogonalBasis(name + '_eigenvalues', len(v.value), constrain=constrain)
    c = pm.Deterministic(eval=ev_to_cov,
                name=name, parents={'o': o, 'v': v},
                doc=doc, *args, **kwds)
    return o,c