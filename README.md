# Overview
This repository contains three Python scripts designed to facilitate user interface interactions and logging for an autonomous vehicle simulator. The scripts include:

1. ControlUI.py - The main user interface with functional controls.
2. ControlUI_placebo.py - A placebo user interface to test user interaction without actual functionality.
3. logger.py - A logger to record user interactions with the interfaces.
   
# Files and Descriptions
## ControlUI.py
This script creates a functional user interface for controlling various parameters of an autonomous vehicle using *customtkinter*. It includes sliders and toggles for different vehicle settings.

**Key Components:**

- UI Setup: Sets up the window, appearance, and fonts.
- Sliders and Toggles: Adds controls for parameters like acceleration, deceleration, lane offset, and more.
- Event Handlers: Updates the vehicle parameters based on user interactions.
- CarMaker Integration: Initializes and communicates with the CarMaker simulator.

### ControlUI_placebo.py

This script creates a placebo user interface that mimics the ControlUI.py but without actual functionality. It's used to test user interaction without influencing the vehicle's behavior.

### logger.py

This script provides logging functionality to record user interactions with the interfaces, including changes to slider values and toggle states.

## Usage
To run the functional UI, execute:
python ControlUI.py

To run the placebo UI, execute:
python ControlUI_placebo.py

The logger.py script is used internally by the UI scripts to log interactions.

### Requirements
- Python 3.x
- customtkinter
- pycarmaker
