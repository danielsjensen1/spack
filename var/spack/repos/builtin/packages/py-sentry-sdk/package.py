# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PySentrySdk(PythonPackage):
    """Sentry-Python is an SDK for Sentry.."""

    homepage = "https://docs.sentry.io/error-reporting/quickstart/?platform=python"
    url      = "https://pypi.io/packages/source/s/sentry-sdk/sentry-sdk-0.14.1.tar.gz"
    git      = "https://github.com/getsentry/sentry-python"

    version('0.14.1', sha256='e023da07cfbead3868e1e2ba994160517885a32dfd994fc455b118e37989479b')
    version('master', branch='master')

    # TODO: add optional dependencies: flask, bottle, falcon, django, sanic, 
    # celery, beam, rq, aiohttp, tornado, sqlalchemy, pyspark
    depends_on('py-setuptools', type='build')
