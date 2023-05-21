#!/bin/bash
set -e

PROFILE="config-profile/software-update-setting.mobileconfig"
if [ -f "$PROFILE" ]; then
    echo "Test pass!"
else
    exit 1
fi