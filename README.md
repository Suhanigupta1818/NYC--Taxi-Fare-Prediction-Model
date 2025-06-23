
---

# 🚖 NYC Taxi Fare Prediction

Welcome to the **NYC Taxi Fare Prediction** project! This is a cutting-edge machine learning application designed to predict taxi fares in New York City with precision and ease. Whether you're a tourist planning a ride or a data enthusiast exploring predictive modeling, this app has something for you! 🚕

---

## ✨ Project Highlights

* **Accurate Fare Predictions:** Estimate taxi fares based on pickup/dropoff locations, passenger count, and trip timing.
* **Powerful ML Models:** Leverages **Ridge Regression** and **XGBoost** for robust and reliable predictions.
* **Interactive UI:** Built with **Streamlit**, featuring a sleek dark-themed interface with glassmorphism design.
* **Map Visualization:** Visualize your trip on an interactive map with pickup and dropoff markers, powered by **Folium**.
* **Real-World Application:** Deployed on **Streamlit Cloud** for global accessibility.

---

## 🛠️ Features

* **Dynamic Fare Prediction:** Enter trip details (pickup/dropoff locations, passenger count, pickup time) to get an instant fare estimate.
* **NYC Landmark Support:** Choose from popular NYC locations like Times Square, Central Park, and the Empire State Building.
* **Trip Visualization:** View your route on a map with a blue polyline connecting pickup and dropoff points.
* **Fare Breakdown:** Get a detailed breakdown including base fare, distance cost, and time-based charges.
* **Responsive Design:** Modern UI with a dark theme, 3D touch effects, and seamless user experience.

---

## 📸 Screenshots

### Home Page

![Home Page](https://github.com/user-attachments/assets/336395d8-e1f8-4827-89c3-735b33ce4238)

### Fare Prediction

![Fare Prediction](https://github.com/user-attachments/assets/23396678-df68-42bb-ab2b-80af5ddfdb49)

---

## 🧠 Machine Learning Details

### 🔍 Models Used

* **Ridge Regression:** A linear model with L2 regularization to handle multicollinearity.
* **XGBoost:** A powerful gradient-boosting model with tuned hyperparameters for superior performance.

### 🧮 Feature Engineering

* **Trip Distance:** Calculated using the Haversine formula between pickup and dropoff coordinates.
* **Temporal Features:** Extracted from pickup datetime (year, month, day, weekday, hour).
* **Landmark Distances:** Distances to major NYC landmarks (JFK, LaGuardia, etc.) for enhanced accuracy.

### 📈 Performance

* Achieved a **validation RMSE of \~3.90** using XGBoost for highly accurate fare predictions.

---

## ⚙️ Tech Stack

* **Python:** Core programming language.
* **Pandas & NumPy:** For data manipulation and numerical processing.
* **Scikit-learn:** Ridge Regression model and preprocessing tools.
* **XGBoost:** Gradient boosting machine learning model.
* **Streamlit:** Web app framework.
* **Folium & Streamlit-Folium:** Interactive map visualizations.
* **GitHub & Streamlit Cloud:** Version control and deployment.

---

## 🚀 Setup & Installation

Get started with the project in a few simple steps:

### 1. Clone the Repository


### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App Locally

```bash
streamlit run app.py
```

Open your browser and go to **[http://localhost:8501](http://localhost:8501)** to see the app in action!

---

## 🌐 Live Demo

👉 **[NYC Taxi Fare Predictor on Streamlit Cloud](https://nyc--taxi-fare-prediction-model-suhani1809.streamlit.app/)**

---

## 📜 Usage Guide

1. **Select Locations:** Choose pickup and dropoff from popular NYC landmarks.
2. **Enter Trip Details:** Input passenger count and pickup time.
3. **Visualize Trip:** View your route on an interactive map.
4. **Predict Fare:** Click “Predict Fare” to get the estimated cost with a detailed fare breakdown.

---

## 🤝 Contributing

Contributions are welcome! To improve or extend the project:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:

   ```bash
   git commit -m "Add your feature"
   ```
4. Push the branch:

   ```bash
   git push origin feature/your-feature
   ```
5. Open a Pull Request.

---

## 📧 Contact

Have questions or suggestions? Feel free to connect!

* **GitHub:** [Suhanigupta1818](https://github.com/Suhanigupta1818)
* **Email:** [gsuhani053@gmail.com](mailto:gsuhani053@gmail.com)
* **LinkedIn:** [Suhani Gupta](https://www.linkedin.com/in/suhani-gupta-154667280/)

---

## 🌟 Acknowledgments

* Inspired by real-world taxi fare prediction challenges.
* Thanks to the **Streamlit community** for the powerful framework.
* Built with ❤️ by **Suhani Gupta**.

---
