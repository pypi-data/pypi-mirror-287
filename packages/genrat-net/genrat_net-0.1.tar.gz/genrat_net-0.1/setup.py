from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    name='genrat_net',
    version='0.1',
    packages=['genrat_net'],
    ext_modules=cythonize(Extension(
        "genrat_net.main",
        sources=["genrat_net/main.pyx"],
    )),
)
