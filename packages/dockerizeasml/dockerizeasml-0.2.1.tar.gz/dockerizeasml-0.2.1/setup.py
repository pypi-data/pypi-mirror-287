from setuptools import setup, find_packages

setup(
    name="dockerizeasml",
    version="0.2.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dockerizeasml=dockerizeasml.dockerizer:main',
        ],
    },
)