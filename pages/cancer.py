import streamlit as st
import numpy as np
import pandas as pd
import joblib
import io
from fpdf import FPDF
import matplotlib.pyplot as plt
import seaborn as sns
import time

# Load the trained model
model = joblib.load("cancer_prediction_final.pkl")

# Streamlit Page Configuration
st.set_page_config(
    page_title="Cancer Risk Assessment",
    page_icon="♋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
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
            background-color: #0d6efd;
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

# Sidebar with enhanced information
with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-content">
            <h3 style="color: #0d6efd; text-align: center;">♋ Cancer Prediction System</h3>
            <p style="text-align: center;">Advanced Cancer Risk Assessment System</p>
            <hr>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div class="sidebar-content">
            <h4 style="color: #333;">🩺 About This Tool</h4>
            <p style="color: #555;">
                 MediPredixt uses machine learning to analyze your health factors and predict potential cancer risk. This assessment tool helps you understand your personal risk factors and take proactive steps for better health management.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div class="sidebar-content">
            <h4 style="color: #333;">🔍 How It Works</h4>
            <p>Our AI model has been trained on extensive medical data to identify risk patterns.</p>
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
            <h4 style="color: #333;">⚠️ Disclaimer</h4>
            <p style="color: #555; font-size: 0.8rem;">
                This tool provides an assessment based on the information you provide, but it is not a substitute for professional medical advice. Always consult with a healthcare provider for proper diagnosis and treatment.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Main Content
st.markdown(
    """
    <div class="title-container">
        <h1 style="color: #0d6efd;">♋ Cancer Prediction System </h1>
        <p>Advanced Machine Learning Cancer Risk Assessment System</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Create tabs for different sections
tab1, tab2, tab3 = st.tabs(["📝 Risk Assessment", "📊 Risk Factors", "ℹ️ About Cancer"])

with tab1:
    st.markdown("<div class='input-section'>", unsafe_allow_html=True)
    st.subheader("📋 Personal Health Information")
    st.markdown("Please provide accurate information for the most reliable assessment.")
    
    # Create a more organized layout with columns
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown("""
        <div class="card">
            <h4>Personal Details</h4>
        """, unsafe_allow_html=True)
        Age = st.number_input("📅 Age", min_value=0, max_value=120, value=30, help="Enter your current age in years")
        Gender = st.radio("👫 Gender", ["Male", "Female"], index=0, help="Select your biological gender")
        BMI = st.number_input("⚖️ BMI", min_value=10.0, max_value=50.0, value=22.0, step=0.1, 
                              help="Body Mass Index - weight(kg) / height²(m)")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h4>Lifestyle Factors</h4>
        """, unsafe_allow_html=True)
        Smoking = st.radio("🚬 Smoking Status", ["Yes", "No"], index=1, 
                          help="Do you currently smoke tobacco products?")
        AlcoholIntake = st.slider("🍷 Alcohol Consumption", 1, 5, 1, 
                                 help="1: None, 2: Occasionally, 3: Moderate, 4: Regular, 5: Heavy")
        PhysicalActivity = st.slider("🏃‍♂️ Physical Activity", 1, 10, 5, 
                                    help="1: Very Sedentary, 10: Highly Active")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <h4>Medical History</h4>
        """, unsafe_allow_html=True)
        GeneticRisk = st.radio("🧬 Genetic Risk Factors", ["Yes", "No"], index=1, 
                              help="Any known genetic mutations associated with cancer?")
        CancerHistory = st.radio("👪 Family Cancer History", ["Yes", "No"], index=1, 
                               help="First-degree relatives with cancer diagnosis?")
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Convert categorical inputs to numeric format
    Gender_numeric = 1 if Gender == "Male" else 0
    Smoking_numeric = 1 if Smoking == "Yes" else 0
    GeneticRisk_numeric = 1 if GeneticRisk == "Yes" else 0
    CancerHistory_numeric = 1 if CancerHistory == "Yes" else 0
    
    # Creating feature DataFrame
    features_df = pd.DataFrame({
        "Age": [Age],
        "Gender": [Gender_numeric],
        "BMI": [BMI],
        "Smoking": [Smoking_numeric],
        "GeneticRisk": [GeneticRisk_numeric],
        "PhysicalActivity": [PhysicalActivity],
        "AlcoholIntake": [AlcoholIntake],
        "CancerHistory": [CancerHistory_numeric]
    })
    
    # Calculate risk score for visualization (simplified example)
    def calculate_risk_score():
        score = 0
        if Age > 50: score += 15
        if Gender == "Male": score += 5
        if BMI > 30: score += 10
        if Smoking == "Yes": score += 20
        if GeneticRisk == "Yes": score += 20
        if CancerHistory == "Yes": score += 15
        if AlcoholIntake > 3: score += 10
        if PhysicalActivity < 3: score += 5
        return min(score, 100)  # Cap at 100
    
    risk_score = calculate_risk_score()
    
    # Prediction Button with loading animation
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        predict_button = st.button("🔍 Analyze Cancer Risk")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
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
        prediction = model.predict(features_df)
        
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
            ax.set_title(f'Risk Score: {risk_score}%', fontsize=16)
            ax.spines['right'].set_visible(False)
            ax.spines['top'].set_visible(False)
            ax.spines['left'].set_visible(False)
            
            st.pyplot(fig)
        
        with col2:
            # Display risk factors breakdown
            data = {
                'Factor': ['Age', 'Gender', 'BMI', 'Smoking', 'Genetics', 'Physical Activity', 'Alcohol', 'Family History'],
                'Impact': [
                    15 if Age > 50 else 5,
                    5 if Gender == "Male" else 3,
                    10 if BMI > 30 else (5 if BMI > 25 else 0),
                    20 if Smoking == "Yes" else 0,
                    20 if GeneticRisk == "Yes" else 0,
                    10 - min(10, PhysicalActivity),
                    AlcoholIntake * 2,
                    15 if CancerHistory == "Yes" else 0
                ]
            }
            
            risk_df = pd.DataFrame(data)
            risk_df = risk_df.sort_values('Impact', ascending=False)
            
            fig, ax = plt.subplots(figsize=(8, 6))
            colors = ['#dc3545' if x > 10 else '#ffc107' if x > 5 else '#28a745' for x in risk_df['Impact']]
            sns.barplot(x='Impact', y='Factor', data=risk_df, palette=colors, ax=ax)
            ax.set_title('Risk Factor Breakdown', fontsize=16)
            ax.set_xlabel('Impact Score')
            
            st.pyplot(fig)
        
        # Display the prediction result with enhanced UI
        if prediction[0] == 1:
            st.markdown("<p class='result-red'>🛑 High Risk of Cancer Detected!</p>", unsafe_allow_html=True)
            st.markdown("<div class='alert-box'>⚠️ Immediate Attention Required! Please consult a healthcare professional as soon as possible for a comprehensive evaluation.</div>", unsafe_allow_html=True)
            
            st.subheader("🩺 Personalized Recommendations")
            
            # Add expandable sections for more detailed information
            with st.expander("View Detailed Prevention Recommendations"):
                st.markdown("### Key Steps to Lower Your Cancer Risk")
                
                # Create cards for each recommendation
                col1, col2 = st.columns(2)
                
                with col1:
                    if Smoking == "Yes":
                        st.markdown("""
                        <div class="tip-card">
                            <h4>🚭 Quit Smoking - High Priority</h4>
                            <p>Tobacco use is linked to multiple cancer types. Consider nicotine replacement therapy or medication to help quit.</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    if BMI > 25:
                        st.markdown("""
                        <div class="tip-card">
                            <h4>⚖️ Healthy Weight Management</h4>
                            <p>Aim for a BMI between 18.5-24.9 through balanced diet and regular exercise.</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    if AlcoholIntake > 2:
                        st.markdown("""
                        <div class="tip-card">
                            <h4>🍷 Reduce Alcohol Consumption</h4>
                            <p>Limit intake to no more than 1 drink per day for women and 2 for men.</p>
                        </div>
                        """, unsafe_allow_html=True)
                
                with col2:
                    if PhysicalActivity < 5:
                        st.markdown("""
                        <div class="tip-card">
                            <h4>🏃‍♂️ Increase Physical Activity</h4>
                            <p>Aim for at least 150 minutes of moderate exercise or 75 minutes of vigorous activity weekly.</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.markdown("""
                    <div class="tip-card">
                        <h4>🍎 Improve Your Diet</h4>
                        <p>Focus on plant-based foods, limit processed meat, and increase fiber intake.</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown("""
                    <div class="tip-card">
                        <h4>🔍 Regular Screenings</h4>
                        <p>Follow age-appropriate cancer screening guidelines and discuss your specific risk factors with your doctor.</p>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.markdown("<p class='result-green'>✅ Low Risk of Cancer Detected</p>", unsafe_allow_html=True)
            st.markdown("<div class='info-box'>🎉 Good news! Based on the information provided, you have a relatively low risk of cancer. Continue maintaining your healthy lifestyle choices.</div>", unsafe_allow_html=True)
            
            st.subheader("🛡️ Maintain Your Healthy Lifestyle")
            st.markdown("""
            Even with low risk, it's important to:
            - Continue regular health check-ups
            - Maintain a balanced diet rich in fruits and vegetables
            - Stay physically active
            - Limit alcohol consumption
            - Avoid tobacco products
            - Protect your skin from excessive sun exposure
            """)
        
        # PDF Generation Function
        def generate_pdf():
            pdf = FPDF()
            pdf.add_page()
            
            # Add header and styling
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, "CancerScan AI: Your Personal Risk Assessment", ln=True, align='C')
            pdf.ln(5)
            
            # Add date
            pdf.set_font("Arial", 'I', 10)
            pdf.cell(0, 10, f"Generated on: {time.strftime('%B %d, %Y')}", ln=True)
            pdf.ln(5)
            
            # Add risk assessment
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, f"Risk Assessment Result: {'High Risk' if prediction[0] == 1 else 'Low Risk'}", ln=True)
            pdf.set_font("Arial", '', 10)
            pdf.cell(0, 10, f"Risk Score: {risk_score}%", ln=True)
            pdf.ln(5)
            
            # Add personal information
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, "Your Health Information:", ln=True)
            pdf.set_font("Arial", '', 10)
            pdf.cell(0, 10, f"Age: {Age} | Gender: {Gender} | BMI: {BMI}", ln=True)
            pdf.cell(0, 10, f"Smoking: {Smoking} | Alcohol Intake: {AlcoholIntake}/5 | Physical Activity: {PhysicalActivity}/10", ln=True)
            pdf.cell(0, 10, f"Genetic Risk: {GeneticRisk} | Family Cancer History: {CancerHistory}", ln=True)
            pdf.ln(10)
            
            # Add recommendations
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, "Personalized Recommendations:", ln=True)
            pdf.set_font("Arial", '', 10)
            
            recommendations = [
                "Schedule regular check-ups with your healthcare provider.",
                "Maintain a balanced diet rich in fruits, vegetables, and whole grains.",
                "Stay physically active with at least 150 minutes of moderate exercise weekly.",
                "Limit alcohol consumption to moderate levels.",
                "Avoid tobacco products and secondhand smoke.",
                "Protect your skin from excessive sun exposure.",
                "Learn about early warning signs of common cancers.",
                "Follow age-appropriate cancer screening guidelines."
            ]
            
            for i, item in enumerate(recommendations):
                pdf.cell(0, 8, f"{i+1}. {item}", ln=True)
            
            pdf.ln(10)
            
            # Add disclaimer
            pdf.set_font("Arial", 'I', 8)
            pdf.multi_cell(0, 5, "Disclaimer: This assessment is based on the information provided and is not a substitute for professional medical advice. Always consult with a healthcare provider for proper diagnosis and treatment.")
            
            # Save PDF to a BytesIO buffer
            pdf_buffer = io.BytesIO()
            pdf.output(pdf_buffer, 'S')
            pdf_buffer.seek(0)
            return pdf_buffer
        
        # Generate and Provide PDF Download
        pdf_file = generate_pdf()
        st.download_button(
            label="📄 Download Your Personalized Report",
            data=pdf_file,
            file_name="cancer_risk_assessment.pdf",
            mime="application/pdf"
        )
        
        st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("<div class='input-section'>", unsafe_allow_html=True)
    st.subheader("📊 Understanding Cancer Risk Factors")
    
    st.markdown("""
    Cancer risk is influenced by various factors, some of which can be modified while others cannot.
    Understanding these factors can help you make informed decisions about your health.
    """)
    
    # Create expandable sections for different risk factors
    with st.expander("Non-Modifiable Risk Factors"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="card">
                <h4>🧬 Genetic Factors</h4>
                <p>Some genetic mutations can significantly increase cancer risk. Examples include BRCA1 and BRCA2 mutations for breast and ovarian cancer, and Lynch syndrome for colorectal cancer.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="card">
                <h4>👪 Family History</h4>
                <p>Having first-degree relatives (parents, siblings, children) who developed cancer at a young age may indicate a hereditary risk factor.</p>
            </div>
            """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="card">
                <h4>📅 Age</h4>
                <p>Cancer risk generally increases with age. Most cancers occur in people over the age of 65, though certain types can affect younger individuals.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="card">
                <h4>👫 Gender</h4>
                <p>Some cancers are gender-specific (e.g., prostate, ovarian), while others affect genders differently (e.g., higher lung cancer rates in men).</p>
            </div>
            """, unsafe_allow_html=True)
    
    with st.expander("Modifiable Risk Factors"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="card">
                <h4>🚬 Tobacco Use</h4>
                <p>Smoking is linked to many cancer types, not just lung cancer. It's estimated to cause about 30% of all cancer deaths.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="card">
                <h4>🍷 Alcohol Consumption</h4>
                <p>Regular heavy drinking increases risk for several cancers, including mouth, throat, larynx, esophagus, liver, and breast cancers.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="card">
                <h4>⚖️ Weight & BMI</h4>
                <p>Obesity is associated with increased risks of breast, colorectal, endometrial, kidney, and pancreatic cancers.</p>
            </div>
            """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="card">
                <h4>🏃‍♂️ Physical Activity</h4>
                <p>Regular exercise can reduce the risk of several cancers including colon, breast, and endometrial cancers.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="card">
                <h4>🍎 Diet</h4>
                <p>Diets high in processed foods, red meat, and low in fruits and vegetables may increase cancer risk.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="card">
                <h4>☀️ Sun Exposure</h4>
                <p>Excessive UV radiation exposure increases risk of skin cancers. Use sunscreen and avoid tanning beds.</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Add an interactive visualization
    st.subheader("Cancer Risk Factor Impact")
    
    # Sample data for visualization
    risk_factors = ['Smoking', 'Obesity', 'Physical Inactivity', 'Poor Diet', 'Alcohol', 'UV Exposure', 'Genetics']
    impact_values = [30, 20, 15, 15, 10, 5, 5]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(risk_factors, impact_values, color=['#dc3545', '#fd7e14', '#ffc107', '#20c997', '#0dcaf0', '#6f42c1', '#6c757d'])
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.5, f'{height}%', ha='center', va='bottom')
    
    ax.set_ylim(0, 35)
    ax.set_ylabel('Estimated Contribution to Cancer Risk (%)')
    ax.set_title('Relative Impact of Different Risk Factors on Overall Cancer Risk')
    
    st.pyplot(fig)
    
    st.caption("Note: This chart shows estimated relative contributions of different factors to overall cancer risk based on population studies. Individual risk may vary significantly.")
    
    st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    st.markdown("<div class='input-section'>", unsafe_allow_html=True)
    st.subheader("ℹ️ About Cancer")
    
    st.markdown("""
    ### What is Cancer?
    
    Cancer is a group of diseases characterized by the uncontrolled growth and spread of abnormal cells. These cells can invade and destroy surrounding healthy tissue and can spread (metastasize) to other parts of the body.
    
    ### Key Facts About Cancer:
    
    - Cancer is the second leading cause of death globally
    - Early detection significantly improves treatment outcomes
    - Between 30-50% of cancers can be prevented by avoiding risk factors and implementing prevention strategies
    - Many cancers have a high cure rate when detected early and treated according to best practices
    """)
