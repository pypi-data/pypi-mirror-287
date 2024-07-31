# ML-Dockerizer

ML-Dockerizer is a Python library that allows users to effortlessly dockerize an entire machine learning (ML) project with a single command-line instruction. It automatically recognizes the path of ML model files in the project directory and generates an appropriate Dockerfile.

## Installation

You can install ML-Dockerizer using pip:
`pip install ml-dockerizer`

## Usage

To dockerize your ML project, navigate to your project's root directory and run:
`ml-dockerizer /path/to/your/ml/project`

By default, ML-Dockerizer will use `main.py` as the entry point for your Docker container. If you want to specify a different entry point, use the `--entry-point` option:

## Features

- Automatic detection of common ML model file formats (pkl, h5, joblib, pt, pth, onnx)
- Generation of a Dockerfile tailored to your ML project
- Customizable entry point for your dockerized application
- Easy-to-use command-line interface

## Requirements

- Python 3.6+
- Docker (for building and running the generated Docker image)

## How it works

1. ML-Dockerizer scans your project directory for ML model files.
2. It generates a Dockerfile that:
   - Uses a Python 3.8 slim base image
   - Copies and installs the requirements from `requirements.txt`
   - Copies the identified model files
   - Copies the rest of the project files
   - Sets the default command to run your specified entry point

3. You can then use standard Docker commands to build and run your containerized ML project.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request (git repository coming soon !).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to all contributors who have helped shape ML-Dockerizer.
- Inspired by the need for simplified ML project containerization in the data science community.

## Contact

If you have any questions, feel free to reach out to [aviroop-pal] at [avirooppal42@gmail.com].