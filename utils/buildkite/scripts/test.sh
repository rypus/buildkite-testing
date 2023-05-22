#!/bin/bash
set -e

PROFILE="config-profile/software-update-setting1.mobileconfig"
if [ -f "$PROFILE" ]; then
    echo "Test pass!"
    exit 0
else
    echo "Test failed!"
    exit 1
fi