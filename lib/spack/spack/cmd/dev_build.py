# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import shutil
import sys
import tempfile

import llnl.util.filesystem as fs
import llnl.util.tty as tty

import spack.config
import spack.cmd
import spack.cmd.common.arguments as arguments
import spack.repo

description = "developer build: build from code in current working directory"
section = "build"
level = "long"


def setup_parser(subparser):
    arguments.add_common_arguments(subparser, ['jobs'])
    subparser.add_argument(
        '-d', '--source-path', dest='source_path', default=None,
        help="path to source directory. defaults to the current directory")
    subparser.add_argument(
        '-s', '--stage-path', dest='stage_path', default=None,
        help="path to stage directory. defaults to a subdirectory of the "
        "current directory with the spec name")
    subparser.add_argument(
        '-i', '--ignore-dependencies', action='store_true', dest='ignore_deps',
        help="don't try to install dependencies of requested packages")
    arguments.add_common_arguments(subparser, ['no_checksum'])
    subparser.add_argument(
        '--keep-prefix', action='store_true',
        help="do not remove the install prefix if installation fails")
    subparser.add_argument(
        '--skip-patch', action='store_true',
        help="skip patching for the developer build")
    subparser.add_argument(
        '-q', '--quiet', action='store_true', dest='quiet',
        help="do not display verbose build output while installing")
    subparser.add_argument(
        '--drop-in', type=str, dest='shell', default=None,
        help="drop into a build environment in a new shell, e.g. bash, zsh")
    subparser.add_argument(
        '--test', default=None,
        choices=['root', 'all'],
        help="""If 'root' is chosen, run package tests during
installation for top-level packages (but skip tests for dependencies).
if 'all' is chosen, run package tests during installation for all
packages. If neither are chosen, don't run tests for any packages.""")
    arguments.add_common_arguments(subparser, ['spec'])

    stop_group = subparser.add_mutually_exclusive_group()
    stop_group.add_argument(
        '-b', '--before', type=str, dest='before', default=None,
        help="phase to stop before when installing (default None)")
    stop_group.add_argument(
        '-u', '--until', type=str, dest='until', default=None,
        help="phase to stop after when installing (default None)")

    cd_group = subparser.add_mutually_exclusive_group()
    arguments.add_common_arguments(cd_group, ['clean', 'dirty'])


def dev_build(self, args):
    if not args.spec:
        tty.die("spack dev-build requires a package spec argument.")

    specs = spack.cmd.parse_specs(args.spec)
    if len(specs) > 1:
        tty.die("spack dev-build only takes one spec.")

    spec = specs[0]
    if not spack.repo.path.exists(spec.name):
        tty.die("No package for '{0}' was found.".format(spec.name),
                "  Use `spack create` to create a new package")
    if not spec.versions.concrete:
        tty.die(
            "spack dev-build spec must have a single, concrete version. "
            "Did you forget a package version number?")

    source_path = args.source_path
    if source_path is None:
        source_path = os.getcwd()
    source_path = os.path.abspath(source_path)
    
    # Create a temporary staging directory in case the staging directory is a 
    # subdirectory of the source directory.
    tmpdir = tempfile.mkdtemp()
    spack_src = os.path.join(tmpdir, 'spack-src')
    fs.copy_tree(source_path, spack_src)
    
    stage_path = args.stage_path
    if stage_path is None:
        stage_name = dirname = 'spack-stage-%s' % spec.dag_hash(7)
        stage_path = os.path.join(os.getcwd(), stage_name)
    # TODO: possibly allow the user to forcefully overwrite an existing 
    # directory
    if os.path.isdir(stage_path):
#         raise RuntimeError('the stage-path directory %s already exists' 
#                            % stage_path)
        # It is actually useful to be able to rerun `dev-build` even if the
        # directory already exists.  For example, you've made changes, built
        # the code, and now want to install it.  Raising an error would be
        # annoying because you would have to wipe the build directory and 
        # rebuild everything.
        pass
    else:
        shutil.move(tmpdir, stage_path)
    
    # Forces the build to run out of the staging directory.
    spec.constrain('dev_path=%s' % stage_path)

    spec.concretize()
    package = spack.repo.get(spec)

    if package.installed:
        tty.error("Already installed in %s" % package.prefix)
        tty.msg("Uninstall or try adding a version suffix for this dev build.")
        sys.exit(1)

    # disable checksumming if requested
    if args.no_checksum:
        spack.config.set('config:checksum', False, scope='command_line')

    tests = False
    if args.test == 'all':
        tests = True
    elif args.test == 'root':
        tests = [spec.name for spec in specs]
    print(spec)
    package.do_install(
        tests=tests,
        make_jobs=args.jobs,
        keep_prefix=args.keep_prefix,
        install_deps=not args.ignore_deps,
        verbose=not args.quiet,
        dirty=args.dirty,
        stop_before=args.before,
        stop_at=args.until)

    # drop into the build environment of the package?
    if args.shell is not None:
        spack.build_environment.setup_package(package, dirty=False)
        os.execvp(args.shell, [args.shell])
