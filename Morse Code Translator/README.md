# Morse Code Translator Flask App

A modern, responsive web application for converting text to Morse code and vice versa.

## Features

- 🔤 **Text to Morse Code**: Convert any text message to Morse code
- 📡 **Morse Code to Text**: Decode Morse code back to readable text  
- 📱 **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- 📊 **Reference Chart**: Built-in Morse code reference for all letters and numbers
- ⚡ **Real-time Processing**: Fast conversion with loading indicators
- 🎨 **Modern UI**: Beautiful gradient design with smooth animations

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application:**
   ```bash
   python Morse_Code_Translator.py
   ```

4. **Open your web browser and go to:**
   ```
   http://localhost:5000
   ```

## Usage

### Text to Morse Code
1. Enter your text in the "Text to Morse Code" section
2. Click "Convert to Morse" button
3. The Morse code will appear in the result area

### Morse Code to Text
1. Enter Morse code in the "Morse Code to Text" section
2. Use spaces between letters and `/` for word breaks
3. Click "Convert to Text" button
4. The decoded text will appear in the result area

### Keyboard Shortcuts
- **Ctrl + Enter**: Convert text/Morse code in the focused textarea

## File Structure

```
Morse Code Translator/
├── Morse_Code_Translator.py    # Main Flask application
├── requirements.txt            # Python dependencies
├── templates/
│   └── index.html             # HTML template
└── README.md                  # This file
```

## API Endpoints

### POST /encrypt
Convert text to Morse code
- **Body**: `{"text": "Hello World"}`
- **Response**: `{"encrypted": ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."}`

### POST /decrypt  
Convert Morse code to text
- **Body**: `{"morse": ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."}`
- **Response**: `{"decrypted": "HELLO WORLD"}`

## Morse Code Format

- **Letters**: Separated by spaces
- **Words**: Separated by ` / ` (space-slash-space)
- **Example**: `HELLO WORLD` → `.... . .-.. .-.. --- / .-- --- .-. .-.. -..`

## Supported Characters

- **Letters**: A-Z
- **Numbers**: 0-9  
- **Punctuation**: `,` `.` `?` `/` `-` `(` `)`
- **Spaces**: Converted to `/` in Morse code

## Development

The app is built with:
- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Icons**: Font Awesome
- **Styling**: CSS Grid, Flexbox, CSS animations

## License

This project is open source and available under the MIT License.
