from setuptools import setup, find_packages

import os

import subways


def get_readme():
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='subways',
    version=subways.__version__,
    packages=find_packages(),
    url='https://github.com/midoriiro/subways/',
    license=open('LICENSE').read(),
    author='midoriiro',
    author_email='contact@smartsoftwa.re',
    maintainer='midoriiro',
    maintainer_email='contact@smartsoftwa.re',
    description=subways.__doc__,
    long_description=open('README.md').read(),
    tests_require=['tox'],
    install_requires=[],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries'
    ],
)
