#!/bin/bash
set -e

PROFILE="config-profile/software-update-setting.mobileconfig"
if [ -f "$PROFILE" ]; then
    eho "Test pass!"
else
    exit 1
fi