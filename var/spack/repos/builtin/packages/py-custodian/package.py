# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyCustodian(PythonPackage):
    """Custodian is a simple, robust and flexible just-in-time (JIT) job management 
       framework written in Python."""

    homepage = "https://materialsproject.github.io/custodian"
    url      = "https://pypi.io/packages/source/c/custodian/custodian-2019.9.23.tar.gz"
    git      = "https://github.com/materialsproject/custodian"

    version('2019.9.23', sha256='ba1ebb17c524fb502f42382d363d2f20ea09eef63ccabea810a4c31349bd7d89')
    version('master', branch='master')

    depends_on('py-monty@3.0.2:', type=('run'))
    depends_on('py-ruamel-yaml@0.16.5:', type=('run'))
    depends_on('py-sentry-sdk@0.13.5:', type=('run'))
