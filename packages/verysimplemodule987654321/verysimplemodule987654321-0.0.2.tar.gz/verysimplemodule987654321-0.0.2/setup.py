from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'A very simple module'
LONG_DESCRIPTION = 'A very simple module that does nothing'

setup(
    name="verysimplemodule987654321",
    version=VERSION,
    author="Rob McInerney",
    author_email="rob@robmcinerney.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)