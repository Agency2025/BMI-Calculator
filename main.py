import streamlit as st

# Page configuration
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="🏥",
    layout="centered"
)

# Custom CSS for professional medical look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stTitle {
        color: #2c3e50;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
        padding: 20px 0;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .disclaimer {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 15px;
        margin: 20px 0;
        border-radius: 5px;
        font-size: 0.9em;
    }
    .recommendation {
        background-color: #d1ecf1;
        border-left: 4px solid #17a2b8;
        padding: 15px;
        margin: 15px 0;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🏥 BMI Calculator")
st.markdown("### Body Mass Index Assessment Tool")
st.markdown("---")

# Create two columns for unit selection
col1, col2 = st.columns(2)

with col1:
    height_unit = st.radio("Height Unit", ["Centimeters (cm)", "Inches (in)"])

with col2:
    weight_unit = st.radio("Weight Unit", ["Kilograms (kg)", "Pounds (lbs)"])

st.markdown("---")

# Input fields
col3, col4 = st.columns(2)

with col3:
    if height_unit == "Centimeters (cm)":
        height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0, step=0.1)
        height_m = height / 100  # Convert to meters
    else:
        height = st.number_input("Height (inches)", min_value=20.0, max_value=100.0, value=67.0, step=0.1)
        height_m = height * 0.0254  # Convert inches to meters

with col4:
    if weight_unit == "Kilograms (kg)":
        weight = st.number_input("Weight (kg)", min_value=20.0, max_value=300.0, value=70.0, step=0.1)
        weight_kg = weight
    else:
        weight = st.number_input("Weight (lbs)", min_value=44.0, max_value=660.0, value=154.0, step=0.1)
        weight_kg = weight * 0.453592  # Convert lbs to kg

st.markdown("---")

# Calculate BMI button
if st.button("Calculate BMI", use_container_width=True):
    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)
    
    # Determine category and color
    if bmi < 18.5:
        category = "Underweight"
        color = "#3498db"
        recommendation = """
        **Recommendations for Underweight:**
        - Consult with a healthcare provider or registered dietitian
        - Increase caloric intake with nutrient-dense foods
        - Consider strength training exercises to build muscle mass
        - Ensure adequate protein intake
        - Monitor for any underlying health conditions
        """
    elif 18.5 <= bmi < 25:
        category = "Normal Weight"
        color = "#2ecc71"
        recommendation = """
        **Recommendations for Normal Weight:**
        - Maintain your current healthy lifestyle
        - Continue balanced nutrition with varied foods
        - Engage in regular physical activity (150 minutes/week)
        - Stay hydrated and get adequate sleep
        - Schedule regular health check-ups
        """
    elif 25 <= bmi < 30:
        category = "Overweight"
        color = "#f39c12"
        recommendation = """
        **Recommendations for Overweight:**
        - Consult with a healthcare provider for personalized advice
        - Aim for gradual weight loss (1-2 lbs per week)
        - Increase physical activity to 300 minutes/week
        - Focus on portion control and whole foods
        - Consider keeping a food diary
        - Reduce intake of processed foods and added sugars
        """
    else:
        category = "Obese"
        color = "#e74c3c"
        recommendation = """
        **Recommendations for Obesity:**
        - Consult with a healthcare provider for a comprehensive evaluation
        - Work with a registered dietitian for a personalized meal plan
        - Start with moderate exercise and gradually increase intensity
        - Consider behavioral therapy or support groups
        - Address any underlying health conditions
        - Set realistic, achievable goals for weight management
        - Monitor blood pressure, cholesterol, and blood sugar levels
        """
    
    # Display results
    st.markdown("## 📊 Your Results")
    
    # BMI value with color coding
    st.markdown(f"""
        <div style='background-color: {color}; padding: 20px; border-radius: 10px; text-align: center; margin: 20px 0;'>
            <h1 style='color: white; margin: 0;'>{bmi:.1f}</h1>
            <h3 style='color: white; margin: 10px 0 0 0;'>{category}</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # BMI categories reference
    st.markdown("### BMI Categories")
    st.markdown("""
    - **Underweight:** BMI < 18.5
    - **Normal Weight:** BMI 18.5 - 24.9
    - **Overweight:** BMI 25 - 29.9
    - **Obese:** BMI ≥ 30
    """)
    
    # Recommendations
    st.markdown("### 💡 Health Recommendations")
    st.markdown(f"<div class='recommendation'>{recommendation}</div>", unsafe_allow_html=True)

# Disclaimer
st.markdown("---")
st.markdown("""
<div class='disclaimer'>
    <strong>⚠️ Medical Disclaimer:</strong><br>
    This BMI calculator is for educational and informational purposes only. BMI is a screening tool 
    and does not diagnose body fatness or health. It does not account for muscle mass, bone density, 
    overall body composition, age, sex, or ethnicity. Always consult with a qualified healthcare 
    professional for medical advice, diagnosis, or treatment. This tool should not be used as a 
    substitute for professional medical care.
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #7f8c8d; padding: 20px;'>
        <p>BMI Formula: weight (kg) / height² (m²)</p>
        <p style='font-size: 0.8em;'>Developed for educational purposes | © 2024</p>
    </div>
""", unsafe_allow_html=True)
