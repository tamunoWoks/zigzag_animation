# Initialize indentation settings
indent = 0 # How many spaces to indent
indentIncreasing = True # Whether the indentation is increasing or not

try:
    while True: # The main program infinite loop to keep animation running
        # Print the current indentation followed by the asterisks on the same line
        print(' ' * indent, end='') # Print spaces without newline
        print('********') # Print the asterisks with newline

        time.sleep(0.1) # Pause for 1/10th of a second.

        # Adjust indentation based on the current direction
        if indentIncreasing:
            indent += 1  # Move to the right by increasing indentation
            if indent == 20: # If it reaches the far right limit
                indentIncreasing = False  # Change direction 
        else:
            indent -= 1  # Move to the left by decreasing indentation
            if indent == 0:  # If it reaches the far left limit
                indentIncreasing = True  # Change direction to move right again
