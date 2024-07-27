from setuptools import setup, find_packages

setup(
    name="ggstats",
    version="0.1.2",
    packages=find_packages(),
    install_requires=['pandas>=1.0.0','numpy>=1.18.0'],
    author="Gaurav G",
    author_email="lotusheart2016@gmail.com",
    description="A package for evaluating model performance metrics",
    url="https://github.com/visit-www/ggstats.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
