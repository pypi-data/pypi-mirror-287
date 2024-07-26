#it will chanaged to use

from setuptools import setup, find_packages

setup(
    name='mpti',
    version='0.0.2',
    description='MyPathTemperImporter',
    author='FarAway6834',
    author_email='faway6834@gmail.com',
    url='https://github.com/FarAway6834/MyPathTemperImporter',
    install_requires=[
        'mypkggener',  #actually use in delpoy later.
        'hgen'  #actually use in build C project. not now.
    ],
    packages=find_packages(exclude=[]),
    keywords=[
        'FarAway', 'FarAway6834', 'MyPathTempImporter', 'MPTI',
        'imports more perfact', 'imports'
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
