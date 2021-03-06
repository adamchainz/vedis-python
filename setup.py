import os

from distutils.core import setup, Extension
try:
    from Cython.Build import cythonize
except ImportError:
    raise RuntimeError('Cython must be installed')


python_source = 'vedis.pyx'
library_source = 'src/vedis.c'

vedis_extension = Extension(
    'vedis',
    sources=[python_source, library_source])

setup(
    name='vedis',
    version='0.4.1',
    description='Fast Python bindings for the Vedis embedded NoSQL database.',
    author='Charles Leifer',
    author_email='',
    install_requires=['cython'],
    ext_modules=cythonize(vedis_extension),
)
