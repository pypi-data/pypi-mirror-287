from setuptools import setup, find_packages

setup(
    name='mypkggener',
    version='0.0.1',
    description='MyPyPIPkgDirGener',
    author='FarAway6834',
    author_email='faway6834@gmail.com',
    url='https://github.com/FarAway6834/MyPkgGener',
    install_requires=['setuptools', 'wheel', 'twine', ],
    packages=find_packages(exclude=[]),
    keywords=['FarAway', 'FarAway6834', 'MyPkgGener', 'PythonPkg2WheelableOnlinePkg', 'pypi'],
    python_requires='>=3.10',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ],
)