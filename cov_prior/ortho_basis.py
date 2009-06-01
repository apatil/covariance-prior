import pymc as pm
import numpy as np

__all__ = ['OrthogonalBasis','check_orthogonality','covariance']

class OrthogonalBasis(pm.Uninformative):
    "An orthogonal basis, stored in the columns of a matrix."
    def __init__(self, name, n, *args, **kwargs):
        pm.Uninformative.__init__(self, name, np.array(np.eye(n), order='F'), *args, **kwargs)

def check_orthogonality(o, tol=1e-10):
    """
    Returns 0 if the matrix is orthogonal (up to tolerance), 
    -inf if it is not. You can use this in potentials.
    """
    if np.abs(np.dot(o,o.T) - np.eye(o.shape[0])).max() > tol:
        return -np.inf
    else:
        return 0

def ev_to_cov(o,v):
    return np.dot(o*v,o.T)

def covariance(name, v, o=None, doc="A covariance matrix", *args, **kwds):
    """Deterministic converting a vector of eigenvalues and 
    an orthogonal basis to a covariance matrix."""
    
    if o is None:
        o = OrthogonalBasis(name + '_eigenvalues', len(v.value))
    c = pm.Deterministic(eval=ev_to_cov,
                name=name, parents={'o': o, 'v': v},
                doc=doc, *args, **kwds)
    return v,o,c
        