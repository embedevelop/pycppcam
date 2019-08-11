#!/usr/bin/env python3

from setuptools import setup, Extension
from Cython.Build import cythonize


def main():
    compiler_directives = {
        'language_level': '3',
        'embedsignature': True,
        'c_string_encoding': 'utf-8'
    }

    ext_modules = cythonize([Extension('cppcam', ['src/cppcam.pyx'])],
                            compiler_directives=compiler_directives)

    setup(name='cppcam',
          version='0.1.0',
          description='Simple Cython binding for C++ V4L Camera',
          author='Konstantin Dobratulin',
          author_email='zsxoff@gmail.com',
          ext_modules=ext_modules)


if __name__ == "__main__":
    main()
