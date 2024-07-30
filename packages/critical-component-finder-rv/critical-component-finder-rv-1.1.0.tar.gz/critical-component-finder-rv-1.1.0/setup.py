import setuptools

VERSION = "1.1.0"

NAME = "critical-component-finder-rv"

INSTALL_REQUIRES = [
    "grapihviz",
    "networkx"
]


setuptools.setup(
    name=NAME,
    version=VERSION,
    description="Finds critical component in C/C++ CMake projects",
    url="https://github.com/Valiewramis/Critical-Component-Finder",
    project_urls={
        "Source": "https://github.com/Valiewramis/Critical-Component-Finder",
    },
    author="Ramis",
    license="MIT",
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: POSIX :: Linux",
],
    python_requires=">=3.11",
    install_requires=INSTALL_REQUIRES,
    packages=["src/critical_component_finder_rv"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)