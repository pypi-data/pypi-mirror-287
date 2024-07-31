#!/bin/bash
set -e

PACKAGE_NAME="marearts-anpr-d"
PYTHON_VERSIONS=("3.8" "3.9" "3.10" "3.11")

# Function to fetch the latest version from PyPI
fetch_latest_version() {
    local pypi_url="https://pypi.org/pypi/${PACKAGE_NAME}/json"
    if command -v curl &> /dev/null; then
        local latest_version=$(curl -s $pypi_url | grep -o '"version":"[^"]*' | cut -d'"' -f4 | sort -V | tail -n1)
    elif command -v wget &> /dev/null; then
        local latest_version=$(wget -qO- $pypi_url | grep -o '"version":"[^"]*' | cut -d'"' -f4 | sort -V | tail -n1)
    else
        echo "Error: Neither curl nor wget is installed." >&2
        return 1
    fi
    if [ -z "$latest_version" ]; then
        echo "Package not found on PyPI or unable to fetch version."
        return 1
    else
        echo "$latest_version"
    fi
}

# Function to build for distribution
build_for_distribution() {
    local python_version=$1
    echo "Building for Python $python_version..."
    python$python_version -m venv venv_$python_version
    source venv_$python_version/bin/activate
    pip install --upgrade pip build cython numpy
    # Use python -m build to create both sdist and wheel
    python -m build
    deactivate
    mkdir -p dist_all
    mv dist/* dist_all/
    rm -rf dist
}

# Function to deploy to PyPI
deploy_to_pypi() {
    echo "Deploying to PyPI..."
    python3.10 -m venv venv_deploy
    source venv_deploy/bin/activate
    pip install --upgrade twine
    python -m twine upload dist_all/*
    deactivate
}

cleanup() {
    echo "Cleaning up..."
    rm -rf dist dist_all venv_* marearts_anpr_d.egg-info *.so || true
}

# Main execution
echo "Starting deployment process..."

# Cleanup first
cleanup

# Fetch current version from PyPI
PYPI_VERSION=$(fetch_latest_version)
if [ $? -ne 0 ]; then
    echo "Failed to fetch PyPI version. Assuming this is a new package."
    PYPI_VERSION="Not found on PyPI"
fi
echo "Current version on PyPI: $PYPI_VERSION"

# Get new version from user
read -p "Enter the new version number: " NEW_VERSION
if [[ ! $NEW_VERSION =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "Invalid version format. Please use X.Y.Z format."
    exit 1
fi

# Update version in pyproject.toml and setup.cfg
sed -i '' "s/^version = \".*\"/version = \"$NEW_VERSION\"/" pyproject.toml
sed -i '' "s/^version = .*/version = $NEW_VERSION/" setup.cfg
echo "Updated version in pyproject.toml and setup.cfg to $NEW_VERSION"

# Build for all Python versions
for version in "${PYTHON_VERSIONS[@]}"; do
    build_for_distribution $version
done

# Confirm deployment
read -p "Ready to deploy version $NEW_VERSION for all Python versions. Proceed? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    # Deploy to PyPI
    deploy_to_pypi
    echo "Deployment process completed."
else
    echo "Deployment cancelled."
    exit 1
fi

cleanup