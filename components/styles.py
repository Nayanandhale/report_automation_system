import streamlit as st

def show_style():
    # Page configuration
    st.set_page_config(
        page_title="Unnatva Foundation - Report Automation System",
        page_icon="🌱",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    custom_css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700&display=swap');

    :root {
        --unnatva-green: #005A36;
        --unnatva-green-dark: #004328;
        --unnatva-green-light: #0D7A4D;
        --unnatva-gold: #F5C518;
        --unnatva-gold-light: #FFF4D0;
        --unnatva-bg-soft: #F4F8F5;
        --unnatva-card-bg: #FFFFFF;
        --unnatva-text-main: #1A2B23;
        --unnatva-text-muted: #52635B;
        --unnatva-border: #E0EAE4;
    }

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        color: var(--unnatva-text-main);
    }

    /* Main App Background */
    [data-testid="stAppViewContainer"] {
        background-color: #F8FAF9;
        background-image: 
            radial-gradient(at 0% 0%, rgba(0, 90, 54, 0.04) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(245, 197, 24, 0.05) 0px, transparent 50%);
    }

    /* Top Header Background */
    [data-testid="stHeader"] {
        background: rgba(248, 250, 249, 0.85);
        backdrop-filter: blur(8px);
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #F0F6F2 0%, #E8F2EC 100%);
        border-right: 1px solid var(--unnatva-border);
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1300px;
    }

    /* Brand Header Banner */
    .brand-hero-card {
        background: linear-gradient(135deg, #005A36 0%, #004226 100%);
        color: #FFFFFF;
        border-radius: 18px;
        padding: 24px 32px;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px rgba(0, 90, 54, 0.15);
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: relative;
        overflow: hidden;
    }

    .brand-hero-card::after {
        content: "";
        position: absolute;
        right: -30px;
        bottom: -30px;
        width: 180px;
        height: 180px;
        border-radius: 50%;
        background: rgba(245, 197, 24, 0.12);
        pointer-events: none;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background-color: #EBF3EE;
        padding: 6px;
        border-radius: 14px;
        border: 1px solid var(--unnatva-border);
    }

    .stTabs [data-baseweb="tab"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 15px;
        font-weight: 600;
        padding: 10px 22px;
        border-radius: 10px;
        color: var(--unnatva-green-dark);
        background: transparent;
        border: none;
        transition: all 0.2s ease;
    }

    .stTabs [aria-selected="true"] {
        background: #005A36 !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 12px rgba(0, 90, 54, 0.25);
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #005A36 0%, #0D7A4D 100%);
        color: #FFFFFF;
        border: 1px solid #005A36;
        border-radius: 12px;
        font-weight: 600;
        font-size: 15px;
        padding: 0.6rem 1.4rem;
        transition: all 0.25s ease;
        box-shadow: 0 4px 12px rgba(0, 90, 54, 0.15);
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #004328 0%, #005A36 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(0, 90, 54, 0.25);
        color: #FFFFFF;
    }

    /* Metric Cards */
    [data-testid="metric-container"] {
        background: #FFFFFF;
        border: 1px solid var(--unnatva-border);
        border-left: 5px solid #005A36;
        border-radius: 14px;
        padding: 16px 20px;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.04);
        transition: transform 0.2s ease;
    }

    [data-testid="metric-container"]:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 22px rgba(0, 90, 54, 0.08);
    }

    [data-testid="stMetricValue"] {
        font-family: 'Outfit', sans-serif;
        color: #005A36 !important;
        font-weight: 700;
    }

    [data-testid="stMetricLabel"] {
        color: #52635B !important;
        font-weight: 600;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Text areas & Inputs */
    .stTextInput input, .stTextArea textarea, .stSelectbox [data-baseweb="select"] {
        border-radius: 10px !important;
        border: 1px solid #CEDCD4 !important;
        background-color: #FFFFFF !important;
        font-size: 14px;
    }

    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #005A36 !important;
        box-shadow: 0 0 0 3px rgba(0, 90, 54, 0.15) !important;
    }

    /* Card Containers */
    .unnatva-card {
        background: #FFFFFF;
        border: 1px solid var(--unnatva-border);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03);
    }

    /* Highlight Badges (Golden Brush style from website screenshot) */
    .unnatva-highlight-badge {
        display: inline-block;
        background: #F5C518;
        color: #1A2B23;
        font-weight: 700;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 13px;
        box-shadow: 0 2px 6px rgba(245, 197, 24, 0.35);
        margin-right: 6px;
    }

    .unnatva-pill-badge {
        display: inline-block;
        background: #005A36;
        color: #FFFFFF;
        font-weight: 600;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 12px;
        margin-right: 6px;
        margin-bottom: 6px;
    }

    /* Impact Strip */
    .impact-banner {
        background: #004D2C;
        color: white;
        border-radius: 14px;
        padding: 16px 22px;
        margin: 15px 0 25px 0;
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
        align-items: center;
        justify-content: space-around;
    }

    .impact-item {
        text-align: center;
    }

    .impact-num {
        background: #F5C518;
        color: #142E1F;
        font-weight: 800;
        font-size: 17px;
        padding: 2px 10px;
        border-radius: 12px;
        display: inline-block;
        margin-bottom: 4px;
    }

    .impact-label {
        font-size: 12px;
        color: #E2ECE5;
        font-weight: 500;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
