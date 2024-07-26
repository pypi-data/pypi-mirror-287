#it will chanaged to use

from setuptools import setup, find_packages

setup(
    name='hgenfw',
    version='0.0.1',
    description='Header File Gen FW',
    author='FarAway6834',
    author_email='faway6834@gmail.com',
    url='https://github.com/FarAway6834/Hgen',
    install_requires=[
        'mypkggener', #actually use in delpoy later.
        'setuptools', #cython lib make
        'cython', #core.
    ],
    packages=find_packages(exclude=[]),
    keywords=[
        'FarAway', 'FarAway6834', 'HeaderFileGen', 'Hgen', 'my personal hfilegen libs', 'C/C++', 'hfilegen', 'HgenFW', ''
    ],
    python_requires='>=3.10',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ],
)