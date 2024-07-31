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
    echo "Building for macOS..."
    python3.11 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install cython numpy
    python setup_docker.py build_ext --inplace
    find . -name "crypto_mng*.so" -not -path "./builds/*" -exec cp {} builds/ \;
    deactivate
    echo "macOS build completed."
}

# Function to build for Linux using Docker
build_linux() {
    echo "Building for Linux..."
    docker build -f Dockerfile.linux -t marearts-anpr-d-linux .
    docker run --rm -v "$(pwd)"/builds:/output marearts-anpr-d-linux /bin/bash -c "
        python setup_docker.py build_ext --inplace &&
        find . -name 'crypto_mng*.so' -not -path './builds/*' -exec cp {} /output/ \;
    "
    echo "Linux build completed."
}

# Function to build for Windows using Docker
build_windows() {
    echo "Building for Windows..."
    docker build -f Dockerfile.windows -t marearts-anpr-d-windows .
    docker run --rm -v "$(pwd)"/builds/windows:/output marearts-anpr-d-windows
    echo "Windows build completed."
}

# Main execution
echo "Starting build process..."

# Initial cleanup
cleanup

# Detect operating system and run appropriate build
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows
    build_windows
else
    build_macos
    build_linux
fi

# Final cleanup
cleanup
