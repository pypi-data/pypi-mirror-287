from setuptools import find_packages, setup

setup(
    name="prevail_operations",
    version="0.1",
    packages=find_packages(),
    install_requires=["ratelimit==2.2.1", "Requests==2.32.3"],
)
