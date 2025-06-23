import streamlit as st
from src.predict import predict_fare
from datetime import datetime
import folium
from streamlit_folium import folium_static

# Page Configuration
st.set_page_config(page_title="🚖 NYC Taxi Fare Predictor", layout="wide", page_icon="🚖")

# Fancy Dark Theme CSS with Glassmorphism and 3D Touch
fancy_css = """
<style>
body {
    background: linear-gradient(145deg, #121212, #1e1e1e);
    color: #ffffff;
    font-family: 'Segoe UI', sans-serif;
}

.card {
    background: rgba(44, 47, 51, 0.5);
    border-radius: 15px;
    padding: 20px;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    border: 1px solid rgba(255, 255, 255, 0.18);
    margin-bottom: 25px;
}

input, .stNumberInput input, .stDateInput input {
    background-color: #2a2a2a !important;
    color: #ffffff !important;
    border: 1px solid #555;
    border-radius: 10px;
}

h1, h2, h3, h4, h5 {
    color: #f1c40f;
}

button[kind="primary"] {
    background: linear-gradient(to right, #ffcc00, #ff9900);
    color: #000;
    padding: 12px 28px;
    border-radius: 10px;
    font-weight: bold;
    box-shadow: 0 10px 20px rgba(255, 165, 0, 0.3);
    transition: all 0.3s ease;
}

button[kind="primary"]:hover {
    transform: scale(1.05);
    box-shadow: 0 12px 24px rgba(255, 165, 0, 0.5);
}

hr {
    border: none;
    border-top: 1px solid #444;
    margin: 30px 0;
}
</style>
"""
st.markdown(fancy_css, unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align:center;'>🚖 NYC Taxi Fare Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Estimate your cab fare instantly by entering trip details!</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# NYC Landmarks with Coordinates (latitude, longitude)
places_coords = {
    "Times Square": (40.758896, -73.985130),
    "Central Park": (40.785091, -73.968285),
    "Empire State Building": (40.748817, -73.985428),
    "Wall Street": (40.706036, -74.008966),
    "Brooklyn Bridge": (40.706085, -73.996864),
    "JFK Airport": (40.641311, -73.778139),
    "LaGuardia Airport": (40.776927, -73.873966),
    "Statue of Liberty": (40.689249, -74.044500),
    "Columbia University": (40.807536, -73.962573),
    "Yankee Stadium": (40.829643, -73.926175)
}

# List of place names for the dropdown
places = list(places_coords.keys())

# Input Section
with st.container():
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📍 Pickup Location")
        pickup_place = st.selectbox("Select Pickup Place", places, index=0)
        pickup_lat, pickup_lon = places_coords[pickup_place]
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📍 Dropoff Location")
        dropoff_place = st.selectbox("Select Dropoff Place", places, index=1)
        dropoff_lat, dropoff_lon = places_coords[dropoff_place]
        st.markdown('</div>', unsafe_allow_html=True)

# More Inputs
with st.container():
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🧍 Passenger Count")
        passenger_count = st.number_input("", 1, 6, 1)
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🕒 Pickup Time")
        pickup_datetime = st.date_input("", datetime.now())
        st.markdown('</div>', unsafe_allow_html=True)

# Map
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🗺️ Trip Visualization")
m = folium.Map(location=[pickup_lat, pickup_lon], zoom_start=13, tiles="CartoDB dark_matter")
folium.Marker([pickup_lat, pickup_lon], popup="Pickup", icon=folium.Icon(color="green")).add_to(m)
folium.Marker([dropoff_lat, dropoff_lon], popup="Dropoff", icon=folium.Icon(color="red")).add_to(m)
folium.PolyLine([[pickup_lat, pickup_lon], [dropoff_lat, dropoff_lon]], color="blue", weight=4).add_to(m)
folium_static(m, height=300)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Predict Button
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
if st.button("💸 Predict Fare"):
    fare = predict_fare(pickup_lon, pickup_lat, dropoff_lon, dropoff_lat, passenger_count, pickup_datetime)
    st.markdown(f"<h2 style='text-align:center; color:#2ecc71;'>Estimated Fare: ${fare:.2f}</h2>", unsafe_allow_html=True)

    # Breakdown
    base = 2.5
    dist = fare * 0.7
    time = fare * 0.3
    st.markdown("""
    <div class="card">
    <h4>📊 Fare Breakdown</h4>
    <ul>
        <li>Base Fare: ${:.2f}</li>
        <li>Distance Component: ${:.2f}</li>
        <li>Time Component: ${:.2f}</li>
        <li><strong>Total Fare: ${:.2f}</strong></li>
    </ul>
    </div>
    """.format(base, dist, time, fare), unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
---
<p style='text-align:center;'>Made by Suhani Gupta | Powered by Streamlit</p>
""", unsafe_allow_html=True)