# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyFlaskPaginate(PythonPackage):
    """Simple paginate for flask (study from will_paginate). Use bootstrap css
    framework, supports bootstrap2&3 and foundation."""

    homepage = "https://pythonhosted.org/Flask-paginate/"
    git      = "https://github.com/lixxu/flask-paginate"

    version('0.5.4', tag='0.5.4')

    depends_on('py-setuptools', type='build')
    depends_on('py-flask@0.9:', type=('build', 'run'))

