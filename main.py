morse_dict = {
    'A': ' .-', 'B': ' -...', 'C': ' -.-.', 'D': ' -..', 'E': ' .', 'F': ' ..-.', 'G': ' --.', 'H': ' ....',
    'I': ' ..', 'J': ' .---', 'K': ' -.-', 'L': ' .-..', 'M': ' --', 'N': ' -.', 'O': ' ---', 'P': ' .--.',
    'Q': ' --.-', 'R': ' .-.', 'S': ' ...', 'T': ' -', 'U': ' ..-', 'V': ' ...-', 'W': ' .--', 'X': ' -..-',
    'Y': ' -.--', 'Z': ' --..', '0': ' -----', '1': ' .----', '2': ' ..---', '3': ' ...--', '4': ' ....-',
    '5': ' .....', '6': ' -....', '7': ' --...', '8': ' ---..', '9': ' ----.', '.': ' .-.-.-', ',': ' --..--',
    '?': ' ..--..', "'": ' .----.', '!': ' -.-.--', '/': '-..-.', '(': ' -.--.', ')': ' -.--.-', '&': ' .-...',
    ':': ' ---...', ';': ' -.-.-.', '=': ' -...-', '+': ' .-.-.', '-': ' -....-', '_': ' ..--.-', '"': ' .-..-.',
    '$': ' ...-..-', '@': ' .--.-.', ' ': '/'
}

def into_morse(message):
  morse_code = ""
  for char in message.upper():
    if char in morse_dict:
      morse_code += morse_dict[char] + ""
  return morse_code

def main():
  message = input("Enter your message: ")
  print("Original Message: ", message)
  print("Morse Code: ", into_morse(message)) 
main()
