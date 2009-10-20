import numpy as np
from numpy.testing import *
from givens_step import *
from ortho_basis import *
import nose
import pymc as pm
import pylab as pl
from scipy import stats

__all__ = ['test']

class TestStep(TestCase):
    
    def test_assignment(self):
        o,c=covariance('c',pm.Gamma('v',3,3,size=2))
        M = pm.MCMC([o])
        M.assign_step_methods()
        assert(isinstance(M.step_method_dict[o][0],GivensStepper))
        
    def test_step(self):
        o,c = covariance('c',pm.Gamma('v',3,3,size=2))
        M = pm.MCMC([o])
        M.sample(10000,1000)
        theta1=(np.arctan2(M.trace('c_eigenvalues')[:][:,0,0],M.trace('c_eigenvalues')[:][:,0,1])+np.pi)/2./np.pi
        theta2 =(np.arctan2(M.trace('c_eigenvalues')[:][:,1,0],M.trace('c_eigenvalues')[:][:,1,1])+np.pi)/2./np.pi
        
        d1,p1 = stats.kstest(theta1,'uniform')
        d2,p2 = stats.kstest(theta2,'uniform')
        
        assert(p1>.05)
        assert(p2>.05)
        
        
        
# def test():
if __name__ == '__main__':
    C =nose.config.Config(verbosity=1)
    nose.runmodule(config=C)