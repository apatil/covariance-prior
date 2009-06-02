from fast_givens import fg
import pymc as pm
import numpy as np
from ortho_basis import OrthogonalBasis

__all__ = ['fast_givens', 'GivensStepper']

def fast_givens(o,i,j,t):
    "Givens rotates the matrix o."
    if i==j:
        raise ValueError, 'i must be different from j.'
    oc = o.copy('F')
    fg(o,oc,i+1,j+1,t)
    return oc
    
class GivensStepper(pm.Metropolis):
    """docstring for GivensStepper"""
    def __init__(self, o, kappa=1.):
        pm.Metropolis.__init__(self, o)
        self.o = o
        self.adaptive_scale_factor = 1./kappa
        
    def propose(self):
        t_p = pm.rvon_mises(0, 1./self.adaptive_scale_factor)
        i_p = np.random.randint(self.o.n-1)
        j_p = np.random.randint(i_p+1, self.o.n)
        
        self.o.value = fast_givens(self.o.value, i_p, j_p, t_p)
        
    def tune(self, *args, **kwargs):
        if self.adaptive_scale_factor>=1e6:
            return False
        else:
            return pm.Metropolis.tune(self, *args, **kwargs)
        
        
    @staticmethod
    def competence(o):
        if isinstance(o, OrthogonalBasis):
            if o.value.shape[0] > 1:
                return 3
            else:
                return 0
        else:
            return 0