from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension("distan_matr.tran", ["distan_matr/tran.pyx"]),
]

setup(
    name="distan_matr",
    version="0.1.2",
    description="A package for processing FASTA files",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Geroge",
    author_email="",
    packages=["distan_matr"],
    ext_modules=cythonize(ext_modules),
    install_requires=[
        'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
