import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from streamlit_lottie import st_lottie
import numpy as np
import time
from PIL import Image
import base64
import requests

st.set_page_config(
    page_title="MediPredixt Lab",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)
def local_css():
    st.markdown("""
    <style>
    /* Main Styles */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Header Styles */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        background-color: white;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .logo-container {
        display: flex;
        align-items: center;
    }
    
    .nav-links {
        display: flex;
        gap: 2rem;
    }
    
    .nav-link {
        color: #333;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s ease;
    }
    
    .nav-link:hover {
        color: #4361ee;
    }
    
    .auth-buttons {
        display: flex;
        gap: 1rem;
    }
    
    .btn {
        padding: 0.5rem 1.5rem;
        border-radius: 5px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .btn-login {
        background-color: transparent;
        border: 1px solid #4361ee;
        color: #4361ee;
    }
    
    .btn-login:hover {
        background-color: #4361ee;
        color: white;
    }
    
    .btn-signup {
        background-color: #4361ee;
        color: white;
        border: none;
    }
    
    .btn-signup:hover {
        background-color: #3a56d4;
    }
    
    /* Hero Section */
    .hero-section {
        display: flex;
        align-items: center;
        padding: 2rem;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        margin-bottom: 2rem;
    }
    
    .hero-content {
        flex: 1;
        padding-right: 2rem;
    }
    
    .hero-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #333;
        margin-bottom: 1rem;
    }
    
    .hero-description {
        font-size: 1.1rem;
        color: #666;
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    
    .hero-buttons {
        display: flex;
        gap: 1rem;
    }
    .btn-primary {
        background-color: #4361ee;
        color: white;
        padding: 0.8rem 2rem;
        border-radius: 5px;
        font-weight: 600;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
    }
    
    .btn-primary:hover {
        background-color: #3a56d4;
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(67, 97, 238, 0.3);
    }
    
    .btn-secondary {
        background-color: transparent;
        color: white;
        padding: 0.8rem 2rem;
        border-radius: 5px;
        font-weight: 600;
        border: 1px solid #4361ee;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
    }
    
    .btn-secondary:hover {
        background-color: #f0f3ff;
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(67, 97, 238, 0.1);
    }
    
    .hero-image {
        flex: 1;
        display: flex;
        justify-content: center;
    }
    
    /* Features Section */
    .section-title {
        font-size: 2rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        color: #333;
    }
    
    .features-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 2rem;
        margin-bottom: 2rem;
    }
    
    .feature-card {
        background-color: white;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
    }
    
    .feature-icon {
        font-size: 2.5rem;
        color: #4361ee;
        margin-bottom: 1rem;
    }
    
    .feature-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #333;
    }
    
    .feature-description {
        color: #666;
        line-height: 1.6;
    }
    
    /* About Section */
    .about-section {
        background-color: white;
        border-radius: 10px;
        padding: 3rem;
        margin-bottom: 2rem;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    }
    
    .vision-mission-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 2rem;
        margin-top: 2rem;
    }
    
    .vision-card, .mission-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03);
    }
    
    .card-title {
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #333;
        display: flex;
        align-items: center;
    }
    
    .card-title i {
        margin-right: 1rem;
        color: #4361ee;
    }
    
    .card-content {
        color: #666;
        line-height: 1.6;
    }
    
    /* Team Section */
    .team-section {
        margin-bottom: 2rem;
    }
    
    .team-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 2rem;
    }
    
    .team-card {
        background-color: white;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    .team-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
    }
    
    .team-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
    }
    
    .team-info {
        padding: 1.5rem;
    }
    
    .team-name {
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: #333;
    }
    
    .team-position {
        color: #4361ee;
        font-weight: 500;
        margin-bottom: 1rem;
    }
    
    .team-bio {
        color: #666;
        font-size: 0.9rem;
        line-height: 1.6;
    }
    
    .team-social {
        display: flex;
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .social-icon {
        color: #4361ee;
        font-size: 1.2rem;
        transition: transform 0.3s ease;
    }
    
    .social-icon:hover {
        transform: scale(1.2);
    }
    
    /* Footer */
    .footer {
        background-color: #333;
        color: white;
        padding: 3rem 2rem;
        border-radius: 10px;
    }
    
    .footer-content {
        display: grid;
        grid-template-columns: 2fr 1fr 1fr 1fr;
        gap: 2rem;
    }
    
    .footer-logo {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .footer-description {
        color: #ccc;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    .footer-social {
        display: flex;
        gap: 1rem;
    }
    
    .footer-title {
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
    }
    
    .footer-links {
        display: flex;
        flex-direction: column;
        gap: 0.8rem;
    }
    
    .footer-link {
        color: #ccc;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    
    .footer-link:hover {
        color: #4361ee;
    }
    
    .footer-bottom {
        margin-top: 2rem;
        padding-top: 2rem;
        border-top: 1px solid #444;
        text-align: center;
        color: #ccc;
    }
    
    /* Animation */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .animated {
        animation: fadeIn 1s ease-out;
    }
    
    /* Prediction Cards */
    .prediction-cards {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 2rem;
        margin-bottom: 2rem;
    }
    
    .prediction-card {
        background-color: white;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    
    .prediction-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
    }
    
    .prediction-icon {
        font-size: 3rem;
        color: #4361ee;
        margin-bottom: 1rem;
    }
    
    .prediction-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #333;
    }
    
    .prediction-description {
        color: #666;
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }
    
    /* Hover effects for buttons */
    .hover-effect {
        transition: all 0.3s ease;
    }
    
    .hover-effect:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(67, 97, 238, 0.2);
    }
    
    /* Custom Streamlit Elements */
    .stButton>button {
        background-color: #4361ee;
        color: white;
        border: none;
        padding: 0.8rem 2rem;
        font-weight: 600;
        border-radius: 5px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #3a56d4;
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(67, 97, 238, 0.3);
    }
    
    div.stSelectbox>div>div {
        background-color: white;
        border: 1px solid #ddd;
        border-radius: 5px;
    }
    
    div.stTextInput>div>div>input {
        background-color: white;
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    
    div.stNumberInput>div>div>input {
        background-color: white;
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    
    .css-1d391kg, .css-12oz5g7 {
        padding: 2rem 1rem;
    }
    .header {
    text-align: center;
    padding: 2rem 0;
    background: linear-gradient(135deg, #4682B4 0%, #1E90FF 100%);

    border-radius: 15px;
    margin-bottom: 2rem;
    color: white;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
    }
    </style>
    """, unsafe_allow_html=True)

def render_html(html_content):
    components.html(html_content, height=50)

def apply_custom_styles():
    st.markdown("""
        <style>
            /* Fix the black input field issue */
            div[data-testid="stNumberInput"] input {
                background-color: white !important;
                color: black !important;
                border-radius: 5px !important;
            }
            div[data-testid="stSlider"] .st-br {
                background-color: white !important;
            }
        </style>
    """, unsafe_allow_html=True)

apply_custom_styles()

def main():
    local_css()
    # create_vision_mission()
    # create_about_section()
    st.markdown('<div class="header animate"><h1 style="font-size: 3rem;">MediPredixt</h1><p style="font-size: 1.5rem;">Advanced Machine Learning Lab Prediction System</p></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="navbar">
        <div class="logo-container">
        </div>
        <div class="nav-links"> 
            <a href="#" class="nav-link">Home</a>
            <a href="#features" class="nav-link">Features</a>
            <a href="#about" class="nav-link">About</a>
            <a href="#team" class="nav-link">Team</a>
            <a href="#support" class="nav-link">Support</a>
        </div>
        <div class="auth-buttons">
            <button class="btn btn-login">Log In</button>
            <button class="btn btn-signup">Sign Up</button>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Hero Section
    st.markdown("""
    <div class="hero-section animated">
        <div class="hero-content">
            <h1 class="hero-title">Advanced AI-Powered Health Predictions</h1>
            <p class="hero-description">
                MediPredixt Lab uses cutting-edge machine learning algorithms to predict cancer and diabetes risks with high accuracy. Our platform is designed to assist healthcare professionals and individuals in early detection and prevention.
            </p>
            <div class="hero-buttons">
                <a href="#predict-cancer" class="btn-secondary hover-effect">Predict Cancer</a>
                <a href="#predict-diabetes" class="btn-secondary hover-effect">Predict Diabetes</a>
            </div>
        </div>
        <div class="hero-image">
            <lottie-player src="https://assets3.lottiefiles.com/packages/lf20_5njmohct.json" background="transparent" speed="1" style="width: 300px; height: 300px;" loop autoplay></lottie-player>
        </div>
    </div>
    """,unsafe_allow_html=True)
    
    # Add Lottie animation script
    components.html("""
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    """, height=0)
    
    # Prediction Cards
    st.markdown('<h2 class="section-title" id="predictions">Our Prediction Services</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="prediction-cards animated">
        <div class="prediction-card" id="predict-cancer">
            <div class="prediction-icon">🔬</div>
            <h3 class="prediction-title">Cancer Risk Prediction</h3>
            <p class="prediction-description">
                Using advanced machine learning models trained on extensive medical data, our system can analyze various parameters to predict cancer risk with high accuracy.
            </p>
        </div>
        <div class="prediction-card" id="predict-diabetes">
            <div class="prediction-icon">📊</div>
            <h3 class="prediction-title">Diabetes Risk Assessment</h3>
            <p class="prediction-description">
                Our diabetes prediction model analyzes critical health parameters to provide an accurate assessment of diabetes risk, enabling early intervention.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Prediction Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Predict Cancer Risk"):
            st.success("Redirecting to Cancer Risk Prediction module...")
            time.sleep(1)
            st.switch_page("pages/cancer.py")
            
    with col2:
        if st.button("Predict Diabetes Risk"):
            st.success("Redirecting to Diabetes Risk Prediction module...")
            time.sleep(1)
            st.switch_page("pages/diabetes.py")
    st.markdown('<h2 class="section-title" id="features">Key Features</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="features-container animated">
        <div class="feature-card">
            <div class="feature-icon">🧠</div>
            <h3 class="feature-title">Advanced AI Models</h3>
            <p class="feature-description">
                Our platform leverages state-of-the-art machine learning algorithms to provide accurate predictions based on input parameters.
            </p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🔒</div>
            <h3 class="feature-title">Data Security</h3>
            <p class="feature-description">
                We prioritize the security and privacy of your health data with enterprise-grade encryption and compliance with health data regulations.
            </p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">📱</div>
            <h3 class="feature-title">User-Friendly Interface</h3>
            <p class="feature-description">
                Easy to use interface designed for both healthcare professionals and individuals with intuitive controls and clear results.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    def create_about_section():
        st.markdown("""
        <div id="about" class="animated delay-3">
            <h2 style="text-align: center; margin: 60px 0 30px;">About MediPredixt</h2>
            <p style="font-size: 1.1rem; line-height: 1.6; max-width: 900px; margin: 0 auto;">
                MediPredixt is a revolutionary healthcare technology platform leveraging the power of artificial intelligence 
                and machine learning to predict disease risks. Founded in 2024, our mission is to make preventive healthcare 
                accessible to everyone through cutting-edge technology.
            </p>
            <p style="font-size: 1.1rem; line-height: 1.6; max-width: 900px; margin: 20px auto 0;">
                Our team of healthcare professionals, data scientists, and AI experts has developed proprietary algorithms 
                that can analyze patient data to predict the risk of diseases like cancer and diabetes with high accuracy. 
                By identifying risks early, we help patients and healthcare providers take preventive measures before conditions worsen.
            </p>
        </div>
    """, unsafe_allow_html=True)

# Create Vision & Mission
    def create_vision_mission():
        st.markdown("""
        <div id="vision-mission" class="vision-mission animated delay-4">
            <div class="vision">
                <h2>Our Vision</h2>
                <p>To revolutionize healthcare by making predictive health assessments accessible to everyone, 
                regardless of location or socioeconomic status.</p>
                <p>We envision a world where preventable diseases are detected early, 
                leading to better treatment outcomes and improved quality of life.</p>
            </div>
            <div class="mission">
                <h2>Our Mission</h2>
                <p>To develop and deploy cutting-edge machine learning algorithms that predict disease risks 
                with unprecedented accuracy.</p>
                <p>To bridge the gap between technology and healthcare, creating tools that empower both 
                patients and healthcare providers to make informed decisions.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
        
    def display_team_section():
        st.markdown('<h2 class="section-title" id="team">Our Expert Team</h2>', unsafe_allow_html=True)
    
    # Create columns for team members
    st.markdown("""
    <style>
    .team-section {
        margin-bottom: 2rem;
    }
    .team-card {
        background-color: white;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        height: 100%;
    }
    .team-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
    }
    .team-info {
        padding: 1.5rem;
    }
    .team-name {
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: #333;
    }
    .team-position {
        color: #4361ee;
        font-weight: 500;
        margin-bottom: 1rem;
    }
    .team-bio {
        color: #666;
        font-size: 0.9rem;
        line-height: 1.6;
    }
    .team-social {
        margin-top: 1rem;
    }
    .social-link {
        color: #4361ee;
        margin-right: 10px;
        text-decoration: none;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create a 2x2 grid for team members
    col1, col2 = st.columns(2)
    
    # First row
    with col1:
        st.markdown("""
        <div class="team-card">
            <img src="me.jpg" width="100%" height="200" style="object-fit: cover;">
            <div class="team-info">
                <h3 class="team-name">Manas Borse</h3>
                <p class="team-position">Team Lead</p>
                <p class="team-bio">
                    Manas leads our medical research team with over 15 years of experience in oncology and preventive medicine.
                </p>
                <div class="team-social">
                    <a href="linkedin.com/in/manas-borse-485028257/" class="social-link">LinkedIn</a>
                    <a href="#" class="social-link">Twitter</a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="team-card">
            <img src="https://source.unsplash.com/featured/?programmer" width="100%" height="200" style="object-fit: cover;">
            <div class="team-info">
                <h3 class="team-name">Alex Chen</h3>
                <p class="team-position">AI Research Lead</p>
                <p class="team-bio">
                    Alex specializes in machine learning algorithms for medical diagnostics with a Ph.D. in Computational Biology.
                </p>
                <div class="team-social">
                    <a href="#" class="social-link">LinkedIn</a>
                    <a href="#" class="social-link">Github</a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Second row
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("""
        <div class="team-card">
            <img src="https://source.unsplash.com/featured/?scientist" width="100%" height="200" style="object-fit: cover;">
            <div class="team-info">
                <h3 class="team-name">Dr. Michael Rodriguez</h3>
                <p class="team-position">Data Science Director</p>
                <p class="team-bio">
                    Dr. Rodriguez brings expertise in statistical modeling and health data analytics with 10+ years in epidemiology.
                </p>
                <div class="team-social">
                    <a href="#" class="social-link">LinkedIn</a>
                    <a href="#" class="social-link">ResearchGate</a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="team-card">
            <img src="https://source.unsplash.com/featured/?designer" width="100%" height="200" style="object-fit: cover;">
            <div class="team-info">
                <h3 class="team-name">Emily Parker</h3>
                <p class="team-position">UX/UI Lead</p>
                <p class="team-bio">
                    Emily ensures our platform is accessible, intuitive, and effective for users of all technical backgrounds.
                </p>
                <div class="team-social">
                    <a href="#" class="social-link">LinkedIn</a>
                    <a href="#" class="social-link">Dribbble</a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def footer():
    """Footer section for MediPredixt website"""
    st.markdown("""---""")
    
    cols = st.columns([1, 1, 1, 1])
    
    with cols[0]:
        st.markdown("### MediPredixt")
        st.markdown("Revolutionizing healthcare with AI-powered disease prediction")
        
        # Social media icons with hover effects (using custom CSS)
        st.markdown("""
        <div class="social-icons">
            <a href="#" class="social-icon"><i class="fab fa-facebook-f"></i></a>
            <a href="#" class="social-icon"><i class="fab fa-twitter"></i></a>
            <a href="#" class="social-icon"><i class="fab fa-linkedin-in"></i></a>
            <a href="#" class="social-icon"><i class="fab fa-instagram"></i></a>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("### Quick Links")
        st.markdown("""
        * [Home](#)
        * [Our Services](#)
        * [About Us](#)
        * [Cancer Prediction](#)
        * [Diabetes Prediction](#)
        * [Team](#)
        """)
    
    with cols[2]:
        st.markdown("### Contact Us")
        st.markdown("""
        **Address:** Medical Technology Park,  
        Innovation Avenue, Health District
        
        **Email:** info@medipredixt.com
        
        **Phone:** +1 (800) 555-MEDI
        """)
    
    with cols[3]:
        st.markdown("### Newsletter")
        st.text_input("Email Address")
        st.button("Subscribe", key="footer_subscribe")
        st.markdown("Stay updated with our latest research and innovations")
    
    # Copyright row
    st.markdown("""
    <div class="copyright">
        <p>© 2025 MediPredixt Lab. All Rights Reserved. <a href="#">Privacy Policy</a> | <a href="#">Terms of Service</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Add custom CSS for footer styling
    st.markdown("""
    <style>
        .social-icons {
            display: flex;
            gap: 15px;
            margin-top: 15px;
        }
        
        .social-icon {
            background-color: #f0f2f6;
            color: #4e89ae;
            width: 35px;
            height: 35px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            transition: all 0.3s ease;
        }
        
        .social-icon:hover {
            background-color: #4e89ae;
            color: white;
            transform: translateY(-3px);
        }
        
        .copyright {
            text-align: center;
            padding-top: 20px;
            margin-top: 30px;
            border-top: 1px solid #eee;
            font-size: 14px;
        }
        
        .copyright a {
            color: #4e89ae;
            text-decoration: none;
            transition: color 0.3s ease;
        }
        
        .copyright a:hover {
            color: #2a5d82;
            text-decoration: underline;
        }
        
        /* Make footer sticky */
        footer {
            margin-top: auto;
        }
    </style>
    """, unsafe_allow_html=True)

# Cancer Prediction Form
def render_cancer_prediction():
    st.markdown('<h3 class="section-title">Cancer Risk Prediction</h3>', unsafe_allow_html=True)
    
    with st.form("cancer_prediction_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
        <div class="hover-card animate-delay-2">
            <h3>Cancer Prediction</h3>
            <p>Our cancer prediction model analyzes various biomarkers and patient data to assess cancer risk with high accuracy. Early detection is crucial for successful treatment.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Predict Cancer Now 😊"):
            st.switch_page("pages/cancer.py")
        
        with col2:
           st.markdown("""
        <div class="hover-card animate-delay-2">
            <h3>Diabetes Prediction</h3>
            <p>The diabetes prediction system evaluates key health indicators to determine diabetes risk factors and provide early warning for preventive measures.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Predict Diabetes Now 😊",type="secondary"):
            st.switch_page("pages/diabetes.py")
if __name__ == "__main__":
    main()
    footer()
      
