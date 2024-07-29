from setuptools import setup, find_packages
import os

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='open_flags',
    version='0.0.2',
    packages=find_packages(),
    include_package_data=True,
    description='A package for retrieving Open Flags SVGs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='RAD Labz',
    author_email='openflags@radlabz.com',
    url='https://github.com/Open-Flags-API/open_flags_py',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[],
)
