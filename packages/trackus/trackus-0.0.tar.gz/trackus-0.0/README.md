# trackus python package

# dependencies usages
twine securely upload the package to PyPI

# build
python setup.py sdist bdist_wheel
twine upload dist/*

# Installation
pip install trackus