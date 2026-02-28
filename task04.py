import datetime
log_file = "keylog.txt"
print("Simple Keylogger")
print("Type something and press Enter.")
print("Type 'exit' to stop thellohe program.\n")

while True:
    user_input = input("Enter text: ")

    if user_input.lower() == "exit":
        print("\nLogging stopped.")
        break

    # Get current date and time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save to file
    with open(log_file, "a") as file:
        file.write(f"{timestamp} - {user_input}\n")

print("Data saved successfully to keylog.txt")