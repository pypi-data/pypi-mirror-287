from setuptools import setup
from Cython.Build import cythonize
import os

def clean_pyc_files():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.pyc'):
                os.remove(os.path.join(root, file))

# Clean up .pyc files before building
clean_pyc_files()

setup(
    name='genrat_netce',
    version='0.1',
    description='',
    ext_modules=cythonize("genrat_netce/main.pyx"),
    packages=['genrat_netce'],
    install_requires=[
        'Cython',
    ],
)
