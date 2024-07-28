from setuptools import setup, find_packages
from distutils.util import convert_path

with open("README.md", "r") as f:
    long_description = f.read()

version_ns = {}
vpath = convert_path("src/py4DSTEM/version.py")
with open(vpath) as version_file:
    exec(version_file.read(), version_ns)

setup(
    name="py4DSTEM-lite",
    version=version_ns["__version__"],
    packages=find_packages(where='src'),
    package_dir={'':'src'},
    description="A lite version of the open source python package, py4DSTEM.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/py4dstem/py4DSTEM-lite/",
    author="Benjamin H. Savitzky",
    author_email="ben.savitzky@gmail.com",
    license="GNU GPLv3",
    keywords="STEM,4DSTEM,lite",
    python_requires=">=3.10",
    install_requires=[
        "numpy >= 1.19",
        "scipy >= 1.5.2",
        "h5py >= 3.2.0",
        "ncempy >= 1.8.1",
        "matplotlib >= 3.2.2",
        "tqdm >= 4.46.1",
        "dill >= 0.3.3",
        "gdown >= 5.1.0",
        "emdfile >= 0.0.14",
        "pylops >= 2.1.0",
        "colorspacious >= 1.1.2",
    ],
    package_data={
        "py4DSTEM-lite": [
            "process/utils/scattering_factors.txt",
        ]
    },
)
