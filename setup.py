from pathlib import Path
from setuptools import find_packages, setup


# Package meta-data.
NAME = "high-performance-python"
PACKAGE_NAME = "hp"
DESCRIPTION = "Source code for the series of notebooks on high performance python."
URL = "https://github.com/particle1331/high-performance-python"
EMAIL = "particle1331@gmail.com"
AUTHOR = "Ron Medina"
REQUIRES_PYTHON = ">=3.9.0,<3.10"
INSTALL_REQUIRES = []
LICENSE = "MIT"
TROVE_CLASSIFIERS = [
    # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.9",
]


# ==============================================
# The rest you shouldn't have to touch too much.

long_description = DESCRIPTION

# Load the package's VERSION file as a dictionary.
about = {}
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / PACKAGE_NAME
with open(PACKAGE_DIR / "VERSION") as f:
    _version = f.read().strip()
    about["__version__"] = _version

# Where the magic happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(),
    package_data={PACKAGE_NAME: ["VERSION"]},
    install_requires=INSTALL_REQUIRES,
    extras_require={},
    include_package_data=True,
    license=LICENSE,
    classifiers=TROVE_CLASSIFIERS
)
