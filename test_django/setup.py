from setuptools import setup, find_packages

setup(
    name="pseudotest",
    version="0.1",
    packages=["pseudo_test", "test_django"],
    include_package_data=True,
    license="BSD License",  # example license
    description="A simple Django app to manage jobs for running pseudocode tests.",
)
