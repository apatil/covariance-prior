# Author: Anand Patil
# Date: 2 June 2009
# License: Creative Commons BY-NC-SA
####################################

from setuptools import setup
from numpy.distutils.misc_util import Configuration
config = Configuration('cov_prior',parent_package=None,top_path=None)

config.add_extension(name='fast_givens',sources=['cov_prior/fast_givens.f'])

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(  version="1.0",
            description="A convenient prior for covariance matrices.",
            author="Anand Patil", 
            author_email="anand.prabhakar.patil@gmail.com",
            packages = ["cov_prior"],
            license="MIT License",
            requires=['NumPy','PyMC'],
            **(config.todict()))