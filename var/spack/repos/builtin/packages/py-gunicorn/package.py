# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyGunicorn(PythonPackage):
    """Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a 
    pre-fork worker model. The Gunicorn server is broadly compatible with 
    various web frameworks, simply implemented, light on server resources, and 
    fairly speedy."""

    homepage = "https://gunicorn.org/"
    url      = "https://pypi.io/packages/source/g/gunicorn/gunicorn-20.0.4.tar.gz"

    version('20.0.4', sha256='1904bb2b8a43658807108d59c3f3d56c2b6121a701161de0ddf9ad140073c626')

    depends_on('python@3.4:', type='build')
    depends_on('py-setuptools@3:', type='build')
