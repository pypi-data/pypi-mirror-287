from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cerina",
    version="0.0.1",
    description='Next-gen AI agents with 100+ functionalities',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        "aiohttp",
        "nest_asyncio",
        "requests",
        "pytest",
    ],
)