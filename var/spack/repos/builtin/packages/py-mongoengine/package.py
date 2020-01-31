# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMongoengine(PythonPackage):
    """MongoEngine is a Python Object-Document Mapper for working with MongoDB.."""

    homepage = "https://mongoengine-odm.readthedocs.io/"
    url      = "https://pypi.io/packages/source/m/mongoengine/mongoengine-0.19.1.tar.gz"
    git      = "https://github.com/MongoEngine/mongoengine"

    version('0.19.1', sha256='65f6cc48cbaac5ecd518dcec725d9c312286796510a9d93a4388a53811a294b9')

    depends_on('py-pymongo@3.4:', type=('run'))
    depends_on('py-six@1.10.0:', type=('build', 'run'))
    depends_on('py-sphinx@1.5.5:', type=('build', 'run'))
    depends_on('py-sphinx-rtd-theme@0.2.4:',  type=('build', 'run'))
