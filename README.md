# 🔐 Password Strength Classification (Machine Learning + Streamlit)

## 📌 Project Overview
This project predicts the strength of a password as **Weak**, **Medium**, or **Strong** using a machine learning model trained with **GradientBoostingClassifier**.  
The model achieves **91% accuracy** and is integrated into a **Streamlit web application** for real-time password strength prediction.

---

## 🧠 Tech Stack
- **Python 3.x**
- **Scikit-learn**
- **Streamlit**
- **Pandas & NumPy**
- **Pickle** (for saving and loading the ML model)

---

## 📊 Model Details
- **Algorithm:** GradientBoostingClassifier  
- **Accuracy:** 91%  
- **Model Storage:** Pickle (`model.pkl`)  
- **Feature Engineering Includes:**
  - Password length  
  - Number of digits  
  - Number of special characters  
  - Number of uppercase letters  
  - Number of lowercase letters  

---

## 🖥️ Streamlit App
The Streamlit interface allows users to:
- Enter a password  
- Instantly check password strength (Weak / Medium / Strong)  
- View ML-powered predictions in real-time  

---
