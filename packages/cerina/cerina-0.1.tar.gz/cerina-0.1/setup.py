from setuptools import setup, find_packages

setup(
    name="cerina",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "aiohttp",
        "nest_asyncio",
        "requests",
        "pytest",
    ],
)