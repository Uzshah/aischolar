import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI SCHOLAR",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 0rem;
    }
    .hero {
        background: linear-gradient(135deg, #8B3FDB 0%, #4C1D95 100%);
        padding: 4rem 2rem;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    .feature-icon {
        font-size: 2rem;
        color: #8B3FDB;
        margin-bottom: 1rem;
    }
    .button-primary {
        background-color: white;
        color: #8B3FDB;
        padding: 0.5rem 2rem;
        border-radius: 4px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin-top: 1rem;
    }
    .check-icon {
        color: #10B981;
        margin-right: 0.5rem;
    }
    .stButton>button {
        background-color: white;
        color: #8B3FDB;
        font-weight: bold;
        padding: 0.5rem 2rem;
        border-radius: 4px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero">
        <h1>YOU DISCOVER, WE DELIVER</h1>
        <p>Transform your scientific research into publication-ready papers. 
        Let our AI-powered platform handle the writing while you focus on discovery.</p>
    </div>
""", unsafe_allow_html=True)

# Start Now button that redirects to Submit Research page
if st.button("Start Now →"):
    st.switch_page("pages/1_Submit_Research.py")

# Why Choose Section
st.markdown("<h2 style='text-align: center; margin-bottom: 2rem;'>Why Choose MADLAB SCIENCE?</h2>", 
            unsafe_allow_html=True)

# Features Section
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🧠</div>
            <h3>AI-Powered Writing</h3>
            <p>Our advanced AI understands your research and crafts compelling scientific narratives.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📝</div>
            <h3>Structured Input</h3>
            <p>Clear, guided prompts ensure all critical research data is captured accurately.</p>
            <p><span class="check-icon">✓</span> Step-by-step guidance</p>
            <p><span class="check-icon">✓</span> Research templates</p>
            <p><span class="check-icon">✓</span> Data validation</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔬</div>
            <h3>Scientific Focus</h3>
            <p>Specialized in academic writing across various scientific disciplines.</p>
            <p><span class="check-icon">✓</span> Peer-reviewed standards</p>
            <p><span class="check-icon">✓</span> Scientific accuracy</p>
            <p><span class="check-icon">✓</span> Domain-specific expertise</p>
        </div>
    """, unsafe_allow_html=True)

# FAQ Section
st.markdown("<h2 style='text-align: center; margin: 3rem 0;'>Frequently Asked Questions</h2>", 
            unsafe_allow_html=True)

with st.expander("What is MadLab?"):
    st.write("""
        MadLab is an AI-powered platform designed to help researchers transform their 
        scientific discoveries into publication-ready papers. We combine advanced AI technology 
        with scientific expertise to streamline the academic writing process.
    """)

# Header navigation using session state
if 'email' not in st.session_state:
    st.session_state.email = "uzairshahmd@gmail.com"

# Header navigation
header_col1, header_col2, header_col3, header_col4 = st.columns([1, 1, 2, 1])
with header_col1:
    st.markdown("[Home](#)")
with header_col2:
    if st.button("Submit Research"):
        st.switch_page("pages/1_Submit_Research.py")
with header_col3:
    st.markdown(f"[{st.session_state.email}](#)")
with header_col4:
    if st.button("Logout"):
        st.session_state.clear()
        st.rerun()
