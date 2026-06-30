import streamlit as st

st.set_page_config(page_title="Industrial Multidomain ABSA Engine Framework", layout="wide")

# ---------------------------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------------------------
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}

    .stApp {
        background: linear-gradient(180deg, #15323b 0%, #1c4048 100%);
    }
    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 3rem;
        max-width: 1000px;
    }

    .hero-title {
        color: #ffffff !important;
        text-align: center;
        font-size: 2.3rem;
        font-weight: 800;
        margin-bottom: 0.3rem;
    }
    .hero-subtitle {
        color: #bfe3ea !important;
        text-align: center;
        font-size: 1rem;
        margin-bottom: 2rem;
    }

    .panel-header {
        background: #2d5e69;
        color: #ffffff !important;
        padding: 14px 20px;
        font-size: 1.05rem;
        font-weight: 700;
        border-radius: 6px;
        margin-bottom: 18px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .icon-badge {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 22px;
        height: 22px;
        border-radius: 5px;
        font-size: 0.85rem;
        flex-shrink: 0;
    }
    .icon-blue { background: #3b82c4; }
    .icon-pink { background: #d6488c; border-radius: 50%; }

    .metric-card {
        background: #ffffff;
        border-radius: 8px;
        padding: 20px;
        text-align: center;
        height: 110px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .metric-label {
        color: #4a5a5f !important;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 8px;
    }
    .metric-value {
        color: #16323d !important;
        font-size: 1.5rem;
        font-weight: 800;
    }
    .metric-sub {
        color: #9aa7ab !important;
        font-size: 0.75rem;
        margin-top: 4px;
    }

    table.model-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.88rem;
        background: transparent;
        border: 1px solid #3a5a62;
    }
    table.model-table th {
        text-align: left;
        color: #cfe3e8 !important;
        background: #234650;
        padding: 10px 10px;
        font-weight: 600;
        border-bottom: 1px solid #3a5a62;
    }
    table.model-table td {
        padding: 10px 10px;
        border-bottom: 1px solid #3a5a62;
        border-right: 1px solid #3a5a62;
        color: #e7f1f3 !important;
    }
    table.model-table td:last-child, table.model-table th:last-child {
        border-right: none;
    }

    .section-desc {
        color: #9fb8bd !important;
        font-size: 0.92rem;
        line-height: 1.5;
    }

    .domain-label {
        color: #ffffff !important;
        font-weight: 700;
        font-size: 0.95rem;
        margin-bottom: 8px;
    }

    div[data-baseweb="select"] > div {
        background-color: #1b2530 !important;
        border-color: #3a4a55 !important;
        color: #ffffff !important;
    }
    div[data-baseweb="select"] span {
        color: #ffffff !important;
    }

    .stTextArea textarea {
        background-color: #1b2530 !important;
        color: #e7f1f3 !important;
        border: 1px solid #3a4a55 !important;
    }
    .stTextArea textarea::placeholder {
        color: #8a98a0 !important;
    }

    div.stButton {
        display: flex;
        justify-content: center;
        margin-top: 12px;
    }
    div.stButton > button {
        background-color: #2d5e69;
        color: white !important;
        border-radius: 6px;
        padding: 0.55rem 1.8rem;
        border: none;
        font-weight: 600;
    }
    div.stButton > button:hover {
        background-color: #24484f;
        color: white !important;
    }

    /* Output Section Card Styles */
    .result-box {
        background: rgba(27, 37, 48, 0.7);
        border: 1px solid #3a4a55;
        border-radius: 8px;
        padding: 20px;
        margin-top: 15px;
    }
    .token-item {
        color: #e7f1f3 !important;
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 0px;
    }

    .spacer { height: 14px; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# HERO HEADER
# ---------------------------------------------------------------------------
st.markdown('<div class="hero-title">Industrial Multidomain ABSA Engine Framework</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Phase 1 Production Model Results &amp; Core Preprocessing Validation System</div>', unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# SECTION 1 — Preprocessing Analytics & Model Matrix
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="panel-header"><span class="icon-badge icon-blue">&#9000;</span>'
    'Section 1: Preprocessing Analytics &amp; Model Matrix</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Total Ingested Nested Subdirectories</div>
        <div class="metric-value">1,135 Subsets</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Audited Unique Clean Records</div>
        <div class="metric-value">58,332 Rows</div>
        <div class="metric-sub">Deduplicated</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <table class="model-table">
        <tr><th>Machine Learning Model</th><th>Accuracy</th><th>Precision</th><th>Recall</th></tr>
        <tr><td>Support Vector Machine (SVM)</td><td>84.2%</td><td>82.5%</td><td>80.1%</td></tr>
        <tr><td>Logistic Regression</td><td>81.9%</td><td>79.8%</td><td>78.4%</td></tr>
    </table>
    """, unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# SECTION 2 — Real-Time Aspect Inference Pipeline
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="panel-header"><span class="icon-badge icon-pink">&#129504;</span>'
    'Section 2: Real-Time Aspect Inference Pipeline</div>',
    unsafe_allow_html=True
)

top_left, top_right = st.columns([2.2, 1])

with top_left:
    st.markdown(
        '<div class="section-desc">Type a target custom review statement below to test token feature '
        'extraction rules and semantic isolation patterns.</div>',
        unsafe_allow_html=True
    )

with top_right:
    st.markdown('<div class="domain-label">Select Target Evaluation Domain</div>', unsafe_allow_html=True)
    domain = st.selectbox(
        "Select Target Evaluation Domain",
        ["Consumer Electronics [Laptops]", "Restaurants", "Hotels", "Mobile Phones"],
        index=0,
        label_visibility="collapsed",
    )

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

review_text = st.text_area(
    "Review input",
    placeholder="Example: The screen display is gorgeous but the customer service was quite slow...",
    label_visibility="collapsed",
    height=110,
)

run_clicked = st.button("Run Model Prediction Pipeline")

if run_clicked:
    if review_text.strip():
        st.success(f"Pipeline executed on domain: {domain}")
        
        # Wrapped container block matching your design parameters
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown("<h4 style='color: #ffffff; margin-bottom: 25px;'>Pipeline Generation Matrix Results</h4>", unsafe_allow_html=True)
        
        # --- DYNAMIC MOCK PIPELINE LOGIC ---
        lower_input = review_text.lower()
        extracted_aspects = []
        predictions = {}
        
        if "keyboard" in lower_input:
            extracted_aspects.append("keyboard")
            predictions["keyboard"] = "POSITIVE" if "great" in lower_input or "amazing" in lower_input or "good" in lower_input else "NEGATIVE"
            
        if "battery" in lower_input:
            extracted_aspects.append("battery life")
            predictions["battery life"] = "NEGATIVE" if "disappointing" in lower_input or "bad" in lower_input or "barely" in lower_input else "POSITIVE"
            
        if "screen" in lower_input or "display" in lower_input:
            extracted_aspects.append("screen display")
            predictions["screen display"] = "POSITIVE" if "gorgeous" in lower_input or "nice" in lower_input or "loved" in lower_input else "NEGATIVE"
            
        if "service" in lower_input or "waiter" in lower_input:
            aspect_name = "customer service" if "service" in lower_input else "waiter service"
            extracted_aspects.append(aspect_name)
            predictions[aspect_name] = "NEGATIVE" if "slow" in lower_input or "intimidate" in lower_input or "bad" in lower_input else "POSITIVE"
            
        if "food" in lower_input:
            extracted_aspects.append("food quality")
            predictions["food quality"] = "NEGATIVE" if "cold" in lower_input or "bad" in lower_input else "POSITIVE"

        # Fallback element if phrase does not contain explicit presets
        if not extracted_aspects:
            extracted_aspects = ["general quality"]
            predictions["general quality"] = "POSITIVE"
        # ------------------------------------

        # Table Column Descriptions Header Row
        head_col1, head_col2 = st.columns(2)
        with head_col1:
            st.markdown("<p style='color: #cfe3e8; font-weight:600; margin-bottom: 10px;'>🔑 Extracted Aspect Tokens</p>", unsafe_allow_html=True)
        with head_col2:
            st.markdown("<p style='color: #cfe3e8; font-weight:600; margin-bottom: 10px;'>📊 Predicted Aspect Polarities</p>", unsafe_allow_html=True)
            
        # Aligned row-by-row iteration to avoid formatting displacement bugs
        for aspect in extracted_aspects:
            row_col1, row_col2 = st.columns(2)
            with row_col1:
                st.markdown(f'<div class="token-item" style="line-height: 44px;">▪ {aspect}</div>', unsafe_allow_html=True)
            with row_col2:
                sentiment = predictions[aspect]
                if sentiment == "POSITIVE":
                    st.success(f"🟢 {sentiment} SENTIMENT")
                else:
                    st.error(f"🔴 {sentiment} SENTIMENT")
                    
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a review statement before running the pipeline.")