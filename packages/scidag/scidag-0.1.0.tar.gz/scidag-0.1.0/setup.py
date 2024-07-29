from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="scidag",
    version="0.1.0",
    author="Vahid Pourheidari",
    author_email="vahid.pourheidari@gmail.com",
    description="A simple library to manage scikit-learn DAGs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/detend/scidag",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
