
import streamlit as st
import joblib
import os

st.set_page_config(
    page_title="SMS Spam Detection",
    page_icon="📩",
    layout="centered"
)

st.title("📩 SMS Spam Detection System")
st.write("Machine Learning Based Spam Message Classifier")

model_path = os.path.join(
    os.path.dirname(__file__),
    "models",
    "sms_spam_model.joblib"
)

model = joblib.load(model_path)

st.subheader("Enter Your SMS Message")

message = st.text_area(
    "Type or paste your SMS here:",
    height=150,
    placeholder="Enter your message..."
)

if st.button("Check Message"):
    if message.strip():

        prediction = model.predict([message])[0]

        if prediction == 1:
            st.error("⚠️ SPAM MESSAGE DETECTED!")
            st.write("This message is classified as spam.")
        else:
            st.success("✅ NORMAL MESSAGE (HAM)")
            st.write("This message is classified as normal.")

    else:
        st.warning("Please enter a message first.")

st.divider()
st.caption("Developed using Python and Machine Learning.")
