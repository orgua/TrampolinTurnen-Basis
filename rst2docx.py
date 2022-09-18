"""
A script that feeds the sphinx-rst-content into pandoc and generates a complete DocX

Note: pandoc must be installed via apt

pre-tests with other tools:

rstdoc  index.rst test.docx docx
rstdoc ./doc test.docx docx
rstdcx -I docs docs/index.rst test.docx docx
rstdcx --rest ./doco --rstrest

pandoc -o test.docx docs/index.rst

Things to also try with pandoc:

--file-scope
--toc
--toc-depth
--reference-doc=

"""
import os
from pathlib import Path

file_path = Path("./docs/content").absolute()
temp_path = Path("./docs/_build").absolute()

files = [
    "einleitung",
    "pflichten",
    "sicherheit",
    "gymnastik",
    "tuchgewoehnung",
    "spiele",
    "grundspruenge",
    "sprungverbindung",
    "materialien",
]

content = []
with open(temp_path / "content.rst", "w", encoding="utf-8") as fw:
    fw.seek(0)
    fw.truncate()

    for file in files:
        fw.write("\n\n")
        with open(file_path / (file + ".rst"), encoding="utf-8") as fd:
            content = fd.read()
            fw.write(content)


os.chdir(temp_path)
os.system(f"pandoc -o content.docx content.rst")
