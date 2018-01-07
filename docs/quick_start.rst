Quick Start Guide
=================


Download TaskBuster Django Project Boilerplate
----------------------------------------------

First, you need to download the BoilerPlate from GitHub.


Secret Django Key
-----------------

This boilerplate has the **DJANGO_KEY** setting variable hidden.

You can generate your DJANGO_KEY |django_key|.

.. |django_key| raw:: html

    <a href="http://www.miniwebtool.com/django-secret-key-generator"
    target="_blank">here</a>


Project Name
------------

This project is named *TaskBuster*, so if you are using this
Boilerplate to create your own project, you'll have to change
the name in a few places:

 - *taskbuster_project* **folder** (your top project container)
 - *taskbuster_project/taskbuster* **folder** (your project name)
 - virtual environment names: **tb_dev** and **tb_test** (name them whatever you want)
 - in virtual environments **postactivate** files (see section below), you have to change **taskbuster.settings.development** for your **projectname.settings.development**. Same works for the testing environment.


Virtual environments and Settings Files
---------------------------------------

First, you must know your Python 3 path::

    $ which python3

which is something similar to /usr/local/bin/python3.

Next, create a Development virtual environment with Python 3 installed::

    $ mkvirtualenv --python=/usr/local/bin/python3 tb_dev

where you might need to change it with your python path.

Go to the virtual enviornment folder with::

    $ cd $VIRTUAL_ENV/bin

and edit the postactivate file.:

    $ vi postactivate

You must add the lines: ::

    export DJANGO_SETTINGS_MODULE="taskbuster.settings.development"
    export SECRET_KEY="your_secret_django_key"

with your project name and your own secret key.

Next, edit the **predeactivate** file and add the line::

    unset SECRET_KEY

Repeat the last steps for your testing environment::

    $ mkvirtualenv --python=/usr/local/bin/python3 tb_test
    $ cd $VIRTUAL_ENV/bin
    $ vi postactivate

where you have to add the lines::

    export DJANGO_SETTINGS_MODULE="taskbuster.settings.testing"
    export SECRET_KEY="your_secret_django_key"

and in the predeactivate file::

    unset SECRET_KEY

Next, install the packages in each environment::

    $ workon tb_dev
    $ pip install -r requirements/development.txt
    $ workon tb_test
    $ pip install -r requirements/testing.txt