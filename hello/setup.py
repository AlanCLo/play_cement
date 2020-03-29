
from setuptools import setup, find_packages
from hello.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='hello',
    version=VERSION,
    description='blah blah blah',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='alan',
    author_email='asdfasdf',
    url='https://github.com/johndoe/myapp/',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'hello': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        hello = hello.main:main
    """,
)
