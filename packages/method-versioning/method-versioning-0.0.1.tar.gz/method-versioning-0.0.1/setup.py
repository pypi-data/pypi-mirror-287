import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="method-versioning",
    version="0.0.1",
    author="Sanghun Lee",
    author_email="nrhys2005@gmail.com",
    description="Method versioning package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nrhys2005/method-versioning",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
