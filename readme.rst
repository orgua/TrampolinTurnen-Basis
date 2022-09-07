Einführung ins TrampolinTurnen
==============================

[![pages-deployment](https://github.com/orgua/TrampolinTurnen-Basis/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/orgua/TrampolinTurnen-Basis/actions/workflows/pages/pages-build-deployment)

`Inhalt als Webseite 📱 <https://orgua.github.io/TrampolinTurnen-Basis/>`_

`Inhalt als PDF 📄 -> TODO <https://github.com/orgua/TrampolinTurnen-Basis/releases>`_

`Inhalt als reStructuredText 💻 <https://github.com/orgua/TrampolinTurnen-Basis/tree/main/docs/content>`_

Installation
--------------

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


In browser go to `localhost:8000`_ to view the documentation.

Generating a PDF
----------------

Install for Ubuntu / Debian, following `Sphinx.LaTeXBuilder <https://www.sphinx-doc.org/en/master/usage/builders/index.html#sphinx.builders.latex.LaTeXBuilder>`_

.. code-block:: bash

    sudo apt install texlive-latex-recommended
    sudo apt install texlive-fonts-recommended
    sudo apt install texlive-latex-extra
    sudo apt install tex-gyre latexmk
    sudo apt install texlive-lang-german

Generating the PDF

.. code-block:: bash

    cd docs/
    make latex
    make latexpdf


Wie kann ich beitragen?
--------------------------------

Hilfe und Anmerkungen willkommen. Die Quellen befinden sich unter `docs/content` in Form von rst-Dateien.

- `Writing reStructuredText <https://www.writethedocs.org/guide/writing/reStructuredText/>`_
-

