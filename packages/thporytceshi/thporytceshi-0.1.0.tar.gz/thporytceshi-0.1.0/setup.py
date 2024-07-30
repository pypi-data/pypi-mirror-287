from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("thporytceshi.timer", ["thporytceshi/timer.pyx"]),
    Extension("thporytceshi.main", ["thporytceshi/main.pyx"]),
]

setup(
    name='thporytceshi',
    version='0.1.0',
    packages=['thporytceshi'],
    ext_modules=cythonize(extensions),
    zip_safe=False,
)
