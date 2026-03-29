import streamlit as st
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.predict import predict_load
from src.recommender import get_recommendations

st.title("Cognitive Load Estimator")

study = st.slider("Study Hours", 0, 10)
sleep = st.slider("Sleep Hours", 0, 10)
difficulty = st.slider("Task Difficulty", 1, 5)
phone = st.slider("Phone Usage", 0, 10)
noise = st.slider("Noise Level", 1, 5)
switch = st.slider("Task Switching", 0, 10)
stress = st.slider("Stress Level", 1, 5)
revision = st.slider("Revision Ratio", 0, 100)

if st.button("Analyze"):
    data = [study, sleep, difficulty, phone, noise, switch, stress, revision]

    intrinsic, extraneous, germane = predict_load(data)

    st.subheader("Results")
    st.write("Intrinsic:", intrinsic)
    st.write("Extraneous:", extraneous)
    st.write("Germane:", germane)

    rec, precautions = get_recommendations(intrinsic, extraneous, germane)

    st.subheader("Recommendations")
    for r in rec:
        st.write("-", r)

    st.subheader("Precautions")
    for p in precautions:
        st.write("-", p)