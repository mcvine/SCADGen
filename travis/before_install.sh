#!/usr/bin bash

if [[ "$TRAVIS_PYTHON_VERSION" == "2.7"]]
then
    wget http://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O miniconda.sh
else
    wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
fi

chmod +x miniconda.sh

./miniconda.sh -b -p $HOME/miniconda
export PATH=/home/travis/mc/bin:$PATH
