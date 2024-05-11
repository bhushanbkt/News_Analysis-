# Text Mood and Aspect Analysis App

![App Screenshot] ![Screenshot (298)](https://github.com/bhushanbkt/News_Analysis-/assets/91175596/04b820d4-69fa-454b-8b62-ed0b0b262e77)


## Introduction

This Streamlit app analyzes the mood, aspects, and connections in a given text article. It utilizes natural language processing techniques to perform sentiment analysis, aspect detection, text summarization, and connections identification, providing valuable insights to the users.

## Features

- **Mood Analysis**: Classifies the overall mood of the text as positive, negative, or neutral.
- **Aspect Analysis**: Detects various aspects present in the text, such as Technology, Business, Health, and Politics.
- **Text Summarization**: Generates a concise summary of the text article.
- **Audio Summary**: Converts the text summary into audio format, allowing users to listen to it.
- **Connections Identification**: Identifies connections related to key themes or topics present in the text.

## How to Use

1. **Clone the Repository**:

    ```bash
    https://github.com/bhushanbkt/News_Analysis
    ```

2. **Install Dependencies**:

    Navigate to the project directory and install the required Python libraries:

    ```bash
    pip install -r req.txt
    ```

3. **Run the App**:

    Execute the following command to run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

    The app will be launched in your default web browser.

4. **Input Text**:

    Enter the text article you want to analyze in the text area provided.

5. **Analyze**:

    Click on the "Analyze" button to trigger the analysis process.
![Screenshot (299)](https://github.com/bhushanbkt/News_Analysis-/assets/91175596/f59d3fff-731e-40db-a91a-4e86a8b85629)

6. **View Results**:

    - Mood Analysis: The detected mood (positive, negative, or neutral).
    - Aspect Analysis: The detected aspects present in the text.
    - Text Summary: A concise summary of the text article.
    - Audio Summary: Play the audio summary generated from the text.
    - Connections Identification: Connections related to key themes or topics in the text.

## Tools/Libraries Used

- **Streamlit**: Used to create the web application interface.
- **NLTK (Natural Language Toolkit)**: Utilized for text preprocessing and tokenization.
- **Sumy**: Employed for text summarization.
- **gTTS (Google Text-to-Speech)**: Used to convert text summaries into audio.

