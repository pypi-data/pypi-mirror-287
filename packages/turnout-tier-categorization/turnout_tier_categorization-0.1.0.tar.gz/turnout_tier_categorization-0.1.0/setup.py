
from setuptools import setup, find_packages

# Read the contents of the README file
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="turnout_tier_categorization",
    version="0.1.0",
    author="David White",
    author_email="david@generationdata.org",
    description="A function to add a turnout tier categorization column to a pandas DataFrame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/davidwhite/turnout_tier_categorization",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
