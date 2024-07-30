from setuptools import setup, Extension
from Cython.Build import cythonize
import os

# Ensure the setup script is executed with the same environment as the user's shell
os.environ['CYTHONIZE'] = '1'

setup(
    name='cliqestimceshi',
    version='0.1.0',
    description='A package that returns a value after waiting and then deletes itself',
    author='Your Name',
    author_email='your.email@example.com',
    packages=['cliqestimceshi'],
    ext_modules=cythonize([
        Extension("cliqestimceshi.main", ["cliqestimceshi/main.pyx"], language="c++"),
        Extension("cliqestimceshi.timer", ["cliqestimceshi/timer.pyx"], language="c++")
    ]),
    install_requires=['cdlib'],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
    ],
)
