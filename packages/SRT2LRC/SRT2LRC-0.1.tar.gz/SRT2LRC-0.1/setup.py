# setup.py

from setuptools import setup, find_packages

setup(
    name="SRT2LRC",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Oni-Sparrow",
    author_email="omarashrafgeddawy@gmail.com",
    description="Converts from SRT to LRC and vice versa.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your_library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
