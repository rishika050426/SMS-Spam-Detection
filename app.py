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
# CUSTOM CSS - MIDNIGHT NEON THEME
# ==========================================

st.markdown("""
<style>

/* MAIN BACKGROUND */

.stApp {
    background: linear-gradient(135deg, #0b1020, #151b35, #21183d);
    color: #f8fafc;
}

/* GENERAL TEXT */

.stMarkdown,
.stMarkdown p,
.stMarkdown li {
    color: #e2e8f0 !important;
}

.stMarkdown h1,
.stMarkdown h2,
.stMarkdown h3,
.stMarkdown h4 {
    color: #f8fafc !important;
}

/* HEADER */

.header {
    background: linear-gradient(120deg, #312e81, #6d28d9, #0891b2);
    padding: 42px 25px;
    border-radius: 22px;
    text-align: center;
    margin-bottom: 30px;
    box-shadow: 0 0 35px rgba(124, 58, 237, 0.3);
    border: 1px solid rgba(255,255,255,0.15);
}

.header h1 {
    color: white !important;
    font-size: 46px;
    font-weight: 900;
    margin-bottom: 8px;
}

.header p {
    color: #e0f2fe !important;
    font-size: 17px;
}

/* SECTION TITLES */

.section-title {
    color: #67e8f9 !important;
    font-size: 26px;
    font-weight: 800;
    margin-top: 20px;
    margin-bottom: 12px;
}

/* METRIC CARDS */

.metric-card {
    background: linear-gradient(145deg, #202b49, #29204a);
    border-radius: 18px;
    padding: 24px 12px;
    text-align: center;
    border: 1px solid #5541a5;
    box-shadow: 0 8px 25px rgba(0,0,0,0.25);
    transition: 0.3s;
}

.metric-card:hover {
    border-color: #22d3ee;
    transform: translateY(-5px);
}

.metric-icon {
    font-size: 30px;
}

.metric-value {
    color: #67e8f9;
    font-size: 32px;
    font-weight: 900;
    margin: 10px 0;
}

.metric-label {
    color: #e2e8f0;
    font-size: 14px;
    font-weight: 700;
}

/* INPUT LABELS */

label,
.stTextArea label,
.stSelectbox label {
    color: #f1f5f9 !important;
    font-weight: 700 !important;
}

/* TEXT AREA */

.stTextArea textarea {
    background-color: #18233d !important;
    color: white !important;
    border: 1px solid #6366f1 !important;
    border-radius: 14px !important;
    font-size: 15px !important;
}

.stTextArea textarea::placeholder {
    color: #a5b4fc !important;
    opacity: 1 !important;
}

/* DROPDOWN */

[data-testid="stSelectbox"] > div > div {
    background-color: #18233d !important;
    color: white !important;
    border: 1px solid #6366f1 !important;
    border-radius: 12px !important;
}

[data-testid="stSelectbox"] * {
    color: white !important;
}

/* BUTTON */

div.stButton > button {
    background: linear-gradient(90deg, #7c3aed, #0891b2);
    color: white !important;
    border: 1px solid #67e8f9;
    border-radius: 13px;
    padding: 14px 20px;
    font-size: 16px;
    font-weight: 800;
    width: 100%;
    box-shadow: 0 0 20px rgba(34,211,238,0.2);
    transition: 0.3s;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #6d28d9, #0e7490);
    color: white !important;
    box-shadow: 0 0 25px rgba(34,211,238,0.5);
}

/* SPAM RESULT */

.spam-result {
    background: linear-gradient(135deg, #451a2b, #7f1d35);
    border: 1px solid #fb7185;
    border-left: 7px solid #fb385f;
    border-radius: 17px;
    padding: 28px;
    text-align: center;
    box-shadow: 0 0 25px rgba(244,63,94,0.2);
}

.spam-result h2,
.spam-result p {
    color: #ffe4e6 !important;
}

/* HAM RESULT */

.ham-result {
    background: linear-gradient(135deg, #064e3b, #065f46);
    border: 1px solid #34d399;
    border-left: 7px solid #10b981;
    border-radius: 17px;
    padding: 28px;
    text-align: center;
    box-shadow: 0 0 25px rgba(16,185,129,0.2);
}

.ham-result h2,
.ham-result p {
    color: #d1fae5 !important;
}

/* PROCESS CARDS */

.process-card {
    background: linear-gradient(145deg, #202b49, #29204a);
    padding: 25px;
    border-radius: 17px;
    border: 1px solid #5541a5;
    text-align: center;
    min-height: 175px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
}

.process-card h3 {
    color: #67e8f9 !important;
}

.process-card h4 {
    color: #f8fafc !important;
}

.process-card p {
    color: #cbd5e1 !important;
}

/* ABOUT PROJECT */

[data-testid="stExpander"] {
    background: #202b49;
    border: 1px solid #5541a5;
    border-radius: 12px;
}

[data-testid="stExpander"] summary {
    color: #67e8f9 !important;
}

/* FOOTER */

.footer {
    background: linear-gradient(120deg, #312e81, #581c87, #164e63);
    color: white;
    padding: 30px;
    text-align: center;
    border-radius: 18px;
    margin-top: 30px;
    border: 1px solid #6366f1;
}

.footer h3,
.footer p {
    color: white !important;
}

/* DIVIDER */

hr {
    border-color: #475569;
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
# ABOUT PROJECT
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
