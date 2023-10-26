# Import necessary libraries
import tkinter as tk  # For creating a graphical user interface (GUI)
import RPi.GPIO as GPIO  # For controlling the Raspberry Pi's GPIO pins
import time  # For adding time delays

# Define the GPIO pin number for the LED
LED_PIN = 17

# Define a dictionary that maps characters to their Morse code representations
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

# Function to convert a text message to Morse code
def convert_to_morse(text):
    morse_code = ""
    text = text.upper()  # Convert the text to uppercase
    for char in text:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + " "
    return morse_code

# Function to blink the LED based on Morse code
def blink_morse_code(morse_code):
    GPIO.output(LED_PIN, GPIO.LOW)  # Turn off the LED
    time.sleep(1)  # Pause for 1 second
    for symbol in morse_code:
        if symbol == '.':
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on the LED (short blink)
            time.sleep(0.2)  # Keep the LED on for 0.2 seconds
            GPIO.output(LED_PIN, GPIO.LOW)  # Turn off the LED
            time.sleep(0.2)  # Pause for 0.2 seconds
        elif symbol == '-':
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on the LED (long blink)
            time.sleep(0.6)  # Keep the LED on for 0.6 seconds
            GPIO.output(LED_PIN, GPIO.LOW)  # Turn off the LED
            time.sleep(0.2)  # Pause for 0.2 seconds
        elif symbol == ' ':
            time.sleep(0.4)  # Pause for 0.4 seconds between words
    GPIO.output(LED_PIN, GPIO.LOW)  # Turn off the LED at the end

# Function to start blinking based on user input
def start_blink():
    input_text = text_entry.get()  # Get the user input from the text entry field
    morse_code = convert_to_morse(input_text)  # Convert the input to Morse code
    blink_morse_code(morse_code)  # Start blinking the Morse code

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Set the GPIO mode to BCM
GPIO.setup(LED_PIN, GPIO.OUT)  # Set the LED pin as an output
GPIO.output(LED_PIN, GPIO.LOW)  # Ensure the LED is initially off

# Create a GUI window
root = tk.Tk()
root.title("Morse Code Blinker")

# Create GUI elements: label, text entry field, and start button
label = tk.Label(root, text="Enter a word (Maximum 12 characters):")
text_entry = tk.Entry(root, width=15)
start_button = tk.Button(root, text="Start Blinking", command=start_blink)

# Place the GUI elements in the window
label.pack()
text_entry.pack()
start_button.pack()

# Start the GUI event loop
root.mainloop()

# Cleanup GPIO configuration when the program exits
GPIO.cleanup()
