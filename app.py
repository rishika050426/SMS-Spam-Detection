import streamlit as st
import joblib
import os

# ---------------------------------
# PAGE CONFIGURATION
# ---------------------------------

st.set_page_config(
    page_title="SMS Shield | Spam Detector",
    page_icon="🛡️",
    layout="wide"
)

# ---------------------------------
# CUSTOM CSS
# ---------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f5f7ff, #edf2ff);
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #263b80;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #64748b;
    font-size: 17px;
    margin-bottom: 30px;
}

.hero {
    background: linear-gradient(120deg, #263b80, #6554c0);
    padding: 30px;
    border-radius: 18px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}

.hero h2 {
    color: white;
    font-size: 29px;
}

.hero p {
    color: #e0e7ff;
    font-size: 16px;
}

.result-spam {
    background: #fff0f0;
    border-left: 7px solid #e63946;
    padding: 22px;
    border-radius: 12px;
    color: #a4161a;
    text-align: center;
}

.result-ham {
    background: #e9fff2;
    border-left: 7px solid #16a34a;
    padding: 22px;
    border-radius: 12px;
    color: #166534;
    text-align: center;
}

.metric-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 3px 12px rgba(0,0,0,0.07);
}

.metric-value {
    font-size: 29px;
    font-weight: bold;
    color: #3446a5;
}

.metric-label {
    color: #64748b;
    font-size: 14px;
}

.section-heading {
    color: #263b80;
    font-size: 25px;
    font-weight: 700;
}

.footer {
    text-align: center;
    color: #64748b;
    padding: 25px;
}

div.stButton > button {
    background: linear-gradient(90deg, #3446a5, #6554c0);
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 25px;
    font-weight: bold;
    width: 100%;
}

div.stButton > button:hover {
    color: white;
    border: 1px solid #3446a5;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------
# LOAD MACHINE LEARNING MODEL
# ---------------------------------

model_path = os.path.join(
    os.path.dirname(__file__),
    "models",
    "sms_spam_model.joblib"
)

@st.cache_resource
def load_model():
    return joblib.load(model_path)

try:
    model = load_model()
except Exception as e:
    st.error("Unable to load the trained model. Please check the model file.")
    st.stop()


# ---------------------------------
# HEADER
# ---------------------------------

st.markdown(
    '<div class="main-title">🛡️ SMS SHIELD</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Intelligent SMS Spam Detection Using Machine Learning</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="hero">
    <h2>Protect Yourself from Spam Messages!</h2>
    <p>
    Analyze SMS messages instantly using our trained
    Machine Learning classification model.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------------------------
# SMS INPUT SECTION
# ---------------------------------

st.markdown(
    '<div class="section-heading">📩 Message Analyzer</div>',
    unsafe_allow_html=True
)

st.write("Enter an SMS message below to check whether it is Spam or Ham.")

sample = st.selectbox(
    "Try an example message:",
    [
        "Choose an example...",
        "Hey, are we meeting for lunch today? Let me know when you reach college.",
        "Congratulations! You have won a free prize. Claim your reward now!"
    ]
)

default_message = ""

if sample != "Choose an example...":
    default_message = sample

message = st.text_area(
    "Enter your SMS message:",
    value=default_message,
    height=140,
    placeholder="Type or paste your SMS message here..."
)

st.write("")

if st.button("🔍 ANALYZE MESSAGE"):

    if message.strip():

        prediction = model.predict([message])[0]

        # Supports numeric and text labels
        is_spam = (
            str(prediction).strip().lower()
            in ["1", "spam", "true", "yes"]
        )

        st.divider()

        if is_spam:

            st.markdown("""
            <div class="result-spam">
                <h2>🚨 SPAM MESSAGE DETECTED!</h2>
                <h4>This message has been classified as SPAM.</h4>
                <p>Be careful before responding or clicking any links.</p>
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div class="result-ham">
                <h2>✅ NORMAL MESSAGE (HAM)</h2>
                <h4>This message has been classified as HAM.</h4>
                <p>The model identifies this as a normal message.</p>
            </div>
            """, unsafe_allow_html=True)

    else:
        st.warning("Please enter a message before analyzing.")


# ---------------------------------
# MODEL PERFORMANCE
# ---------------------------------

st.divider()

st.markdown(
    '<div class="section-heading">📊 Model Performance</div>',
    unsafe_allow_html=True
)

st.write("Performance of the final tuned Multinomial Naive Bayes model.")

col1, col2, col3, col4 = st.columns(4)

metrics = [
    (col1, "98.07%", "Accuracy"),
    (col2, "95.12%", "Precision"),
    (col3, "89.31%", "Recall"),
    (col4, "92.13%", "F1 Score")
]

for col, value, label in metrics:
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{value}</div>
            <div class="metric-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)


# ---------------------------------
# HOW IT WORKS
# ---------------------------------

st.divider()

st.markdown(
    '<div class="section-heading">⚙️ How Does It Work?</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 1️⃣ Enter Message
    Provide an SMS message that you want to analyze.
    """)

with col2:
    st.markdown("""
    ### 2️⃣ ML Analysis
    The trained Machine Learning model analyzes the message.
    """)

with col3:
    st.markdown("""
    ### 3️⃣ Get Result
    The system predicts whether the message is Spam or Ham.
    """)


# ---------------------------------
# FOOTER
# ---------------------------------

st.divider()

st.markdown("""
<div class="footer">
    <h4>🛡️ SMS Shield - SMS Spam Detection System</h4>
    <p>Developed using Python, Streamlit and Machine Learning.</p>
    <p>Academic Machine Learning Project</p>
</div>
""", unsafe_allow_html=True)
