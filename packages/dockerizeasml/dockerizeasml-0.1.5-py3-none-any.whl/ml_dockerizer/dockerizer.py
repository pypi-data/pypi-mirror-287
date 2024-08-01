import os
import argparse
import glob
import ast

class Dockerizeasml:
    def __init__(self, project_path, entry_point, port, python_version, extra_installs):
        self.project_path = project_path
        self.entry_point = entry_point
        self.port = port
        self.python_version = python_version
        self.extra_installs = extra_installs
        self.model_files = []
        self.requirements_file = 'requirements.txt'
        self.dockerfile_path = os.path.join(project_path, 'Dockerfile')

    def find_model_files(self):
        extensions = ['*.pkl', '*.h5', '*.joblib', '*.pt', '*.pth', '*.onnx', '*.pickle']
        for ext in extensions:
            self.model_files.extend(glob.glob(os.path.join(self.project_path, '**', ext), recursive=True))
        return [os.path.relpath(f, self.project_path) for f in self.model_files]

    def find_model_in_scripts(self):
        python_files = glob.glob(os.path.join(self.project_path, '**', '*.py'), recursive=True)
        model_variables = set()

        for file in python_files:
            with open(file, 'r') as f:
                tree = ast.parse(f.read())
                for node in ast.walk(tree):
                    if isinstance(node, ast.Assign):
                        for target in node.targets:
                            if isinstance(target, ast.Name) and 'model' in target.id.lower():
                                if isinstance(node.value, ast.Call):
                                    if isinstance(node.value.func, ast.Name):
                                        model_variables.add(target.id)
        
        return list(model_variables)

    def generate_dockerfile(self):
        model_files = self.find_model_files()
        model_variables = self.find_model_in_scripts()
        
        dockerfile_content = f"""
FROM python:{self.python_version}-slim

WORKDIR /app

COPY {self.requirements_file} .
RUN pip install --no-cache-dir -r {self.requirements_file}

{chr(10).join(f"COPY {file} {file}" for file in model_files)}

COPY . /app

# Environment variables for model files
{chr(10).join(f'ENV {var.upper()}_PATH="/app/{var}.pkl"' for var in model_variables)}

# Set the NLTK_DATA environment variable
ENV NLTK_DATA=/usr/local/nltk_data

# Install additional Python packages
RUN {' && '.join(f'python -m {install}' for install in self.extra_installs)}

# Make port {self.port} available to the world outside this container
EXPOSE {self.port}

# Run the entry point script when the container launches
CMD ["python", "{self.entry_point}"]
"""
        with open(self.dockerfile_path, 'w') as dockerfile:
            dockerfile.write(dockerfile_content)

    def dockerize(self):
        self.generate_dockerfile()
        print(f"Dockerfile generated at: {self.dockerfile_path}")
        print("You can now build and run your Docker image.")
        print("Build: docker build -t dockerizeasml .")
        print(f"Run: docker run -p {self.port}:{self.port} dockerizeasml")

def main():
    parser = argparse.ArgumentParser(description="Dockerize ML Project")
    parser.add_argument("project_path", help="Path to the ML project directory")
    parser.add_argument("--entry-point", default="app.py", help="Entry point Python script (default: app.py)")
    parser.add_argument("--port", type=int, default=5000, help="Port to expose (default: 5000)")
    parser.add_argument("--python-version", default="3.9", help="Python version to use (default: 3.9)")
    parser.add_argument("--extra-installs", nargs='+', default=["nltk.downloader -d /usr/local/nltk_data wordnet omw"], 
                        help="Additional Python installations (default: NLTK data)")
    args = parser.parse_args()

    dockerizer = Dockerizeasml(args.project_path, args.entry_point, args.port, args.python_version, args.extra_installs)
    dockerizer.dockerize()

if __name__ == "__main__":
    main()