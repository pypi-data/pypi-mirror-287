========================
ProBullStats Data Engine
========================

|Ruff| |Test Status| |PyPI Version|

This is the ``probullstats`` package.  An engine to pull data from the `ProBullStats website`_
so that it can be collated with other relevant data and put into a standard format. Then clients
can use that data for any analysis or research they wish to pursue.


---------
IMPORTANT
---------

Unfettered Data Access Requires a Subscription.

- This package does not grant the user with any rights to access the curated data in the `ProBullStats database`_.
- Full Data access requires a subscription_ level that grants the rights to generate and use API keys to
  access the site's data.  See the website's `terms and service`__.
- The author of this package is not affiliated with the `ProBullStats website`_.

__ subscription_


Installation
============

Install the package into you desired environment.

::

   $ python3 -m pip install probullstats
   $ probullstats --help

**NOTE**: If you install the package into a virtual environment, then the CLI will only be available when that environment is active.



.. _ProBullStats website: https://probullstats.com
.. _ProBullStats database: https://probullstats.com/statstats.php
.. _subscription: https://probullstats.com/terms.php
.. _UBCoTx github: https://github.com/ubcotx
.. _UBCoTx website: https://ubcotx.com/

.. |Ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff
.. |Test Status| image:: https://img.shields.io/github/actions/workflow/status/ubcotx/probullstats/ci-cd.yml?branch=main&label=Test%20Status&Logo=github
    :target: https://github.com/ubcotx/probullstats/actions/workflows/ci-cd.yml
    :alt: test-status
.. |PyPI Version| image:: https://img.shields/pypi/v/probullstats?label=PyPI&logo=pypi
    :target: https://pypi.org/project/probullstats/
    :alt: pypi
