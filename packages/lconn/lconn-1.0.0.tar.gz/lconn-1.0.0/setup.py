from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lconn",
    version="1.0.0",
    author="Alko.Platyna",
    author_email="alko.richy@my.com",
    description="Helps you connecy with LangConnector plugin.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/your_repository",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "aiohttp",
    ],
)
