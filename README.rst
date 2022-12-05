.. image:: ./.github/assets/logo.png

|

.. image:: https://github.com/arovira/fastapi-k8s-example-app/workflows/API%20spec/badge.svg
   :target: https://github.com/arovira/fastapi-k8s-example-app

.. image:: https://github.com/arovira/fastapi-k8s-example-app/workflows/Tests/badge.svg
   :target: https://github.com/arovira/fastapi-k8s-example-app

.. image:: https://github.com/arovira/fastapi-k8s-example-app/workflows/Styles/badge.svg
   :target: https://github.com/arovira/fastapi-k8s-example-app

.. image:: https://codecov.io/gh/arovira/fastapi-k8s-example-app/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/arovira/fastapi-k8s-example-app

.. image:: https://img.shields.io/github/license/Naereen/StrapDown.js.svg
   :target: https://github.com/arovira/fastapi-k8s-example-app/blob/master/LICENSE

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black

.. image:: https://img.shields.io/badge/style-wemake-000000.svg
   :target: https://github.com/wemake-services/wemake-python-styleguide

----------


Quickstart
----------

Then run the following commands to bootstrap your environment with ``poetry``: ::

   git clone https://github.com/arovira/fastapi-k8s-example-app
   cd fastapi-k8s-example-app/src
   poetry install
   poetry shell

To run the web application in debug use::

   uvicorn app.main:app --reload

Application will be available on ``localhost`` in your browser.


Run tests
---------

Tests for this project are defined in the ``tests/`` folder.


This project uses `pytest
<https://docs.pytest.org/>`_ to define tests because it allows you to use the ``assert`` keyword with good formatting for failed assertations.


To run all the tests of a project, simply run the ``pytest`` command: ::

    
   $ pytest
   ================================================= test session starts =================================================
   platform darwin -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0
   rootdir: /Users/arnaurovira/Work/GitHub/fastapi-k8s-example-app
   plugins: anyio-3.6.2
   collected 2 items

   src/tests/test_main.py ..                                                                                        [100%]

   ================================================== 2 passed in 3.94s ==================================================
   $


If you want to run a specific test, you can do this with `this
<https://docs.pytest.org/en/latest/usage.html#specifying-tests-selecting-tests>`_ pytest feature: ::

   $ pytest src/tests/test_main.py

Deployment with Docker
----------------------

You must have ``docker`` and ``docker-compose`` tools installed to work with material in this section.
Then just run::

   docker-compose up --build

Application will be available on ``localhost`` in your browser.

Web routes
----------

All routes are available on ``/docs`` or ``/redoc`` paths with Swagger or ReDoc.


Project structure
-----------------

Files related to application are in the ``app`` or ``tests`` directories.
Application parts are:

::

   app
   ├── api
   │   └── api.py       - web routes.
   │   └── root.py      - web routes.
   ├── core
   │   └── config.py    - application configuration.
   │   └── events.py    - start/stop events.
   │   └── logging.py   - logging config.
   └── main.py          - FastAPI application creation and configuration.
   tests
   └── test_main.py     - basic pytests