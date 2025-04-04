import streamlit as st
import numpy as np
import joblib
import time
import io
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from fpdf import FPDF

model = joblib.load("diabetes_model.pkl")

st.set_page_config(
    page_title="Diabetes Risk Assessment",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown(
    """
    <style>
        .main {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 15px;
        }
        .stApp {
            background-image: linear-gradient(to bottom right, #ffffff, #f0f2f6);
        }
        .result-green {
            color: #28a745;
            font-size: 24px;
            font-weight: bold;
            padding: 20px;
            border-radius: 10px;
            background-color: rgba(40, 167, 69, 0.1);
            text-align: center;
            margin: 20px 0;
        }
        .result-red {
            color: #dc3545;
            font-size: 24px;
            font-weight: bold;
            padding: 20px;
            border-radius: 10px;
            background-color: rgba(220, 53, 69, 0.1);
            text-align: center;
            margin: 20px 0;
        }
        .alert-box {
            background-color: rgba(220, 53, 69, 0.15);
            padding: 15px;
            border-radius: 10px;
            color: #dc3545;
            font-weight: bold;
            border-left: 5px solid #dc3545;
            margin: 20px 0;
        }
        .info-box {
            background-color: rgba(13, 110, 253, 0.1);
            padding: 15px;
            border-radius: 10px;
            color: #0d6efd;
            border-left: 5px solid #0d6efd;
            margin: 20px 0;
        }
        .title-container {
            text-align: center;
            padding: 20px 0;
            margin-bottom: 30px;
            background-color: #ffffff;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .input-section {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .results-section {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .sidebar-content {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            margin-bottom: 15px;
        }
        .stButton>button {
            width: 100%;
            border-radius: 50px;
            height: 50px;
            font-weight: bold;
        }
        .predict-button>button {
            background-color: #0d6efd;
            color: white;
        }
        .reset-button>button {
            background-color: #6c757d;
            color: white;
        }
        .footer {
            text-align: center;
            padding: 20px;
            color: #6c757d;
            font-size: 0.8rem;
        }
        .icon-text {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }
        .avatar {
            text-align: center;
            margin: 30px 0;
        }
        .progress-bar {
            height: 15px;
            border-radius: 10px;
            background-color: #e9ecef;
            margin-bottom: 20px;
        }
        .progress-bar-fill {
            height: 100%;
            border-radius: 10px;
            text-align: center;
            color: white;
            font-weight: bold;
            line-height: 15px;
            font-size: 0.7rem;
        }
        .card {
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            margin-bottom: 15px;
            background-color: white;
        }
        .tip-card {
            background-color: #f8f9fa;
            border-left: 4px solid #0d6efd;
            padding: 10px 15px;
            margin-bottom: 10px;
            border-radius: 5px;
        }
        .metric-card {
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            padding: 20px;
            text-align: center;
            transition: transform 0.3s;
        }
        .metric-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .metric-value {
            font-size: 24px;
            font-weight: bold;
            color: #0d6efd;
        }
        .metric-label {
            color: #6c757d;
            font-size: 14px;
        }
        .range-info {
            font-size: 12px;
            color: #6c757d;
            margin-top: 5px;
        }
        .header-image {
            display: block;
            margin: 0 auto;
            max-width: 100%;
            border-radius: 10px;
        }
        .info-section {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .comparison-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        .comparison-table th, .comparison-table td {
            border: 1px solid #dee2e6;
            padding: 12px;
            text-align: left;
        }
        .comparison-table th {
            background-color: #f8f9fa;
            font-weight: bold;
        }
        .comparison-table tr:nth-child(even) {
            background-color: #f8f9fa;
        }
        .stat-box {
            background-color: #0d6efd;
            color: white;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            margin-bottom: 20px;
        }
        .stat-number {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .risk-factor-card {
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            padding: 20px;
            margin-bottom: 20px;
            border-left: 5px solid #0d6efd;
        }
        .risk-factor-title {
            color: #0d6efd;
            font-weight: bold;
            font-size: 18px;
            margin-bottom: 10px;
        }
        .expandable-section {
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
        }
        .timeline {
            position: relative;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px 0;
        }
        .timeline::after {
            content: '';
            position: absolute;
            width: 6px;
            background-color: #0d6efd;
            top: 0;
            bottom: 0;
            left: 50%;
            margin-left: -3px;
        }
        .timeline-item {
            padding: 10px 40px;
            position: relative;
            width: 50%;
            box-sizing: border-box;
        }
        .timeline-item::after {
            content: '';
            position: absolute;
            width: 20px;
            height: 20px;
            right: -10px;
            background-color: white;
            border: 4px solid #0d6efd;
            top: 15px;
            border-radius: 50%;
            z-index: 1;
        }
        .left {
            left: 0;
        }
        .right {
            left: 50%;
        }
        .right::after {
            left: -10px;
        }
        .timeline-content {
            padding: 20px;
            background-color: white;
            position: relative;
            border-radius: 6px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        /* Tooltip styling */
        .tooltip {
            position: relative;
            display: inline-block;
            cursor: help;
        }
        .tooltip .tooltiptext {
            visibility: hidden;
            width: 200px;
            background-color: #555;
            color: #fff;
            text-align: center;
            border-radius: 6px;
            padding: 5px;
            position: absolute;
            z-index: 1;
            bottom: 125%;
            left: 50%;
            margin-left: -100px;
            opacity: 0;
            transition: opacity 0.3s;
        }
        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
    </style>
    """,
    unsafe_allow_html=True
)

if "reset_flag" not in st.session_state:
    st.session_state.reset_flag = True

def reset_inputs():
    st.session_state.age = 30
    st.session_state.glucose = 85
    st.session_state.activity = 3
    st.session_state.bp = 120
    st.session_state.bmi = 22.5
    st.session_state.history = "No"

with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-content">
            <h3 style="color: #0d6efd; text-align: center;">🩺 Diabetes Prediction System</h3>
            <p style="text-align: center;">Advanced Diabetes Risk Assessment System</p>
            <hr>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div class="sidebar-content">
            <h4 style="color: #333;">📊 About This Tool</h4>
            <p style="color: #555;">
                DiabetesScan AI uses machine learning to analyze your health metrics and predict potential diabetes risk. This assessment tool helps you understand your personal risk factors and take proactive steps for better health management.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div class="sidebar-content">
            <h4 style="color: #333;">🔍 How It Works</h4>
            <p>Our AI model has been trained on extensive medical data to identify diabetes risk patterns.</p>
            <div class="progress-bar">
                <div class="progress-bar-fill" style="width: 25%; background-color: #0d6efd;">Input</div>
            </div>
            <div class="progress-bar">
                <div class="progress-bar-fill" style="width: 50%; background-color: #0d6efd;">Analysis</div>
            </div>
            <div class="progress-bar">
                <div class="progress-bar-fill" style="width: 75%; background-color: #0d6efd;">Prediction</div>
            </div>
            <div class="progress-bar">
                <div class="progress-bar-fill" style="width: 100%; background-color: #0d6efd;">Recommendation</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div class="sidebar-content">
            <h4 style="color: #333;">📚 Diabetes Facts</h4>
            <ul style="color: #555;">
                <li>Over 460 million adults worldwide have diabetes</li>
                <li>1 in 2 adults with diabetes remain undiagnosed</li>
                <li>Type 2 diabetes can often be prevented or delayed with lifestyle changes</li>
                <li>Early detection and treatment can prevent serious complications</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div class="sidebar-content">
            <h4 style="color: #333;">⚠️ Disclaimer</h4>
            <p style="color: #555; font-size: 0.8rem;">
                This tool provides an assessment based on the information you provide, but it is not a substitute for professional medical advice. Always consult with a healthcare provider for proper diagnosis and treatment.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
    <div class="title-container">
        <h1 style="color: #0d6efd;">🩺 Diabetes Prediction System</h1>
        <p>Advanced Machine Learning Diabetes Risk Assessment System</p>
    </div>
    """, 
    unsafe_allow_html=True
)

tab1, tab2 = st.tabs(["📝 Risk Assessment", "📊 Understanding Diabetes"])

with tab1:
    st.markdown("<div class='input-section'>", unsafe_allow_html=True)
    st.subheader("📋 Health Information")
    st.markdown("Please provide accurate information for the most reliable assessment.")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown("""
        <div class="card">
            <h4>Personal Details</h4>
        """, unsafe_allow_html=True)
        age = st.number_input("📅 Age", min_value=0, max_value=120, value=30, key="age", 
                             help="Enter your current age in years")
        bmi = st.number_input("⚖️ BMI", min_value=10.0, max_value=50.0, value=22.5, step=0.1, key="bmi",
                             help="Body Mass Index - weight(kg) / height²(m)")
        st.markdown("""
        <div class="range-info">
            <strong>BMI Categories:</strong><br>
            • Under 18.5: Underweight<br>
            • 18.5-24.9: Normal weight<br>
            • 25-29.9: Overweight<br>
            • 30 and above: Obesity
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h4>Clinical Measurements</h4>
        """, unsafe_allow_html=True)
        glucose = st.number_input("🍬 Fasting Glucose Level (mg/dL)", min_value=50, max_value=300, value=85, key="glucose",
                                 help="Blood glucose level after fasting for at least 8 hours")
        st.markdown("""
        <div class="range-info">
            <strong>Glucose Level Categories:</strong><br>
            • Normal: Below 100 mg/dL<br>
            • Prediabetes: 100-125 mg/dL<br>
            • Diabetes: 126 mg/dL or higher
        </div>
        """, unsafe_allow_html=True)
        
        bp = st.number_input("🩸 Systolic Blood Pressure (mmHg)", min_value=70, max_value=200, value=120, key="bp",
                            help="The top number in a blood pressure reading")
        st.markdown("""
        <div class="range-info">
            <strong>Blood Pressure Categories:</strong><br>
            • Normal: Below 120 mmHg<br>
            • Elevated: 120-129 mmHg<br>
            • High: 130 mmHg and higher
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <h4>Lifestyle & History</h4>
        """, unsafe_allow_html=True)
        activity = st.slider("🏃 Physical Activity Level", 1, 5, 3, key="activity",
                           help="1: Very sedentary, 5: Very active")
        st.markdown("""
        <div class="range-info">
            <strong>Activity Level Guide:</strong><br>
            • 1: Sedentary (little to no exercise)<br>
            • 2: Light activity (1-3 days/week)<br>
            • 3: Moderate activity (3-5 days/week)<br>
            • 4: Active (6-7 days/week)<br>
            • 5: Very active (twice daily training)
        </div>
        """, unsafe_allow_html=True)
        
        history = st.radio("👨‍👩‍👧 Family History of Diabetes?", ["No", "Yes"], index=0, key="history",
                         help="Do you have parents, siblings, or children with diabetes?")
        st.markdown("</div>", unsafe_allow_html=True)
    
    history_numeric = 1 if history == "Yes" else 0
    
    def calculate_risk_score():
        score = 0
        if age > 45: score += 20
        if bmi >= 30: score += 20
        elif bmi >= 25: score += 10
        
        if glucose >= 126: score += 40
        elif glucose >= 100: score += 25
        
        if bp > 140: score += 15
        elif bp > 120: score += 5
        
        if activity == 1: score += 15
        elif activity == 2: score += 10
        elif activity == 3: score += 5
        
        if history_numeric == 1: score += 15
        
        return min(score, 100)  # Cap at 100
    
    risk_score = calculate_risk_score()
    
    # Button layout
    col1, col2 = st.columns(2)
    with col1:
        predict_button = st.button("🔍 Analyze Diabetes Risk", key="predict", type="primary")
    with col2:
        reset_button = st.button("🔄 Reset All Fields", key="reset", on_click=reset_inputs)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Prepare features for prediction
    features = np.array([[age, bp, glucose, bmi, activity, history_numeric]])
    
    # Results Section
    if predict_button:
        st.markdown("<div class='results-section'>", unsafe_allow_html=True)
        
        # Add a progress bar for analysis
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        
        st.success("Analysis Complete!")
        
        # Get prediction
        prediction = model.predict(features)
        
        # Display the key health metrics
        st.subheader("Your Health Metrics")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <p class="metric-label">Glucose Level</p>
                <p class="metric-value">{glucose} mg/dL</p>
                <p class="metric-label">{
                    "Normal" if glucose < 100 else 
                    "Prediabetic" if glucose < 126 else 
                    "Diabetic Range"
                }</p>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <p class="metric-label">BMI</p>
                <p class="metric-value">{bmi:.1f}</p>
                <p class="metric-label">{
                    "Underweight" if bmi < 18.5 else
                    "Normal" if bmi < 25 else
                    "Overweight" if bmi < 30 else
                    "Obese"
                }</p>
            </div>
            """, unsafe_allow_html=True)
            
        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <p class="metric-label">Blood Pressure</p>
                <p class="metric-value">{bp} mmHg</p>
                <p class="metric-label">{
                    "Normal" if bp < 120 else
                    "Elevated" if bp < 130 else
                    "High"
                }</p>
            </div>
            """, unsafe_allow_html=True)
            
        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <p class="metric-label">Activity Level</p>
                <p class="metric-value">{activity}/5</p>
                <p class="metric-label">{
                    "Sedentary" if activity == 1 else
                    "Light" if activity == 2 else
                    "Moderate" if activity == 3 else
                    "Active" if activity == 4 else
                    "Very Active"
                }</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Create columns for visualization
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Display risk gauge chart
            fig, ax = plt.subplots(figsize=(8, 4))
            
            # Create gauge chart
            gauge_colors = ['green', 'yellowgreen', 'orange', 'red']
            gauge_ranges = [0, 25, 50, 75, 100]
            
            for i in range(len(gauge_ranges)-1):
                ax.barh(0, gauge_ranges[i+1]-gauge_ranges[i], left=gauge_ranges[i], height=0.5, color=gauge_colors[i])
            
            # Add pointer
            ax.barh(0, 0.5, left=risk_score, height=0.5, color='black')
            
            # Customize chart
            ax.set_xlim(0, 100)
            ax.set_ylim(-0.5, 0.5)
            ax.set_yticks([])
            ax.set_xticks([0, 25, 50, 75, 100])
            ax.set_xticklabels(['Very Low', 'Low', 'Moderate', 'High', 'Very High'])
            ax.set_title(f'Diabetes Risk Score: {risk_score}%', fontsize=16)
            ax.spines['right'].set_visible(False)
            ax.spines['top'].set_visible(False)
            ax.spines['left'].set_visible(False)
            
            st.pyplot(fig)
        
        with col2:
            # Display risk factors breakdown
            data = {
                'Factor': ['Glucose Level', 'Age', 'BMI', 'Family History', 'Physical Activity', 'Blood Pressure'],
                'Impact': [
                    40 if glucose >= 126 else (25 if glucose >= 100 else 0),
                    20 if age > 45 else (10 if age > 35 else 0),
                    20 if bmi >= 30 else (10 if bmi >= 25 else 0),
                    15 if history == "Yes" else 0,
                    15 if activity == 1 else (10 if activity == 2 else (5 if activity == 3 else 0)),
                    15 if bp > 140 else (5 if bp > 120 else 0)
                ]
            }
            
            risk_df = pd.DataFrame(data)
            risk_df = risk_df.sort_values('Impact', ascending=False)
            
            fig, ax = plt.subplots(figsize=(8, 6))
            colors = ['#dc3545' if x > 15 else '#ffc107' if x > 5 else '#28a745' for x in risk_df['Impact']]
            sns.barplot(x='Impact', y='Factor', data=risk_df, palette=colors, ax=ax)
            ax.set_title('Risk Factor Breakdown', fontsize=16)
            ax.set_xlabel('Impact Score')
            
            st.pyplot(fig)
        
        # Display the prediction result with enhanced UI
        if prediction[0] == 1:
            st.markdown("<p class='result-red'>🛑 High Risk of Diabetes Detected!</p>", unsafe_allow_html=True)
            st.markdown("<div class='alert-box'>⚠️ Attention Required! It's recommended that you consult a healthcare professional for proper evaluation and testing.</div>", unsafe_allow_html=True)
            
            st.subheader("🩺 Personalized Recommendations")
            
            # Add expandable sections for more detailed information
            with st.expander("View Detailed Prevention Recommendations"):
                st.markdown("### Key Steps to Lower Your Diabetes Risk")
                
                # Create cards for each recommendation
                col1, col2 = st.columns(2)
                
                with col1:
                    if glucose >= 100:
                        st.markdown("""
                        <div class="tip-card">
                            <h4>🍬 Monitor Blood Sugar - High Priority</h4>
                            <p>Your glucose level indicates increased risk. Consider regular monitoring and consult a healthcare provider for appropriate testing.</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    if bmi >= 25:
                        st.markdown("""
                        <div class="tip-card">
                            <h4>⚖️ Weight Management</h4>
                            <p>Even a modest weight loss of 5-7% of body weight can significantly reduce diabetes risk if you're overweight.</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    if activity < 3:
                        st.markdown("""
                        <div class="tip-card">
                            <h4>🏃‍♂️ Increase Physical Activity</h4>
                            <p>Aim for at least 150 minutes of moderate-intensity exercise per week. Even short walks can make a difference.</p>
                        </div>
                        """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown("""
                    <div class="tip-card">
                        <h4>🍎 Improve Your Diet</h4>
                        <p>Focus on a diet rich in whole grains, fruits, vegetables, and lean proteins. Limit refined carbohydrates and added sugars.</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if history == "Yes":
                        st.markdown("""
                        <div class="tip-card">
                            <h4>📊 Regular Screenings</h4>
                            <p>With your family history, consider more frequent diabetes screenings even if you're feeling healthy.</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    if bp > 120:
                        st.markdown("""
                        <div class="tip-card">
                            <h4>🩸 Control Blood Pressure</h4>
                            <p>High blood pressure often occurs alongside diabetes. Monitor your blood pressure and take steps to keep it in a healthy range.</p>
                        </div>
                        """, unsafe_allow_html=True)
        else:
            st.markdown("<p class='result-green'>✅ Low Risk of Diabetes Detected</p>", unsafe_allow_html=True)
            st.markdown("<div class='info-box'>🎉 Good news! Based on the information provided, you have a relatively low risk of diabetes. Continue maintaining your healthy lifestyle choices.</div>", unsafe_allow_html=True)
            
            st.subheader("🛡️ Maintain Your Healthy Lifestyle")
            st.markdown("""
            Even with low risk, it's important to:
            - Continue regular health check-ups
            - Maintain a balanced diet low in refined sugars
            - Stay physically active
            - Monitor your weight
            - Have your blood sugar checked periodically, especially after age 45
            """)
        
        # PDF Generation Function
        def generate_pdf():
            pdf = FPDF()
            pdf.add_page()
            
            # Add header and styling
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, "DiabetesScan AI: Your Personal Risk Assessment", ln=True, align='C')
            pdf.ln(5)
            
            # Add date
            pdf.set_font("Arial", 'I', 10)
            pdf.cell(0, 10, f"Generated on: {time.strftime('%B %d, %Y')}", ln=True)
            pdf.ln(5)
            
            # Add risk assessment
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, f"Risk Assessment Result: {'High Risk' if prediction[0] == 1 else 'Low Risk'}", ln=True)
            pdf.set_font("Arial", '', 10)
with tab2:
    st.header("Understanding Diabetes")
    
    # Introduction section
    st.subheader("What is Diabetes?")
    st.write("""
    Diabetes is a chronic health condition that affects how your body turns food into energy. 
    Most of the food you eat is broken down into sugar (glucose) and released into your bloodstream. 
    When your blood sugar goes up, it signals your pancreas to release insulin. Insulin acts like a key to 
    let the blood sugar into your body's cells for use as energy.
    
    With diabetes, your body either doesn't make enough insulin or can't use the insulin it makes as well as it should. 
    When there isn't enough insulin or cells stop responding to insulin, too much blood sugar stays in your bloodstream. 
    Over time, this can cause serious health problems, such as heart disease, vision loss, and kidney disease.
    """)
    
    # Types of diabetes
    st.subheader("Types of Diabetes")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Type 1 Diabetes")
        st.write("""
        - Thought to be an autoimmune reaction
        - The body attacks itself by mistake
        - Prevents your body from making insulin
        - About 5-10% of people with diabetes have Type 1
        - Usually diagnosed in children, teens, and young adults
        - Requires taking insulin every day
        """)
    
    with col2:
        st.markdown("#### Type 2 Diabetes")
        st.write("""
        - Cells don't respond normally to insulin
        - Your pancreas makes more insulin to try to get cells to respond
        - Eventually your pancreas can't keep up
        - About 90-95% of people with diabetes have Type 2
        - Develops over many years
        - Usually diagnosed in adults
        - Can be prevented or delayed with healthy lifestyle changes
        """)
    
    st.markdown("#### Gestational Diabetes")
    st.write("""
    Gestational diabetes develops in pregnant women who have never had diabetes. 
    If you have gestational diabetes, your baby could be at higher risk for health problems. 
    Gestational diabetes usually goes away after your baby is born but increases your risk for Type 2 diabetes later in life.
    """)
    
    # Risk factors
    st.subheader("Risk Factors for Diabetes")
    
    
    
    # Symptoms comparison
    st.subheader("Common Symptoms")
    
    st.write("""
    Although Type 1 and Type 2 diabetes have different causes, they share many symptoms:
    - Frequent urination
    - Excessive thirst
    - Extreme hunger
    - Unexplained weight loss
    - Fatigue
    - Blurred vision
    - Slow-healing sores
    - Frequent infections
    
    Type 1 diabetes symptoms often develop quickly, while Type 2 symptoms may develop slowly over years 
    and can be so mild that they go unnoticed.
    """)
    
    # Visualization of diabetes prevalence
    st.subheader("Diabetes Prevalence by Age Group")
    
    # Sample data for visualization
    age_groups = ['18-44', '45-64', '65-74', '75+']
    prevalence = [4.2, 17.5, 26.8, 29.2]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(age_groups, prevalence, color='steelblue')
    ax.set_ylabel('Prevalence (%)')
    ax.set_xlabel('Age Group')
    ax.set_title('Diabetes Prevalence by Age Group')
    
    # Add data labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{height}%', ha='center', va='bottom')
    
    st.pyplot(fig)
    
    # Complications
    st.subheader("Complications of Diabetes")
    
    complications = {
        'Cardiovascular disease': 'Heart disease, stroke, and high blood pressure',
        'Neuropathy': 'Nerve damage, especially in legs and feet',
        'Nephropathy': 'Kidney damage and kidney failure',
        'Retinopathy': 'Eye damage that can lead to vision loss',
        'Foot damage': 'Nerve damage and poor blood flow can lead to serious foot problems',
        'Skin conditions': 'Bacterial and fungal infections',
        'Hearing impairment': 'Higher risk of hearing problems',
        'Alzheimer\'s disease': 'Possible link between Type 2 diabetes and Alzheimer\'s'
    }
    
    complication_df = pd.DataFrame(complications.items(), columns=['Complication', 'Description'])
    st.table(complication_df)
    
    # Management and prevention
    st.subheader("Managing and Preventing Diabetes")
    
    st.write("""
    ### Type 1 Diabetes Management
    - Insulin therapy
    - Blood sugar monitoring
    - Healthy eating
    - Regular physical activity
    
    ### Type 2 Diabetes Management and Prevention
    - Maintain a healthy weight
    - Eat a balanced diet
    - Exercise regularly (at least 30 minutes, 5 days a week)
    - Monitor blood sugar
    - Take medications as prescribed
    - Manage stress
    - Get regular checkups
    """)
    
    # Interactive BMI calculator
    st.subheader("Check Your BMI")
    st.write("Body Mass Index (BMI) is one indicator of diabetes risk. A BMI over 25 increases your risk for Type 2 diabetes.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight = st.number_input("Weight (kg)", min_value=30.0, max_value=300.0, value=70.0, step=0.1)
        height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0, step=0.1)
    
    if st.button("Calculate BMI"):
        height_m = height / 100
        bmi = weight / (height_m * height_m)
        
        st.write(f"Your BMI is: {bmi:.1f}")
        
        if bmi < 18.5:
            st.write("Category: Underweight")
        elif 18.5 <= bmi < 25:
            st.write("Category: Normal weight")
        elif 25 <= bmi < 30:
            st.write("Category: Overweight (increased risk for diabetes)")
        else:
            st.write("Category: Obesity (high risk for diabetes)")
    
    # Resources
    st.subheader("Additional Resources")
    st.markdown("""
    - [American Diabetes Association](https://www.diabetes.org/)
    - [CDC Diabetes Information](https://www.cdc.gov/diabetes/index.html)
    - [International Diabetes Federation](https://www.idf.org/)
    - [World Health Organization - Diabetes](https://www.who.int/health-topics/diabetes)
    """)
            