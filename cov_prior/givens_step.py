from fast_givens import fg
import pymc as pm
import numpy as np
from ortho_basis import OrthogonalBasis

__all__ = ['fast_givens', 'GivensStepper']

def fast_givens(o,i,j,t):
    "Givens rotates the matrix o."
    ro = o.copy(order='F')
    fg(ro,i,j,t)
    return ro
    
class GivensStepper(pm.Metropolis):
    """docstring for GivensStepper"""
    def __init__(self, o, kappa):
        pm.Metropolis.__init__(self, o)
        self.o = o
        self.adaptive_scale_factor = 1./kappa
        
    def propose(self):
        t_p = pm.rvon_mises(0, 1./self.adaptive_scale_factor)
        i_p, j_p = np.random.randint(self.o.n, size=2)
        
        self.o.value = fast_givens(self.o.value, i_p, j_p, t_p)
        
    @staticmethod
    def competence(o):
        if isinstance(o, OrthogonalBasis):
            return 3
        else:
            return 0