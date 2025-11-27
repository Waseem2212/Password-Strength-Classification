import streamlit as st
import pickle

# ------------------------------
# FIX: Define the tokenizer function BEFORE loading pickle
# ------------------------------
def character(inputs):
    characters = []
    for i in inputs:
        characters.append(i)
    return characters

# ------------------------------
# Load Model and Vectorizer
# ------------------------------
@st.cache_resource
def load_model():
    vec = pickle.load(open("vectorizer.pkl", "rb"))
    model = pickle.load(open("model.pkl", "rb"))
    return vec, model

vec, model = load_model()

# ------------------------------
# Streamlit App UI
# ------------------------------
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")

st.title("🔐 Password Strength Prediction App")

# Input Field
password = st.text_input("Enter Password", type="password")

if st.button("Check Strength"):
    if password.strip() == "":
        st.error("Please enter a password!")
    else:
        # Vectorize
        x_vec = vec.transform([password])
        
        # Prediction
        pred = model.predict(x_vec)[0]

        # Label Mapping
        label_map = {
            0: "Weak Password ❌",
            1: "Medium Strength Password ⚠️",
            2: "Strong Password ✅"
        }

        st.subheader("🔎 Prediction Result:")
        st.success(label_map[int(pred)])

        # Strength Bar
        if pred == 0:
            st.progress(0)
        elif pred == 1:
            st.progress(50)
        else:
            st.progress(100)

st.write("---")

