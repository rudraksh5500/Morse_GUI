import tkinter as tk
import RPi.GPIO as GPIO
import time

LED_PIN = 17

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

def convert_to_morse(text):
    morse_code = ""
    text = text.upper()
    for char in text:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + " "
    return morse_code

def blink_morse_code(morse_code):
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1)
    for symbol in morse_code:
        if symbol == '.':
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(0.2)
        elif symbol == '-':
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(0.6)
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(0.2)
        elif symbol == ' ':
            time.sleep(0.4)
    GPIO.output(LED_PIN, GPIO.LOW)

def start_blink():
    input_text = text_entry.get()
    morse_code = convert_to_morse(input_text)
    blink_morse_code(morse_code)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

root = tk.Tk()
root.title("Morse Code Blinker")

label = tk.Label(root, text="Enter a word (Maximum 12 characters):")
text_entry = tk.Entry(root, width=15)
start_button = tk.Button(root, text="Start Blinking", command=start_blink)

label.pack()
text_entry.pack()
start_button.pack()

root.mainloop()

GPIO.cleanup()
