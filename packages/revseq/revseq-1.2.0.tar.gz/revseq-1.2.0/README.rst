revseq
==========

A simple script to generate the (reverse) (complement) of a sequence

|Status| |Python Version| |License|

|Tests| |Codecov|

|pre-commit| |Black|

|Repobeats analytics image|

.. |Status| image:: https://img.shields.io/pypi/status/revseq.svg
   :target: https://pypi.org/project/revseq/
   :alt: Status
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/revseq
   :target: https://pypi.org/project/revseq
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/revseq
   :target: https://opensource.org/licenses/GPL-3.0
   :alt: License
.. |Tests| image:: https://github.com/milescsmith/revseq/actions/workflows/python-package.yml/badge.svg
   :target: https://github.com/milescsmith/revseq/actions?workflow=python-package
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/milescsmith/revseq/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/milescsmith/revseq
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black
.. |Repobeats analytics image| image:: https://repobeats.axiom.co/api/embed/6349b1047335304b1f73d5d1c0d0fb1ab74ee6e8.svg
   :target: https://repobeats.axiom.co
   :alt: Repobeats analytics image



Requirements
------------

* Python 3.10 or higher
* typer
* icontract
* rich
* typeguard


Installation
------------

You can install *revseq* via pip_:

.. code:: console

   $ pip install revseq

or the latest development version from `Github <https://github.com/milescsmith/revseq/>`_:

.. code:: console

   $ pip install git+https://github.com/milescsmith/revseq



Usage
-----

By default, the reverse complement is returned.

.. code:: console

   revseq "aaggctt"

Alternatively, can use within another module or the Python REPL

.. code:: console

    from revseq import revseq

    revseq("aaggctt", rev=True, comp=True)


Contributing
------------

Contributions are very welcome.
To learn more, see the `Contributor Guide`_.


License
-------

Distributed under the terms of the `GPL 3.0 license`_,
*revseq* is free and open source software.


Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.


Credits
-------

.. _GPL 3.0 license: https://opensource.org/licenses/GPL-3.0
.. _file an issue: https://github.com/milescsmith/revseq/issues
.. _pip: https://pip.pypa.io/
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
