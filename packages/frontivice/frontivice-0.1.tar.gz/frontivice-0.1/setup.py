from setuptools import setup, find_packages

setup(
    name="frontivice",
    version="0.1",
    packages=find_packages(),
    author="Aung Htoo Khine",
    install_requires=["pydantic>=2.8.2"],
    description="This package is designed to generate regular expression formats based on device names.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
