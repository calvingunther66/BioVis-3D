from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="BioVis-3D",
    version="0.1.0",
    author="calvingunther66",
    description="An interactive tool for visualizing and manipulating macromolecular structures.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/calvingunther66/BioVis-3D",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pyvista',
        'biopython',
        'pyvistaqt',
        'PyQt6'
    ],
    entry_points={
        'console_scripts': [
            'biovis-3d = src.main:main',
        ],
    },
)
