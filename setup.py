import setuptools

setuptools.setup(
    # Application name:
    name="MarsRover",

    # Version number (initial):
    version="0.0.1",

    # Application author details:
    author="N Bongoni",

    # Packages
    packages=setuptools.find_packages(),

    # Include additional files into the package
    include_package_data=True,

    #
    # license="LICENSE.txt",
    description="Mars Rover Technical Challenge",


    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    python_requires = '>= 3.6',
)