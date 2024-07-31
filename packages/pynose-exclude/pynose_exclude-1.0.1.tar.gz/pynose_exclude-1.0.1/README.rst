Overview
========

pynose-exclude is a `Pynose`_ plugin that allows you to easily specify
directories to be excluded from testing.

.. _Pynose: https://github.com/mdmintz/pynose


Exclude Directories
===================

The ``--exclude-dir=`` option is made available after installation of the
plugin. The option may be used multiple times to exclude multiple directories 
from testing. The directory paths provided may be absolute or relative.

Example::

    $ pynose --exclude-dir=test_dirs/build \
        --exclude-dir=test_dirs/test_not_me test_dirs
    ....
    ----------------------------------------------------------------------
    Ran 4 tests in 0.006s

    OK

This example will exclude the directories test_dirs/build and
test_dirs/test_not_me from pynose' test searching.

Using File-Based Exclusion List
-------------------------------

The ``--exclude-dir-file=`` option can be used to pass in a predefined
list of directories contained within a file. ``pynose-exclude`` expects each
directory to be excluded to be on its own line.

Example::

    $ pynose --exclude-dir-file=test_dirs/exclude_dirs.txt \
        test_dirs
    ....
    ----------------------------------------------------------------------
    Ran 4 tests in 0.006s

    OK

where ``exclude_dirs.txt`` might look like: ::

    test_dirs/build
    # Start a line with a '#' to include
    # Comments
    test_dirs/test_not_me


Excluding Specific Test Methods and Classes
-------------------------------------------

Tests can now be excluded by specifying their fully qualified test paths.
Tests can be excluded using either ``--exclude-test`` or ``--exclude-test-file``.

To exclude test methods:

``--exclude-test=module1.module2.TestClass.test_method``

To exclude test classes:

``--exclude-test=module1.module2.TestClass``

To exclude test functions:

``--exclude-test=module1.module2.test_function``


Using Environment Variables
---------------------------

``--exclude-dir=`` and ``--exclude-test=`` can be set by the environment
variables ``PYNOSE_EXCLUDE_DIRS`` and ``PYNOSE_EXCLUDE_TESTS`` respectively.
Multiple exclude paths may be entered by separating them using a ``;``. The
environment variable ``PYNOSE_EXCLUDE_DIRS_FILE`` when set to the path of a
file-based exclusion list functions as though it were passed in with
``--exclude-dir-file=``.

Pynose Configuration Files
==========================

``pynose-exclude`` options can also be passed to ``pynose`` using a ``.pynoserc`` or ``pynose.cfg`` file. If you more than one directory are to be excluded
separate their values with newlines using the same configuration key: ::

    [nosetests]
    exclude-dir=test_dirs/exclude_dirs
                test_dirs/more_excludes



Bugs
====
Please report all bugs (and patches) to https://github.com/nyefan/pynose-exclude/

NOTE: The previous bitbucket repository is no longer actively maintained.
