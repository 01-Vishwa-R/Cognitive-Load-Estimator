import streamlit as st
import sys, os



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.predict import predict_load
from src.recommender import get_recommendations

# Function to explain the load levels

def explain_load(intrinsic, extraneous, germane):
    explanation = []

    explanation.append(f"Intrinsic Load ({intrinsic}): This reflects how difficult the topic is for you.")
    explanation.append("Higher intrinsic load means the content is complex or unfamiliar.")

    explanation.append(f"Extraneous Load ({extraneous}): This is caused by distractions or poor study environment.")
    explanation.append("Higher extraneous load means your focus is getting interrupted.")

    explanation.append(f"Germane Load ({germane}): This shows how effectively you are learning and understanding.")
    explanation.append("Higher germane load means better engagement and learning efficiency.")

    return explanation

# Function to generate precautions based on load levels 

def generate_precautions(intrinsic, extraneous, germane):
    precautions = []

    if extraneous == "High":
        precautions.append("Avoid using phone while studying")
        precautions.append("Stay away from noisy environments")

    if intrinsic == "High":
        precautions.append("Do not try to learn everything at once")
        precautions.append("Avoid long continuous study sessions without breaks")

    if germane == "Low":
        precautions.append("Avoid passive reading without understanding")
        precautions.append("Do not skip revision")

    precautions.append("Avoid multitasking")
    precautions.append("Take regular short breaks to prevent burnout")

    return precautions



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
    # Generate explanations
    explanations = explain_load(intrinsic, extraneous, germane)

    # Generate precautions
    precautions = generate_precautions(intrinsic, extraneous, germane)

    st.subheader("Results")

    st.write("Intrinsic:", intrinsic)

    st.write("Extraneous:", extraneous)

    st.subheader("🧠 What this means:")
    for e in explanations:
        st.write("- " + e)

    st.write("Germane:", germane)

    rec, precautions = get_recommendations(intrinsic, extraneous, germane)

    st.subheader("Recommendations")
    for r in rec:
        st.write("-", r)

    st.subheader("Precautions")
    for p in precautions:
        st.write("-", p)