#!/bin/bash

# Self-Improve Hook Script
# This script is triggered on the "stop" hook event
# When automatic mode is enabled, it triggers the self-improve analysis

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"

# Check if disabled (automatic mode off)
if [ -f "$SKILL_DIR/.disabled" ]; then
  exit 0
fi

# Automatic mode is enabled - trigger the self-improve analysis
cat << 'EOF'
{"systemMessage": "AUTOMATIC SELF-IMPROVE MODE ENABLED. Before ending this session, analyze the conversation for potential skill improvements. Follow the workflow described in the `self-improve` skill: detect corrections, evaluate against the 4 criteria, and propose any improvements to the user for approval. If no improvements detected, say so briefly."}
EOF
