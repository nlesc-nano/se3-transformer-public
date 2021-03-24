from setuptools import setup, find_packages

try:
    import dgl
except ImportError:
    raise ImportError("The DGL module is required: https://www.dgl.ai/")


setup(name='equivariant-attention',
      version='1.1',
      packages=find_packages(),
      install_requires=[
          'lie_learn@git+https://github.com/AMLab-Amsterdam/lie_learn',
          'numpy', 'scipy'
      ]
      )
