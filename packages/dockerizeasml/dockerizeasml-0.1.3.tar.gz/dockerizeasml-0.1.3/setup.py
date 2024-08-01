from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dockerizeasml",
    version="0.1.3",
    author="palaviroop",
    author_email="avirooppal42@gmail.com",
    description="A tool to dockerize machine learning projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/yourusername/ml-dockerizer",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "ml-dockerizer=ml_dockerizer.dockerizer:main",
        ],
    },
)