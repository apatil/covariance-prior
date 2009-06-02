:Date: 2 June 2009
:Author: Anand Patil
:Contact: anand.prabhakar.patil@gmail.com
:Web site: github.com/onyin/covariance-prior
:Copyright: Anand Patil, 2009.
:License: MIT License, see LICENSE


This package provides a convenient prior for covariance matrices in PyMC. To use it,
do the following::

    c,o = covariance(name, v)
    
where ``v`` is any vector-valued variable whose elements will always be positive.
``o`` will be an ``OrthogonalBasis`` object and ``c`` will be a deterministic
returning a covariance matrix whose eigenvalues are ``v`` and whose eigenvectors
are ``c``.

``OrthogonalBasis`` objects are matrix-valued stochastics whose columns form an
orthonormal basis, but which are otherwise indifferent to their values. They are 
handled by ``GivensStepper`` step methods, which propose Givens rotations in
randomly-selected planes.

By default, ``OrthogonalBasis`` objects' logp functions enforce orthogonality. You
can skip this check for speed if you like by setting ``constrain=False``.