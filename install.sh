#!/usr/bin/env bash
# Lunheng (论衡) one-click installer for macOS / Linux
# Usage: bash install.sh

set -e
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Try python3, fall back to python
if command -v python3 &> /dev/null; then
    python3 "$SCRIPT_DIR/install.py" "$@"
elif command -v python &> /dev/null; then
    python "$SCRIPT_DIR/install.py" "$@"
else
    echo "Error: Python 3 not found in PATH"
    exit 1
fi
