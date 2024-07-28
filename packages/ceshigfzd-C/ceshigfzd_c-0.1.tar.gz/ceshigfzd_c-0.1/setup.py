# ceshigfzd_c/setup.py

from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("ceshigfzd_c.calculate", ["ceshigfzd_c/calculate.pyx"])
]

setup(
    name='ceshigfzd_c',
    version='0.1',
    packages=['ceshigfzd_c'],
    ext_modules=cythonize(extensions),
    install_requires=[
        'pandas',
        'openpyxl'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='lixintong shi shabi',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
