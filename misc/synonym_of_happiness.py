import random
import time

# Define a list of colors to choose from
colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']

# Generate the heart of hearts string
heart = '\n'.join([''.join([(random.choice(colors) + 'Getty'[(x-y)%5] + '\033[0m' if ((x*0.04)**2+(y*0.1)**2-1)**3 - (x*0.04)**2 * (y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(15, -15, -1)])

# Define the message to flash
message = 'You are an amazing person Getty!'
message_len = len(message)

'''
Flash the message in random colors
while True:
    color = random.choice(colors)
    print('\033[2J')  # Clear the screen
    print('\033[1;1H')  # Move the cursor to the top-left corner
    print(color + heart)  # Print the heart of hearts with the chosen color
    print('\033[0m')  # Reset the text color
    print()  # Print a blank line
    print(color + message)  # Print the message with the chosen color
    print('\033[0m')  # Reset the text color
    time.sleep(4)  # Pause for one second
'''