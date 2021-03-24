from setuptools import setup

setup(name='equivariant-attention',
      version='1.1',
      packages=[
          'equivariant_attention'
      ],
      install_require=[
          'lie_learn@git+https://github.com/AMLab-Amsterdam/lie_learn',
          'numpy'
      ]
      )
