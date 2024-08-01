from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dockerizeasml",
    version="0.2.2",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dockerizeasml=dockerizeasml.dockerizer:main',
        ],
    },
)