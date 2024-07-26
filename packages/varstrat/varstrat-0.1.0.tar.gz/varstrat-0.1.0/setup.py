import os
import sys
from setuptools import find_packages, setup


def check_bedtools():
    if os.system("bedtools --version") != 0:
        print("Error: bedtools is not installed.", file=sys.stderr)
        sys.exit(1)


check_bedtools()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="varstrat",
    version="0.1.0",
    author="Thinh Quyen",
    author_email="thinhquyen9461@gmail.com",
    description="A tool to annotate VCF files using genome stratification files, targeting difficult regions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/yourusername/varstrat",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        # List your Python dependencies here
    ],
    entry_points={
        'console_scripts': [
            'varstrat=varstrat.stratify:main',
        ],
    },
)
