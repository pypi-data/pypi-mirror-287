from setuptools import setup, find_packages

setup(
    name='open_flags',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    description='A package for retrieving Open Flags SVGs',
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
