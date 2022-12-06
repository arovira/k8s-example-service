Quickstart
----------

Then run the following commands to bootstrap your environment with ``poetry``::

   git clone https://github.com/arovira/fastapi-k8s-example-app
   cd fastapi-k8s-example-app
   poetry install
   poetry shell

To run the web application in debug use::

   uvicorn app.main:app --reload

Application will be available on `localhost <http://localhost:8000/docs>`_ in your browser.


Run tests
---------

Tests for this project are defined in the ``tests/`` folder.

This project uses `pytest <https://docs.pytest.org/>`_ to define tests because it allows you to use the ``assert`` keyword with good formatting for failed assertations.

To run all the tests of a project, simply run the ``pytest`` command:
::
   $ pytest
   ================================================= test session starts =================================================
   platform darwin -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0
   rootdir: /xxxxx/fastapi-k8s-example-app
   plugins: anyio-3.6.2
   collected 2 items

   src/tests/test_main.py ..                                                                                        [100%]

   ================================================== 2 passed in 3.94s ==================================================
   $


If you want to run a specific test, you can do this with `this <https://docs.pytest.org/en/latest/usage.html#specifying-tests-selecting-tests>`_ pytest feature:
::
   $ pytest src/tests/test_main.py


Local deployment with Docker Compose
------------------------------------

You must have ``docker`` and ``docker-compose`` tools installed to work with material in this section.
Then just run:
::
   $ docker-compose up --build

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


Helm deployment to k8s
----------------------

In order to deploy to kubernetes, the service image needs to be available on an image repository
Since this example uses AWS resources, we will create the ECR repository.

First step is to define some variables we will use related to your AWS account:
::
   export TF_VAR_aws_region=<change to your region>
   export TF_VAR_aws_profile=<change to your aws_profile>
   export TF_VAR_aws_account_id=<change to your aws_profile>

Execute the following to create it:
::
   cd deploy/terraform/environment
   terraform init
   terraform apply

Note this uses a terraform module developed on `git@github.com:arovira/tfm-aws-ecr-repository.git <https://github.com/arovira/tfm-aws-ecr-repository>`_

Then get the ECR repo name:
::
   export $(terraform output | sed 's/ //g')

Then, go back to the root of the project and build the image (you need docker to do so):
::
   cd ../..
   docker build . --tag fastapi-k8s-example-image

Then, authenticate on the ECR repo and push the image:
::
   aws_ecr_base=${TF_VAR_aws_account_id}.dkr.ecr.${TF_VAR_aws_region}.amazonaws.com
   aws ecr get-login-password --region $TF_VAR_aws_region --profile ${TF_VAR_aws_profile} | docker login --username AWS --password-stdin ${aws_ecr_base}
   docker tag fastapi-k8s-example-image ${aws_ecr_base}/fastapi-k8s-example-app:0.1.0
   docker push ${aws_ecr_base}/fastapi-k8s-example-app:latest

Then set your kubernetes context and install via helm:
::
   helm upgrade --install fastapi-example deploy/helm/fastapi-k8s-example-app --set image.repository=${aws_ecr_base}/fastapi-k8s-example-app

If ingress is not enabled, you can access the application with on localhost:8888 after:
::
   kubectl port-forward svc/fastapi-example-fastapi-k8s-example-app 8888:80