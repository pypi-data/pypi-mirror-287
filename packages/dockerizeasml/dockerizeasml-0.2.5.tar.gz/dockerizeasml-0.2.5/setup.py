from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dockerizeasml",
    version="0.2.5",
    author="Aviroop Pal",
    author_email="avirooppal42@gmail.com",
    description="A tool to dockerize machine learning projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/yourusername/dockerizeasml",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "dockerizeasml=dockerizeasml.dockerizer:main",
        ],
    },
)