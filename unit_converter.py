import streamlit as st  # type: ignore

# Custom CSS Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
        font-family: 'Segoe UI', sans-serif;
        padding: 2rem;
    }
    h1 {
        color: #222831;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .stButton > button {
        background-color: #30475e;
        color: white;
        padding: 0.6rem 1.2rem;
        font-size: 1rem;
        border-radius: 8px;
        border: none;
    }
    .stButton > button:hover {
        background-color: #222831;
    }
    .result-box {
        background-color: #222831;
        color: #ffffff;
        padding: 1rem;
        border-radius: 8px;
        font-size: 1.1rem;
        margin-top: 1.5rem;
    }
    .footer {
        text-align: center;
        font-size: 0.9rem;
        color: #777;
        margin-top: 3rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>📏 Unit Converter</h1>", unsafe_allow_html=True)
st.write("---")

# Define conversion factors
conversion_factors = {
    "Meters": 1,
    "Kilometers": 1000,
    "Centimeters": 0.01,
    "Millimeters": 0.001,
    "Miles": 1609.34,
    "Yards": 0.9144,
    "Feet": 0.3048,
    "Inches": 0.0254
}

# Sidebar Inputs
st.sidebar.header("Enter Conversion Values")
value = st.sidebar.number_input("Value", min_value=0.0, step=0.1)
from_unit = st.sidebar.selectbox("From Unit", list(conversion_factors.keys()))
to_unit = st.sidebar.selectbox("To Unit", list(conversion_factors.keys()))

# Conversion
if value:
    meters = value * conversion_factors[from_unit]
    result = meters / conversion_factors[to_unit]

    # Display Result
    st.markdown(f"""
        <div class='result-box'>
            <strong>Result:</strong><br>
            {value} {from_unit} = {result:.6f} {to_unit}
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        Created by Hassan Nadeem • 2025 © All rights reserved
    </div>
""", unsafe_allow_html=True)
