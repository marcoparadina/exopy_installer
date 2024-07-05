import subprocess

# Read the package names from the file
with open('packages.txt', 'r') as file:
    packages = file.readlines()

# Install each package in editable mode
for package in packages:
    package = package.strip()  # Remove any leading/trailing whitespace
    if package:  # Skip any blank lines
        print(f"Installing {package} in editable mode")
        subprocess.run(["pip", "install", "-e", package])
