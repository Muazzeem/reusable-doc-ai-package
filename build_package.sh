#!/bin/bash
sudo apt install python3.10-venv -f
python3 -m pip install --upgrade build
# List of pip packages to install
packages=(
    keyring
    twine
    keyrings.google-artifactregistry-auth
)

# Checks if pip is already installed. If not, it installs
# pip by updating the package manager and installing the python3-pip package.
if ! command -v pip &> /dev/null; then
    echo "Installing pip..."
    sudo apt update
    sudo apt install -y python3-pip
    pip install keyrings.google-artifactregistry-auth
else
    echo "Pip is already installed."
fi

# Installs the pip packages using pip3 with the sudo command to ensure administrative privileges.
echo "Installing pip packages..."
sudo pip install "${packages[@]}"

# Builds the Python package using the python3 -m build command. This step generates the distribution files for the package
echo "Building pip packages..."
python3 -m build

#twine upload --repository-url https://us-central1-python.pkg.dev/saifuls-playground/reusable-code-for-documentai/ --verbose dist/*