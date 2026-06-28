#!/bin/bash

# Path to the system sampling frequency file
FREQ_FILE="/sys/bus/iio/devices/trigger0/sampling_frequency"

if [ -f "$FREQ_FILE" ]; then
    ORIGINAL_FREQ=$(cat "$FREQ_FILE")
else
    echo "Error: IIO trigger file not found. Are drivers loaded?"
    exit 1
fi

echo "Lower the sampling frequency to 10Hz"
echo 10 | sudo tee "$FREQ_FILE" > /dev/null

echo "------------------------------------------------"
echo "System optimized! sampling_frequency is now 10Hz."
echo "Press exit key to keep 10Hz or other key to revert"
echo "------------------------------------------------"

read -n 1 -s -r -p "Press any key to restore settings and exit..."
echo ""

echo "Restoring original sampling frequency ($ORIGINAL_FREQ Hz)..."
echo "$ORIGINAL_FREQ" | sudo tee "$FREQ_FILE" > /dev/null

echo "Done! System restored to defaults."
