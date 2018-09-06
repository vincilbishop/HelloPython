
from setuptools import setup, find_packages
from hellopython.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='hellopython',
    version=VERSION,
    description='Hello Python!',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Vincil Bishop',
    author_email='vincil.bishop@colostate.edu',
    url='https://github.com/johndoe/myapp/',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'hellopython': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        hellopython = hellopython.main:main
    """,
)
