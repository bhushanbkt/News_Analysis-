import streamlit as st
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from gtts import gTTS
import io
import base64

# Download NLTK resources
nltk.download('punkt')

# Function to preprocess text
def preprocess_text(text):
    # Tokenize text into sentences
    sentences = sent_tokenize(text)
    return sentences

# Function to classify mood
def classify_mood(sentences):
    # Calculate sentiment score for each sentence
    sentiment_scores = []
    for sentence in sentences:
        # Perform sentiment analysis on the sentence (positive: +1, neutral: 0, negative: -1)
        if "good" in sentence.lower() or "great" in sentence.lower():
            sentiment_scores.append(1)
        elif "bad" in sentence.lower() or "poor" in sentence.lower():
            sentiment_scores.append(-1)
        else:
            sentiment_scores.append(0)
    
    # Aggregate sentiment scores to classify overall mood
    overall_sentiment = sum(sentiment_scores)
    if overall_sentiment > 0:
        return "Positive"
    elif overall_sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

# Function for aspect analysis
def analyze_aspects(sentences):
    # Define keywords or phrases related to each aspect
    aspect_keywords = {
        "Technology": ["technology", "tech", "innovation", "digital"],
        "Business": ["business", "finance", "economy", "investment"],
        "Health": ["health", "medical", "wellness", "nutrition"],
        "Politics": ["politics", "government", "policy", "election"]
    }

    # Initialize an empty list to store the detected aspects
    detected_aspects = []

    # Iterate over each sentence in the text
    for sentence in sentences:
        # Convert the sentence to lowercase for case-insensitive matching
        sentence_lower = sentence.lower()
        
        # Iterate over each aspect and its associated keywords
        for aspect, keywords in aspect_keywords.items():
            # Check if any of the keywords related to the aspect are present in the sentence
            if any(keyword in sentence_lower for keyword in keywords):
                detected_aspects.append(aspect)

    # Remove duplicates and return the list of detected aspects
    return list(set(detected_aspects))


# Function to find connections
def find_connections(texts):
    # Define the keywords or themes to search for
    keywords = ["technology", "business", "health", "politics"]

    # Initialize a dictionary to store the counts of each keyword/theme
    connections = {keyword.capitalize(): 0 for keyword in keywords}

    # Iterate over each text
    for text in texts:
        # Tokenize the text into words
        words = text.lower().split()
        # Count the occurrences of each keyword/theme in the text
        for keyword in keywords:
            connections[keyword.capitalize()] += words.count(keyword)

    return connections

# Function to generate summary
def generate_summary(text):
    # Parse the text using Sumy
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    
    # Initialize LSA summarizer
    summarizer = LsaSummarizer()
    
    # Summarize the text
    summary = summarizer(parser.document, sentences_count=2)  # You can adjust the number of sentences in the summary
    
    # Combine the sentences in the summary
    summary_text = " ".join([str(sentence) for sentence in summary])
    
    # Convert the summary text to speech
    tts = gTTS(summary_text)
    speech_io = io.BytesIO()
    tts.write_to_fp(speech_io)
    speech_io.seek(0)
    
    return summary_text, speech_io

# Streamlit app
def main():
    st.set_page_config(page_title="Text Mood and Aspect Analysis App", page_icon=":sunny:")
    st.title("News Analysis App: Uncover What Matters")
    st.sidebar.image('img.png')
    st.sidebar.markdown("<p style='font-family:serif;font-size:30px'>Welcome to News Analysis App! Enter a text article in the main panel to analyze its mood, aspects, and connections.", unsafe_allow_html=True)
    # st.sidebar.write("Welcome to News Analysis App! Enter a text article in the main panel to analyze its mood, aspects, and connections.")

    # Text input for user to enter the article
    text_input = st.text_area("Enter the article:", height=200)

    # Button to trigger analysis
    if st.button("Analyze"):
        # Preprocess the text into sentences
        sentences = preprocess_text(text_input)
        
        # Classify mood
        mood = classify_mood(sentences)
        st.subheader("Mood:")
        st.write(mood)

        # Perform aspect analysis
        aspects = analyze_aspects(sentences)
        st.subheader("Aspects:")
        st.write(", ".join(aspects))

        # Generate summary
        summary_text, audio_summary = generate_summary(text_input)
        st.subheader("Summary:")
        st.write(summary_text)

        # Play button for audio summary
        st.audio(audio_summary.read(), format='audio/mp3')

        # Find connections
        connections = find_connections([text_input])  # For now, we analyze only one article
        st.subheader("Connections:")
        st.write(connections)

if __name__ == "__main__":
    main()
