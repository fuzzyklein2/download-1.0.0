#!/bin/bash

# Function to check for the presence of -d or --debug in the arguments
contains_debug_flag() {
    for arg in "$@"; do
        if [[ "$arg" == "-d" || "$arg" == "--debug" ]]; then
            return 0  # Found the debug flag
        fi
    done
    return 1  # Debug flag not found
}

# Check if debug flag is present and set Python options
PYTHON_OPTS="-OO"
if contains_debug_flag "$@"; then
    PYTHON_OPTS=""
fi

# Check for verbose flag
VERBOSE=0
if [[ " $@ " =~ " -v " || " $@ " =~ " --verbose " ]]; then
    VERBOSE=1
fi

# Log function for verbose output
log() {
    if [ $VERBOSE -eq 1 ]; then
        echo "$@"
    fi
}

# Display help message
# if [[ " $@ " =~ " -h " || " $@ " =~ " --help " ]]; then
#     echo "Usage: $0 [options]"
#     echo ""
#     echo "Options:"
#     echo "  -d, --debug     Run Python with -OO optimization"
#     echo "  -v, --verbose   Enable verbose output"
#     echo "  -h, --help      Show this help message"
#     exit 0
# fi

# Ensure Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "python3 could not be found. Please install Python 3."
    exit 1
fi

# Extract script name without path or extension
SCRIPT_PATH="$(realpath "${BASH_SOURCE[0]}")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"
SCRIPT_DIR="$(dirname "$SCRIPT_DIR")"
DIR_NAME="$(basename "$SCRIPT_DIR")"
STEM="${DIR_NAME%%-*}"

PYTHON_SCRIPT="$STEM"
echo $PYTHON_SCRIPT
LOGFILE="./log/$STEM.log"
echo $LOGFILE
[ -f "$LOGFILE" ] && rm "$LOGFILE"
mkdir -p "$(dirname "$LOGFILE")"
touch "$LOGFILE"
# Enable logging to file if verbose mode is on
if [ $VERBOSE -eq 1 ]; then
    exec > >(tee -a "$LOGFILE") 2>&1
fi

log "Script Path: $SCRIPT_PATH"
log "Script Directory: $SCRIPT_DIR"
log "Derived Stem: $STEM"
log "Python Options: $PYTHON_OPTS"

if [ -d "$STEM" ]; then
    if [ -f "$STEM/__init__.py" ]; then
        if [ -f "$STEM/__main__.py" ]; then
            # Run the directory as a module
            log "Running as module: python3 $PYTHON_OPTS -m $STEM $@"
            if ! python3 $PYTHON_OPTS -m "$STEM" "$@"; then
                echo "Python execution failed with status $?"
                exit 1
            fi
        elif [ -f "$STEM/__init__.py" ]; then
            # Attempt to import the module
            log "Importing module: $STEM"
            if ! python3 $PYTHON_OPTS -c "import $STEM"; then
                echo "Python import failed with status $?"
                exit 1
            fi
        fi
    else
        # Run the script inside the directory
        if [ -f "$STEM/$STEM.py" ]; then
            log "Running script: python3 $PYTHON_OPTS $STEM/$STEM.py $@"
            if ! python3 $PYTHON_OPTS "$STEM/$STEM.py" "$@"; then
                echo "Python script execution failed with status $?"
                exit 1
            fi
        else
            echo "No valid Python entry point found in $STEM."
            echo "Ensure you have __main__.py, __init__.py, or $STEM.py."
            exit 1
        fi
    fi
else
    echo "Directory $STEM does not exist."
    exit 1
fi
