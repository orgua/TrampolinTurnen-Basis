Einführung ins TrampolinTurnen
==============================

Compiling this document needs Python 3 and a shell.
For installation:

.. code-block:: bash

    git clone ....

    pip3 install pipenv
    # pip3 install --upgrade pip pipenv wheel setuptools

    pipenv install

    pipenv shell

Compiling the document:

.. code-block:: bash

    cd docs
    sphinx-build -b html ./ _build/html
    # or ?
    make html

Viewing the document in a browser:

.. code-block:: bash

    cd _build/html
    python3 -m http.server


In browser go to `localhost:8000` to view the documentation.

Wie kann ich beitragen?
--------------------------------

Hilfe und Anmerkungen willkommen

