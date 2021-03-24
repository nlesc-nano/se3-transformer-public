from setuptools import setup, find_packages

setup(name='equivariant-attention',
      version='1.1',
      packages=find_packages(),
      install_requires=[
          'lie_learn@git+https://github.com/AMLab-Amsterdam',
          'numpy'
      ]
      )
