import streamlit as st  # Importing Streamlit for creating the web interface
import ollama  # Importing the Ollama library for OCR text extraction
from PIL import Image  # Importing the Python Imaging Library for image handling

# Configure the page settings
st.set_page_config(
    page_title="Advanced OCR Tool",  # Set the title of the page
    layout="wide",  # Set the layout to wide for better visibility
    initial_sidebar_state="expanded"  # Expand the sidebar by default
)

# Title and description
st.title("OCR Text Extraction Tool")  # Display the main title of the application

# Clear button implementation
col1, col2 = st.columns([6, 1])  # Divide the layout into two columns
with col2:
    if st.button("Reset"):  # Add a button labeled "Reset"
        if 'extracted_text' in st.session_state:  # Check if extracted text exists in session state
            del st.session_state['extracted_text']  # Delete the extracted text from session state
        st.experimental_rerun()  # Refresh the page

st.markdown('<p style="margin-top: -20px;">Easily extract and structure text content from images!</p>', unsafe_allow_html=True)  # Add a descriptive text below the title
st.markdown("---")  # Add a horizontal line separator

# Sidebar for file upload
with st.sidebar:
    st.header("Upload Your Image")  # Add a header in the sidebar for file upload
    uploaded_image = st.file_uploader("Select an image file (PNG, JPG, JPEG):", type=['png', 'jpg', 'jpeg'])  # Create a file uploader for image files

    if uploaded_image is not None:  # Check if an image is uploaded
        img = Image.open(uploaded_image)  # Open the uploaded image
        st.image(img, caption="Uploaded Image")  # Display the uploaded image with a caption

        if st.button("Process Text"):  # Add a button labeled "Process Text"
            with st.spinner("Analyzing the image, please wait..."):  # Show a spinner while processing
                try:
                    response = ollama.chat(  # Call the Ollama chat API for OCR processing
                        model='llama3.2-vision',  # Specify the OCR model to use
                        messages=[{
                            'role': 'user',  # Define the role of the message sender
                            'content': """Please extract and structure the text content from the provided image.
                                        Ensure the output is formatted properly with headings, lists, or code blocks
                                        as needed for clarity and organization.""",  # Instruction for the OCR model
                            'images': [uploaded_image.getvalue()]  # Pass the uploaded image content
                        }]
                    )
                    st.session_state['extracted_text'] = response.message.content  # Save the extracted text in session state
                except Exception as e:  # Handle any exceptions
                    st.error(f"An error occurred during processing: {str(e)}")  # Display an error message

# Display the extracted text
if 'extracted_text' in st.session_state:  # Check if extracted text exists in session state
    st.markdown(st.session_state['extracted_text'])  # Display the extracted text in markdown format
else:
    st.info("Upload an image and click 'Process Text' to see the results here.")  # Show an informational message if no text is extracted
