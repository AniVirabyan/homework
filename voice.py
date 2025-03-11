
import speech_recognition as sr
import subprocess


COMMANDS = {
    "list directory": "dir",  # List directory
    "open firefox": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",  # Open Firefox
    "show calendar": "cal",  # Show calendar
    "check disk usage": "wmic logicaldisk get size,freespace,caption",  # Check disk usage
    "show processes": "tasklist"  # Show processes
}

def execute_command(command):
    """Execute the mapped shell command."""
    try:
        process = subprocess.Popen(command, shell=True)
        process.communicate()
    except Exception as e:
        print(f"Error executing command: {e}")

def recognize_speech():
    """Recognize and process voice commands."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        try:
            audio = recognizer.listen(source)
            command_text = recognizer.recognize_google(audio).lower()  # Convert speech to text
            print(f"You said: {command_text}")

            # Check if the command is in our predefined list
            if command_text in COMMANDS:
                execute_command(COMMANDS[command_text])
            else:
                print("Command not recognized.")
        except sr.UnknownValueError:
            print("Could not understand the command.")
        except sr.RequestError:
            print("Speech recognition service unavailable.")

if __name__ == "__main__":
    while True:
        recognize_speech()

