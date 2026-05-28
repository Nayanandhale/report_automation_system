import streamlit as st

def show_style():

# PAGE CONFIG
    st.set_page_config (
        page_title="Report Automation System",
        page_icon="📊",
        layout="wide"
    )

    page_bg = """<style>

        [data-testid="stAppViewContainer"]{
        background-image: linear-gradient(
        rgba(255,255,255,0.88),
        rgba(255,255,255,0.88)
        ),
        url("https://i.imgur.com/IRfCm2C.png"); 

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        }

        [data-testid="stSidebar"]{
        background-color: rgba(240,248,245,0.92);
        }

        [data-testid="stHeader"]{
        background: rgba(0,0,0,0);
        }

        .block-container{
        padding-top: 2rem;
        padding-bottom: 2rem;
        }

        .stTabs [data-baseweb="tab-list"]{
        gap: 20px;
        }

        .stTabs [data-baseweb="tab"]{
        font-size: 16px;
        font-weight: 600;
        padding: 10px 20px;
        border-radius: 10px;
        }

        div[data-testid="stVerticalBlock"] > div:has(div.stTabs){
        background: rgba(255,255,255,0.75);
        padding: 20px;
        border-radius: 20px;
        backdrop-filter: blur(6px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }
        </style>"""
    st.markdown(page_bg, unsafe_allow_html=True) 

    st.markdown("""<style>

    .stButton > button {
        background: linear-gradient(
            90deg,
            #2E8B57,
            #3AA76D
        );
        color: white;
        border: none;
        border-radius: 12px;
        height: 3em;
        font-size: 16px;
        font-weight: 600;
        width: 100%;
        transition: 0.3s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow:
            0px 6px 15px rgba(46,139,87,0.25);
    }

    [data-testid="metric-container"] {
        background: rgba(255,255,255,0.65);
        border-radius: 16px;
        padding: 18px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.3);
        box-shadow:
            0px 4px 12px rgba(0,0,0,0.06);
    }

    [data-testid="stFileUploader"] {
        background: rgba(255,255,255,0.6);
        border-radius: 15px;
        padding: 15px;
        border: 1px solid rgba(255,255,255,0.4);
    }

    textarea {
        border-radius: 12px !important;
        background-color: rgba(255,255,255,0.7) !important;
    }
                
    h1, h2, h3 {
        font-weight: 700 !important;
    }

    button[data-baseweb="tab"] {
        font-size: 16px;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)
