import PyPDF2
from gtts import gTTS
import os


def pdf_to_speech(pdf_file, output_file, language='en'):
    # Open the PDF file
    with open(pdf_file, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Extract text from each page of the PDF
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Create a gTTS object with the extracted text and specified language
        tts = gTTS(text, lang=language)

        # Save the speech output to a file
        tts.save(output_file)

        # Play the speech output
        os.system('start ' + output_file)  # For Windows
        # os.system('afplay ' + output_file)  # For macOS


# Example usage
pdf_file = 'example1.pdf'
output_file = 'output.mp3'
language = 'en'  # Specify the language code, e.g., 'en' for English, 'ro' for Romanian, 'fr' for French, etc.
pdf_to_speech(pdf_file, output_file, language)
