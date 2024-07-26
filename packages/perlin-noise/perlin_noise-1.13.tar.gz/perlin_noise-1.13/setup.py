from setuptools import find_packages, setup

try:
    with open("Readme_pypi.md", "r") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "Perlin Noise Generator"

setup(
    name="perlin_noise",
    version="1.13",
    description="Python implementation for Perlin Noise with unlimited coordinates space",
    author="salaxieb",
    username="__token__",
    password="pypi-AgEIcHlwaS5vcmcCJGU0ZTZlOWM3LTMyYjctNGZkMS1iOTA2LTlkYTU3NjYzOGFmMgACFFsxLFsicGVybGluLW5vaXNlIl1dAAIsWzIsWyI5NWIyZmFmNS00MjUwLTQxMmMtODE0Ny0wNzhmYzNkMTFjNTUiXV0AAAYgmXLf0nKH_Th7otxKb8x2d9WnZZ1xmxa8L4_Sgx_sJzk",
    author_email="salaxieb.ildar@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=["perlin_noise"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
)
