# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PySpglib(PythonPackage):
    """Python bindings for C library for finding and handling
    crystal symmetries."""

    homepage = "http://atztogo.github.io/spglib/"
    url      = "https://pypi.io/packages/source/s/spglib/spglib-1.9.9.18.tar.gz"

    version('1.14.1.post0', '1823aa0a10c0cde0504c8dae8c0012591e5334fd38e21c3bf540dc0219a3b44e')
    version('1.12.2.post0', '15b02b74c0f06179bc3650c43a710a5200abbba387c6eda3105bfd9236041443')
    version('1.9.9.18', 'b8b46268d3aeada7b9b201b11882548f')

    # Most Python packages only require setuptools as a build dependency.
    # However, spglib requires setuptools during runtime as well.
    depends_on('py-setuptools@18.0:', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
