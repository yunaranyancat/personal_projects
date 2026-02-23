#!/bin/bash

# Define the absolute path to your video folder
VIDEO_DIR="/var/www/html/congratulations/videos"
LOG_FILE="/var/www/html/congratulations/upload_debug.log"

echo "--- Starting Cleanup: $(date) ---"

# Delete all video files (webm, mp4, mov)
if [ -d "$VIDEO_DIR" ]; then
    find "$VIDEO_DIR" -type f \( -name "*.webm" -o -name "*.mp4" -o -name "*.mov" \) -delete
    echo "Deleted all video files in $VIDEO_DIR."
else
    echo "Directory $VIDEO_DIR not found."
fi

# Optional: Clear the debug log as well
if [ -f "$LOG_FILE" ]; then
    > "$LOG_FILE"
    echo "Cleared debug log."
fi

echo "--- Cleanup Complete ---"
