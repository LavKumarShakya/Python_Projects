# Morse Code Translator Flask App
# A web application that converts text to Morse code and vice versa
# Created by: Lav Kumar Shakya
# Date: July 2025

import os
from flask import Flask, render_template, request, jsonify

# Get the directory of the current script to ensure proper path resolution
basedir = os.path.abspath(os.path.dirname(__file__))

# Initialize Flask application with explicit template folder path
app = Flask(__name__, template_folder=os.path.join(basedir, 'templates'))

morse_code = {
    # Alphabet A-Z
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    
    # Numbers 0-9
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    
    # Common punctuation marks
    ',': '--..--',  
    '.': '.-.-.-',  
    '?': '..--..',  
    '/': '-..-.', 
    '-': '-....-',  
    '(': '-.--.',   
    ')': '-.--.-',  
    ' ': '/'        
}
def encrypt_message(message):
    """
    Convert text to Morse code
    
    Args:
        message (str): The text message to convert to Morse code
        
    Returns:
        str: The Morse code representation of the input text
        
    Raises:
        ValueError: If the message contains characters not supported in Morse code
        
    Process:
        1. Convert input to uppercase for consistency
        2. Iterate through each character
        3. Look up Morse code equivalent from dictionary
        4. Handle spaces by converting to '/ ' 
        5. Raise error for unknown characters that aren't in the dictionary
        6. Return the complete Morse code string
    """
    # Convert to uppercase since Morse code is case-insensitive
    message = message.upper()
    encrypted_message = ''
    invalid_chars = []  # Track invalid characters for error reporting
    
    # Process each character in the message
    for letter in message:
        if letter in morse_code:
            # Add the Morse code for this character followed by a space
            encrypted_message += morse_code[letter] + ' '
        elif letter == ' ':
            # Spaces between words are represented as '/ ' in Morse code
            encrypted_message += '/ '
        else:
            # Collect unknown characters for error reporting
            if letter not in invalid_chars:
                invalid_chars.append(letter)
    
    # Check if any invalid characters were found
    if invalid_chars:
        invalid_chars_str = ', '.join([f"'{char}'" for char in invalid_chars])
        raise ValueError(f"Invalid character(s) found: {invalid_chars_str}. Only letters, numbers, and basic punctuation (.,?/-()'') are supported in Morse code.")
    
    # Remove trailing space and return the result
    return encrypted_message.strip()

def decrypt_morse_code(message):
    """
    Convert Morse code back to readable text
    
    Args:
        message (str): The Morse code string to decode
        
    Returns:
        str: The decoded text message
        
    Raises:
        ValueError: If the message contains invalid Morse code patterns
        
    Process:
        1. Split the message by ' / ' to separate words
        2. For each word, split by spaces to get individual Morse characters
        3. Look up each Morse pattern in the dictionary to find the corresponding letter
        4. Raise error for invalid Morse code patterns
        5. Reconstruct the original text with proper spacing
        
    Expected Morse format: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    This represents: "HELLO WORLD"
    """
    # Split the message by ' / ' to separate words
    words = message.strip().split(' / ')
    decrypted_message = ""
    invalid_patterns = []  # Track invalid Morse patterns for error reporting
    
    # Process each word separately
    for word in words:
        # Split each word by spaces to get individual Morse code letters
        morse_letters = word.strip().split(' ')
        
        # Decode each Morse code letter
        for morse_letter in morse_letters:
            if morse_letter:  # Skip empty strings that might result from extra spaces
                # Search through the dictionary to find the character for this Morse code
                found = False
                for key, value in morse_code.items():
                    if morse_letter == value:
                        decrypted_message += key
                        found = True
                        break  # Found the match, move to next Morse letter
                
                # If no match was found, collect the invalid pattern
                if not found:
                    if morse_letter not in invalid_patterns:
                        invalid_patterns.append(morse_letter)
        
        # Add a space between words
        decrypted_message += ' '
    
    # Check if any invalid Morse patterns were found
    if invalid_patterns:
        invalid_patterns_str = ', '.join([f"'{pattern}'" for pattern in invalid_patterns])
        raise ValueError(f"Invalid Morse code pattern(s) found: {invalid_patterns_str}. Please check your Morse code format.")
    
    # Remove trailing space and return the decoded message
    return decrypted_message.strip()


@app.route('/')
def index():
    """
    Main page route - serves the web interface
    
    Returns:
        HTML template: The main Morse code translator web page
    """
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    """
    API endpoint for text-to-Morse code conversion
    
    Expected JSON payload:
        {
            "text": "Hello World"
        }
    
    Returns:
        JSON response:
        Success: {"encrypted": ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."}
        Error: {"error": "Error message"}, HTTP status code
    """
    try:
        # Parse JSON data from the request
        data = request.get_json()
        text = data.get('text', '')
        
        # Validate input - ensure text is provided
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        # Convert text to Morse code using our encryption function
        encrypted = encrypt_message(text)
        
        # Return successful response with Morse code
        return jsonify({'encrypted': encrypted})
    
    except ValueError as e:
        # Handle invalid character errors with specific error message
        return jsonify({'error': str(e)}), 400
    
    except Exception as e:
        # Handle any other unexpected errors and return error response
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/decrypt', methods=['POST'])
def decrypt():
    """
    API endpoint for Morse code-to-text conversion
    
    Expected JSON payload:
        {
            "morse": ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
        }
    
    Returns:
        JSON response:
        Success: {"decrypted": "HELLO WORLD"}
        Error: {"error": "Error message"}, HTTP status code
    """
    try:
        # Parse JSON data from the request
        data = request.get_json()
        morse = data.get('morse', '')
        
        # Validate input - ensure Morse code is provided
        if not morse:
            return jsonify({'error': 'No Morse code provided'}), 400
        
        # Convert Morse code to text using our decryption function
        decrypted = decrypt_morse_code(morse)
        
        # Return successful response with decoded text
        return jsonify({'decrypted': decrypted})
    
    except ValueError as e:
        # Handle invalid Morse code pattern errors with specific error message
        return jsonify({'error': str(e)}), 400
    
    except Exception as e:
        # Handle any other unexpected errors and return error response
        return jsonify({'error': f'Server error: {str(e)}'}), 500


if __name__ == '__main__':
    """
    Start the Flask development server
    
    Configuration:
        - debug=True: Enable debug mode for development (auto-reload on changes)
        - host='0.0.0.0': Allow connections from any IP address (not just localhost)
        - port=5000: Run the server on port 5000
        
    Access URLs:
        - Local: http://127.0.0.1:5000
        - Network: http://[your-ip]:5000
        
    Note: This is a development server. For production, use a WSGI server like Gunicorn.
    """
    print("🚀 Starting Morse Code Translator Flask App...")
    print("🌐 Access the app at: http://localhost:5000")
    print("✋ Press Ctrl+C to stop the server")
    
    app.run(debug=True, host='0.0.0.0', port=5000)