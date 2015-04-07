import os
from setuptools import setup, find_packages
import IProgress

setup(
    name='IProgress',
    version=IProgress.__version__,
    packages=find_packages(),

    description=IProgress.__doc__.split('\n')[0],
    long_description=IProgress.__doc__,

    author=IProgress.__author__,
    maintainer="Ali Ebrahim",
    author_email=IProgress.__author_email__,
    maintainer_email="ali.ebrahim314@gmail.com",

    install_requires=["six"],

    url='https://github.com/aebrahim/IProgress',
    license='GPL v2.1',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: '
            'GNU Library or Lesser General Public License (LGPL)',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Terminals'
    ],
)
