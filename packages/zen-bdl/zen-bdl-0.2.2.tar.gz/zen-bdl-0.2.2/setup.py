from setuptools import setup, find_packages
import io
from os import path

# --- get version ---
version = "unknown"
with open("bdl/version.py") as f:
    line = f.read().strip()
    version = line.replace("version = ", "").replace('"', "")
# --- /get version ---

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with io.open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with io.open(path.join(here, "requirements.txt"), encoding="utf-8") as f:
    requirements = [line.rstrip() for line in f]


setup(
    name='zen-bdl',
    version=version,
    description='Bloomberg Data License REST API wrapper',
    author='José Governo',
    author_email='zegoverno@hey.com',
    url="https://github.com/zegoverno/bdl",
    license="Apache Software License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    platforms=["any"],
    keywords="""quant finance analysis portfolio""",
    entry_points={
        "console_scripts": [
            "sample=sample:main",
        ],
    },
    packages=find_packages(exclude=["contrib", "docs", "tests", "examples"]),
    install_requires=requirements,
    python_requires=">=3.6",
    include_package_data=True,
)