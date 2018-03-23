#!usr/bin bash

conda create -q -n scadgen_test python=$TRAVIS_PYTHON_VERSION pytest pytest_cov
source activate scadgen_test
python setup.py install
