# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyFireworks(PythonPackage):
    """FireWorks stores, executes, and manages calculation workflows."""

    homepage = "https://materialsproject.github.io/fireworks"
    url      = "https://pypi.io/packages/source/f/fireworks/FireWorks-1.9.5.tar.gz"
    git      = "https://github.com/materialsproject/fireworks"

    version('1.9.5', sha256='441e1bfa70e2612173eb153421c6e240b2687c471e179458c88e32482afedf80')

    depends_on('py-ruamel-yaml@0.15.97:', type=('run'))
    depends_on('py-mongo@3.9.0:', type=('run'))
    depends_on('py-jinja2@2.10.3:', type='run')
    depends_on('py-six@1.13.0:',  type=('build', 'run'))
    depends_on('py-monty@3.0.2:', type=('run'))
    depends_on('py-python-dateutil@2.8.1:', type=('build', 'run'))
    depends_on('py-tabulate', type=('build', 'run'))
    depends_on('py-flask@1.1.1:', type=('build', 'run'))
    depends_on('py-flask-paginate@0.5.4:', type=('run'))
    depends_on('py-tqdm', type=('build', 'run'))
