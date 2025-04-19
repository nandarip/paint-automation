# Paint Automation Script

This project automates tasks in Microsoft Paint using Python and PyAutoGUI. It demonstrates how to:
- Open Paint
- Add text with formatting
- Automate mouse and keyboard actions

## Features
- Opens Paint automatically
- Adds formatted text (bold, large font)
- Uses keyboard shortcuts for tool selection
- Implements fail-safe features

## Requirements
- Python 3.x
- PyAutoGUI
- Other dependencies listed in requirements.txt

## Installation
1. Clone this repository
2. Install requirements:
```bash
pip install -r requirements.txt
```

## Usage
Run the script:
```bash
python test.py
```

## How It Works
The script:
1. Opens Paint using subprocess
2. Uses PyAutoGUI to:
   - Select the text tool
   - Add formatted text
   - Handle mouse movements and clicks

## Safety Features
- Includes PyAutoGUI fail-safe (move mouse to corner to stop)
- Proper timing between actions
- Error handling for all operations 