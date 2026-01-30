#!/usr/bin/env bash
set -e

# Usage: ./manage_refs.sh <clone|pull> [repo_file]

COMMAND="$1"
REPO_FILE="${2:-docs/references/repositories.txt}"

if [ -z "$COMMAND" ]; then
    echo "Usage: $0 <clone|pull> [repo_file]"
    exit 1
fi

if [ ! -f "$REPO_FILE" ]; then
    echo "Error: Repository file '$REPO_FILE' not found."
    exit 1
fi

while read -r url dir; do
    # Skip empty lines and comments
    [[ -z "$url" || "$url" =~ ^# ]] && continue

    if [ "$COMMAND" == "clone" ]; then
        if [ ! -d "$dir" ]; then
            echo "Cloning $url into $dir..."
            mkdir -p "$(dirname "$dir")"
            git clone "$url" "$dir"
        else
            echo "Directory $dir already exists. Skipping."
        fi
    elif [ "$COMMAND" == "pull" ]; then
        if [ -d "$dir" ]; then
            echo "Updating $dir..."
            (cd "$dir" && git pull)
        else
            echo "Warning: $dir does not exist for $url. Run 'just clone-refs' first."
        fi
    else
        echo "Unknown command: $COMMAND. Use 'clone' or 'pull'."
        exit 1
    fi
done < "$REPO_FILE"
