import streamlit as st
import pandas as pd
from datetime import datetime

# Set page config
st.set_page_config(page_title="AI SCHOLAR", layout="centered")

# Custom CSS to match the style
st.markdown("""
    <style>
    .stTextInput > label, .stTextArea > label {
        font-size: 1rem;
        color: #333;
        font-weight: 500;
    }
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: white;
        border: 1px solid #ddd;
        border-radius: 4px;
        padding: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("Submit Your Research")

# Form
with st.form("research_submission"):
    # Topic Area
    st.subheader("Topic Area")
    paper_title = st.text_input("Paper Title")
    
    # Research Objective
    st.subheader("Research Objective")
    research_objective = st.text_area("Describe your research question or objective")
    
    # Keywords
    st.subheader("Keywords")
    keywords = st.text_input("Enter 3-5 keywords, separated by commas")
    
    # Hypothesis
    st.subheader("Hypothesis")
    hypothesis = st.text_area("State your research hypothesis")
    
    # Literature Review
    st.subheader("Literature Review")
    st.markdown("Insert 3 to 5 relevant studies to your work in a BibTeX format")
    literature_review = st.text_area("Paste your BibTeX entries here")
    
    # Experiment Notes
    st.subheader("Experiment Notes")
    st.markdown("Dataset")
    dataset_source = st.text_input("Dataset source")
    dataset_size = st.text_input("Dataset size")
    key_variables = st.text_area("Key variables")
    
    # Submit button
    submitted = st.form_submit_button("Submit Research")
    
    if submitted:
        # Create a dictionary with the form data
        form_data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "paper_title": paper_title,
            "research_objective": research_objective,
            "keywords": keywords,
            "hypothesis": hypothesis,
            "literature_review": literature_review,
            "dataset_source": dataset_source,
            "dataset_size": dataset_size,
            "key_variables": key_variables
        }
        
        try:
            # Try to read existing CSV file
            df = pd.read_csv("research_submissions.csv")
        except FileNotFoundError:
            # If file doesn't exist, create new DataFrame
            df = pd.DataFrame()
        
        # Append new submission
        df = pd.concat([df, pd.DataFrame([form_data])], ignore_index=True)
        
        # Save to CSV
        df.to_csv("research_submissions.csv", index=False)
        
        st.success("Research submission saved successfully!")
        st.balloons()
