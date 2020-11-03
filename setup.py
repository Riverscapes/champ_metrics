# -*- coding: utf-8 -*-

"""setup.py: setuptools control."""
"""
A Lot of this methodology was "borrowed" from
    - https://github.com/jgehrcke/python-cmdline-bootstrap/blob/master/bootstrap/bootstrap.py
"""

import re
from setuptools import setup

install_requires = [
    'argparse', 'shapely', 'numpy', 'GDAL>=3.0', 'scipy==1.5.1', 'pytz==2020.4',
    'pandas==1.1.4', 'Shapely==1.7.1'
]

version = re.search(
    r'^__version__\s*=\s*"(.*)"',
    open('champmetrics/__version__.py').read(),
    re.M
).group(1)

with open("README.md", "rb") as f:
      long_descr = f.read().decode("utf-8")

setup(
      name='champmetrics',
      description='Tools that are part of the CHaMP Automation pipeline',
      url='https://github.com/SouthForkResearch/CHaMPToolbox',
      author='Matt Reimer',
      author_email='matt@northarrowresearch.com',
      python_requires='>3.5.2',      
      license='MIT',
      packages=['champmetrics', 'scripts'],
      zip_safe=False,
      install_requires=install_requires,
      entry_points={
            "console_scripts": [
                  'champtopometrics = champmetrics.topometrics.topometrics:main',
                  'champvalidation = champmetrics.validation.validation:main',
                  'champhydroprep = champmetrics.hydroprep:main',
                  'champsiteprops = champmetrics.siteprops:main',
            ]
      },
      version=version,
      long_description=long_descr,
)
