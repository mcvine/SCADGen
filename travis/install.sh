#!usr/bin bash

conda config --set always_yes true
conda update conda
conda config --add channels conda-forge
conda config --add channels mcvine
conda install -n root conda-build
conda create -q --name testenv python=$TRAVIS_PYTHON_VERSION
conda install -n testenv pytest pytest-cov
conda install -n testenv -c mcvine pyre
source activate testenv
