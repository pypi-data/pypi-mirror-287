#!/bin/bash
set -e

# Function to clean up
cleanup() {
    echo "Cleaning up..."
    rm -rf build venv *.so || true
    find . -name "*.pyc" -delete || true
    find . -name "__pycache__" -type d -exec rm -r {} + || true
}

# Function to build for macOS
build_macos() {
    local python_version=$1
    echo "Building for macOS with Python $python_version..."
    python$python_version -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install cython numpy
    python setup_docker.py build_ext --inplace
    find . -name "crypto_mng*.so" -not -path "./builds/*" -exec cp {} builds/ \;
    deactivate
    rm -rf venv
    echo "macOS build for Python $python_version completed."
}

# Function to build for Linux using Docker
build_linux() {
    local python_version=$1
    echo "Building for Linux with Python $python_version..."
    docker build -f Dockerfile.linux --build-arg PYTHON_VERSION=$python_version -t marearts-anpr-d-linux:$python_version .
    docker run --rm -v "$(pwd)"/builds:/output marearts-anpr-d-linux:$python_version /bin/bash -c "
        python setup_docker.py build_ext --inplace &&
        find . -name 'crypto_mng*.so' -not -path './builds/*' -exec cp {} /output/ \;
    "
    echo "Linux build for Python $python_version completed."
}

# Function to build for Windows using Docker
build_windows() {
    local python_version=$1
    echo "Building for Windows with Python $python_version..."
    docker build -f Dockerfile.windows --build-arg PYTHON_VERSION=$python_version -t marearts-anpr-d-windows:$python_version .
    docker run --rm -v "$(pwd)"/builds:/output marearts-anpr-d-windows:$python_version
    echo "Windows build for Python $python_version completed."
}

# Main execution
echo "Starting build process..."

# Initial cleanup
cleanup

# Ensure builds directory exists
mkdir -p builds

# Python versions to build for
python_versions=("3.8") # "3.9" "3.10" "3.11")

# Detect operating system and run appropriate build
# Detect operating system and run appropriate build
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows
    echo "Building for Windows..."
    # for version in "${python_versions[@]}"; do
    #     build_windows $version
    # done
else
    # Mac and Linux (and any other OS)
    echo "Building for Mac and Linux..."
    for version in "${python_versions[@]}"; do
        build_macos $version
        build_linux $version
    done
fi

# Final cleanup
cleanup

echo "All builds completed. Output files are in the ./builds directory."