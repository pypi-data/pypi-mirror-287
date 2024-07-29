Release 2.0.0 (2024-07-28)
==========================

* Adopt Ruff
* Tighten MyPy settings
* Update GitHub actions versions

Release 1.1.10 (2024-01-13)
===========================

* Remove Sphinx as a required dependency, as circular dependencies may cause
  failure with package managers that expect a directed acyclic graph (DAG)
  of dependencies.

Release 1.1.9 (2023-08-20)
==========================

* Serialise context["script_files"] and context["css_files"] as their filenames
  on Sphinx 7.2.0.

Release 1.1.8 (2023-08-14)
==========================

* Use ``os.PathLike`` over ``pathlib.Path``

Release 1.1.7 (2023-08-09)
==========================

* Fix tests for Sphinx 7.1 and below

Release 1.1.6 (2023-08-07)
==========================

* Drop support for Python 3.5, 3.6, 3.7, and 3.8
* Raise minimum required Sphinx version to 5.0

Release 1.1.5 (2021-05-23)
==========================

* Remove deprecation warnings for Sphinx-3.x

Release 1.1.4 (2020-02-29)
==========================

* Fix package metadata has broken

Release 1.1.3 (2019-04-05)
==========================

* Fix #6245: circular import error

Release 1.1.1 (2019-02-17)
==========================

* Fix failed to load HTML extension

Release 1.1.0 (2019-02-17)
==========================

* Add ``JSONHTMLBuilder`` and ``PickleHTMLBuilder`` (copied from sphinx package)

Release 1.0.0 (2019-02-17)
==========================

* Initial release (copied from sphinx package)
