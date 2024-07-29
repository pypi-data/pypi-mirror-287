from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize
import numpy

extensions = [
    Extension(
        'discqueue.core',
        sources=['discqueue/core.pyx'],
        include_dirs=[numpy.get_include()]
    )
]

setup(
    name='discqueue',
    version='0.1.0',
    author='YY',
    author_email='',
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    ext_modules=cythonize(extensions),
    install_requires=[
        'matplotlib',
        'numpy',
        'cython'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
