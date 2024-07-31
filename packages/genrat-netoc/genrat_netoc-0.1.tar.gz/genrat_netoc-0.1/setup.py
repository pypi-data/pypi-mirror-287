from setuptools import setup
from Cython.Build import cythonize

setup(
    name='genrat_netoc',
    version='0.1',
    description='',
    ext_modules=cythonize("genrat_netoc/main.pyx"),
    packages=['genrat_netoc'],
    install_requires=[
        'Cython',
    ],
)
