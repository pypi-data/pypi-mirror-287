# setup.py

from setuptools import setup, find_packages

setup(
    name="SubLyric",
    version="1.0",
    packages=find_packages(),
    install_requires=[],
    author="Oni-Sparrow",
    author_email="omarashrafgeddawy@gmail.com",
    description="Converts from SRT to LRC and vice versa.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Oni-Sparrow/SubLyric",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
