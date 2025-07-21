# Import necessary modules
import time  # For adding delay between prints
import sys   # For exiting the program gracefully

# Introduce constants
MAX_INDENT = 20      # Maximum number of spaces before changing direction
DISPLAY_STRING = '********'  # The animated string to display
DELAY = 0.1          # Delay in seconds between frames

# Initialize indentation settings
indent = 0 # How many spaces to indent
indentIncreasing = True # Whether the indentation is increasing or not

try:
    while True:
        # Print the indented string on a new line
        print(' ' * indent + DISPLAY_STRING)

        time.sleep(DELAY)  # Control animation speed

        # Adjust indentation based on direction
        if increasing:
            indent += 1
            if indent == MAX_INDENT:
                increasing = False  # Change direction at rightmost point
        else:
            indent -= 1
            if indent == 0:
                increasing = True   # Change direction at leftmost point

# Allow the user to interrupt the animation with Ctrl+C
except KeyboardInterrupt:
    sys.exit()  # Exit the program gracefully
