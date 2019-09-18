# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPymatgen(PythonPackage):
    """Python Materials Genomics is a robust materials analysis code that
    defines core object representations for structures and molecules with
    support for many electronic structure codes. It is currently the core
    analysis code powering the Materials Project."""

    homepage = "http://www.pymatgen.org/"
    url      = "https://pypi.io/packages/source/p/pymatgen/pymatgen-4.7.2.tar.gz"

    version('2019.9.16', 'f994ec313b63607c8e596a3e683acdc4d0d708fc410a8b934154cb00e2485cb1')
    version('2019.6.20', '5612c2117c5ab751c6783a057ee53b40f52e90d379c2558f20f04f09dd9a72bc')
    version('4.7.2', '9c3a6e8608671c216e4ef89778646fd6')
    version('4.6.2', '508f77fdc3e783587348e93e4dfed1b8')

    extends('python', ignore='bin/tabulate')

    depends_on('py-setuptools@18.0:', type='build')

    after2019 = '@2019.6.20:'
    before2019 = '@:4.7.2'
    depends_on('python@3.3:3.7.9999',    type=('build', 'run'), when=after2019)
    depends_on('py-numpy@1.16.4:',       type=('build', 'run'), when=after2019)
    depends_on('py-numpy@1.9:',          type=('build', 'run'), when=before2019)
    depends_on('py-six',                 type=('build', 'run'))
    depends_on('py-requests',            type=('build', 'run'))
    depends_on('py-pyyaml@3.11:',        type=('build', 'run'))
    depends_on('py-monty@2.0.4:',        type=('build', 'run'), when=after2019)
    depends_on('py-monty@0.9.6:',        type=('build', 'run'), when=before2019)
    depends_on('py-scipy@1.2.1:',        type=('build', 'run'), when=after2019)
    depends_on('py-scipy@0.14:',         type=('build', 'run'), when=before2019)
    depends_on('py-pydispatcher@2.0.5:', type=('build', 'run'))
    depends_on('py-tabulate',            type=('build', 'run'))
    depends_on('py-spglib@1.12.2.post0:',type=('build', 'run'), when=after2019)
    depends_on('py-spglib@1.9.8.7:',     type=('build', 'run'), when=before2019)
    depends_on('py-matplotlib@3.1.0:',   type=('build', 'run'), when=after2019)
    depends_on('py-matplotlib@1.5:',     type=('build', 'run'), when=before2019)
    depends_on('py-palettable@3.1.1:',   type=('build', 'run'), when=after2019)
    depends_on('py-palettable@2.1.1:',   type=('build', 'run'), when=before2019)
    depends_on('py-networkx@2.2:',       type=('build', 'run'), when=after2019)
    depends_on('py-ruamel-yaml@0.15.97:',type=('build', 'run'), when=after2019)
    depends_on('py-pandas@0.24.2:',      type=('build', 'run'), when=after2019)
