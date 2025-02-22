# OCR Text Extraction Tool

---

## Overview
This application is a simple OCR (Optical Character Recognition) text extraction tool built with Streamlit. It allows users to upload image files and extract readable text content from them. The extracted text is displayed in a structured and user-friendly format.

---

## Features
- **Image Uploading**: Users can upload image files in PNG, JPG, or JPEG formats.
- **Text Extraction**: Automatically extracts and structures text content from uploaded images.
- **Interactive Interface**: Provides a user-friendly interface with clear buttons for actions like resetting and processing images.
- **Session Management**: Maintains the extracted text within the session until reset.

---

## Design and Approach
### Application Workflow
1. **Image Upload**: Users upload an image file through the sidebar.
2. **Image Display**: The uploaded image is displayed for preview.
3. **Text Processing**: Upon clicking the "Process Text" button, the application:
    - Analyzes the image using the Ollama API.
    - Extracts text and formats it for clarity.
4. **Text Display**: The extracted text is displayed in the main content area.
5. **Reset Functionality**: Users can clear the extracted text and reset the session using the "Reset" button.

### Context Management
- The application stores extracted text in the session state for seamless user interaction.
- The "Reset" button clears the session state and refreshes the application.

---

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- API keys for:
  - Ollama

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Harshini1909/OCR-Text-Extraction-Tool.git
   cd OCR-Text-Extraction-Tool
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Keys**:
   Create a `.env` file in the project root with the following structure:
   ```
   OLLAMA_API_KEY="your_ollama_api_key"
   ```

5. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

---

## Usage Instructions
1. Launch the application by running:
   ```bash
   streamlit run app.py
   ```
2. Use the file uploader in the sidebar to upload an image file (PNG, JPG, or JPEG).
3. Click "Process Text" to extract text from the image.
4. View the extracted text in the main content area.
5. Use the "Reset" button to clear the extracted text and reset the session.

---

## Enhancements and Future Improvements
- **Additional Image Formats**: Extend support for other image types like BMP and GIF.
- **Language Support**: Add multilingual OCR capabilities.
- **Advanced Formatting**: Improve text structuring with semantic analysis.
- **UI Enhancements**: Introduce a progress bar and drag-and-drop file upload functionality.

---

## Acknowledgments
This project utilizes the following tools and libraries:
- **[Streamlit](https://streamlit.io/)**: For building an interactive web application.
- **[Pillow](https://pillow.readthedocs.io/en/stable/)**: For handling image uploads and processing.
- **[Ollama API](https://ollama.ai/)**: For OCR text extraction.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

