import os
from setuptools import setup, find_packages

here = os.path.dirname(__file__)
version_ns = {}
with open(os.path.join(here, 'SCADGen', '_version.py')) as f:
    exec(f.read(), {}, version_ns)

# define distribution
setup(
    name = "SCADGen",
    version = version_ns['__version__'],
    packages = find_packages(".", exclude=['tests', 'travis']),
    package_dir = {'': "."},
    data_files = [],
    test_suite = 'tests',
    install_requires = [
    ],
    dependency_links = [
    ],
    author = "MCViNE team",
    description="Tools for converting MCViNE sample assembly XMLs into OpenSCAD code",
    license = 'BSD',
    keywords = "instrument, neutron, CAD",
    url="https://github.com/mcvine/SCADGen/",
    # download_url = '',
)
