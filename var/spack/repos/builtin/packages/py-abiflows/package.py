# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyAbiflows(PythonPackage):
    """Abiflows provides fireworks workflows to run several kind of DFT/DFPT
       simulations with Abinit."""

    homepage = "http://abinit.github.io/abiflows"
    url      = "https://pypi.io/packages/source/a/abiflows/abipy-0.4.tar.gz"
#    git      = "https://github.com/abinit/abipy.git"
    git      = "https://github.com/danielsjensen1/abiflows"

    version('develop', branch='develop')
    version('efield-piezo', branch='develop')
    version('0.4', 'df5ea4232b8ac2b61a2fb983fe4593a2b8e77d649c58b567d6168970014c8704')

    depends_on('python@2.7:')

    depends_on('py-setuptools', type='build')

    depends_on('py-six',                 type=('build', 'run'))
    depends_on('py-numpy@1.9:',          type=('build', 'run'))
    depends_on('py-pymongo',             type=('build', 'run'))
    depends_on('py-prettytable',         type=('build', 'run'))
    depends_on('py-mongoengine',         type=('build', 'run'))
    depends_on('py-paramiko',            type=('build', 'run'))
    depends_on('py-fireworks',           type=('build', 'run'))
    depends_on('py-custodian',           type=('build', 'run'))
    depends_on('py-abipy@0.7.0:',        type=('build', 'run'))
