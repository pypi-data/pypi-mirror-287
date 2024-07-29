from setuptools import setup, find_packages

setup(
    name="PackageBuilding",
    version="1.0.2",
    description="This is the initial version on exploring How to build the custom package in Python",
    author="Krishna Belamkonda",
    author_email="Krishna@gmail.com",
    packages=find_packages(),  # Automatically discover all packages and sub-packages
    python_requires='>=3.8',  # Required Python version
    license='MIT',  # License type
    platforms='Any',  # Supported platforms
    license_files='LICENSE',  # Path to the license file
    # entry_points={  # Required when we are working with Command-Line Interface and Executable Module
    #     'console_scripts': [
    #         'my_custom_package=custom_module.__main__:main',  # CLI command and entry point
    #     ],
    # },
)
