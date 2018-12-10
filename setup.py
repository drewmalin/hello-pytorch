import pip

##
# Prefer setuptools for the setup, find_packages modules, but legacy
# systems and pre Python 2.7 runtimes may require distutils.
##
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

##
# Accepts the name of a requirements file to parse. Returns all non-commented requirements.
##
def parse_requirements(requirementsFile):
    trimmedLines = (line.strip() for line in open(requirementsFile))
    return [line for line in trimmedLines if line and not line.startswith("#")]

##
# Parse the requirements map into links that can be fed directly into setup().
##
requires = parse_requirements('requirements.txt')

setup(
    # Metadata
    name = 'hello-pytorch',
    version = '0.0.1',
    # Dependencies
    install_requires = requires,
    packages = find_packages(),
    include_package_data = True,
    # Runtime
    entry_points = {
        'console_scripts': ['hello-pytorch=cli.cli:cli']
    },
    classifiers = [
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)