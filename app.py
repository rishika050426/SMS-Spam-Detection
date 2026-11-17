import streamlit as st
import joblib
import os

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="SMS Shield | AI Spam Detector",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

/* Main Background */

.stApp {
    background: #f4f6fc;
}

/* General Text */

.stApp,
.stMarkdown,
.stMarkdown p,
.stMarkdown li {
    color: #263247;
}

.stMarkdown h1,
.stMarkdown h2,
.stMarkdown h3,
.stMarkdown h4 {
    color: #263b80;
}

/* Header */

.header {
    background: linear-gradient(120deg, #172554, #4338a8, #6d5ce7);
    padding: 38px 25px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 28px;
    box-shadow: 0 8px 25px rgba(50, 55, 130, 0.18);
}

.header h1 {
    color: white !important;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 8px;
}

.header p {
    color: #e0e7ff !important;
    font-size: 17px;
}

/* Section Titles */

.section-title {
    color: #243b80;
    font-size: 25px;
    font-weight: 800;
    margin-top: 15px;
    margin-bottom: 5px;
}

/* Metric Cards */

.metric-card {
    background: white;
    border-radius: 16px;
    padding: 22px 12px;
    text-align: center;
    border: 1px solid #e5e9f5;
    box-shadow: 0 5px 16px rgba(30, 50, 100, 0.06);
}

.metric-icon {
    font-size: 27px;
}

.metric-value {
    color: #3949ab;
    font-size: 30px;
    font-weight: 800;
    margin: 8px 0;
}

.metric-label {
    color: #475569;
    font-size: 14px;
    font-weight: 600;
}

/* Analyzer Container */

.analyzer-box {
    background: white;
    padding: 22px;
    border-radius: 17px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 5px 18px rgba(30, 50, 100, 0.05);
}

/* Input Labels */

label,
.stTextArea label,
.stSelectbox label {
    color: #263247 !important;
    font-weight: 700 !important;
}

/* Text Area */

.stTextArea textarea {
    background-color: white !important;
    color: #172554 !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 12px !important;
    font-size: 15px !important;
}

.stTextArea textarea::placeholder {
    color: #64748b !important;
    opacity: 1 !important;
}

/* Select Box */

[data-testid="stSelectbox"] > div > div {
    background-color: white !important;
    color: #172554 !important;
    border-radius: 10px !important;
}

[data-testid="stSelectbox"] * {
    color: #172554 !important;
}

/* Buttons */

div.stButton > button {
    background: linear-gradient(90deg, #3949ab, #7059d9);
    color: white !important;
    border: none;
    border-radius: 11px;
    padding: 12px 20px;
    font-weight: 700;
    width: 100%;
    transition: 0.3s;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #283593, #5945c0);
    color: white !important;
    transform: translateY(-2px);
}

/* Spam Result */

.spam-result {
    background: #fff1f2;
    border: 1px solid #fecdd3;
    border-left: 7px solid #e11d48;
    border-radius: 15px;
    padding: 25px;
    text-align: center;
}

.spam-result h2,
.spam-result p {
    color: #9f1239 !important;
}

/* Ham Result */

.ham-result {
    background: #ecfdf5;
    border: 1px solid #bbf7d0;
    border-left: 7px solid #16a34a;
    border-radius: 15px;
    padding: 25px;
    text-align: center;
}

.ham-result h2,
.ham-result p {
    color: #166534 !important;
}

/* Process Cards */

.process-card {
    background: white;
    padding: 23px;
    border-radius: 15px;
    border: 1px solid #e2e8f0;
    text-align: center;
    min-height: 165px;
    box-shadow: 0 4px 14px rgba(30, 50, 100, 0.05);
}

.process-card h3 {
    color: #3949ab !important;
}

.process-card p {
    color: #475569 !important;
}

/* Footer */

.footer {
    background: #172554;
    color: white;
    padding: 25px;
    text-align: center;
    border-radius: 15px;
    margin-top: 25px;
}

.footer h3,
.footer p {
    color: white !important;
}

hr {
    border-color: #dce3f0;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# LOAD TRAINED MODEL
# ==========================================

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

except Exception:
    st.error(
        "Unable to load the trained model. "
        "Please check the models folder."
    )
    st.stop()


# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div class="header">
    <h1>🛡️ SMS SHIELD</h1>
    <p>AI-Powered SMS Spam Detection System</p>
    <p>Smart • Fast • Reliable Message Classification</p>
</div>
""", unsafe_allow_html=True)


# ==========================================
# DASHBOARD OVERVIEW
# ==========================================

st.markdown(
    '<div class="section-title">📊 Model Performance Overview</div>',
    unsafe_allow_html=True
)

st.write(
    "Performance of our final tuned Multinomial Naive Bayes model."
)

c1, c2, c3, c4 = st.columns(4)

metric_data = [
    (c1, "🎯", "98.07%", "Accuracy"),
    (c2, "⚡", "95.12%", "Precision"),
    (c3, "🔍", "89.31%", "Recall"),
    (c4, "📈", "92.13%", "F1 Score")
]

for col, icon, value, label in metric_data:

    with col:

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon">{icon}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)


st.divider()


# ==========================================
# MESSAGE ANALYZER
# ==========================================

st.markdown(
    '<div class="section-title">📩 Smart Message Analyzer</div>',
    unsafe_allow_html=True
)

st.write(
    "Enter any SMS message below and let our machine learning "
    "model identify whether it is Spam or Ham."
)

sample = st.selectbox(
    "✨ Try a sample message",
    [
        "Choose an example...",
        "Hey, are we meeting for lunch today? Let me know when you reach college.",
        "Congratulations! You have won a free prize. Claim your reward now!"
    ]
)

if sample != "Choose an example...":
    default_message = sample
else:
    default_message = ""

message = st.text_area(
    "Enter your SMS message",
    value=default_message,
    height=150,
    placeholder="Type or paste your SMS message here..."
)

st.write("")

analyze = st.button("🔍 ANALYZE MESSAGE")

if analyze:

    if message.strip():

        with st.spinner("Analyzing your message..."):

            prediction = model.predict([message])[0]

            is_spam = (
                str(prediction).strip().lower()
                in ["1", "spam", "true", "yes"]
            )

        st.divider()

        if is_spam:

            st.markdown("""
            <div class="spam-result">
                <h2>🚨 SPAM MESSAGE DETECTED!</h2>
                <p><b>Classification:</b> SPAM</p>
                <p>
                This message has been classified as spam
                by our machine learning model.
                </p>
                <p>⚠️ Be careful before responding or clicking links.</p>
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div class="ham-result">
                <h2>✅ NORMAL MESSAGE DETECTED!</h2>
                <p><b>Classification:</b> HAM</p>
                <p>
                This message has been classified as a
                normal message by our machine learning model.
                </p>
                <p>✔️ The model identifies this as a normal SMS.</p>
            </div>
            """, unsafe_allow_html=True)

    else:

        st.warning("⚠️ Please enter a message before analyzing.")


st.divider()


# ==========================================
# HOW IT WORKS
# ==========================================

st.markdown(
    '<div class="section-title">⚙️ How Does SMS Shield Work?</div>',
    unsafe_allow_html=True
)

st.write(
    "Our system follows three simple steps to classify SMS messages."
)

a, b, c = st.columns(3)

with a:

    st.markdown("""
    <div class="process-card">
        <h3>📩 Step 1</h3>
        <h4>Enter Message</h4>
        <p>Enter or paste the SMS you want to analyze.</p>
    </div>
    """, unsafe_allow_html=True)

with b:

    st.markdown("""
    <div class="process-card">
        <h3>🤖 Step 2</h3>
        <h4>AI Analysis</h4>
        <p>The trained model analyzes the message using text features.</p>
    </div>
    """, unsafe_allow_html=True)

with c:

    st.markdown("""
    <div class="process-card">
        <h3>📊 Step 3</h3>
        <h4>Get Prediction</h4>
        <p>The system classifies the message as Spam or Ham.</p>
    </div>
    """, unsafe_allow_html=True)


st.divider()


# ==========================================
# PROJECT INFORMATION
# ==========================================

with st.expander("ℹ️ About This Project"):

    st.write("""
    **SMS Shield** is a Machine Learning based SMS Spam
    Detection System.

    The project uses a trained Multinomial Naive Bayes
    classifier with TF-IDF text features.

    The model analyzes the input message and predicts
    whether it belongs to the Spam or Ham category.

    **Technologies Used:**
    - Python
    - Streamlit
    - Scikit-learn
    - TF-IDF Vectorization
    - Multinomial Naive Bayes
    """)


# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class="footer">
    <h3>🛡️ SMS SHIELD</h3>
    <p>AI-Powered SMS Spam Detection System</p>
    <p>Developed using Python, Streamlit and Machine Learning.</p>
    <p>Academic Machine Learning Project</p>
</div>
""", unsafe_allow_html=True)
