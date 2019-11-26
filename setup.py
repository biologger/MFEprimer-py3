#!/usr/bin/env python3

import setuptools
from distutils.core import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(name="mfeprimer-py3",
      version='0.1.1',
      long_description = readme,
      long_description_content_type='text/markdown',
      url='https://github.com/Ulises-Rosas/mfeprimer-py3',
      packages=['chilli'],
      package_dir={'chilli': 'chilli'},
      scripts=[
          'MFEprimer.py',
          'IndexDB.py',
          'chilli/UniFastaFormat.py',
          'chilli/mfe_index_db.py'
      ],
      data_files=[
          ('bin', [ 'bin/MFEprimer_Darwin_32_faToTwoBit',
                    'bin/MFEprimer_Darwin_32_twoBitToFa',
                    'bin/MFEprimer_Darwin_64_faToTwoBit',
                    'bin/MFEprimer_Darwin_64_twoBitToFa',
                    'bin/MFEprimer_Linux_32_faToTwoBit',
                    'bin/MFEprimer_Linux_32_twoBitToFa',
                    'bin/MFEprimer_Linux_64_faToTwoBit',
                    'bin/MFEprimer_Linux_64_twoBitToFa'  ])
      ],
      install_requires=['psutil'],
      classifiers=[
          'Programming Language :: Python :: 3'
      ]
    )
